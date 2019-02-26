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

class AdVideo(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdVideo = True
        super(AdVideo, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_breaks = 'ad_breaks'
        backdated_time = 'backdated_time'
        backdated_time_granularity = 'backdated_time_granularity'
        content_category = 'content_category'
        content_tags = 'content_tags'
        created_time = 'created_time'
        custom_labels = 'custom_labels'
        description = 'description'
        embed_html = 'embed_html'
        embeddable = 'embeddable'
        event = 'event'
        expiration = 'expiration'
        format = 'format'
        field_from = 'from'
        icon = 'icon'
        id = 'id'
        is_crosspost_video = 'is_crosspost_video'
        is_crossposting_eligible = 'is_crossposting_eligible'
        is_episode = 'is_episode'
        is_instagram_eligible = 'is_instagram_eligible'
        length = 'length'
        live_audience_count = 'live_audience_count'
        live_status = 'live_status'
        permalink_url = 'permalink_url'
        picture = 'picture'
        place = 'place'
        premiere_living_room_status = 'premiere_living_room_status'
        privacy = 'privacy'
        published = 'published'
        scheduled_publish_time = 'scheduled_publish_time'
        source = 'source'
        spherical = 'spherical'
        status = 'status'
        title = 'title'
        tv_banner_ad = 'tv_banner_ad'
        universal_video_id = 'universal_video_id'
        updated_time = 'updated_time'
        unpublished_content_type = 'unpublished_content_type'
        time_since_original_post = 'time_since_original_post'
        file_url = 'file_url'
        composer_session_id = 'composer_session_id'
        waterfall_id = 'waterfall_id'
        og_action_type_id = 'og_action_type_id'
        og_object_id = 'og_object_id'
        og_phrase = 'og_phrase'
        og_icon_id = 'og_icon_id'
        og_suggestion_mechanism = 'og_suggestion_mechanism'
        thumb = 'thumb'
        original_projection_type = 'original_projection_type'
        initial_heading = 'initial_heading'
        initial_pitch = 'initial_pitch'
        fov = 'fov'
        original_fov = 'original_fov'
        fisheye_video_cropped = 'fisheye_video_cropped'
        front_z_rotation = 'front_z_rotation'
        guide_enabled = 'guide_enabled'
        guide = 'guide'
        audio_story_wave_animation_handle = 'audio_story_wave_animation_handle'
        adaptive_type = 'adaptive_type'
        animated_effect_id = 'animated_effect_id'
        asked_fun_fact_prompt_id = 'asked_fun_fact_prompt_id'
        composer_entry_picker = 'composer_entry_picker'
        composer_entry_point = 'composer_entry_point'
        composer_entry_time = 'composer_entry_time'
        composer_session_events_log = 'composer_session_events_log'
        composer_source_surface = 'composer_source_surface'
        composer_type = 'composer_type'
        formatting = 'formatting'
        fun_fact_prompt_id = 'fun_fact_prompt_id'
        fun_fact_toastee_id = 'fun_fact_toastee_id'
        is_group_linking_post = 'is_group_linking_post'
        has_nickname = 'has_nickname'
        holiday_card = 'holiday_card'
        instant_game_entry_point_data = 'instant_game_entry_point_data'
        is_boost_intended = 'is_boost_intended'
        location_source_id = 'location_source_id'
        offer_like_post_id = 'offer_like_post_id'
        publish_event_id = 'publish_event_id'
        react_mode_metadata = 'react_mode_metadata'
        sales_promo_id = 'sales_promo_id'
        text_format_metadata = 'text_format_metadata'
        throwback_camera_roll_media = 'throwback_camera_roll_media'
        video_start_time_ms = 'video_start_time_ms'
        application_id = 'application_id'
        upload_phase = 'upload_phase'
        file_size = 'file_size'
        start_offset = 'start_offset'
        end_offset = 'end_offset'
        video_file_chunk = 'video_file_chunk'
        fbuploader_video_file_chunk = 'fbuploader_video_file_chunk'
        upload_session_id = 'upload_session_id'
        is_voice_clip = 'is_voice_clip'
        attribution_app_id = 'attribution_app_id'
        slideshow_spec = 'slideshow_spec'
        upload_setting_properties = 'upload_setting_properties'
        transcode_setting_properties = 'transcode_setting_properties'
        container_type = 'container_type'
        referenced_sticker_id = 'referenced_sticker_id'
        replace_video_id = 'replace_video_id'
        swap_mode = 'swap_mode'
        name = 'name'
        chunk_session_id = 'chunk_session_id'
        manual_privacy = 'manual_privacy'
        is_explicit_share = 'is_explicit_share'
        filename = 'filename'
        filepath = 'filepath'

    class ContainerType:
        ad_break_preview = 'AD_BREAK_PREVIEW'
        ad_derivative = 'AD_DERIVATIVE'
        age_up = 'AGE_UP'
        album_multimedia_post = 'ALBUM_MULTIMEDIA_POST'
        aloha_call_video = 'ALOHA_CALL_VIDEO'
        aloha_superframe = 'ALOHA_SUPERFRAME'
        app_review_screencast = 'APP_REVIEW_SCREENCAST'
        atlas_video = 'ATLAS_VIDEO'
        audio_broadcast = 'AUDIO_BROADCAST'
        bell_poll = 'BELL_POLL'
        brand_equity_poll_video = 'BRAND_EQUITY_POLL_VIDEO'
        broadcast = 'BROADCAST'
        candidate_videos = 'CANDIDATE_VIDEOS'
        canvas = 'CANVAS'
        civic_proposal_cover_video = 'CIVIC_PROPOSAL_COVER_VIDEO'
        contained_post_attachment = 'CONTAINED_POST_ATTACHMENT'
        contained_post_audio_broadcast = 'CONTAINED_POST_AUDIO_BROADCAST'
        contained_post_broadcast = 'CONTAINED_POST_BROADCAST'
        copyright_reference_broadcast = 'COPYRIGHT_REFERENCE_BROADCAST'
        copyright_reference_video = 'COPYRIGHT_REFERENCE_VIDEO'
        cultural_moment_deprecated = 'CULTURAL_MOMENT_DEPRECATED'
        dco_ad_asset_feed = 'DCO_AD_ASSET_FEED'
        dco_autogen_video = 'DCO_AUTOGEN_VIDEO'
        directed_post_attachment = 'DIRECTED_POST_ATTACHMENT'
        direct_inbox = 'DIRECT_INBOX'
        direct_inbox_reaction = 'DIRECT_INBOX_REACTION'
        dynamic_item_display_bundle = 'DYNAMIC_ITEM_DISPLAY_BUNDLE'
        dynamic_item_video = 'DYNAMIC_ITEM_VIDEO'
        dynamic_template_video = 'DYNAMIC_TEMPLATE_VIDEO'
        event_cover_video = 'EVENT_COVER_VIDEO'
        event_tour = 'EVENT_TOUR'
        facecast_dvr = 'FACECAST_DVR'
        fundraiser_cover_video = 'FUNDRAISER_COVER_VIDEO'
        game_clip = 'GAME_CLIP'
        goodwill_anniversary_deprecated = 'GOODWILL_ANNIVERSARY_DEPRECATED'
        goodwill_anniversary_promotion_deprecated = 'GOODWILL_ANNIVERSARY_PROMOTION_DEPRECATED'
        goodwill_video_contained_share = 'GOODWILL_VIDEO_CONTAINED_SHARE'
        goodwill_video_promotion = 'GOODWILL_VIDEO_PROMOTION'
        goodwill_video_share = 'GOODWILL_VIDEO_SHARE'
        goodwill_video_token_required = 'GOODWILL_VIDEO_TOKEN_REQUIRED'
        group_post = 'GROUP_POST'
        heuristic_cluster_video = 'HEURISTIC_CLUSTER_VIDEO'
        heuristic_preview = 'HEURISTIC_PREVIEW'
        inspiration_video = 'INSPIRATION_VIDEO'
        instagram_video_copy = 'INSTAGRAM_VIDEO_COPY'
        instant_application_preview = 'INSTANT_APPLICATION_PREVIEW'
        instant_article = 'INSTANT_ARTICLE'
        instant_game_clip = 'INSTANT_GAME_CLIP'
        issue_module = 'ISSUE_MODULE'
        job_application_video = 'JOB_APPLICATION_VIDEO'
        job_opening_video = 'JOB_OPENING_VIDEO'
        kototoro = 'KOTOTORO'
        learn = 'LEARN'
        legacy = 'LEGACY'
        live_creative_kit_video = 'LIVE_CREATIVE_KIT_VIDEO'
        live_photo = 'LIVE_PHOTO'
        look_now_deprecated = 'LOOK_NOW_DEPRECATED'
        moments_video = 'MOMENTS_VIDEO'
        no_story = 'NO_STORY'
        oculus_venues_broadcast = 'OCULUS_VENUES_BROADCAST'
        offers_video = 'OFFERS_VIDEO'
        pages_cover_video = 'PAGES_COVER_VIDEO'
        page_review_screencast = 'PAGE_REVIEW_SCREENCAST'
        page_slideshow_video = 'PAGE_SLIDESHOW_VIDEO'
        pixelcloud = 'PIXELCLOUD'
        premiere_source = 'PREMIERE_SOURCE'
        private_gallery_video = 'PRIVATE_GALLERY_VIDEO'
        product_video = 'PRODUCT_VIDEO'
        profile_cover_video = 'PROFILE_COVER_VIDEO'
        profile_intro_card = 'PROFILE_INTRO_CARD'
        profile_to_page_uploaded_video = 'PROFILE_TO_PAGE_UPLOADED_VIDEO'
        profile_video = 'PROFILE_VIDEO'
        proton = 'PROTON'
        quick_promotion = 'QUICK_PROMOTION'
        replace_video = 'REPLACE_VIDEO'
        say_thanks_deprecated = 'SAY_THANKS_DEPRECATED'
        slideshow_animoto = 'SLIDESHOW_ANIMOTO'
        slideshow_shakr = 'SLIDESHOW_SHAKR'
        sotto_content = 'SOTTO_CONTENT'
        storyline = 'STORYLINE'
        storyline_with_external_music = 'STORYLINE_WITH_EXTERNAL_MUSIC'
        story_archive_video = 'STORY_ARCHIVE_VIDEO'
        tarot_digest = 'TAROT_DIGEST'
        temp_multimedia_post = 'TEMP_MULTIMEDIA_POST'
        unlisted = 'UNLISTED'
        video_comment = 'VIDEO_COMMENT'
        woodhenge = 'WOODHENGE'
        your_day = 'YOUR_DAY'

    class ContentCategory:
        beauty_fashion = 'BEAUTY_FASHION'
        business = 'BUSINESS'
        cars_trucks = 'CARS_TRUCKS'
        comedy = 'COMEDY'
        cute_animals = 'CUTE_ANIMALS'
        entertainment = 'ENTERTAINMENT'
        family = 'FAMILY'
        food_health = 'FOOD_HEALTH'
        home = 'HOME'
        lifestyle = 'LIFESTYLE'
        music = 'MUSIC'
        news = 'NEWS'
        other = 'OTHER'
        politics = 'POLITICS'
        science = 'SCIENCE'
        sports = 'SPORTS'
        technology = 'TECHNOLOGY'
        video_gaming = 'VIDEO_GAMING'

    class Formatting:
        markdown = 'MARKDOWN'
        plaintext = 'PLAINTEXT'

    class OriginalProjectionType:
        cubemap = 'cubemap'
        equiangular_cubemap = 'equiangular_cubemap'
        equirectangular = 'equirectangular'
        half_equirectangular = 'half_equirectangular'

    class SwapMode:
        replace = 'replace'

    class UnpublishedContentType:
        ads_post = 'ADS_POST'
        draft = 'DRAFT'
        inline_created = 'INLINE_CREATED'
        published = 'PUBLISHED'
        scheduled = 'SCHEDULED'

    class UploadPhase:
        cancel = 'cancel'
        finish = 'finish'
        start = 'start'
        transfer = 'transfer'

    class Type:
        tagged = 'tagged'
        uploaded = 'uploaded'

    class BackdatedTimeGranularity:
        day = 'day'
        hour = 'hour'
        min = 'min'
        month = 'month'
        none = 'none'
        year = 'year'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'advideos'

    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_video(fields, params, batch, success, failure, pending)

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

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
            target_class=AdVideo,
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

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'privacy': 'string',
            'published': 'bool',
            'target': 'string',
            'scheduled_publish_time': 'unsigned int',
            'name': 'string',
            'description': 'string',
            'tags': 'list<string>',
            'preferred_thumbnail_id': 'string',
            'ad_breaks': 'list',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'call_to_action': 'Object',
            'custom_labels': 'list<string>',
            'expiration': 'Object',
            'expire_now': 'bool',
            'embeddable': 'bool',
            'allow_bm_crossposting': 'bool',
            'allow_crossposting_for_pages': 'list<Object>',
            'social_actions': 'bool',
            'content_category': 'content_category_enum',
            'publish_to_videos_tab': 'bool',
            'publish_to_news_feed': 'bool',
            'universal_video_id': 'string',
            'content_tags': 'list<string>',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
            'sponsor_relationship': 'unsigned int',
            'increment_play_count': 'bool',
        }
        enums = {
            'backdated_time_granularity_enum': AdVideo.BackdatedTimeGranularity.__dict__.values(),
            'content_category_enum': AdVideo.ContentCategory.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
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

    def get_auto_generated_captions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/auto_generated_captions',
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

    def create_auto_trim(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'target_id': 'unsigned int',
            'auto_trim_type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/auto_trims',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def create_blocked_user(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'uid': 'Object',
            'remove_block': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/blocked_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def delete_captions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'locale': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/captions',
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

    def get_captions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/captions',
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

    def create_caption(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'default_locale': 'string',
            'captions_file': 'file',
            'locales_to_delete': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/captions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def get_comments(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_comment(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.comment import Comment
        param_types = {
            'object_id': 'string',
            'parent_comment_id': 'Object',
            'nectar_module': 'string',
            'attachment_id': 'string',
            'attachment_url': 'string',
            'attachment_share_url': 'string',
            'feedback_source': 'string',
            'facepile_mentioned_ids': 'list<string>',
            'is_offline': 'bool',
            'comment_privacy_value': 'comment_privacy_value_enum',
            'message': 'string',
            'text': 'string',
            'tracking': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_crosspost_shared_pages(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/crosspost_shared_pages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def delete_likes(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'tracking': 'string',
            'nectar_module': 'string',
            'notify': 'bool',
            'feedback_source': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_likes(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_like(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'tracking': 'string',
            'nectar_module': 'string',
            'notify': 'bool',
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
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def get_polls(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.videopoll import VideoPoll
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/polls',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoPoll,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoPoll, api=self._api),
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

    def create_poll(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.videopoll import VideoPoll
        param_types = {
            'question': 'string',
            'options': 'list<string>',
            'correct_option': 'unsigned int',
            'default_open': 'bool',
            'show_results': 'bool',
            'show_gradient': 'bool',
            'close_after_voting': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/polls',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoPoll,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoPoll, api=self._api),
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

    def get_reactions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_shared_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.post import Post
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_sponsor_tags(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_summarization(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'target_id': 'unsigned int',
            'summarization_type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/summarizations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def get_tags(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.taggablesubject import TaggableSubject
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tags',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=TaggableSubject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=TaggableSubject, api=self._api),
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

    def create_tag(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'uid': 'int',
            'vid': 'string',
            'tag_uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/tags',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def get_thumbnails(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.videothumbnail import VideoThumbnail
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/thumbnails',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoThumbnail,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoThumbnail, api=self._api),
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

    def create_thumbnail(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'source': 'file',
            'is_preferred': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/thumbnails',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def get_video_insights(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.insightsresult import InsightsResult
        param_types = {
            'metric': 'list<Object>',
            'period': 'period_enum',
            'since': 'datetime',
            'until': 'datetime',
        }
        enums = {
            'period_enum': InsightsResult.Period.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InsightsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InsightsResult, api=self._api),
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
        'ad_breaks': 'list<int>',
        'backdated_time': 'datetime',
        'backdated_time_granularity': 'string',
        'content_category': 'string',
        'content_tags': 'list<string>',
        'created_time': 'datetime',
        'custom_labels': 'list<string>',
        'description': 'string',
        'embed_html': 'string',
        'embeddable': 'bool',
        'event': 'Event',
        'expiration': 'Object',
        'format': 'list<Object>',
        'from': 'Object',
        'icon': 'string',
        'id': 'string',
        'is_crosspost_video': 'bool',
        'is_crossposting_eligible': 'bool',
        'is_episode': 'bool',
        'is_instagram_eligible': 'bool',
        'length': 'float',
        'live_audience_count': 'unsigned int',
        'live_status': 'string',
        'permalink_url': 'string',
        'picture': 'string',
        'place': 'Place',
        'premiere_living_room_status': 'string',
        'privacy': 'Privacy',
        'published': 'bool',
        'scheduled_publish_time': 'datetime',
        'source': 'string',
        'spherical': 'bool',
        'status': 'Object',
        'title': 'string',
        'tv_banner_ad': 'Object',
        'universal_video_id': 'string',
        'updated_time': 'datetime',
        'unpublished_content_type': 'UnpublishedContentType',
        'time_since_original_post': 'unsigned int',
        'file_url': 'string',
        'composer_session_id': 'string',
        'waterfall_id': 'string',
        'og_action_type_id': 'string',
        'og_object_id': 'string',
        'og_phrase': 'string',
        'og_icon_id': 'string',
        'og_suggestion_mechanism': 'string',
        'thumb': 'file',
        'original_projection_type': 'OriginalProjectionType',
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
        'formatting': 'Formatting',
        'fun_fact_prompt_id': 'unsigned int',
        'fun_fact_toastee_id': 'unsigned int',
        'is_group_linking_post': 'bool',
        'has_nickname': 'bool',
        'holiday_card': 'string',
        'instant_game_entry_point_data': 'string',
        'is_boost_intended': 'bool',
        'location_source_id': 'string',
        'offer_like_post_id': 'unsigned int',
        'publish_event_id': 'unsigned int',
        'react_mode_metadata': 'string',
        'sales_promo_id': 'unsigned int',
        'text_format_metadata': 'string',
        'throwback_camera_roll_media': 'string',
        'video_start_time_ms': 'unsigned int',
        'application_id': 'string',
        'upload_phase': 'UploadPhase',
        'file_size': 'unsigned int',
        'start_offset': 'unsigned int',
        'end_offset': 'unsigned int',
        'video_file_chunk': 'string',
        'fbuploader_video_file_chunk': 'string',
        'upload_session_id': 'string',
        'is_voice_clip': 'bool',
        'attribution_app_id': 'string',
        'slideshow_spec': 'map',
        'upload_setting_properties': 'string',
        'transcode_setting_properties': 'string',
        'container_type': 'ContainerType',
        'referenced_sticker_id': 'string',
        'replace_video_id': 'string',
        'swap_mode': 'SwapMode',
        'name': 'string',
        'chunk_session_id': 'string',
        'manual_privacy': 'bool',
        'is_explicit_share': 'bool',
        'filename': 'file'
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ContainerType'] = AdVideo.ContainerType.__dict__.values()
        field_enum_info['ContentCategory'] = AdVideo.ContentCategory.__dict__.values()
        field_enum_info['Formatting'] = AdVideo.Formatting.__dict__.values()
        field_enum_info['OriginalProjectionType'] = AdVideo.OriginalProjectionType.__dict__.values()
        field_enum_info['SwapMode'] = AdVideo.SwapMode.__dict__.values()
        field_enum_info['UnpublishedContentType'] = AdVideo.UnpublishedContentType.__dict__.values()
        field_enum_info['UploadPhase'] = AdVideo.UploadPhase.__dict__.values()
        field_enum_info['Type'] = AdVideo.Type.__dict__.values()
        field_enum_info['BackdatedTimeGranularity'] = AdVideo.BackdatedTimeGranularity.__dict__.values()
        return field_enum_info


    def remote_create(
        self,
        batch=None,
        failure=None,
        params=None,
        success=None,
    ):
        """
        Uploads filepath and creates the AdVideo object from it.
        It has same arguments as AbstractCrudObject.remote_create except it
        does not have the files argument but requires the 'filepath' property
        to be defined.
        """
        from facebook_business.exceptions import FacebookBadObjectError
        from facebook_business.video_uploader import (
            VideoUploader,
            VideoUploadRequest,
        )

        if (self.Field.slideshow_spec in self and
        self[self.Field.slideshow_spec] is not None):
            request = VideoUploadRequest(self.get_api_assured())
            request.setParams(params={'slideshow_spec': {
                'images_urls': self[self.Field.slideshow_spec]['images_urls'],
                'duration_ms': self[self.Field.slideshow_spec]['duration_ms'],
                'transition_ms': self[self.Field.slideshow_spec]['transition_ms'],
            }})
            response = request.send((self.get_parent_id_assured(), 'advideos')).json()
        elif not (self.Field.filepath in self):
            raise FacebookBadObjectError(
                "AdVideo requires a filepath or slideshow_spec to be defined.",
            )
        else:
            video_uploader = VideoUploader()
            response = video_uploader.upload(self)
        self._set_data(response)
        return response

    def waitUntilEncodingReady(self, interval=30, timeout=600):
        from facebook_business.video_uploader import VideoEncodingStatusChecker
        from facebook_business.exceptions import FacebookError

        if 'id' not in self:
            raise FacebookError(
                'Invalid Video ID',
            )
        VideoEncodingStatusChecker.waitUntilReady(
            self.get_api_assured(),
            self['id'],
            interval,
            timeout,
        )
