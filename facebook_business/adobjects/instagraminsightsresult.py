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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class InstagramInsightsResult(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isInstagramInsightsResult = True
        super(InstagramInsightsResult, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        description = 'description'
        id = 'id'
        name = 'name'
        period = 'period'
        title = 'title'
        values = 'values'

    class Metric:
        carousel_album_engagement = 'carousel_album_engagement'
        carousel_album_impressions = 'carousel_album_impressions'
        carousel_album_reach = 'carousel_album_reach'
        carousel_album_saved = 'carousel_album_saved'
        carousel_album_video_views = 'carousel_album_video_views'
        engagement = 'engagement'
        exits = 'exits'
        impressions = 'impressions'
        reach = 'reach'
        replies = 'replies'
        saved = 'saved'
        taps_back = 'taps_back'
        taps_forward = 'taps_forward'
        video_views = 'video_views'

    class Period:
        day = 'day'
        days_28 = 'days_28'
        lifetime = 'lifetime'
        month = 'month'
        week = 'week'

    _field_types = {
        'description': 'string',
        'id': 'string',
        'name': 'string',
        'period': 'string',
        'title': 'string',
        'values': 'list<InstagramInsightsValue>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Metric'] = InstagramInsightsResult.Metric.__dict__.values()
        field_enum_info['Period'] = InstagramInsightsResult.Period.__dict__.values()
        return field_enum_info


