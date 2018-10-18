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

class Post(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPost = True
        super(Post, self).__init__(fbid, parent_id, api)

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
            target_class=Post,
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
            'privacy': 'Object',
            'composer_session_id': 'string',
            'message': 'string',
            'is_hidden': 'bool',
            'is_published': 'bool',
            'scheduled_publish_time': 'unsigned int',
            'is_pinned': 'bool',
            'timeline_visibility': 'timeline_visibility_enum',
            'feed_story_visibility': 'feed_story_visibility_enum',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'tracking': 'string',
            'source_type': 'string',
            'attached_media': 'list<Object>',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_suggestion_mechanism': 'string',
            'og_hide_object_attachment': 'bool',
            'tags': 'list<int>',
            'og_set_profile_badge': 'bool',
            'place': 'Object',
            'is_explicit_location': 'bool',
            'product_item': 'Object',
            'should_sync_product_edit': 'bool',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
            'sponsor_relationship': 'unsigned int',
            'text_format_preset_id': 'string',
        }
        enums = {
            'timeline_visibility_enum': Post.TimelineVisibility.__dict__.values(),
            'feed_story_visibility_enum': Post.FeedStoryVisibility.__dict__.values(),
            'backdated_time_granularity_enum': Post.BackdatedTimeGranularity.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Post,
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

    def get_attachments(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/attachments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_comments(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.comment import Comment
        param_types = {
            'filter': 'filter_enum',
            'order': 'order_enum',
            'live_filter': 'live_filter_enum',
            'since': 'datetime',
        }
        enums = {
            'filter_enum': Comment.Filter.__dict__.values(),
            'order_enum': Comment.Order.__dict__.values(),
            'live_filter_enum': Comment.LiveFilter.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
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

    def create_comment(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.comment import Comment
        param_types = {
            'message': 'string',
            'tracking': 'string',
            'nectar_module': 'string',
            'attachment_id': 'string',
            'attachment_url': 'string',
            'attachment_share_url': 'string',
            'post_id': 'string',
            'parent_comment_id': 'Object',
            'comment': 'string',
            'feedback_source': 'string',
            'comment_privacy_value': 'comment_privacy_value_enum',
        }
        enums = {
            'comment_privacy_value_enum': Comment.CommentPrivacyValue.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
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

    def get_dynamic_posts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.rtbdynamicpost import RTBDynamicPost
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/dynamic_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=RTBDynamicPost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=RTBDynamicPost, api=self._api),
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

    def get_edit_actions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/edit_actions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, pending=False):
        from facebook_business.adobjects.insightsresult import InsightsResult
        if is_async:
          return self.get_insights_async(fields, params, batch, pending)
        param_types = {
            'since': 'datetime',
            'until': 'datetime',
            'metric': 'list<Object>',
            'period': 'period_enum',
            'show_permission_error': 'bool',
            'date_preset': 'date_preset_enum',
        }
        enums = {
            'period_enum': InsightsResult.Period.__dict__.values(),
            'date_preset_enum': InsightsResult.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InsightsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InsightsResult, api=self._api),
            include_summary=False,
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

    def delete_likes(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tracking': 'string',
            'nectar_module': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_likes(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profile import Profile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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

    def create_like(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tracking': 'string',
            'nectar_module': 'string',
            'feedback_source': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Post,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Post, api=self._api),
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

    def create_photo(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.photo import Photo
        param_types = {
            'aid': 'string',
            'caption': 'string',
            'url': 'string',
            'uid': 'int',
            'profile_id': 'int',
            'target_id': 'int',
            'checkin_id': 'Object',
            'vault_image_id': 'string',
            'tags': 'list<Object>',
            'place': 'Object',
            'is_explicit_place': 'bool',
            'is_explicit_location': 'bool',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_suggestion_mechanism': 'string',
            'og_set_profile_badge': 'bool',
            'privacy': 'Object',
            'targeting': 'Object',
            'feed_targeting': 'Object',
            'no_story': 'bool',
            'published': 'bool',
            'offline_id': 'unsigned int',
            'attempt': 'unsigned int',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'time_since_original_post': 'unsigned int',
            'filter_type': 'unsigned int',
            'scheduled_publish_time': 'unsigned int',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'full_res_is_coming_later': 'bool',
            'composer_session_id': 'string',
            'qn': 'string',
            'manual_privacy': 'bool',
            'audience_exp': 'bool',
            'proxied_app_id': 'string',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'user_selected_tags': 'bool',
            'allow_spherical_photo': 'bool',
            'spherical_metadata': 'map',
            'initial_view_heading_override_degrees': 'unsigned int',
            'initial_view_pitch_override_degrees': 'unsigned int',
            'initial_view_vertical_fov_override_degrees': 'unsigned int',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
            'sponsor_relationship': 'unsigned int',
            'application_id': 'string',
            'name': 'string',
            'message': 'string',
        }
        enums = {
            'backdated_time_granularity_enum': Photo.BackdatedTimeGranularity.__dict__.values(),
            'unpublished_content_type_enum': Photo.UnpublishedContentType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/photos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Photo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Photo, api=self._api),
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

    def create_promotion(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'budget': 'unsigned int',
            'currency': 'string',
            'ad_account_id': 'string',
            'audience': 'audience_enum',
            'targeting': 'Targeting',
            'start_time': 'unsigned int',
            'stop_time': 'unsigned int',
            'ad_conversion_pixel_id': 'unsigned int',
            'placement': 'string',
            'flow_id': 'string',
            'audience_id': 'string',
            'bid_amount': 'unsigned int',
            'cta_type': 'cta_type_enum',
        }
        enums = {
            'audience_enum': [
                'GROUPER',
                'NCPP',
                'CUSTOM_AUDIENCE',
                'LOOKALIKE',
                'FANS',
                'LOCAL',
                'IG_PROMOTED_POST_AUTO',
                'SAVED_AUDIENCE',
                'EVENT_ENGAGEMENT',
                'DISTRICT',
                'SMART_AUDIENCE',
                'CREATE_NEW',
                'AUTO_LOOKALIKE',
                'MULT_CUSTOM_AUDIENCES',
                'EVENT_CUSTOM_AUDIENCES',
            ],
            'cta_type_enum': [
                'OPEN_LINK',
                'LIKE_PAGE',
                'SHOP_NOW',
                'PLAY_GAME',
                'INSTALL_APP',
                'USE_APP',
                'CALL',
                'CALL_ME',
                'INSTALL_MOBILE_APP',
                'USE_MOBILE_APP',
                'MOBILE_DOWNLOAD',
                'BOOK_TRAVEL',
                'LISTEN_MUSIC',
                'WATCH_VIDEO',
                'LEARN_MORE',
                'SIGN_UP',
                'DOWNLOAD',
                'WATCH_MORE',
                'NO_BUTTON',
                'VISIT_PAGES_FEED',
                'APPLY_NOW',
                'BUY_NOW',
                'GET_OFFER',
                'GET_OFFER_VIEW',
                'BUY_TICKETS',
                'UPDATE_APP',
                'GET_DIRECTIONS',
                'BUY',
                'MESSAGE_PAGE',
                'DONATE',
                'SUBSCRIBE',
                'SAY_THANKS',
                'SELL_NOW',
                'SHARE',
                'DONATE_NOW',
                'GET_QUOTE',
                'CONTACT_US',
                'ORDER_NOW',
                'ADD_TO_CART',
                'VIDEO_ANNOTATION',
                'MOMENTS',
                'RECORD_NOW',
                'GET_SHOWTIMES',
                'LISTEN_NOW',
                'WOODHENGE_SUPPORT',
                'EVENT_RSVP',
                'WHATSAPP_MESSAGE',
                'FOLLOW_NEWS_STORYLINE',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/promotions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_reactions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profile import Profile
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': Profile.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reactions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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

    def get_seen(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/seen',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=User,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=User, api=self._api),
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

    def get_share_d_posts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sharedposts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Post,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Post, api=self._api),
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

    def get_sponsor_tags(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sponsor_tags',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def get_to(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profile import Profile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/to',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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

    def get_with_tags(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profile import Profile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/with_tags',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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
        'application': 'Application',
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
        'place': 'Place',
        'privacy': 'Privacy',
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
        field_enum_info['BackdatedTimeGranularity'] = Post.BackdatedTimeGranularity.__dict__.values()
        field_enum_info['FeedStoryVisibility'] = Post.FeedStoryVisibility.__dict__.values()
        field_enum_info['TimelineVisibility'] = Post.TimelineVisibility.__dict__.values()
        return field_enum_info


