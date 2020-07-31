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
from facebook_business.adobjects.helpers.adpreviewmixin import AdPreviewMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdPreview(
    AdPreviewMixin,
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdPreview, self).__init__()
        self._isAdPreview = True
        self._api = api

    class Field(AbstractObject.Field):
        body = 'body'

    class AdFormat:
        audience_network_instream_video = 'AUDIENCE_NETWORK_INSTREAM_VIDEO'
        audience_network_instream_video_mobile = 'AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE'
        audience_network_outstream_video = 'AUDIENCE_NETWORK_OUTSTREAM_VIDEO'
        audience_network_rewarded_video = 'AUDIENCE_NETWORK_REWARDED_VIDEO'
        desktop_feed_standard = 'DESKTOP_FEED_STANDARD'
        facebook_story_mobile = 'FACEBOOK_STORY_MOBILE'
        instagram_explore_contextual = 'INSTAGRAM_EXPLORE_CONTEXTUAL'
        instagram_explore_immersive = 'INSTAGRAM_EXPLORE_IMMERSIVE'
        instagram_standard = 'INSTAGRAM_STANDARD'
        instagram_story = 'INSTAGRAM_STORY'
        instant_article_recirculation_ad = 'INSTANT_ARTICLE_RECIRCULATION_AD'
        instant_article_standard = 'INSTANT_ARTICLE_STANDARD'
        instream_video_desktop = 'INSTREAM_VIDEO_DESKTOP'
        instream_video_image = 'INSTREAM_VIDEO_IMAGE'
        instream_video_mobile = 'INSTREAM_VIDEO_MOBILE'
        job_browser_desktop = 'JOB_BROWSER_DESKTOP'
        job_browser_mobile = 'JOB_BROWSER_MOBILE'
        marketplace_mobile = 'MARKETPLACE_MOBILE'
        messenger_mobile_inbox_media = 'MESSENGER_MOBILE_INBOX_MEDIA'
        messenger_mobile_story_media = 'MESSENGER_MOBILE_STORY_MEDIA'
        mobile_banner = 'MOBILE_BANNER'
        mobile_feed_basic = 'MOBILE_FEED_BASIC'
        mobile_feed_standard = 'MOBILE_FEED_STANDARD'
        mobile_fullwidth = 'MOBILE_FULLWIDTH'
        mobile_interstitial = 'MOBILE_INTERSTITIAL'
        mobile_medium_rectangle = 'MOBILE_MEDIUM_RECTANGLE'
        mobile_native = 'MOBILE_NATIVE'
        right_column_standard = 'RIGHT_COLUMN_STANDARD'
        suggested_video_desktop = 'SUGGESTED_VIDEO_DESKTOP'
        suggested_video_mobile = 'SUGGESTED_VIDEO_MOBILE'
        watch_feed_mobile = 'WATCH_FEED_MOBILE'

    class RenderType:
        fallback = 'FALLBACK'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'previews'

    _field_types = {
        'body': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AdFormat'] = AdPreview.AdFormat.__dict__.values()
        field_enum_info['RenderType'] = AdPreview.RenderType.__dict__.values()
        return field_enum_info


