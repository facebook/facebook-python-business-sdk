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
video uploader that is used to upload video to adaccount
"""

from facebookads.exceptions import FacebookError


class VideoUploader(object):
    """
    Video Uploader that can upload videos to adaccount
    """

    def __init__(self):
        self.session = None

    @classmethod
    def upload(self, file_path):
        """
        Upload the given video file.

        Args:
            file_path(required): The path of the file
        """
        # Check there is no existing session
        if self.session:
            raise FacebookError(
                "There is already an upload session for this video uploader"
            )

        # Initiate an upload session

        # subscribe the session from
        return


class VideoUploadSession(object):

    def __init__(self):
        # Setup start request manager
        self._start_request_manager = VideoUploadStartRequestManager()

        # Setup receive request manager
        self._receive_request_manager = VideoUploadReceiveRequestManager()

        # Setup post request manager
        self._post_request_manager = VideoUploadPostRequestManager()

    @classmethod
    def start(self, file_path):
        # Validate the file

        # Run start request manager

        # Run receive request manager

        # Run post request manager

        return


class VideoUploadStartRequestManager(object):

    @classmethod
    def send_request(self, context):
        """
        send start request with the given context
        """
        # Init a VideoUploadRequest and send the request


class VideoUploadReceiveRequestManager(object):

    @classmethod
    def send_request(self, context):
        """
        send receive request with the given context
        """
        # Init a VideoUploadRequest

        # Parse the context

        # send the request


class VideoUploadPostRequestManager(object):

    @classmethod
    def send_request(self, context):
        """
        send receive request with the given context
        """
        # Init a VideoUploadRequest

        # Parse the context

        # send the request


class VideoUploadRequestContext(object):
    """
    Upload request context that contains the param data
    """


class VideoUploadRequest(object):

    @classmethod
    def send(self, uri, params):
        """
        send the current request
        """
