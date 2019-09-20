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

class Event(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isEvent = True
        super(Event, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        attending_count = 'attending_count'
        can_guests_invite = 'can_guests_invite'
        category = 'category'
        cover = 'cover'
        declined_count = 'declined_count'
        description = 'description'
        discount_code_enabled = 'discount_code_enabled'
        end_time = 'end_time'
        event_times = 'event_times'
        guest_list_enabled = 'guest_list_enabled'
        id = 'id'
        interested_count = 'interested_count'
        is_canceled = 'is_canceled'
        is_draft = 'is_draft'
        is_page_owned = 'is_page_owned'
        maybe_count = 'maybe_count'
        name = 'name'
        noreply_count = 'noreply_count'
        owner = 'owner'
        parent_group = 'parent_group'
        place = 'place'
        scheduled_publish_time = 'scheduled_publish_time'
        start_time = 'start_time'
        ticket_uri = 'ticket_uri'
        ticket_uri_start_sales_time = 'ticket_uri_start_sales_time'
        ticketing_privacy_uri = 'ticketing_privacy_uri'
        ticketing_terms_uri = 'ticketing_terms_uri'
        timezone = 'timezone'
        type = 'type'
        updated_time = 'updated_time'

    class Category:
        art_event = 'ART_EVENT'
        book_event = 'BOOK_EVENT'
        class_event = 'CLASS_EVENT'
        comedy_event = 'COMEDY_EVENT'
        conference_event = 'CONFERENCE_EVENT'
        dance_event = 'DANCE_EVENT'
        dining_event = 'DINING_EVENT'
        family_event = 'FAMILY_EVENT'
        festival_event = 'FESTIVAL_EVENT'
        fitness = 'FITNESS'
        food_tasting = 'FOOD_TASTING'
        fundraiser = 'FUNDRAISER'
        lecture = 'LECTURE'
        meetup = 'MEETUP'
        movie_event = 'MOVIE_EVENT'
        music_event = 'MUSIC_EVENT'
        neighborhood = 'NEIGHBORHOOD'
        nightlife = 'NIGHTLIFE'
        other = 'OTHER'
        religious_event = 'RELIGIOUS_EVENT'
        shopping = 'SHOPPING'
        sports_event = 'SPORTS_EVENT'
        theater_event = 'THEATER_EVENT'
        volunteering = 'VOLUNTEERING'
        workshop = 'WORKSHOP'

    class Type:
        community = 'community'
        group = 'group'
        private = 'private'
        public = 'public'

    class EventStateFilter:
        canceled = 'canceled'
        draft = 'draft'
        published = 'published'
        scheduled_draft_for_publication = 'scheduled_draft_for_publication'

    class TimeFilter:
        past = 'past'
        upcoming = 'upcoming'

    class PromotableEventTypes:
        offsite_ticket = 'OFFSITE_TICKET'
        onsite_ticket = 'ONSITE_TICKET'
        rsvp = 'RSVP'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            target_class=Event,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_admins(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.profile import Profile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/admins',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_feed(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'actions': 'Object',
            'adaptive_type': 'string',
            'album_id': 'string',
            'android_key_hash': 'string',
            'animated_effect_id': 'unsigned int',
            'application_id': 'string',
            'asked_fun_fact_prompt_id': 'unsigned int',
            'asset3d_id': 'unsigned int',
            'associated_id': 'string',
            'attach_place_suggestion': 'bool',
            'attached_media': 'list<Object>',
            'audience_exp': 'bool',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'call_to_action': 'Object',
            'caption': 'string',
            'checkin_entry_point': 'checkin_entry_point_enum',
            'child_attachments': 'list<Object>',
            'client_mutation_id': 'string',
            'composer_entry_picker': 'string',
            'composer_entry_point': 'string',
            'composer_entry_time': 'unsigned int',
            'composer_session_events_log': 'string',
            'composer_session_id': 'string',
            'composer_source_surface': 'string',
            'composer_type': 'string',
            'connection_class': 'string',
            'content_attachment': 'string',
            'coordinates': 'Object',
            'cta_link': 'string',
            'cta_type': 'string',
            'description': 'string',
            'direct_share_status': 'unsigned int',
            'expanded_height': 'unsigned int',
            'expanded_width': 'unsigned int',
            'feed_targeting': 'Object',
            'formatting': 'formatting_enum',
            'fun_fact_prompt_id': 'unsigned int',
            'fun_fact_toastee_id': 'unsigned int',
            'has_nickname': 'bool',
            'height': 'unsigned int',
            'holiday_card': 'string',
            'home_checkin_city_id': 'Object',
            'image_crops': 'map',
            'implicit_with_tags': 'list<int>',
            'instant_game_entry_point_data': 'string',
            'ios_bundle_id': 'string',
            'is_backout_draft': 'bool',
            'is_boost_intended': 'bool',
            'is_explicit_location': 'bool',
            'is_explicit_share': 'bool',
            'is_group_linking_post': 'bool',
            'is_photo_container': 'bool',
            'link': 'string',
            'location_source_id': 'string',
            'manual_privacy': 'bool',
            'message': 'string',
            'multi_share_end_card': 'bool',
            'multi_share_optimized': 'bool',
            'name': 'string',
            'nectar_module': 'string',
            'object_attachment': 'string',
            'offer_like_post_id': 'unsigned int',
            'og_action_type_id': 'string',
            'og_hide_object_attachment': 'bool',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'page_recommendation': 'string',
            'picture': 'string',
            'place': 'Object',
            'place_attachment_setting': 'place_attachment_setting_enum',
            'place_list': 'string',
            'place_list_data': 'list',
            'post_surfaces_blacklist': 'list<post_surfaces_blacklist_enum>',
            'posting_to_redspace': 'posting_to_redspace_enum',
            'privacy': 'string',
            'prompt_id': 'string',
            'prompt_tracking_string': 'string',
            'properties': 'Object',
            'proxied_app_id': 'string',
            'publish_event_id': 'unsigned int',
            'published': 'bool',
            'quote': 'string',
            'react_mode_metadata': 'string',
            'ref': 'list<string>',
            'referenceable_image_ids': 'list<string>',
            'referral_id': 'string',
            'sales_promo_id': 'unsigned int',
            'scheduled_publish_time': 'datetime',
            'source': 'string',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'suggested_place_id': 'Object',
            'tags': 'list<int>',
            'target_surface': 'target_surface_enum',
            'targeting': 'Object',
            'text_format_metadata': 'string',
            'text_format_preset_id': 'string',
            'text_only_place': 'string',
            'throwback_camera_roll_media': 'string',
            'thumbnail': 'file',
            'time_since_original_post': 'unsigned int',
            'title': 'string',
            'tracking_info': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'user_selected_tags': 'bool',
            'video_start_time_ms': 'unsigned int',
            'viewer_coordinates': 'Object',
            'width': 'unsigned int',
        }
        enums = {
            'backdated_time_granularity_enum': [
                'day',
                'hour',
                'min',
                'month',
                'none',
                'year',
            ],
            'checkin_entry_point_enum': [
                'BRANDING_CHECKIN',
                'BRANDING_OTHER',
                'BRANDING_PHOTO',
                'BRANDING_STATUS',
            ],
            'formatting_enum': [
                'MARKDOWN',
                'PLAINTEXT',
            ],
            'place_attachment_setting_enum': [
                '1',
                '2',
            ],
            'post_surfaces_blacklist_enum': [
                '1',
                '2',
                '3',
                '4',
                '5',
            ],
            'posting_to_redspace_enum': [
                'disabled',
                'enabled',
            ],
            'target_surface_enum': [
                'STORY',
                'TIMELINE',
            ],
            'unpublished_content_type_enum': [
                'ADS_POST',
                'DRAFT',
                'INLINE_CREATED',
                'PUBLISHED',
                'REVIEWABLE_BRANDED_CONTENT',
                'SCHEDULED',
                'SCHEDULED_RECURRING',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/feed',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_live_video(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.livevideo import LiveVideo
        param_types = {
            'content_tags': 'list<string>',
            'description': 'string',
            'encoding_settings': 'string',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'is_audio_only': 'bool',
            'is_spherical': 'bool',
            'live_encoders': 'list<string>',
            'original_fov': 'unsigned int',
            'planned_start_time': 'int',
            'privacy': 'string',
            'projection': 'projection_enum',
            'published': 'bool',
            'save_vod': 'bool',
            'schedule_custom_profile_image': 'file',
            'spatial_audio_format': 'spatial_audio_format_enum',
            'status': 'status_enum',
            'stereoscopic_mode': 'stereoscopic_mode_enum',
            'stop_on_delete_stream': 'bool',
            'stream_type': 'stream_type_enum',
            'title': 'string',
        }
        enums = {
            'projection_enum': LiveVideo.Projection.__dict__.values(),
            'spatial_audio_format_enum': LiveVideo.SpatialAudioFormat.__dict__.values(),
            'status_enum': LiveVideo.Status.__dict__.values(),
            'stereoscopic_mode_enum': LiveVideo.StereoscopicMode.__dict__.values(),
            'stream_type_enum': LiveVideo.StreamType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/live_videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LiveVideo, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_photo(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.photo import Photo
        param_types = {
            'aid': 'string',
            'allow_spherical_photo': 'bool',
            'alt_text_custom': 'string',
            'android_key_hash': 'string',
            'application_id': 'string',
            'attempt': 'unsigned int',
            'audience_exp': 'bool',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'caption': 'string',
            'composer_session_id': 'string',
            'direct_share_status': 'unsigned int',
            'feed_targeting': 'Object',
            'filter_type': 'unsigned int',
            'full_res_is_coming_later': 'bool',
            'initial_view_heading_override_degrees': 'unsigned int',
            'initial_view_pitch_override_degrees': 'unsigned int',
            'initial_view_vertical_fov_override_degrees': 'unsigned int',
            'ios_bundle_id': 'string',
            'is_explicit_location': 'bool',
            'is_explicit_place': 'bool',
            'manual_privacy': 'bool',
            'message': 'string',
            'name': 'string',
            'no_story': 'bool',
            'offline_id': 'unsigned int',
            'og_action_type_id': 'string',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'place': 'Object',
            'privacy': 'string',
            'profile_id': 'int',
            'proxied_app_id': 'string',
            'published': 'bool',
            'qn': 'string',
            'scheduled_publish_time': 'unsigned int',
            'spherical_metadata': 'map',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'tags': 'list<Object>',
            'target_id': 'int',
            'targeting': 'Object',
            'time_since_original_post': 'unsigned int',
            'uid': 'int',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'url': 'string',
            'user_selected_tags': 'bool',
            'vault_image_id': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_picture(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.profilepicturesource import ProfilePictureSource
        param_types = {
            'height': 'int',
            'redirect': 'bool',
            'type': 'type_enum',
            'width': 'int',
        }
        enums = {
            'type_enum': ProfilePictureSource.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/picture',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProfilePictureSource,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProfilePictureSource, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_roles(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.profile import Profile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/roles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'attending_count': 'int',
        'can_guests_invite': 'bool',
        'category': 'Category',
        'cover': 'CoverPhoto',
        'declined_count': 'int',
        'description': 'string',
        'discount_code_enabled': 'bool',
        'end_time': 'string',
        'event_times': 'list<ChildEvent>',
        'guest_list_enabled': 'bool',
        'id': 'string',
        'interested_count': 'int',
        'is_canceled': 'bool',
        'is_draft': 'bool',
        'is_page_owned': 'bool',
        'maybe_count': 'int',
        'name': 'string',
        'noreply_count': 'int',
        'owner': 'Object',
        'parent_group': 'Group',
        'place': 'Place',
        'scheduled_publish_time': 'string',
        'start_time': 'string',
        'ticket_uri': 'string',
        'ticket_uri_start_sales_time': 'string',
        'ticketing_privacy_uri': 'string',
        'ticketing_terms_uri': 'string',
        'timezone': 'string',
        'type': 'Type',
        'updated_time': 'datetime',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Category'] = Event.Category.__dict__.values()
        field_enum_info['Type'] = Event.Type.__dict__.values()
        field_enum_info['EventStateFilter'] = Event.EventStateFilter.__dict__.values()
        field_enum_info['TimeFilter'] = Event.TimeFilter.__dict__.values()
        field_enum_info['PromotableEventTypes'] = Event.PromotableEventTypes.__dict__.values()
        return field_enum_info


