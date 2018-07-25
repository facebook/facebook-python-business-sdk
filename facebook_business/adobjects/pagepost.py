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

class PagePost(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPagePost = True
        super(PagePost, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        actions = 'actions'
        admin_creator = 'admin_creator'
        allowed_advertising_objectives = 'allowed_advertising_objectives'
        application = 'application'
        backdated_time = 'backdated_time'
        call_to_action = 'call_to_action'
        can_reply_privately = 'can_reply_privately'
        caption = 'caption'
        child_attachments = 'child_attachments'
        comments_mirroring_domain = 'comments_mirroring_domain'
        coordinates = 'coordinates'
        created_time = 'created_time'
        description = 'description'
        event = 'event'
        expanded_height = 'expanded_height'
        expanded_width = 'expanded_width'
        feed_targeting = 'feed_targeting'
        field_from = 'from'
        full_picture = 'full_picture'
        height = 'height'
        icon = 'icon'
        id = 'id'
        instagram_eligibility = 'instagram_eligibility'
        is_app_share = 'is_app_share'
        is_expired = 'is_expired'
        is_hidden = 'is_hidden'
        is_instagram_eligible = 'is_instagram_eligible'
        is_popular = 'is_popular'
        is_published = 'is_published'
        is_spherical = 'is_spherical'
        link = 'link'
        message = 'message'
        message_tags = 'message_tags'
        multi_share_end_card = 'multi_share_end_card'
        multi_share_optimized = 'multi_share_optimized'
        name = 'name'
        object_id = 'object_id'
        parent_id = 'parent_id'
        permalink_url = 'permalink_url'
        picture = 'picture'
        place = 'place'
        privacy = 'privacy'
        promotable_id = 'promotable_id'
        promotion_status = 'promotion_status'
        properties = 'properties'
        scheduled_publish_time = 'scheduled_publish_time'
        shares = 'shares'
        source = 'source'
        status_type = 'status_type'
        story = 'story'
        story_tags = 'story_tags'
        subscribed = 'subscribed'
        target = 'target'
        targeting = 'targeting'
        timeline_visibility = 'timeline_visibility'
        type = 'type'
        updated_time = 'updated_time'
        via = 'via'
        video_buying_eligibility = 'video_buying_eligibility'
        width = 'width'

    class BackdatedTimeGranularity:
        year = 'year'
        month = 'month'
        day = 'day'
        hour = 'hour'
        min = 'min'
        none = 'none'

    class CheckinEntryPoint:
        branding_checkin = 'BRANDING_CHECKIN'
        branding_status = 'BRANDING_STATUS'
        branding_photo = 'BRANDING_PHOTO'
        branding_other = 'BRANDING_OTHER'

    class Formatting:
        plaintext = 'PLAINTEXT'
        markdown = 'MARKDOWN'

    class PlaceAttachmentSetting:
        value_1 = '1'
        value_2 = '2'

    class PostSurfacesBlacklist:
        value_1 = '1'
        value_2 = '2'
        value_3 = '3'
        value_4 = '4'
        value_5 = '5'

    class PostingToRedspace:
        enabled = 'enabled'
        disabled = 'disabled'

    class TargetSurface:
        story = 'STORY'
        timeline = 'TIMELINE'

    class UnpublishedContentType:
        scheduled = 'SCHEDULED'
        draft = 'DRAFT'
        ads_post = 'ADS_POST'
        inline_created = 'INLINE_CREATED'
        published = 'PUBLISHED'

    class With:
        location = 'LOCATION'

    class FeedStoryVisibility:
        hidden = 'hidden'
        visible = 'visible'

    class TimelineVisibility:
        hidden = 'hidden'
        normal = 'normal'
        forced_allow = 'forced_allow'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
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
            target_class=PagePost,
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'attached_media': 'list<Object>',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'composer_session_id': 'string',
            'direct_share_status': 'unsigned int',
            'feed_story_visibility': 'feed_story_visibility_enum',
            'is_explicit_location': 'bool',
            'is_hidden': 'bool',
            'is_pinned': 'bool',
            'is_published': 'bool',
            'message': 'string',
            'og_action_type_id': 'string',
            'og_hide_object_attachment': 'bool',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'place': 'Object',
            'privacy': 'Object',
            'product_item': 'Object',
            'scheduled_publish_time': 'unsigned int',
            'should_sync_product_edit': 'bool',
            'source_type': 'string',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'tags': 'list<int>',
            'text_format_preset_id': 'string',
            'timeline_visibility': 'timeline_visibility_enum',
            'tracking': 'string',
        }
        enums = {
            'backdated_time_granularity_enum': PagePost.BackdatedTimeGranularity.__dict__.values(),
            'feed_story_visibility_enum': PagePost.FeedStoryVisibility.__dict__.values(),
            'timeline_visibility_enum': PagePost.TimelineVisibility.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
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
        'actions': 'list',
        'admin_creator': 'Object',
        'allowed_advertising_objectives': 'list<string>',
        'application': 'Object',
        'backdated_time': 'datetime',
        'call_to_action': 'Object',
        'can_reply_privately': 'bool',
        'caption': 'string',
        'child_attachments': 'list',
        'comments_mirroring_domain': 'string',
        'coordinates': 'Object',
        'created_time': 'datetime',
        'description': 'string',
        'event': 'Event',
        'expanded_height': 'unsigned int',
        'expanded_width': 'unsigned int',
        'feed_targeting': 'Object',
        'from': 'Object',
        'full_picture': 'string',
        'height': 'unsigned int',
        'icon': 'string',
        'id': 'string',
        'instagram_eligibility': 'string',
        'is_app_share': 'bool',
        'is_expired': 'bool',
        'is_hidden': 'bool',
        'is_instagram_eligible': 'bool',
        'is_popular': 'bool',
        'is_published': 'bool',
        'is_spherical': 'bool',
        'link': 'string',
        'message': 'string',
        'message_tags': 'list',
        'multi_share_end_card': 'bool',
        'multi_share_optimized': 'bool',
        'name': 'string',
        'object_id': 'string',
        'parent_id': 'string',
        'permalink_url': 'Object',
        'picture': 'string',
        'place': 'Object',
        'privacy': 'Object',
        'promotable_id': 'string',
        'promotion_status': 'string',
        'properties': 'list',
        'scheduled_publish_time': 'float',
        'shares': 'Object',
        'source': 'string',
        'status_type': 'string',
        'story': 'string',
        'story_tags': 'list',
        'subscribed': 'bool',
        'target': 'Profile',
        'targeting': 'Object',
        'timeline_visibility': 'string',
        'type': 'string',
        'updated_time': 'datetime',
        'via': 'Object',
        'video_buying_eligibility': 'list<string>',
        'width': 'unsigned int',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BackdatedTimeGranularity'] = PagePost.BackdatedTimeGranularity.__dict__.values()
        field_enum_info['CheckinEntryPoint'] = PagePost.CheckinEntryPoint.__dict__.values()
        field_enum_info['Formatting'] = PagePost.Formatting.__dict__.values()
        field_enum_info['PlaceAttachmentSetting'] = PagePost.PlaceAttachmentSetting.__dict__.values()
        field_enum_info['PostSurfacesBlacklist'] = PagePost.PostSurfacesBlacklist.__dict__.values()
        field_enum_info['PostingToRedspace'] = PagePost.PostingToRedspace.__dict__.values()
        field_enum_info['TargetSurface'] = PagePost.TargetSurface.__dict__.values()
        field_enum_info['UnpublishedContentType'] = PagePost.UnpublishedContentType.__dict__.values()
        field_enum_info['With'] = PagePost.With.__dict__.values()
        field_enum_info['FeedStoryVisibility'] = PagePost.FeedStoryVisibility.__dict__.values()
        field_enum_info['TimelineVisibility'] = PagePost.TimelineVisibility.__dict__.values()
        return field_enum_info
