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

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker
from facebook_business.adobjects.helpers.adpreviewmixin import AdPreviewMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdPreview(
    AdPreviewMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdPreview = True
        super(AdPreview, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        body = 'body'
        id = 'id'

    class AdFormat:
        right_column_standard = 'RIGHT_COLUMN_STANDARD'
        desktop_feed_standard = 'DESKTOP_FEED_STANDARD'
        mobile_feed_standard = 'MOBILE_FEED_STANDARD'
        mobile_feed_basic = 'MOBILE_FEED_BASIC'
        mobile_interstitial = 'MOBILE_INTERSTITIAL'
        mobile_banner = 'MOBILE_BANNER'
        mobile_medium_rectangle = 'MOBILE_MEDIUM_RECTANGLE'
        mobile_fullwidth = 'MOBILE_FULLWIDTH'
        mobile_native = 'MOBILE_NATIVE'
        instagram_standard = 'INSTAGRAM_STANDARD'
        instagram_story = 'INSTAGRAM_STORY'
        audience_network_instream_video = 'AUDIENCE_NETWORK_INSTREAM_VIDEO'
        audience_network_outstream_video = 'AUDIENCE_NETWORK_OUTSTREAM_VIDEO'
        audience_network_instream_video_mobile = 'AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE'
        audience_network_rewarded_video = 'AUDIENCE_NETWORK_REWARDED_VIDEO'
        instant_article_standard = 'INSTANT_ARTICLE_STANDARD'
        instream_video_desktop = 'INSTREAM_VIDEO_DESKTOP'
        instream_video_mobile = 'INSTREAM_VIDEO_MOBILE'
        messenger_mobile_inbox_media = 'MESSENGER_MOBILE_INBOX_MEDIA'
        suggested_video_desktop = 'SUGGESTED_VIDEO_DESKTOP'
        suggested_video_mobile = 'SUGGESTED_VIDEO_MOBILE'
        marketplace_mobile = 'MARKETPLACE_MOBILE'
        facebook_story_mobile = 'FACEBOOK_STORY_MOBILE'
        watch_feed_mobile = 'WATCH_FEED_MOBILE'

    class RenderType:
        fallback = 'FALLBACK'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'previews'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPreview,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'body': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AdFormat'] = AdPreview.AdFormat.__dict__.values()
        field_enum_info['RenderType'] = AdPreview.RenderType.__dict__.values()
        return field_enum_info


