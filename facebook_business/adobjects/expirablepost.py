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

class ExpirablePost(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isExpirablePost = True
        super(ExpirablePost, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        admin_creator = 'admin_creator'
        can_republish = 'can_republish'
        content_type = 'content_type'
        creation_time = 'creation_time'
        expiration = 'expiration'
        feed_audience_description = 'feed_audience_description'
        feed_targeting = 'feed_targeting'
        id = 'id'
        message = 'message'
        modified_time = 'modified_time'
        og_action_summary = 'og_action_summary'
        permalink_url = 'permalink_url'
        place = 'place'
        privacy_description = 'privacy_description'
        promotion_info = 'promotion_info'
        scheduled_publish_time = 'scheduled_publish_time'
        story_token = 'story_token'
        thumbnail = 'thumbnail'
        video_id = 'video_id'

    _field_types = {
        'admin_creator': 'User',
        'can_republish': 'bool',
        'content_type': 'string',
        'creation_time': 'datetime',
        'expiration': 'Object',
        'feed_audience_description': 'string',
        'feed_targeting': 'Targeting',
        'id': 'string',
        'message': 'string',
        'modified_time': 'datetime',
        'og_action_summary': 'string',
        'permalink_url': 'string',
        'place': 'Place',
        'privacy_description': 'string',
        'promotion_info': 'Object',
        'scheduled_publish_time': 'datetime',
        'story_token': 'string',
        'thumbnail': 'string',
        'video_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


