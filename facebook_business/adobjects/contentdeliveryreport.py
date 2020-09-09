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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ContentDeliveryReport(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ContentDeliveryReport, self).__init__()
        self._isContentDeliveryReport = True
        self._api = api

    class Field(AbstractObject.Field):
        content_name = 'content_name'
        content_url = 'content_url'
        creator_name = 'creator_name'
        creator_url = 'creator_url'
        estimated_impressions = 'estimated_impressions'

    class Platform:
        audience_network = 'AUDIENCE_NETWORK'
        facebook = 'FACEBOOK'
        hidden_aaa = 'HIDDEN_AAA'
        instagram = 'INSTAGRAM'
        messenger = 'MESSENGER'
        unknown = 'UNKNOWN'
        whatsapp = 'WHATSAPP'

    class Position:
        all_placements = 'ALL_PLACEMENTS'
        an_classic = 'AN_CLASSIC'
        facebook_groups_feed = 'FACEBOOK_GROUPS_FEED'
        facebook_stories = 'FACEBOOK_STORIES'
        feed = 'FEED'
        groups = 'GROUPS'
        hidden_aaa = 'HIDDEN_AAA'
        instagram_explore = 'INSTAGRAM_EXPLORE'
        instagram_igtv = 'INSTAGRAM_IGTV'
        instagram_stories = 'INSTAGRAM_STORIES'
        instant_article = 'INSTANT_ARTICLE'
        instream_video = 'INSTREAM_VIDEO'
        jobs_browser = 'JOBS_BROWSER'
        marketplace = 'MARKETPLACE'
        messenger_inbox = 'MESSENGER_INBOX'
        messenger_stories = 'MESSENGER_STORIES'
        others = 'OTHERS'
        rewarded_video = 'REWARDED_VIDEO'
        right_hand_column = 'RIGHT_HAND_COLUMN'
        search = 'SEARCH'
        status = 'STATUS'
        suggested_video = 'SUGGESTED_VIDEO'
        unknown = 'UNKNOWN'
        video_feeds = 'VIDEO_FEEDS'

    _field_types = {
        'content_name': 'string',
        'content_url': 'string',
        'creator_name': 'string',
        'creator_url': 'string',
        'estimated_impressions': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Platform'] = ContentDeliveryReport.Platform.__dict__.values()
        field_enum_info['Position'] = ContentDeliveryReport.Position.__dict__.values()
        return field_enum_info


