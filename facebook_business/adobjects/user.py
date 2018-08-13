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

class User(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isUser = True
        super(User, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        about = 'about'
        address = 'address'
        admin_notes = 'admin_notes'
        age_range = 'age_range'
        birthday = 'birthday'
        can_review_measurement_request = 'can_review_measurement_request'
        context = 'context'
        cover = 'cover'
        currency = 'currency'
        devices = 'devices'
        education = 'education'
        email = 'email'
        employee_number = 'employee_number'
        favorite_athletes = 'favorite_athletes'
        favorite_teams = 'favorite_teams'
        first_name = 'first_name'
        gender = 'gender'
        hometown = 'hometown'
        id = 'id'
        inspirational_people = 'inspirational_people'
        install_type = 'install_type'
        installed = 'installed'
        interested_in = 'interested_in'
        is_famedeeplinkinguser = 'is_famedeeplinkinguser'
        is_shared_login = 'is_shared_login'
        is_verified = 'is_verified'
        labels = 'labels'
        languages = 'languages'
        last_name = 'last_name'
        link = 'link'
        local_news_megaphone_dismiss_status = 'local_news_megaphone_dismiss_status'
        local_news_subscription_status = 'local_news_subscription_status'
        locale = 'locale'
        location = 'location'
        meeting_for = 'meeting_for'
        middle_name = 'middle_name'
        name = 'name'
        name_format = 'name_format'
        payment_pricepoints = 'payment_pricepoints'
        political = 'political'
        profile_pic = 'profile_pic'
        public_key = 'public_key'
        quotes = 'quotes'
        relationship_status = 'relationship_status'
        religion = 'religion'
        security_settings = 'security_settings'
        shared_login_upgrade_required_by = 'shared_login_upgrade_required_by'
        short_name = 'short_name'
        significant_other = 'significant_other'
        sports = 'sports'
        test_group = 'test_group'
        third_party_id = 'third_party_id'
        timezone = 'timezone'
        token_for_business = 'token_for_business'
        updated_time = 'updated_time'
        verified = 'verified'
        video_upload_limits = 'video_upload_limits'
        viewer_can_send_gift = 'viewer_can_send_gift'
        website = 'website'
        work = 'work'

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
            target_class=User,
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

    def get_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'business_id': 'string',
            'is_business': 'bool',
            'is_place': 'bool',
            'is_promotable': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/accounts',
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

    def create_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'about': 'string',
            'address': 'string',
            'category_enum': 'string',
            'category_list': 'list<string>',
            'city_id': 'Object',
            'coordinates': 'Object',
            'cover_photo': 'Object',
            'description': 'string',
            'ignore_coordinate_warnings': 'bool',
            'location': 'Object',
            'name': 'string',
            'phone': 'string',
            'picture': 'string',
            'website': 'string',
            'zip': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/accounts',
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

    def get_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adaccounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccount,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccount, api=self._api),
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

    def create_album(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.album import Album
        param_types = {
            'contributors': 'list<int>',
            'description': 'string',
            'is_default': 'bool',
            'location': 'string',
            'make_shared_album': 'bool',
            'message': 'string',
            'name': 'string',
            'place': 'Object',
            'privacy': 'Object',
            'tags': 'list<int>',
            'visible': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/albums',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Album,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Album, api=self._api),
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

    def get_conversations(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'folder': 'string',
            'tags': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/conversations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UnifiedThread,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UnifiedThread, api=self._api),
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

    def get_lead_gen_forms(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenform import LeadgenForm
        param_types = {
            'page_id': 'string',
            'query': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_forms',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadgenForm,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadgenForm, api=self._api),
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

    def create_live_encoder(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'brand': 'string',
            'device_id': 'string',
            'model': 'string',
            'name': 'string',
            'version': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/live_encoders',
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

    def get_live_videos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.livevideo import LiveVideo
        param_types = {
            'broadcast_status': 'list<broadcast_status_enum>',
            'source': 'source_enum',
        }
        enums = {
            'broadcast_status_enum': LiveVideo.BroadcastStatus.__dict__.values(),
            'source_enum': LiveVideo.Source.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_live_video(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.livevideo import LiveVideo
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

    def get_picture(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_promotable_domains(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.domain import Domain
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/promotable_domains',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Domain,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Domain, api=self._api),
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

    def get_promotable_events(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.event import Event
        param_types = {
            'include_past_events': 'bool',
            'is_page_event': 'bool',
            'page_id': 'unsigned int',
            'promotable_event_types': 'list<promotable_event_types_enum>',
        }
        enums = {
            'promotable_event_types_enum': Event.PromotableEventTypes.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/promotable_events',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Event,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Event, api=self._api),
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

    def get_threads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'folder': 'string',
            'tags': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/threads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UnifiedThread,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UnifiedThread, api=self._api),
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
        'about': 'string',
        'address': 'Location',
        'admin_notes': 'list<PageAdminNote>',
        'age_range': 'Object',
        'birthday': 'string',
        'can_review_measurement_request': 'bool',
        'context': 'Object',
        'cover': 'Object',
        'currency': 'Object',
        'devices': 'list<Object>',
        'education': 'list<Object>',
        'email': 'string',
        'employee_number': 'string',
        'favorite_athletes': 'list<Object>',
        'favorite_teams': 'list<Object>',
        'first_name': 'string',
        'gender': 'string',
        'hometown': 'Page',
        'id': 'string',
        'inspirational_people': 'list<Object>',
        'install_type': 'string',
        'installed': 'bool',
        'interested_in': 'list<string>',
        'is_famedeeplinkinguser': 'bool',
        'is_shared_login': 'bool',
        'is_verified': 'bool',
        'labels': 'list<PageLabel>',
        'languages': 'list<Object>',
        'last_name': 'string',
        'link': 'string',
        'local_news_megaphone_dismiss_status': 'bool',
        'local_news_subscription_status': 'bool',
        'locale': 'string',
        'location': 'Page',
        'meeting_for': 'list<string>',
        'middle_name': 'string',
        'name': 'string',
        'name_format': 'string',
        'payment_pricepoints': 'Object',
        'political': 'string',
        'profile_pic': 'string',
        'public_key': 'string',
        'quotes': 'string',
        'relationship_status': 'string',
        'religion': 'string',
        'security_settings': 'Object',
        'shared_login_upgrade_required_by': 'datetime',
        'short_name': 'string',
        'significant_other': 'User',
        'sports': 'list<Object>',
        'test_group': 'unsigned int',
        'third_party_id': 'string',
        'timezone': 'float',
        'token_for_business': 'string',
        'updated_time': 'datetime',
        'verified': 'bool',
        'video_upload_limits': 'Object',
        'viewer_can_send_gift': 'bool',
        'website': 'string',
        'work': 'list<Object>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
