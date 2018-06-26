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

    class Type:
        private = 'private'
        public = 'public'
        group = 'group'
        community = 'community'

    class EventStateFilter:
        canceled = 'canceled'
        draft = 'draft'
        scheduled_draft_for_publication = 'scheduled_draft_for_publication'
        published = 'published'

    class TimeFilter:
        upcoming = 'upcoming'
        past = 'past'

    class PromotableEventTypes:
        offsite_ticket = 'OFFSITE_TICKET'
        onsite_ticket = 'ONSITE_TICKET'
        rsvp = 'RSVP'

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
            target_class=Event,
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

    def create_live_video(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'attribution_app_id': 'string',
            'content_tags': 'list<string>',
            'description': 'string',
            'encoding_settings': 'string',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'is_spherical': 'bool',
            'live_encoders': 'list<string>',
            'original_fov': 'unsigned int',
            'planned_start_time': 'int',
            'privacy': 'Object',
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
            'projection_enum': [
                'EQUIRECTANGULAR',
                'CUBEMAP',
            ],
            'spatial_audio_format_enum': [
                'ambiX_4',
            ],
            'status_enum': [
                'UNPUBLISHED',
                'LIVE_NOW',
                'SCHEDULED_UNPUBLISHED',
                'SCHEDULED_LIVE',
                'SCHEDULED_CANCELED',
            ],
            'stereoscopic_mode_enum': [
                'MONO',
                'LEFT_RIGHT',
                'TOP_BOTTOM',
            ],
            'stream_type_enum': [
                'REGULAR',
                'AMBIENT',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/live_videos',
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

    def create_photo(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.photo import Photo
        param_types = {
            'aid': 'string',
            'allow_spherical_photo': 'bool',
            'application_id': 'string',
            'audience_exp': 'bool',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'caption': 'string',
            'composer_session_id': 'string',
            'direct_share_status': 'unsigned int',
            'feed_targeting': 'Object',
            'full_res_is_coming_later': 'bool',
            'initial_view_heading_override_degrees': 'unsigned int',
            'initial_view_pitch_override_degrees': 'unsigned int',
            'initial_view_vertical_fov_override_degrees': 'unsigned int',
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
            'privacy': 'Object',
            'profile_id': 'int',
            'published': 'bool',
            'qn': 'string',
            'scheduled_publish_time': 'unsigned int',
            'spherical_metadata': 'map',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'tags': 'list<Object>',
            'target_id': 'int',
            'targeting': 'Object',
            'url': 'string',
        }
        enums = {
            'backdated_time_granularity_enum': Photo.BackdatedTimeGranularity.__dict__.values(),
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

    def create_video(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'audio_story_wave_animation_handle': 'string',
            'content_category': 'content_category_enum',
            'description': 'string',
            'embeddable': 'bool',
            'end_offset': 'unsigned int',
            'file_size': 'unsigned int',
            'file_url': 'string',
            'fisheye_video_cropped': 'bool',
            'fov': 'unsigned int',
            'front_z_rotation': 'float',
            'guide': 'list<list<unsigned int>>',
            'guide_enabled': 'bool',
            'initial_heading': 'unsigned int',
            'initial_pitch': 'unsigned int',
            'original_fov': 'unsigned int',
            'original_projection_type': 'original_projection_type_enum',
            'react_mode_metadata': 'string',
            'referenced_sticker_id': 'string',
            'replace_video_id': 'string',
            'slideshow_spec': 'map',
            'source': 'string',
            'spherical': 'bool',
            'start_offset': 'unsigned int',
            'swap_mode': 'swap_mode_enum',
            'thumb': 'file',
            'title': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'upload_phase': 'upload_phase_enum',
            'upload_session_id': 'string',
            'video_file_chunk': 'string',
        }
        enums = {
            'content_category_enum': [
                'BEAUTY_FASHION',
                'BUSINESS',
                'CARS_TRUCKS',
                'COMEDY',
                'CUTE_ANIMALS',
                'ENTERTAINMENT',
                'FAMILY',
                'FOOD_HEALTH',
                'HOME',
                'LIFESTYLE',
                'MUSIC',
                'NEWS',
                'POLITICS',
                'SCIENCE',
                'SPORTS',
                'TECHNOLOGY',
                'VIDEO_GAMING',
                'OTHER',
            ],
            'original_projection_type_enum': [
                'equirectangular',
                'cubemap',
                'equiangular_cubemap',
                'half_equirectangular',
            ],
            'swap_mode_enum': [
                'replace',
            ],
            'unpublished_content_type_enum': [
                'SCHEDULED',
                'DRAFT',
                'ADS_POST',
                'INLINE_CREATED',
                'PUBLISHED',
            ],
            'upload_phase_enum': [
                'start',
                'transfer',
                'finish',
                'cancel',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/videos',
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

    _field_types = {
        'attending_count': 'int',
        'can_guests_invite': 'bool',
        'category': 'string',
        'cover': 'CoverPhoto',
        'declined_count': 'int',
        'description': 'string',
        'discount_code_enabled': 'bool',
        'end_time': 'string',
        'event_times': 'list<Object>',
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
        'parent_group': 'Object',
        'place': 'Object',
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
        field_enum_info['Type'] = Event.Type.__dict__.values()
        field_enum_info['EventStateFilter'] = Event.EventStateFilter.__dict__.values()
        field_enum_info['TimeFilter'] = Event.TimeFilter.__dict__.values()
        field_enum_info['PromotableEventTypes'] = Event.PromotableEventTypes.__dict__.values()
        return field_enum_info
