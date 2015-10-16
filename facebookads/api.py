# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""
api module contains classes that make http requests to Facebook's graph API.
"""

from facebookads.exceptions import (
    FacebookRequestError,
    FacebookBadObjectError,
)
from facebookads.session import FacebookSession
from facebookads.utils import urls
from facebookads.utils import version
import json
import six
import collections
import re
from six.moves import http_client


class FacebookResponse(object):

    """Encapsulates an http response from Facebook's Graph API."""

    def __init__(self, body=None, http_status=None, headers=None, call=None):
        """Initializes the object's internal data.

        Args:
            body (optional): The response body as text.
            http_status (optional): The http status code.
            headers (optional): The http headers.
            call (optional): The original call that was made.
        """
        self._body = body
        self._http_status = http_status
        self._headers = headers or {}
        self._call = call

    def body(self):
        """Returns the response body."""
        return self._body

    def json(self):
        """Returns the response body -- in json if possible."""
        try:
            return json.loads(self._body)
        except (TypeError, ValueError):
            return self._body

    def headers(self):
        """Return the response headers."""
        return self._headers

    def etag(self):
        """Returns the ETag header value if it exists."""
        return self._headers.get('ETag')

    def status(self):
        """Returns the http status code of the response."""
        return self._http_status

    def is_success(self):
        """Returns boolean indicating if the call was successful."""

        json_body = self.json()

        if isinstance(json_body, collections.Mapping) and 'error' in json_body:
            # Is a dictionary, has error in it
            return False
        elif bool(json_body):
            # Has body and no error
            if 'success' in json_body:
                return json_body['success']
            return True
        elif self._http_status == http_client.NOT_MODIFIED:
            # ETAG Hit
            return True
        elif self._http_status == http_client.OK:
            # HTTP Okay
            return True
        else:
            # Something else
            return False

    def is_failure(self):
        """Returns boolean indicating if the call failed."""
        return not self.is_success()

    def error(self):
        """
        Returns a FacebookRequestError (located in the exceptions module) with
        an appropriate debug message.
        """
        if self.is_failure():
            return FacebookRequestError(
                "Call was not successful",
                self._call,
                self.status(),
                self.headers(),
                self.body()
            )
        else:
            return None


class FacebookAdsApi(object):

    """Encapsulates session attributes and methods to make API calls.

    Attributes:
        SDK_VERSION (class): indicating sdk version.
        HTTP_METHOD_GET (class): HTTP GET method name.
        HTTP_METHOD_POST (class): HTTP POST method name
        HTTP_METHOD_DELETE (class): HTTP DELETE method name
        HTTP_DEFAULT_HEADERS (class): Default HTTP headers for requests made by
            this sdk.
    """

    SDK_VERSION = version.get_version()

    API_VERSION = 'v' + str(re.sub('^(\d+\.\d+)\.\d+$', '\g<1>', SDK_VERSION))

    HTTP_METHOD_GET = 'GET'

    HTTP_METHOD_POST = 'POST'

    HTTP_METHOD_DELETE = 'DELETE'

    HTTP_DEFAULT_HEADERS = {
        'User-Agent': "fb-python-ads-api-sdk-%s" % SDK_VERSION,
    }

    _default_api = None
    _default_account_id = None

    def __init__(self, session):
        """Initializes the api instance.

        Args:
            session: FacebookSession object that contains a requests interface
                and attribute GRAPH (the Facebook GRAPH API URL).
        """
        self._session = session
        self._num_requests_succeeded = 0
        self._num_requests_attempted = 0

    def get_num_requests_attempted(self):
        """Returns the number of calls attempted."""
        return self._num_requests_attempted

    def get_num_requests_succeeded(self):
        """Returns the number of calls that succeeded."""
        return self._num_requests_succeeded

    @classmethod
    def init(
        cls,
        app_id=None,
        app_secret=None,
        access_token=None,
        account_id=None,
        pool_maxsize=10,
        max_retries=0
    ):
        session = FacebookSession(app_id, app_secret, access_token,
                                  pool_maxsize, max_retries)
        api = cls(session)
        cls.set_default_api(api)

        if account_id:
            cls.set_default_account_id(account_id)

    @classmethod
    def set_default_api(cls, api_instance):
        """Sets the default api instance.

        When making calls to the api, objects will revert to using the default
        api if one is not specified when initializing the objects.

        Args:
            api_instance: The instance which to set as default.
        """
        cls._default_api = api_instance

    @classmethod
    def get_default_api(cls):
        """Returns the default api instance."""
        return cls._default_api

    @classmethod
    def set_default_account_id(cls, account_id):
        account_id = str(account_id)
        if account_id.find('act_') == -1:
            raise ValueError(
                "Account ID provided in FacebookAdsApi.set_default_account_id "
                "expects a string that begins with 'act_'"
            )
        cls._default_account_id = account_id

    @classmethod
    def get_default_account_id(cls):
        return cls._default_account_id

    def call(
        self,
        method,
        path,
        params=None,
        headers=None,
        files=None,
        url_override=None,
        api_version=None,
    ):
        """Makes an API call.

        Args:
            method: The HTTP method name (e.g. 'GET').
            path: A tuple of path tokens or a full URL string. A tuple will
                be translated to a url as follows:
                graph_url/tuple[0]/tuple[1]...
                It will be assumed that if the path is not a string, it will be
                iterable.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
            headers (optional): A mapping of request headers where a key is the
                header name and its value is the header value.
            files (optional): An optional mapping of file names to binary open
                file objects. These files will be attached to the request.

        Returns:
            A FacebookResponse object containing the response body, headers,
            http status, and summary of the call that was made.

        Raises:
            FacebookResponse.error() if the request failed.
        """
        if not params:
            params = {}
        if not headers:
            headers = {}
        if not files:
            files = {}

        if api_version and not re.search('v[0-9]+\.[0-9]+', api_version):
            raise FacebookBadObjectError(
                'Please provide the API version in the following format: %s'
                % self.API_VERSION
            )

        self._num_requests_attempted += 1

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

        # Get request response and encapsulate it in a FacebookResponse
        if method in ('GET', 'DELETE'):
            response = self._session.requests.request(
                method,
                path,
                params=params,
                headers=headers,
                files=files,
            )
        else:
            response = self._session.requests.request(
                method,
                path,
                data=params,
                headers=headers,
                files=files,
            )
        fb_response = FacebookResponse(
            body=response.text,
            headers=response.headers,
            http_status=response.status_code,
            call={
                'method': method,
                'path': path,
                'params': params,
                'headers': headers,
                'files': files,
            },
        )

        if fb_response.is_failure():
            raise fb_response.error()

        self._num_requests_succeeded += 1
        return fb_response

    def new_batch(self):
        """
        Returns a new FacebookAdsApiBatch, which when executed will go through
        this api.
        """
        return FacebookAdsApiBatch(api=self)


class FacebookAdsApiBatch(object):

    """
    Exposes methods to build a sequence of calls which can be executed with
    a single http request.

    Note: Individual exceptions won't be thrown for each call that fails.
        The success and failure callback functions corresponding to a call
        should handle its success or failure.
    """

    def __init__(self, api):
        self._api = api
        self._files = []
        self._batch = []
        self._success_callbacks = []
        self._failure_callbacks = []

    def __len__(self):
        return len(self._batch)

    def add(
        self,
        method,
        relative_path,
        params=None,
        headers=None,
        files=None,
        success=None,
        failure=None,
    ):
        """Adds a call to the batch.

        Args:
            method: The HTTP method name (e.g. 'GET').
            relative_path: A tuple of path tokens or a relative URL string.
                A tuple will be translated to a url as follows:
                    <graph url>/<tuple[0]>/<tuple[1]>...
                It will be assumed that if the path is not a string, it will be
                iterable.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
            headers (optional): A mapping of request headers where a key is the
                header name and its value is the header value.
            files (optional): An optional mapping of file names to binary open
                file objects. These files will be attached to the request.
            success (optional): A callback function which will be called with
                the FacebookResponse of this call if the call succeeded.
            failure (optional): A callback function which will be called with
                the FacebookResponse of this call if the call failed.

        Returns:
            A dictionary describing the call.
        """
        if not isinstance(relative_path, six.string_types):
            relative_url = '/'.join(relative_path)
        else:
            relative_url = relative_path

        call = {
            'method': method,
            'relative_url': relative_url,
        }

        if params:
            params = _top_level_param_json_encode(params)
            keyvals = ['%s=%s' % (key, urls.quote_with_encoding(value))
                       for key, value in params.items()]
            call['body'] = '&'.join(keyvals)

        if files:
            call['attached_files'] = ','.join(files.keys())

        if headers:
            call['headers'] = []
            for header in headers:
                batch_formatted_header = {}
                batch_formatted_header['name'] = header
                batch_formatted_header['value'] = headers[header]
                call['headers'].append(batch_formatted_header)

        self._batch.append(call)
        self._files.append(files)
        self._success_callbacks.append(success)
        self._failure_callbacks.append(failure)

        return call

    def execute(self):
        """Makes a batch call to the api associated with this object.

        For each individual call response, calls the success or failure callback
        function if they were specified.

        Note: Does not explicitly raise exceptions. Individual exceptions won't
        be thrown for each call that fails. The success and failure callback
        functions corresponding to a call should handle its success or failure.

        Returns:
            If some of the calls have failed, returns  a new FacebookAdsApiBatch
            object with those calls. Otherwise, returns None.
        """
        if not self._batch:
            return None
        method = 'POST'
        path = tuple()
        params = {'batch': self._batch}
        files = {}
        for call_files in self._files:
            if call_files:
                files.update(call_files)

        fb_response = self._api.call(
            method,
            path,
            params=params,
            files=files,
        )

        responses = fb_response.json()
        retry_indices = []

        for index, response in enumerate(responses):
            if response:
                body = response.get('body')
                code = response.get('code')
                headers = response.get('headers')

                inner_fb_response = FacebookResponse(
                    body=body,
                    headers=headers,
                    http_status=code,
                    call=self._batch[index],
                )

                if inner_fb_response.is_success():
                    if self._success_callbacks[index]:
                        self._success_callbacks[index](inner_fb_response)
                elif self._failure_callbacks[index]:
                    self._failure_callbacks[index](inner_fb_response)
            else:
                retry_indices.append(index)

        if retry_indices:
            new_batch = self.__class__(self._api)
            new_batch._files = [self._files[index] for index in retry_indices]
            new_batch._batch = [self._batch[index] for index in retry_indices]
            new_batch._success_callbacks = [self._success_callbacks[index]
                                            for index in retry_indices]
            new_batch._failure_callbacks = [self._failure_callbacks[index]
                                            for index in retry_indices]
            return new_batch
        else:
            return None


def _top_level_param_json_encode(params):
    params = params.copy()

    for param, value in params.items():
        if (
            isinstance(value, (collections.Mapping, collections.Sequence, bool))
            and not isinstance(value, six.string_types)
        ):
            params[param] = json.dumps(
                value,
                sort_keys=True,
                separators=(',', ':'),
            )
        else:
            params[param] = value

    return params
