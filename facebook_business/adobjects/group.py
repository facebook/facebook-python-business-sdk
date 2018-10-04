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

class Group(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isGroup = True
        super(Group, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        archived = 'archived'
        cover = 'cover'
        created_time = 'created_time'
        description = 'description'
        email = 'email'
        icon = 'icon'
        id = 'id'
        link = 'link'
        member_count = 'member_count'
        member_request_count = 'member_request_count'
        name = 'name'
        owner = 'owner'
        parent = 'parent'
        permissions = 'permissions'
        privacy = 'privacy'
        purpose = 'purpose'
        subdomain = 'subdomain'
        updated_time = 'updated_time'
        venue = 'venue'

    class GroupType:
        family = 'FAMILY'
        close_friends = 'CLOSE_FRIENDS'
        neighbors = 'NEIGHBORS'
        teammates = 'TEAMMATES'
        for_sale = 'FOR_SALE'
        event_planning = 'EVENT_PLANNING'
        support = 'SUPPORT'
        club = 'CLUB'
        project = 'PROJECT'
        sorority = 'SORORITY'
        fraternity = 'FRATERNITY'
        study_group = 'STUDY_GROUP'
        school_class = 'SCHOOL_CLASS'
        learning = 'LEARNING'
        meme = 'MEME'
        travel_planning = 'TRAVEL_PLANNING'
        couple = 'COUPLE'
        parents = 'PARENTS'
        custom = 'CUSTOM'
        none = 'NONE'
        work_team = 'WORK_TEAM'
        work_teamwork = 'WORK_TEAMWORK'
        work_feedback = 'WORK_FEEDBACK'
        work_announcement = 'WORK_ANNOUNCEMENT'
        work_demo_group = 'WORK_DEMO_GROUP'
        work_social = 'WORK_SOCIAL'
        work_discussion = 'WORK_DISCUSSION'
        work_multi_company = 'WORK_MULTI_COMPANY'
        work_for_sale = 'WORK_FOR_SALE'
        work_learning = 'WORK_LEARNING'
        fitness = 'FITNESS'
        real_world = 'REAL_WORLD'
        casual = 'CASUAL'
        game = 'GAME'
        high_school_forum = 'HIGH_SCHOOL_FORUM'
        real_world_at_work = 'REAL_WORLD_AT_WORK'
        for_work = 'FOR_WORK'
        mentorship = 'MENTORSHIP'
        work_mentorship = 'WORK_MENTORSHIP'
        ephemeral = 'EPHEMERAL'
        work_ephemeral = 'WORK_EPHEMERAL'

    class JoinSetting:
        none = 'NONE'
        anyone = 'ANYONE'
        admin_only = 'ADMIN_ONLY'

    class PostPermissions:
        none = 'NONE'
        admin_only = 'ADMIN_ONLY'
        anyone = 'ANYONE'

    class SuggestionCategory:
        family = 'FAMILY'
        life_event = 'LIFE_EVENT'
        top_page = 'TOP_PAGE'
        work = 'WORK'
        work_generic = 'WORK_GENERIC'
        school = 'SCHOOL'
        school_generic = 'SCHOOL_GENERIC'
        messenger = 'MESSENGER'
        messenger_thread = 'MESSENGER_THREAD'
        page_admin = 'PAGE_ADMIN'
        friend_list = 'FRIEND_LIST'
        games = 'GAMES'
        event = 'EVENT'
        close_friends = 'CLOSE_FRIENDS'
        close_friends_generic = 'CLOSE_FRIENDS_GENERIC'
        nearby_friends = 'NEARBY_FRIENDS'
        current_city = 'CURRENT_CITY'
        workplace_1_1 = 'WORKPLACE_1_1'
        workplace_manager = 'WORKPLACE_MANAGER'
        workplace = 'WORKPLACE'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'icon_size': 'icon_size_enum',
        }
        enums = {
            'icon_size_enum': [
                '16',
                '34',
                '50',
                '68',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Group,
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

    def delete_admins(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/admins',
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

    def create_admin(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/admins',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Group,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Group, api=self._api),
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

    def get_albums(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.album import Album
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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

    def create_album(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.album import Album
        param_types = {
            'is_default': 'bool',
            'name': 'string',
            'description': 'string',
            'contributors': 'list<int>',
            'make_shared_album': 'bool',
            'location': 'string',
            'visible': 'string',
            'privacy': 'Object',
            'place': 'Object',
            'tags': 'list<int>',
            'message': 'string',
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

    def get_docs(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/docs',
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

    def create_doc(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'body': 'string',
            'title': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/docs',
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

    def get_events(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.event import Event
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/events',
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

    def create_feed(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'picture': 'string',
            'name': 'string',
            'link': 'string',
            'caption': 'string',
            'description': 'string',
            'quote': 'string',
            'source': 'string',
            'properties': 'Object',
            'object_attachment': 'string',
            'height': 'unsigned int',
            'width': 'unsigned int',
            'expanded_height': 'unsigned int',
            'expanded_width': 'unsigned int',
            'referral_id': 'string',
            'thumbnail': 'file',
            'image_crops': 'map',
            'call_to_action': 'Object',
            'time_since_original_post': 'unsigned int',
            'client_mutation_id': 'string',
            'privacy': 'Object',
            'composer_session_id': 'string',
            'content_attachment': 'string',
            'actions': 'Object',
            'targeting': 'Object',
            'feed_targeting': 'Object',
            'ref': 'list<string>',
            'tags': 'list<int>',
            'place': 'Object',
            'is_explicit_location': 'bool',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'og_hide_object_attachment': 'bool',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'published': 'bool',
            'scheduled_publish_time': 'datetime',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'application_id': 'string',
            'proxied_app_id': 'string',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'user_selected_tags': 'bool',
            'nectar_module': 'string',
            'manual_privacy': 'bool',
            'audience_exp': 'bool',
            'coordinates': 'Object',
            'is_explicit_share': 'bool',
            'is_photo_container': 'bool',
            'implicit_with_tags': 'list<int>',
            'child_attachments': 'list<Object>',
            'suggested_place_id': 'Object',
            'attach_place_suggestion': 'bool',
            'viewer_coordinates': 'Object',
            'album_id': 'string',
            'multi_share_optimized': 'bool',
            'multi_share_end_card': 'bool',
            'title': 'string',
            'attached_media': 'list<Object>',
            'home_checkin_city_id': 'Object',
            'text_only_place': 'string',
            'connection_class': 'string',
            'associated_id': 'string',
            'posting_to_redspace': 'posting_to_redspace_enum',
            'place_attachment_setting': 'place_attachment_setting_enum',
            'checkin_entry_point': 'checkin_entry_point_enum',
            'is_backout_draft': 'bool',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
            'sponsor_relationship': 'unsigned int',
            'referenceable_image_ids': 'list<string>',
            'prompt_id': 'string',
            'prompt_tracking_string': 'string',
            'post_surfaces_blacklist': 'list<post_surfaces_blacklist_enum>',
            'tracking_info': 'string',
            'text_format_preset_id': 'string',
            'cta_link': 'string',
            'cta_type': 'string',
            'place_list_data': 'Object',
            'formatting': 'formatting_enum',
            'target_surface': 'target_surface_enum',
            'adaptive_type': 'string',
            'animated_effect_id': 'unsigned int',
            'asked_fun_fact_prompt_id': 'unsigned int',
            'asset3d_id': 'unsigned int',
            'composer_entry_picker': 'string',
            'composer_entry_point': 'string',
            'composer_entry_time': 'unsigned int',
            'composer_session_events_log': 'string',
            'composer_source_surface': 'string',
            'composer_type': 'string',
            'fun_fact_prompt_id': 'string',
            'fun_fact_toastee_id': 'unsigned int',
            'is_group_linking_post': 'bool',
            'has_nickname': 'bool',
            'holiday_card': 'string',
            'instant_game_entry_point_data': 'string',
            'is_boost_intended': 'bool',
            'location_source_id': 'string',
            'message': 'string',
            'offer_like_post_id': 'string',
            'page_recommendation': 'string',
            'place_list': 'string',
            'publish_event_id': 'unsigned int',
            'react_mode_metadata': 'string',
            'sales_promo_id': 'unsigned int',
            'text_format_metadata': 'string',
            'throwback_camera_roll_media': 'string',
            'video_start_time_ms': 'unsigned int',
        }
        enums = {
            'backdated_time_granularity_enum': [
                'year',
                'month',
                'day',
                'hour',
                'min',
                'none',
            ],
            'unpublished_content_type_enum': [
                'SCHEDULED',
                'DRAFT',
                'ADS_POST',
                'INLINE_CREATED',
                'PUBLISHED',
            ],
            'posting_to_redspace_enum': [
                'enabled',
                'disabled',
            ],
            'place_attachment_setting_enum': [
                '1',
                '2',
            ],
            'checkin_entry_point_enum': [
                'BRANDING_CHECKIN',
                'BRANDING_STATUS',
                'BRANDING_PHOTO',
                'BRANDING_OTHER',
            ],
            'post_surfaces_blacklist_enum': [
                '1',
                '2',
                '3',
                '4',
                '5',
            ],
            'formatting_enum': [
                'PLAINTEXT',
                'MARKDOWN',
            ],
            'target_surface_enum': [
                'STORY',
                'TIMELINE',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_group_thread(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'thread_id': 'Object',
            'joinable': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/group_threads',
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

    def get_groups(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Group,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Group, api=self._api),
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

    def create_group(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'privacy': 'string',
            'group_type': 'group_type_enum',
            'description': 'string',
            'parent_id': 'Object',
            'group_icon_id': 'Object',
            'suggestion_category': 'suggestion_category_enum',
            'suggestion_identifier': 'string',
            'ref': 'string',
            'join_setting': 'join_setting_enum',
            'post_permissions': 'post_permissions_enum',
            'post_requires_admin_approval': 'bool',
            'admin': 'int',
        }
        enums = {
            'group_type_enum': Group.GroupType.__dict__.values(),
            'suggestion_category_enum': Group.SuggestionCategory.__dict__.values(),
            'join_setting_enum': Group.JoinSetting.__dict__.values(),
            'post_permissions_enum': Group.PostPermissions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Group,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Group, api=self._api),
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
            'type': 'type_enum',
            'source': 'source_enum',
            'broadcast_status': 'list<broadcast_status_enum>',
        }
        enums = {
            'type_enum': LiveVideo.Type.__dict__.values(),
            'source_enum': LiveVideo.Source.__dict__.values(),
            'broadcast_status_enum': LiveVideo.BroadcastStatus.__dict__.values(),
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
            'title': 'string',
            'description': 'string',
            'save_vod': 'bool',
            'published': 'bool',
            'status': 'status_enum',
            'privacy': 'Object',
            'stop_on_delete_stream': 'bool',
            'stream_type': 'stream_type_enum',
            'content_tags': 'list<string>',
            'is_spherical': 'bool',
            'is_audio_only': 'bool',
            'planned_start_time': 'int',
            'schedule_custom_profile_image': 'file',
            'projection': 'projection_enum',
            'spatial_audio_format': 'spatial_audio_format_enum',
            'encoding_settings': 'string',
            'live_encoders': 'list<string>',
            'original_fov': 'unsigned int',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'attribution_app_id': 'string',
            'stereoscopic_mode': 'stereoscopic_mode_enum',
        }
        enums = {
            'status_enum': LiveVideo.Status.__dict__.values(),
            'stream_type_enum': LiveVideo.StreamType.__dict__.values(),
            'projection_enum': LiveVideo.Projection.__dict__.values(),
            'spatial_audio_format_enum': LiveVideo.SpatialAudioFormat.__dict__.values(),
            'stereoscopic_mode_enum': LiveVideo.StereoscopicMode.__dict__.values(),
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

    def delete_members(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'member': 'int',
            'email': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/members',
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

    def create_member(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'member': 'int',
            'email': 'string',
            'from': 'int',
            'rate': 'unsigned int',
            'source': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/members',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Group,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Group, api=self._api),
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

    def delete_moderators(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/moderators',
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

    def create_moderator(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/moderators',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Group,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Group, api=self._api),
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

    def create_open_graph_action_feed(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'to': 'string',
            'client_secret': 'string',
            'preview': 'bool',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'proxied_app_id': 'string',
            'user_selected_tags': 'bool',
            'user_selected_place': 'bool',
            'added': 'string',
            'alias': 'string',
            'fb:channel': 'string',
            'created_time': 'datetime',
            'end_time': 'datetime',
            'expires_in': 'unsigned int',
            'fb:explicitly_shared': 'bool',
            'image:height': 'unsigned int',
            'image:secure_url': 'string',
            'image:type': 'string',
            'image:url': 'string',
            'image:user_generated': 'bool',
            'image:width': 'unsigned int',
            'no_feed_story': 'bool',
            'no_action_link': 'bool',
            'notify': 'bool',
            'message': 'string',
            'place': 'string',
            'privacy': 'Object',
            'ref': 'string',
            'scrape': 'bool',
            'start_time': 'datetime',
            'tags': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/opengraphactionfeed',
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

    def get_opted_in_members(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/opted_in_members',
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

    def get_picture(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profilepicturesource import ProfilePictureSource
        param_types = {
            'height': 'int',
            'width': 'int',
            'type': 'type_enum',
            'redirect': 'bool',
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

    def get_videos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': AdVideo.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'title': 'string',
            'source': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'time_since_original_post': 'unsigned int',
            'file_url': 'string',
            'composer_session_id': 'string',
            'waterfall_id': 'string',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_suggestion_mechanism': 'string',
            'manual_privacy': 'bool',
            'is_explicit_share': 'bool',
            'thumb': 'file',
            'spherical': 'bool',
            'original_projection_type': 'original_projection_type_enum',
            'initial_heading': 'unsigned int',
            'initial_pitch': 'unsigned int',
            'fov': 'unsigned int',
            'original_fov': 'unsigned int',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'guide_enabled': 'bool',
            'guide': 'list<list<unsigned int>>',
            'audio_story_wave_animation_handle': 'string',
            'adaptive_type': 'string',
            'animated_effect_id': 'unsigned int',
            'asked_fun_fact_prompt_id': 'unsigned int',
            'composer_entry_picker': 'string',
            'composer_entry_point': 'string',
            'composer_entry_time': 'unsigned int',
            'composer_session_events_log': 'string',
            'composer_source_surface': 'string',
            'composer_type': 'string',
            'formatting': 'formatting_enum',
            'fun_fact_prompt_id': 'string',
            'fun_fact_toastee_id': 'unsigned int',
            'is_group_linking_post': 'bool',
            'has_nickname': 'bool',
            'holiday_card': 'string',
            'instant_game_entry_point_data': 'string',
            'is_boost_intended': 'bool',
            'location_source_id': 'string',
            'description': 'string',
            'offer_like_post_id': 'string',
            'publish_event_id': 'unsigned int',
            'react_mode_metadata': 'string',
            'sales_promo_id': 'unsigned int',
            'text_format_metadata': 'string',
            'throwback_camera_roll_media': 'string',
            'video_start_time_ms': 'unsigned int',
            'application_id': 'string',
            'upload_phase': 'upload_phase_enum',
            'file_size': 'unsigned int',
            'start_offset': 'unsigned int',
            'end_offset': 'unsigned int',
            'video_file_chunk': 'string',
            'fbuploader_video_file_chunk': 'string',
            'upload_session_id': 'string',
            'is_voice_clip': 'bool',
            'attribution_app_id': 'string',
            'content_category': 'content_category_enum',
            'embeddable': 'bool',
            'slideshow_spec': 'map',
            'upload_setting_properties': 'string',
            'transcode_setting_properties': 'string',
            'container_type': 'container_type_enum',
            'referenced_sticker_id': 'string',
            'replace_video_id': 'string',
            'swap_mode': 'swap_mode_enum',
            'scheduled_publish_time': 'unsigned int',
        }
        enums = {
            'unpublished_content_type_enum': AdVideo.UnpublishedContentType.__dict__.values(),
            'original_projection_type_enum': AdVideo.OriginalProjectionType.__dict__.values(),
            'formatting_enum': AdVideo.Formatting.__dict__.values(),
            'upload_phase_enum': AdVideo.UploadPhase.__dict__.values(),
            'content_category_enum': AdVideo.ContentCategory.__dict__.values(),
            'container_type_enum': AdVideo.ContainerType.__dict__.values(),
            'swap_mode_enum': AdVideo.SwapMode.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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
        'archived': 'bool',
        'cover': 'CoverPhoto',
        'created_time': 'datetime',
        'description': 'string',
        'email': 'string',
        'icon': 'string',
        'id': 'string',
        'link': 'string',
        'member_count': 'unsigned int',
        'member_request_count': 'unsigned int',
        'name': 'string',
        'owner': 'Object',
        'parent': 'Object',
        'permissions': 'list<string>',
        'privacy': 'string',
        'purpose': 'string',
        'subdomain': 'string',
        'updated_time': 'datetime',
        'venue': 'Location',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['GroupType'] = Group.GroupType.__dict__.values()
        field_enum_info['JoinSetting'] = Group.JoinSetting.__dict__.values()
        field_enum_info['PostPermissions'] = Group.PostPermissions.__dict__.values()
        field_enum_info['SuggestionCategory'] = Group.SuggestionCategory.__dict__.values()
        return field_enum_info


