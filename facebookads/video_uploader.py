# Copyright 2015 Facebook, Inc.

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
video uploader that is used to upload video to adaccount
"""

from facebookads.exceptions import FacebookError
from abc import ABCMeta, abstractmethod

import os
import ntpath


class VideoUploader(object):
    """
    Video Uploader that can upload videos to adaccount
    """

    def __init__(self):
        self._session = None

    def upload(self, video):
        """
        Upload the given video file.

        Args:
            file_path(required): The path of the file
        """
        # Check there is no existing session
        if self._session:
            raise FacebookError(
                "There is already an upload session for this video uploader"
            )

        # Initiate an upload session
        self._session = VideoUploadSession(video)
        return self._session.start()


class VideoUploadSession(object):

    def __init__(self, video):
        self._video = video
        self._api = video.get_api_assured()
        self._file_path = video[video.Field.filepath]
        self._account_id = video.get_parent_id_assured()
        # Setup start request manager
        self._start_request_manager = VideoUploadStartRequestManager(
            self._api,
        )

        # Setup receive request manager
        self._receive_request_manager = VideoUploadReceiveRequestManager(
            self._api,
        )

        # Setup post request manager
        self._post_request_manager = VideoUploadPostRequestManager(
            self._api,
        )

    def start(self):
        # TODO: Validate the file

        # Run start request manager
        print "===Start uploading video==="
        start_response = self._start_request_manager.send_request(
            self.getStartRequestContext(),
        ).json()
        self._start_offset = int(start_response['start_offset'])
        self._end_offset = int(start_response['end_offset'])
        self._session_id = start_response['id']
        video_id = start_response['video_id']

        # Run receive request manager
        self._receive_request_manager.send_request(
            self.getReceiveRequestContext(),
        )

        # Run post request manager
        response = self._post_request_manager.send_request(
            self.getPostRequestContext(),
        )
        if response.json()['success']:
            print '===Video uploaded successfully==='
            print 'Video ID: ' + video_id
        else:
            print '===Failed to upload video==='

        # Populate the video info
        body = response.json().copy()
        body['id'] = video_id
        del body['success']

        return body

    def getStartRequestContext(self):
        context = VideoUploadRequestContext()
        context.file_name = ntpath.basename(self._file_path)
        context.file_size = os.path.getsize(self._file_path)
        context.account_id = self._account_id
        return context

    def getReceiveRequestContext(self):
        context = VideoUploadRequestContext()
        context.session_id = self._session_id
        context.start_offset = self._start_offset
        context.end_offset = self._end_offset
        context.file_path = self._file_path
        context.account_id = self._account_id
        return context

    def getPostRequestContext(self):
        context = VideoUploadRequestContext()
        context.session_id = self._session_id
        context.account_id = self._account_id
        return context


class VideoUploadRequestManager(object):
    """
    Abstract class for request managers
    """
    __metaclass__ = ABCMeta

    def __init__(self, api):
        self._api = api

    @abstractmethod
    def send_request(self, context):
        """
        send upload request
        """
        pass

    @abstractmethod
    def getParamsFromContext(self, context):
        """
        get upload params from context
        """
        pass


class VideoUploadStartRequestManager(VideoUploadRequestManager):

    def send_request(self, context):
        """
        send start request with the given context
        """
        # Init a VideoUploadRequest and send the request
        request = VideoUploadRequest(self._api)
        request.setParams(self.getParamsFromContext(context))
        return request.send((context.account_id, 'advideos'))

    def getParamsFromContext(self, context):
        return {
            'name': context.file_name,
            'file_size': context.file_size,
            'upload_phase': 'start',
        }


class VideoUploadReceiveRequestManager(VideoUploadRequestManager):

    def send_request(self, context):
        """
        send receive request with the given context
        """
        # Init a VideoUploadRequest
        request = VideoUploadRequest(self._api)
        self._start_offset = context.start_offset
        self._end_offset = context.end_offset
        filepath = context.file_path
        # While the there are still more chunks to send
        while self._start_offset != self._end_offset:
            # Read a chunk of file
            f = open(filepath, 'rb')
            f.seek(self._start_offset)
            chunk = f.read(self._end_offset - self._start_offset)
            context.start_offset = self._start_offset
            context.end_offset = self._end_offset
            # Parse the context
            request.setParams(
                self.getParamsFromContext(context),
                {'video_file_chunk': (
                    context.file_path,
                    chunk,
                    'multipart/form-data',
                )},
            )
            # send the request
            response = request.send(
                (context.account_id, 'advideos')
            ).json()
            self._start_offset = int(response['start_offset'])
            self._end_offset = int(response['end_offset'])
            # TODO: add retry mechanism
        return response

    def getParamsFromContext(self, context):
        return {
            'upload_phase': 'receive',
            'start_offset': context.start_offset,
            'chunk_session_id': context.session_id,
        }


class VideoUploadPostRequestManager(VideoUploadRequestManager):

    def send_request(self, context):
        """
        send receive request with the given context
        """
        # Init a VideoUploadRequest
        request = VideoUploadRequest(self._api)

        # Parse the context
        request.setParams(self.getParamsFromContext(context))

        # send the request
        return request.send((context.account_id, 'advideos'))

    def getParamsFromContext(self, context):
        return {
            'upload_phase': 'post',
            'chunk_session_id': context.session_id,
        }


class VideoUploadRequestContext(object):
    """
    Upload request context that contains the param data
    """

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def file_name(self):
        return self._name

    @file_name.setter
    def file_name(self, name):
        self._name = name

    @property
    def file_size(self):
        return self._size

    @file_size.setter
    def file_size(self, size):
        self._size = size

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        self._session_id = session_id

    @property
    def start_offset(self):
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        self._start_offset = start_offset

    @property
    def end_offset(self):
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        self._end_offset = end_offset

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    @property
    def file_path(self):
        return self._filepath

    @file_path.setter
    def file_path(self, filepath):
        self._filepath = filepath


class VideoUploadRequest(object):

    def __init__(self, api):
        self._params = None
        self._files = None
        self._api = api

    def send(self, path):
        """
        send the current request
        """
        return self._api.call(
            'POST',
            path,
            params=self._params,
            files=self._files,
            url_override='https://graph-video.facebook.com',
        )

    def setParams(self, params, files=None):
        self._params = params
        self._files = files
