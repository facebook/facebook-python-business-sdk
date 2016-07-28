from __future__ import unicode_literals, absolute_import, print_function
import re
import six
import time
import ujson
import logging
import collections
import concurrent.futures
import threading
# noinspection PyUnresolvedReferences
from six.moves import http_client

from facebookads.exceptions import FacebookCallFailedError, FacebookBadObjectError
from facebookads.api import FacebookSession, FacebookResponse, \
    FacebookAdsApi, _top_level_param_json_encode

__author__ = 'pasha-r'

logger = logging.getLogger("facebookclient")
#logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(30)


class FacebookAsyncResponse(FacebookResponse):
    def __init__(self, body=None, http_status=None, headers=None, call=None, error=None):
        super(FacebookAsyncResponse, self).__init__(body, http_status, headers, call)
        self._error = error
        self._json_body = None

    def json(self):
        """Returns the response body -- in json if possible."""
        if self._json_body:
            return self._json_body

        try:
            self._json_body = ujson.loads(self._body)
            return self._json_body
        except (TypeError, ValueError):
            self._json_body = None
            return self._body

    def is_success(self):
        self.json()

        if isinstance(self._json_body, collections.Mapping) and 'error' in self._json_body:
            # Is a dictionary, has error in it
            return False
        elif self._http_status not in (http_client.NOT_MODIFIED, http_client.OK):
            return False
        elif bool(self._json_body):
            # Has body and no error
            if 'success' in self._json_body:
                return not bool(self._error) and self._json_body['success']
            return not bool(self._error)
        elif self._http_status == http_client.NOT_MODIFIED:
            # ETAG Hit
            return not bool(self._error)
        elif self._http_status == http_client.OK:
            # HTTP Okay
            return not bool(self._error)
        else:
            # Something else
            return False

    def error(self):
        """
        Returns a FacebookRequestError (located in the exceptions module) with
        an appropriate debug message.
        """
        if self._error:
            return self._error
        return super(FacebookAsyncResponse, self).error()


class FacebookAdsAsyncApi(FacebookAdsApi):
    """Encapsulates session attributes and methods to make API calls.
    Provides an ability to issue several calls at the same time.
    """

    _default_api = None
    _default_account_id = None

    def __init__(self, session, api_version=None, threadpool_size=10):
        """Initializes the api instance.

        Args:
            session: FacebookSession object that contains a requests interface
                and attribute GRAPH (the Facebook GRAPH API URL).
        """
        super(FacebookAdsAsyncApi, self).__init__(session, api_version)
        self._thread_lock = threading.Lock()
        self._thread_pool = concurrent.futures.ThreadPoolExecutor(threadpool_size)
        self._futures = {}
        """:type: dict[int, facebookads.asyncobjects.AioEdgeIterator]"""
        self._futures_ordered = []
        """:type: list[facebookads.asyncobjects.AioEdgeIterator]"""

    @classmethod
    def init(cls, app_id=None, app_secret=None, access_token=None,
             account_id=None, api_version=None, pool_maxsize=10, max_retries=0):
        # connection pool size is +1 because there also is the main thread that can also issue a request
        session = FacebookSession(app_id, app_secret, access_token,
                                  pool_maxsize+1, max_retries)
        api = cls(session, api_version=api_version, threadpool_size=pool_maxsize)
        cls.set_default_api(api)
        # TODO: how to avoid this hack?
        FacebookAdsApi.set_default_api(api)

        if account_id:
            cls.set_default_account_id(account_id)

    def prepare_request_params(self, path, params, headers, files,
                               url_override, api_version):
        if not params:
            params = {}
        if not headers:
            headers = {}
        if not files:
            files = {}
        if api_version and not re.search('v[0-9]+\.[0-9]+', api_version):
            raise FacebookBadObjectError(
                    'Please provide the API version in the following format: %s'
                    % self.API_VERSION)
        if not isinstance(path, six.string_types):
            # Path is not a full path
            path = "/".join((
                self._session.GRAPH or url_override,
                api_version or self.API_VERSION,
                '/'.join(map(str, path)),
            ))

        # Include api headers in http request
        headers = headers.copy()
        headers.update(FacebookAdsApi.HTTP_DEFAULT_HEADERS)
        if params:
            params = _top_level_param_json_encode(params)
        return path, params, headers, files

    def non_throwing_call(self, method, path, params=None, headers=None, files=None,
                          delay_next_call_for=0):
        """A non-throwing version of call method.
        Returns FacebookAsyncResponse.

        :param method: The HTTP method name (e.g. 'GET').
        :param path: A tuple of path tokens or a full URL string. A tuple will
            be translated to a url as follows:
            graph_url/tuple[0]/tuple[1]...
            It will be assumed that if the path is not a string, it will be
            iterable.
        :param params: (optional) A mapping of request parameters where a key
            is the parameter name and its value is a string or an object
            which can be JSON-encoded.
        :param headers: (optional) A mapping of request headers where a key is the
            header name and its value is the header value.
        :param files: (optional) A mapping of file names to binary open
            file objects. These files will be attached to the request.
        :param delay_next_call_for: (optional) issue request in X seconds
        :rtype: FacebookAsyncResponse
        """
        self._num_requests_attempted += 1
        call_signature = {'method': method, 'path': path, 'params': params,
                          'headers': headers, 'files': files}
        if delay_next_call_for:
            time.sleep(delay_next_call_for)

        # Get request response and encapsulate it in a FacebookResponse
        logger.debug("Method {}, url: {}, params: {}".format(method, path, params))
        try:
            if method in ('GET', 'DELETE'):
                response = self._session.requests.request(
                    method, path, params=params, headers=headers, files=files)
            else:
                response = self._session.requests.request(
                    method, path, data=params, headers=headers, files=files)
        except Exception as exc:
            error = FacebookCallFailedError(call_signature, exc)
            fb_response = FacebookAsyncResponse(call=call_signature, error=error)
        else:
            fb_response = FacebookAsyncResponse(
                body=response.text, headers=response.headers,
                http_status=response.status_code, call=call_signature)

        if fb_response.is_success():
            self._num_requests_succeeded += 1
        return fb_response

    def call_future(self, edge_iter, method, path, params=None, headers=None, files=None,
                    url_override=None, api_version=None, delay_next_call_for=0):
        """Adds an async API call task to a futures queue.
        Returns a future holder object.

        :param facebookads.asyncobjects.AioEdgeIterator edge_iter:
            edge iterator issuing this call
        :param method: The HTTP method name (e.g. 'GET').
        :param path: A tuple of path tokens or a full URL string. A tuple will
            be translated to a url as follows:
            graph_url/tuple[0]/tuple[1]...
            It will be assumed that if the path is not a string, it will be
            iterable.
        :param params: (optional) A mapping of request parameters where a key
            is the parameter name and its value is a string or an object
            which can be JSON-encoded.
        :param headers: (optional) A mapping of request headers where a key is the
            header name and its value is the header value.
        :param files: (optional) A mapping of file names to binary open
            file objects. These files will be attached to the request.
        :param url_override:
        :param api_version:
        :rtype: FacebookAsyncResponse
        """
        path, params, headers, files = self.prepare_request_params(
                path, params, headers, files, url_override, api_version)

        future = self._thread_pool.submit(
                self.non_throwing_call, method, path,
                params=params, headers=headers, files=files,
                delay_next_call_for=delay_next_call_for)

        self.put_in_futures(edge_iter)
        return future

    def put_in_futures(self, edge_iter):
        """
        Adds iterator to a queue of futures self._futures_ordered and to dictionary self._futures
        """
        with self._thread_lock:
            edge_iter_id = id(edge_iter)
            if edge_iter_id not in self._futures_ordered:
                self._futures_ordered.append(edge_iter_id)
            self._futures[edge_iter_id] = edge_iter

    def remove_from_futures(self, edge_iter):
        with self._thread_lock:
            edge_iter_id = id(edge_iter)
            try:
                del self._futures[edge_iter_id]
            except KeyError:
                pass
            try:
                self._futures_ordered.remove(edge_iter_id)
            except ValueError:
                pass

    def pop_one_from_futures(self):
        with self._thread_lock:
            try:
                edge_iter_id = self._futures_ordered.pop(0)

                if not edge_iter_id in self._futures:
                    return "next"

                edge_iter = self._futures.pop(edge_iter_id)
            except IndexError:
                return None
        return edge_iter

    def __del__(self):
        if self._thread_pool:
            try:
                if not self._thread_pool._shutdown:
                    self._thread_pool.shutdown(False)
            except Exception:
                pass
            del self._thread_pool

    # helper results iterator

    def purge_futures_queue(self):
        while True:
            edge_iter = self.pop_one_from_futures()
            if edge_iter is None:
                break
            elif isinstance(edge_iter, six.string_types) and edge_iter == "next":
                continue

            if edge_iter._future:
                try:
                    if edge_iter._future.done():
                        result = edge_iter._future.result()
                        del result
                    elif edge_iter._future.running():
                        edge_iter._future.cancel()
                except Exception as exc:
                    logger.warn("Future stop failed: {}".format(exc))
                del edge_iter._future

    def get_all_async_results(self):
        """
        Gets one iterator from _futures_ordered attribute and if it's callable,
        calls its method extract_result().

        If iterator is done or failed, returns the iterator, otherwise puts it in the features.

        :rtype: list[facebookads.asyncobjects.AioEdgeIterator]
        """
        time.sleep(0.02)
        cnt = 0

        while True:
            cnt += 1
            edge_iter = self.pop_one_from_futures()

            if edge_iter is None:
                break
            elif isinstance(edge_iter, six.string_types) and edge_iter == "next":
                continue

            edge_iter = edge_iter.extract_results()

            if edge_iter._page_ready and edge_iter._finished_iteration:
                # loaded all the data
                yield edge_iter
            else:
                if edge_iter._request_failed:
                    # request failed unrecoverably
                    yield edge_iter
                else:
                    # some more loading needs to be done
                    edge_iter.submit_next_page_aio()
                    self.put_in_futures(edge_iter)

            if cnt >= len(self._futures):
                cnt = 0
                time.sleep(0.5)

    def get_typed_async_results(self, target_objects_class):
        """
        :rtype: list[facebookads.asyncobjects.AioEdgeIterator]
        """
        time.sleep(0.02)
        cnt, required_type_cnt = 0, 0
        while True:
            cnt += 1
            edge_iter = self.pop_one_from_futures()
            if edge_iter is None:
                break
            elif isinstance(edge_iter, six.string_types) and edge_iter == "next":
                continue

            edge_iter = edge_iter.extract_results()

            if edge_iter._page_ready and edge_iter._finished_iteration:
                # loaded all the data
                if edge_iter._target_objects_class == target_objects_class:
                    required_type_cnt += 1
                    yield edge_iter
                else:
                    self.put_in_futures(edge_iter)

            else:
                if edge_iter._request_failed:
                    # request failed unrecoverably
                    if edge_iter._target_objects_class == target_objects_class:
                        required_type_cnt += 1
                        yield edge_iter
                    else:
                        self.put_in_futures(edge_iter)
                else:
                    if edge_iter._target_objects_class == target_objects_class:
                        required_type_cnt += 1
                    # some more loading needs to be done
                    edge_iter.submit_next_page_aio()
                    self.put_in_futures(edge_iter)

            # checked on all tasks in queue
            if cnt >= len(self._futures):
                # we've yielded all objects of target_objects_class type
                if required_type_cnt <= 0:
                    break
                cnt = 0
                required_type_cnt = 0
                time.sleep(0.5)
