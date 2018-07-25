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

from facebook_business.adobjects.videothumbnail import VideoThumbnail
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject

from facebook_business.video_uploader import (
    VideoUploader,
    VideoUploadRequest,
    VideoEncodingStatusChecker,
)
from facebook_business.exceptions import (
    FacebookBadObjectError,
    FacebookError,
)

class AdVideo(AbstractCrudObject):

    class Field(object):
        filepath = 'filepath'
        id = 'id'
        slideshow_spec = 'slideshow_spec'

    def remote_create(
        self,
        batch=None,
        failure=None,
        params=None,
        success=None,
    ):
        """
        Uploads filepath and creates the AdVideo object from it.
        It has same arguments as AbstractCrudObject.remote_create except it
        does not have the files argument but requires the 'filepath' property
        to be defined.
        """
        if (self.Field.slideshow_spec in self and
        self[self.Field.slideshow_spec] is not None):
            request = VideoUploadRequest(self.get_api_assured())
            request.setParams(params={'slideshow_spec': {
                'images_urls': self[self.Field.slideshow_spec]['images_urls'],
                'duration_ms': self[self.Field.slideshow_spec]['duration_ms'],
                'transition_ms': self[self.Field.slideshow_spec]['transition_ms'],
            }})
            response = request.send((self.get_parent_id_assured(), 'advideos')).json()
        elif not (self.Field.filepath in self):
            raise FacebookBadObjectError(
                "AdVideo requires a filepath or slideshow_spec to be defined.",
            )
        else:
            video_uploader = VideoUploader()
            response = video_uploader.upload(self)
        self._set_data(response)
        return response

    def waitUntilEncodingReady(self, interval=30, timeout=600):
        if 'id' not in self:
            raise FacebookError(
                'Invalid Video ID',
            )
        VideoEncodingStatusChecker.waitUntilReady(
            self.get_api_assured(),
            self['id'],
            interval,
            timeout,
        )

    def get_thumbnails(self, fields=None, params=None):
        """
        Returns all the thumbnails associated with the ad video
        """
        return self.iterate_edge(VideoThumbnail, fields, params, endpoint='thumbnails')
