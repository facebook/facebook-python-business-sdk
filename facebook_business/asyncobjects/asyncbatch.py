from typing import List
from facebook_business.adobjects.asyncsession import AsyncSession
from facebook_business.api import FacebookAdsApiBatch, FacebookResponse


class FacebookAdsAsyncApiBatch(FacebookAdsApiBatch):
    def __init__(self, api, success=None, failure=None):
        super().__init__(api, success, failure)
        self.names = []

    """
    https://developers.facebook.com/docs/graph-api/asynchronous-batch-requests
    """
    def add(
            self,
            method,
            relative_path,
            name=None,
            depends_on=None,
            params=None,
            headers=None,
            files=None,
            success=None,
            failure=None,
            request=None,
    ):
        """Adds a call to the batch.
        Args:
            method: The HTTP method name (e.g. 'GET').
            name: Async batch calls *MUST* specify a unique name
            relative_path: A tuple of path tokens or a relative URL string.
                A tuple will be translated to a url as follows:
                    <graph url>/<tuple[0]>/<tuple[1]>...
                It will be assumed that if the path is not a string, it will be
                iterable.
            depends_on (optional): Specifying dependencies. Must be *ONE* batch-task-id name
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
            request (optional): The APIRequest object
        Returns:
            A dictionary describing the call.

        """

        if name is None or len(name) == 0:
            raise TypeError("Providing a name is required for async batch API!")

        # enforce unique batch-names
        if name in self.names:
            raise ValueError("You must provide unique batch names!")
        self.names.append(name)

        call = super(FacebookAdsAsyncApiBatch, self).add(
            method,
            relative_path,
            params,
            headers,
            files,
            success,
            failure,
            request,
        )

        call['name'] = name

        # register tasks this batch depends on in order
        if isinstance(depends_on, str):
            if depends_on not in self.names:
                raise ValueError("Register dependent task first when using depends_on!")
            call['depends_on'] = depends_on

        return call

    def execute(self) -> List[AsyncSession]:
        """Makes a batch call to the async api associated with this batch object.
        For each individual call response, calls the success or failure callback
        function if they were specified.
        Note: Does not explicitly raise exceptions. Individual exceptions won't
        be thrown for each call that fails. The success and failure callback
        functions corresponding to a call should handle its success or failure.

        :raises Exception If facebook api call itself was not successful
        :raises ValueError If one of the arguments invalidates method invariants about unique and in order batch-names
        :returns List[AsyncSession]

        TODO: implement success/error callbacks
        """
        if not self._batch:
            return None
        method = 'POST'
        path = tuple()
        params = {'asyncbatch': self._batch}
        files = {}
        for call_files in self._files:
            if call_files:
                files.update(call_files)

        fb_async_session_response: FacebookResponse = self._api.call(
            method,
            path,
            params=params,
            files=files,
        )

        if fb_async_session_response.is_failure():
            raise fb_async_session_response.error()

        async_sessions = fb_async_session_response.json().get('async_sessions', [])

        return [AsyncSession(fbid=session.get('id')) for session in async_sessions]
