import logging
import random
import time

from six import string_types, text_type, binary_type
from requests.exceptions import ConnectionError

import facebook_business.api
from facebook_business.exceptions import FacebookUnavailablePropertyException, FacebookApiTimeout, FacebookRequestError
from facebook_business.utils.fberrcodes import FacebookErrorCodes

try:
    from urlparse import parse_qsl, urlparse, urlunsplit
    from urllib import urlencode
except ImportError:  # python 3 compatibility
    from urllib.parse import parse_qsl, urlparse, urlunsplit, urlencode

logger = logging.getLogger("facebookclient")


class AioEdgeIterator(facebook_business.api.Cursor):

    """Asyncronously retrieves pages of data from object's connections.
    Each page is a list of dicts with the data.
    And it iterates over the data.

    """

    def __init__(self, source_object, target_objects_class,
                 fields=None, params=None, include_summary=False,
                 limit=1000):
        """
        Initializes an iterator over the objects to which there is an edge from
        source_object.

        Args:
            source_object: An AbstractObject instance from which to inspect an
                edge. This object should have an id.
            target_objects_class: Objects traversed over will be initialized
                with this AbstractObject class.
            fields (optional): A list of fields of target_objects_class to
                automatically read in.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
        """
        self.limit = 1000 if limit is None else limit
        self.starting_limit = 1000 if limit is None else limit

        if params is None:
            params = {"limit": self.limit}
        elif not params or "limit" not in params:
            params["limit"] = self.limit

        super(AioEdgeIterator, self).__init__(
                source_object, target_objects_class,
                fields=fields, params=params, include_summary=include_summary)

        # AIO future holder
        self._future = None
        # last loaded response
        self._response = None
        """:type: facebook_business.asyncapi.FacebookAsyncResponse"""

        # iterator's state is:
        # self._finished_iteration - True or False
        # self.failed - True or False
        self._request_failed = False
        self._page_ready = False

        self.last_error_type = None
        self.last_error = None
        self.errors_streak = 0
        self.delay_next_call_for = 0

        self.success_cnt = 0
        self.success_streak = 0
        self.last_yield = time.time()

        self.unsupported_retries = 6
        self.tmp_retries = 25
        self.unknown_retries = 30
        self.too_much_data_retries = 14

    @property
    def future(self):
        return self._future

    @property
    def page_ready(self):
        return self._page_ready

    @property
    def target_objects_class(self):
        return self._target_objects_class

    @property
    def source_object(self):
        return self._source_object

    @property
    def finished_iteration(self):
        return self._finished_iteration

    @property
    def request_failed(self):
        return self._request_failed

    def __getitem__(self, index):
        if not self._queue:
            self.load_next_page()
        return self._queue[index]

    def clear_future(self):
        del self._future

    def get_all_results(self):
        """
        :rtype: list[dict]
        """
        return self._queue

    # AIO-based page loader

    def load_next_page(self):
        """Queries server for more nodes and loads them into the internal queue.

        Returns:
            True if successful, else False.
        """
        if self._finished_iteration:
            return False
        if not self._future:
            if not self.submit_next_page_aio():
                return False

        while not self._page_ready or self._request_failed:
            self.extract_results()
            time.sleep(0.2)
        success = self._page_ready and not self._request_failed and self._queue
        self.submit_next_page_aio()
        return success

    # AIO methods

    def submit_next_page_aio(self):
        """Puts future request into thread pool queue.

        Returns:
            True if successful, else False.
        """
        if self._finished_iteration or self._future:
            return False

        if self._include_summary:
            if 'summary' not in self.params:
                self.params['summary'] = True

        self._request_failed = False
        self._page_ready = False
        self._future = self._source_object.get_api_assured().call_future(
                self, 'GET', self._path, params=self.params,
                delay_next_call_for=self.delay_next_call_for)
        return True

    def read_next_page_aio(self, response):
        """
        Parses and returns the data in response.
        Gets the url of the next page in response and sets it as self._path attribute.

        :type response: facebook_business.asyncapi.FacebookAsyncResponse
        :return:
        """
        jresp = response.json()
        if not jresp:
            self._finished_iteration = True
            return 0

        if 'paging' in jresp and 'next' in jresp['paging']:
            self._path = jresp['paging']['next']
            pr = urlparse(jresp['paging']['next'])
            self.params = dict(parse_qsl(pr.query, keep_blank_values=True))

            # url components: scheme, netloc, url, query, fragment
            self._path = urlunsplit((pr.scheme, pr.netloc, pr.path, None, None))
        else:
            # Indicate if this was the last page
            self._finished_iteration = True

        if (
            self._include_summary and
            'summary' in jresp and
            'total_count' in jresp['summary']
        ):
            self._total_count = jresp['summary']['total_count']

        return self.build_objects_from_response(jresp)

    def build_objects_from_response(self, response):
        """
        Returns number of iterms in response.
        Gets response data and adds it to self._queue.
        """
        if not isinstance(response, string_types) and 'data' in response and \
                isinstance(response['data'], list):
            new_cnt = len(response['data'])
            if new_cnt <= 0:
                # API may return paging.next even for the last page
                self._finished_iteration = True

            elif new_cnt == 1 and (isinstance(response['data'][0], dict) and
                                   response['data'][0].get('category') == 'no_match'):
                # API may return [{'category': 'no_match'}] or something like that for the last page
                self._finished_iteration = True

            else:
                self._queue += response['data']

        else:
            self._finished_iteration = True
            if not isinstance(response, string_types) and 'data' in response:
                data = response['data']
            else:
                data = response
            self._queue.append(data)
            new_cnt = 1

        del self._response
        self._response = None

        return new_cnt

    # results processing and state changes

    def extract_results(self):
        """
        If future is done, removes it from the futures list, dict and iterator itself.
        Then, if future finished successfully,

        :rtype: facebook_business.asyncobjects.AioEdgeIterator
        """
        self._request_failed = False

        # If no future in iterator and the iterator is finished, returns the iterator itself.
        if not self._future:
            if self._finished_iteration:
                return self
            raise FacebookUnavailablePropertyException("first submit new async call")

        if self._future.done():
            result = self._future.result()
            self._source_object.get_api_assured().remove_from_futures(self)
            del self._future
            self._future = None

            if self.last_error_type == "rate limit error":
                self.delay_next_call_for -= 10
                if self.delay_next_call_for < 0:
                    self.delay_next_call_for = 0
            else:
                self.delay_next_call_for = 0

            self.last_yield = time.time()
            if result.is_failure():
                self.on_error(result)
            else:
                self.on_success(result)

        else:
            if not self._future.running() and not self._future.cancelled():
                # still not running, just pending in a queue
                self._request_failed = False
                self._page_ready = False
            elif self._future.cancelled():
                # was cancelled
                self.last_yield = time.time()
                self._request_failed = True
                self.delay_next_call_for = 0
                logger.warning("request {} was cancelled, endpoint: {}, params: {}".format(
                        str(self._future), str(self._path), self.params))
                self.last_error = Exception("request {} was cancelled, endpoint: {}, params: {}".format(
                        str(self._future), str(self._path), self.params))
                self._source_object.get_api_assured().remove_from_futures(self)
                del self._future
                self._future = None
            elif int(time.time() - self.last_yield) > 600:
                # running for too long
                self.future_timed_out()
                if self.errors_streak >= 5:
                    return self
                self.last_yield = time.time()
                self.recover_tmp_error(self.last_error)
            else:
                # just running
                self._request_failed = False
                self._page_ready = False
        return self

    def future_timed_out(self):
        self._request_failed = True
        self.delay_next_call_for = 0
        logger.warning("request {} stuck, time: {}, endpoint: {}, params: {}".format(
            str(self._future), int(time.time() - self.last_yield),
            str(self._path), self.params))
        self.last_error = FacebookApiTimeout(
            "request {} stuck, time: {}, endpoint: {}, params: {}".format(
                str(self._future), int(time.time() - self.last_yield),
                str(self._path), self.params))
        self._future.cancel()
        del self._future
        self._future = None

    def on_success(self, response):
        """
        Increments success streak and success count, assigns the next page of response as self._path,
        sets parameter ._page_ready as True.

        If success streak >= 10 and self.limit < starting limit, changes the limit of facebook result data.
        """
        self._response = response
        """:type: facebook_business.asyncapi.FacebookAsyncResponse"""
        self.success_streak += 1
        self.success_cnt += 1
        self.read_next_page_aio(self._response)
        self._page_ready = True

        if not self._finished_iteration:
            if self.success_streak >= 10 and self.last_error_type != "too much data error" \
                    and self.limit < self.starting_limit:
                self.change_the_next_page_limit(self.starting_limit, 2)

    def on_error(self, response):
        """
        If request is failed, submits next page, otherwise
        finishes iterations and sets the number of success streaks as 0.
        """
        if not self.is_exception_fatal(response):
            self.submit_next_page_aio()
        else:
            self._finished_iteration = True
            self.success_streak = 0

    # errors handling

    def is_exception_fatal(self, resp):
        """
        If it is unfatal error, tries to recover.
        If it is fatal error, sets _request_failed = True, logs it and sets _last_error = error.
        """
        exc = resp.error()
        if isinstance(exc, FacebookRequestError):
            if exc.api_error_code() == FacebookErrorCodes.temporary:
                self.recover_tmp_error(exc)
            elif exc.api_error_code() == FacebookErrorCodes.unknown:
                if exc.api_error_message().find("educe the amount of data") > 0:
                    self.recover_too_much_data_error(exc)
                else:
                    self.recover_unknown_error(exc)
            elif exc.api_error_code() == FacebookErrorCodes.too_much_data:
                self.recover_too_much_data_error(exc)
            elif exc.api_error_code() in (FacebookErrorCodes.rate_limit, FacebookErrorCodes.too_many_requests):
                self.recover_rate_limit_error(exc)
            elif not exc.is_body_json() or \
                    exc.api_error_code() == FacebookErrorCodes.report_cannot_be_accessed:
                self.recover_tmp_error(exc)
            else:
                self.recover_other_graph_error(exc)
        elif isinstance(exc, ConnectionError):
            self.recover_tmp_error(exc)
        else:
            if resp.body() and isinstance(resp.json(), (string_types, text_type, binary_type)):
                self.recover_tmp_error(exc)
            else:
                self.set_fatal_error(exc)
        return self._request_failed

    def set_fatal_error(self, exc, exception_type="fatal error"):
        self.set_last_error(exception_type)
        self.last_error = exc
        self._request_failed = True
        logger.warning("Fatal facebook error while loading url: {}, method GET with params: {}. "
                       "Caught an error: {}".format(str(self._path), str(self.params), str(exc)))

    def set_non_fatal_error(self, exc, exception_type="temporary error"):
        self.set_last_error(exception_type)
        self.last_error = exc
        logger.warning("While loading url: {}, method GET with params: {}. "
                       "Caught an error: {}".format(str(self._path), str(self.params), str(exc)))

    def recover_other_graph_error(self, exc):
        if exc._http_status and 400 <= exc._http_status < 500:
            err_type = "other FB graph error"
            if self.errors_streak >= self.unsupported_retries:
                self.set_fatal_error(exc)
            else:
                self.set_non_fatal_error(exc, err_type)
                self.delay_next_call_for = 10 + 10 * self.errors_streak
        else:
            self.recover_unknown_error(exc)

    def recover_tmp_error(self, exc):
        err_type = "temporary error"
        if self.errors_streak >= self.tmp_retries:
            self.set_fatal_error(exc, err_type)
        else:
            self.set_non_fatal_error(exc, err_type)
            self.delay_next_call_for = 5 + 10 * self.errors_streak
            self.change_the_next_page_limit()

    def recover_too_much_data_error(self, exc):
        err_type = "too much data error"
        if self.errors_streak >= self.too_much_data_retries:
            self.set_fatal_error(exc, err_type)
        else:
            self.set_non_fatal_error(exc, err_type)
            self.change_the_next_page_limit(lowest_limit=1)

    def recover_unknown_error(self, exc):
        err_type = "unknown error"
        if self.errors_streak >= self.unknown_retries:
            self.set_fatal_error(exc, err_type)
        else:
            self.set_non_fatal_error(exc, err_type)
            self.delay_next_call_for = 10 + 15 * self.errors_streak
            self.change_the_next_page_limit()

    def recover_rate_limit_error(self, exc):
        err_type = "rate limit error"
        self.set_non_fatal_error(exc, err_type)
        self.delay_next_call_for = rate_limiting_timeout(self.errors_streak)

    # error helpers

    def change_the_next_page_limit(self, new_limit=None, lowest_limit=2):
        if self._finished_iteration:
            return

        if new_limit is None:
            new_limit = int(self.limit / 2)
        self.limit = int(new_limit)
        if self.limit < lowest_limit:
            self.limit = lowest_limit
        elif self.limit < 1:
            self.limit = 1

        if 'limit' in self.params and self.params['limit']:
            self.params['limit'] = self.limit
        else:
            self.params['limit'] = self.starting_limit
        return

    def set_last_error(self, err_type):
        if self.last_error_type == err_type:
            self.errors_streak += 1
        else:
            self.errors_streak = 1
            self.last_error_type = err_type


def rate_limiting_timeout(attempt):
    upper_limit = 20 ** attempt
    if upper_limit >= 600:
        timeout = random.uniform(300, 900)
    else:
        timeout = random.uniform((60 + upper_limit) // 2, 60 + upper_limit)
    return timeout
