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

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.helpers.adpreviewmixin import AdPreviewMixin

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
        right_column_standard = 'RIGHT_COLUMN_STANDARD'
        desktop_feed_standard = 'DESKTOP_FEED_STANDARD'
        mobile_feed_standard = 'MOBILE_FEED_STANDARD'
        mobile_feed_basic = 'MOBILE_FEED_BASIC'
        mobile_interstitial = 'MOBILE_INTERSTITIAL'
        mobile_banner = 'MOBILE_BANNER'
        mobile_medium_rectangle = 'MOBILE_MEDIUM_RECTANGLE'
        mobile_native = 'MOBILE_NATIVE'
        instagram_standard = 'INSTAGRAM_STANDARD'
        audience_network_outstream_video = 'AUDIENCE_NETWORK_OUTSTREAM_VIDEO'

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
        return field_enum_info
