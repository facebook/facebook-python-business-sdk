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
        copyright = 'copyright'
        copyright_monitoring_status = 'copyright_monitoring_status'
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
        is_reference_only = 'is_reference_only'
        length = 'length'
        live_audience_count = 'live_audience_count'
        live_status = 'live_status'
        music_video_copyright = 'music_video_copyright'
        permalink_url = 'permalink_url'
        picture = 'picture'
        place = 'place'
        post_views = 'post_views'
        premiere_living_room_status = 'premiere_living_room_status'
        privacy = 'privacy'
        published = 'published'
        scheduled_publish_time = 'scheduled_publish_time'
        source = 'source'
        spherical = 'spherical'
        status = 'status'
        title = 'title'
        universal_video_id = 'universal_video_id'
        updated_time = 'updated_time'
        views = 'views'
        adaptive_type = 'adaptive_type'
        animated_effect_id = 'animated_effect_id'
        application_id = 'application_id'
        asked_fun_fact_prompt_id = 'asked_fun_fact_prompt_id'
        audio_story_wave_animation_handle = 'audio_story_wave_animation_handle'
        chunk_session_id = 'chunk_session_id'
        composer_entry_picker = 'composer_entry_picker'
        composer_entry_point = 'composer_entry_point'
        composer_entry_time = 'composer_entry_time'
        composer_session_events_log = 'composer_session_events_log'
        composer_session_id = 'composer_session_id'
        composer_source_surface = 'composer_source_surface'
        composer_type = 'composer_type'
        container_type = 'container_type'
        creative_tools = 'creative_tools'
        end_offset = 'end_offset'
        fbuploader_video_file_chunk = 'fbuploader_video_file_chunk'
        file_size = 'file_size'
        file_url = 'file_url'
        fisheye_video_cropped = 'fisheye_video_cropped'
        formatting = 'formatting'
        fov = 'fov'
        front_z_rotation = 'front_z_rotation'
        fun_fact_prompt_id = 'fun_fact_prompt_id'
        fun_fact_toastee_id = 'fun_fact_toastee_id'
        guide = 'guide'
        guide_enabled = 'guide_enabled'
        has_nickname = 'has_nickname'
        holiday_card = 'holiday_card'
        initial_heading = 'initial_heading'
        initial_pitch = 'initial_pitch'
        instant_game_entry_point_data = 'instant_game_entry_point_data'
        is_boost_intended = 'is_boost_intended'
        is_group_linking_post = 'is_group_linking_post'
        is_voice_clip = 'is_voice_clip'
        location_source_id = 'location_source_id'
        name = 'name'
        offer_like_post_id = 'offer_like_post_id'
        og_action_type_id = 'og_action_type_id'
        og_icon_id = 'og_icon_id'
        og_object_id = 'og_object_id'
        og_phrase = 'og_phrase'
        og_suggestion_mechanism = 'og_suggestion_mechanism'
        original_fov = 'original_fov'
        original_projection_type = 'original_projection_type'
        publish_event_id = 'publish_event_id'
        react_mode_metadata = 'react_mode_metadata'
        referenced_sticker_id = 'referenced_sticker_id'
        replace_video_id = 'replace_video_id'
        slideshow_spec = 'slideshow_spec'
        source_instagram_media_id = 'source_instagram_media_id'
        start_offset = 'start_offset'
        swap_mode = 'swap_mode'
        text_format_metadata = 'text_format_metadata'
        throwback_camera_roll_media = 'throwback_camera_roll_media'
        thumb = 'thumb'
        time_since_original_post = 'time_since_original_post'
        transcode_setting_properties = 'transcode_setting_properties'
        unpublished_content_type = 'unpublished_content_type'
        upload_phase = 'upload_phase'
        upload_session_id = 'upload_session_id'
        upload_setting_properties = 'upload_setting_properties'
        video_file_chunk = 'video_file_chunk'
        video_id_original = 'video_id_original'
        video_start_time_ms = 'video_start_time_ms'
        waterfall_id = 'waterfall_id'
        filename = 'filename'
        filepath = 'filepath'

    class ContainerType:
        aco_autoextracted_video = 'ACO_AUTOEXTRACTED_VIDEO'
        aco_video_variation = 'ACO_VIDEO_VARIATION'
        ad_break_preview = 'AD_BREAK_PREVIEW'
        ad_derivative = 'AD_DERIVATIVE'
        age_up = 'AGE_UP'
        album_multimedia_post = 'ALBUM_MULTIMEDIA_POST'
        aloha_call_video = 'ALOHA_CALL_VIDEO'
        aloha_superframe = 'ALOHA_SUPERFRAME'
        app_rereview_screencast = 'APP_REREVIEW_SCREENCAST'
        app_review_screencast = 'APP_REVIEW_SCREENCAST'
        asset_manager = 'ASSET_MANAGER'
        atlas_video = 'ATLAS_VIDEO'
        audio_broadcast = 'AUDIO_BROADCAST'
        audio_comment = 'AUDIO_COMMENT'
        broadcast = 'BROADCAST'
        bulletin_article_audio = 'BULLETIN_ARTICLE_AUDIO'
        canvas = 'CANVAS'
        cfc_video = 'CFC_VIDEO'
        cms_media_manager = 'CMS_MEDIA_MANAGER'
        contained_post_attachment = 'CONTAINED_POST_ATTACHMENT'
        contained_post_audio_broadcast = 'CONTAINED_POST_AUDIO_BROADCAST'
        contained_post_copyright_reference_broadcast = 'CONTAINED_POST_COPYRIGHT_REFERENCE_BROADCAST'
        copyright_reference_broadcast = 'COPYRIGHT_REFERENCE_BROADCAST'
        copyright_reference_video = 'COPYRIGHT_REFERENCE_VIDEO'
        creation_ml_precreation = 'CREATION_ML_PRECREATION'
        cultural_moment_deprecated = 'CULTURAL_MOMENT_DEPRECATED'
        dco_ad_asset_feed = 'DCO_AD_ASSET_FEED'
        dco_autogen_video = 'DCO_AUTOGEN_VIDEO'
        dco_trimmed_video = 'DCO_TRIMMED_VIDEO'
        dim_sum = 'DIM_SUM'
        directed_post_attachment = 'DIRECTED_POST_ATTACHMENT'
        direct_inbox = 'DIRECT_INBOX'
        direct_inbox_reaction = 'DIRECT_INBOX_REACTION'
        dynamic_item_display_bundle = 'DYNAMIC_ITEM_DISPLAY_BUNDLE'
        dynamic_item_video = 'DYNAMIC_ITEM_VIDEO'
        dynamic_template_video = 'DYNAMIC_TEMPLATE_VIDEO'
        event_cover_video = 'EVENT_COVER_VIDEO'
        event_tour = 'EVENT_TOUR'
        facecast_dvr = 'FACECAST_DVR'
        fb_shorts = 'FB_SHORTS'
        fb_shorts_group_post = 'FB_SHORTS_GROUP_POST'
        fb_shorts_pmv_post = 'FB_SHORTS_PMV_POST'
        fb_shorts_post = 'FB_SHORTS_POST'
        fb_shorts_remix_post = 'FB_SHORTS_REMIX_POST'
        fundraiser_cover_video = 'FUNDRAISER_COVER_VIDEO'
        game_clip = 'GAME_CLIP'
        gemstone = 'GEMSTONE'
        goodwill_anniversary_deprecated = 'GOODWILL_ANNIVERSARY_DEPRECATED'
        goodwill_anniversary_promotion_deprecated = 'GOODWILL_ANNIVERSARY_PROMOTION_DEPRECATED'
        goodwill_video_contained_share = 'GOODWILL_VIDEO_CONTAINED_SHARE'
        goodwill_video_promotion = 'GOODWILL_VIDEO_PROMOTION'
        goodwill_video_share = 'GOODWILL_VIDEO_SHARE'
        goodwill_video_token_required = 'GOODWILL_VIDEO_TOKEN_REQUIRED'
        group_post = 'GROUP_POST'
        hack_tv = 'HACK_TV'
        heuristic_cluster_video = 'HEURISTIC_CLUSTER_VIDEO'
        heuristic_preview = 'HEURISTIC_PREVIEW'
        highlight_clip_video = 'HIGHLIGHT_CLIP_VIDEO'
        huddle_broadcast = 'HUDDLE_BROADCAST'
        ig_reels_xpv = 'IG_REELS_XPV'
        ig_stories_reader = 'IG_STORIES_READER'
        inspiration_video = 'INSPIRATION_VIDEO'
        instagram_video_copy = 'INSTAGRAM_VIDEO_COPY'
        instant_application_preview = 'INSTANT_APPLICATION_PREVIEW'
        instant_article = 'INSTANT_ARTICLE'
        instant_game_clip = 'INSTANT_GAME_CLIP'
        issue_module = 'ISSUE_MODULE'
        jobs_careers = 'JOBS_CAREERS'
        jobs_visual_intro_entry = 'JOBS_VISUAL_INTRO_ENTRY'
        job_application_video = 'JOB_APPLICATION_VIDEO'
        job_opening_video = 'JOB_OPENING_VIDEO'
        kototoro = 'KOTOTORO'
        learn = 'LEARN'
        legacy = 'LEGACY'
        legacy_contained_post_broadcast = 'LEGACY_CONTAINED_POST_BROADCAST'
        live_clip_preview = 'LIVE_CLIP_PREVIEW'
        live_creative_kit_video = 'LIVE_CREATIVE_KIT_VIDEO'
        live_photo = 'LIVE_PHOTO'
        look_now_deprecated = 'LOOK_NOW_DEPRECATED'
        marketplace_listing_video = 'MARKETPLACE_LISTING_VIDEO'
        marketplace_pre_recorded_video = 'MARKETPLACE_PRE_RECORDED_VIDEO'
        messenger_watch_together = 'MESSENGER_WATCH_TOGETHER'
        moments_video = 'MOMENTS_VIDEO'
        music_clip = 'MUSIC_CLIP'
        music_clip_in_comment = 'MUSIC_CLIP_IN_COMMENT'
        music_clip_in_lightweight_status = 'MUSIC_CLIP_IN_LIGHTWEIGHT_STATUS'
        music_clip_in_poll_option = 'MUSIC_CLIP_IN_POLL_OPTION'
        music_clip_on_dating_profile = 'MUSIC_CLIP_ON_DATING_PROFILE'
        neo_async_game_video = 'NEO_ASYNC_GAME_VIDEO'
        new_contained_post_broadcast = 'NEW_CONTAINED_POST_BROADCAST'
        no_story = 'NO_STORY'
        no_story_with_entpost = 'NO_STORY_WITH_ENTPOST'
        npe_collab_copyright_check = 'NPE_COLLAB_COPYRIGHT_CHECK'
        oculus_creator_portal = 'OCULUS_CREATOR_PORTAL'
        oculus_venues_broadcast = 'OCULUS_VENUES_BROADCAST'
        offers_video = 'OFFERS_VIDEO'
        pages_cover_video = 'PAGES_COVER_VIDEO'
        page_review_screencast = 'PAGE_REVIEW_SCREENCAST'
        page_slideshow_video = 'PAGE_SLIDESHOW_VIDEO'
        paid_content_preview = 'PAID_CONTENT_PREVIEW'
        paid_content_video = 'PAID_CONTENT_VIDEO'
        paid_content_video__post = 'PAID_CONTENT_VIDEO__POST'
        partner_directory_brand_media = 'PARTNER_DIRECTORY_BRAND_MEDIA'
        pixelcloud = 'PIXELCLOUD'
        podcast_highlight = 'PODCAST_HIGHLIGHT'
        podcast_ml_preview = 'PODCAST_ML_PREVIEW'
        podcast_ml_preview_no_newsfeed_story = 'PODCAST_ML_PREVIEW_NO_NEWSFEED_STORY'
        podcast_rss = 'PODCAST_RSS'
        podcast_rss_ephemeral = 'PODCAST_RSS_EPHEMERAL'
        podcast_rss_no_newsfeed_story = 'PODCAST_RSS_NO_NEWSFEED_STORY'
        podcast_voices = 'PODCAST_VOICES'
        podcast_voices_no_newsfeed_story = 'PODCAST_VOICES_NO_NEWSFEED_STORY'
        premiere_source = 'PREMIERE_SOURCE'
        premium_music_video_clip = 'PREMIUM_MUSIC_VIDEO_CLIP'
        premium_music_video_cropped_clip = 'PREMIUM_MUSIC_VIDEO_CROPPED_CLIP'
        premium_music_video_no_newsfeed_story = 'PREMIUM_MUSIC_VIDEO_NO_NEWSFEED_STORY'
        premium_music_video_with_newsfeed_story = 'PREMIUM_MUSIC_VIDEO_WITH_NEWSFEED_STORY'
        private_gallery_video = 'PRIVATE_GALLERY_VIDEO'
        product_video = 'PRODUCT_VIDEO'
        profile_cover_video = 'PROFILE_COVER_VIDEO'
        profile_intro_card = 'PROFILE_INTRO_CARD'
        profile_video = 'PROFILE_VIDEO'
        proton = 'PROTON'
        quick_promotion = 'QUICK_PROMOTION'
        replace_video = 'REPLACE_VIDEO'
        sales_client_interaction = 'SALES_CLIENT_INTERACTION'
        say_thanks_deprecated = 'SAY_THANKS_DEPRECATED'
        showreel_native_dummy_video = 'SHOWREEL_NATIVE_DUMMY_VIDEO'
        slideshow_animoto = 'SLIDESHOW_ANIMOTO'
        slideshow_shakr = 'SLIDESHOW_SHAKR'
        slideshow_variation_video = 'SLIDESHOW_VARIATION_VIDEO'
        sotto_content = 'SOTTO_CONTENT'
        soundbites_video = 'SOUNDBITES_VIDEO'
        sound_platform_stream = 'SOUND_PLATFORM_STREAM'
        srt_attachment = 'SRT_ATTACHMENT'
        stages_broadcast = 'STAGES_BROADCAST'
        stories_video = 'STORIES_VIDEO'
        storyline = 'STORYLINE'
        storyline_with_external_music = 'STORYLINE_WITH_EXTERNAL_MUSIC'
        story_archive_video = 'STORY_ARCHIVE_VIDEO'
        story_card_template = 'STORY_CARD_TEMPLATE'
        stream_highlights_video = 'STREAM_HIGHLIGHTS_VIDEO'
        tarot_digest = 'TAROT_DIGEST'
        temporary_unlisted = 'TEMPORARY_UNLISTED'
        temp_multimedia_post = 'TEMP_MULTIMEDIA_POST'
        unlisted = 'UNLISTED'
        unlisted_hack_tv = 'UNLISTED_HACK_TV'
        unlisted_oculus = 'UNLISTED_OCULUS'
        video_comment = 'VIDEO_COMMENT'
        video_composition_variation = 'VIDEO_COMPOSITION_VARIATION'
        video_creative_editor_autogen_ad_video = 'VIDEO_CREATIVE_EDITOR_AUTOGEN_AD_VIDEO'
        video_superres = 'VIDEO_SUPERRES'
        voices_article_video = 'VOICES_ARTICLE_VIDEO'
        vu_generated_video = 'VU_GENERATED_VIDEO'
        woodhenge = 'WOODHENGE'
        work_knowledge_video = 'WORK_KNOWLEDGE_VIDEO'
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
        equirectangular = 'equirectangular'
        half_equirectangular = 'half_equirectangular'

    class SwapMode:
        replace = 'replace'

    class UnpublishedContentType:
        ads_post = 'ADS_POST'
        draft = 'DRAFT'
        inline_created = 'INLINE_CREATED'
        published = 'PUBLISHED'
        reviewable_branded_content = 'REVIEWABLE_BRANDED_CONTENT'
        scheduled = 'SCHEDULED'
        scheduled_recurring = 'SCHEDULED_RECURRING'

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

    # @deprecated api_create is being deprecated
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
            'ad_breaks': 'list',
            'allow_bm_crossposting': 'bool',
            'allow_crossposting_for_pages': 'list<Object>',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'call_to_action': 'Object',
            'content_category': 'content_category_enum',
            'content_tags': 'list<string>',
            'custom_labels': 'list<string>',
            'description': 'string',
            'direct_share_status': 'unsigned int',
            'embeddable': 'bool',
            'expiration': 'Object',
            'expire_now': 'bool',
            'increment_play_count': 'bool',
            'name': 'string',
            'preferred_thumbnail_id': 'string',
            'privacy': 'string',
            'publish_to_news_feed': 'bool',
            'publish_to_videos_tab': 'bool',
            'published': 'bool',
            'scheduled_publish_time': 'unsigned int',
            'social_actions': 'bool',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'tags': 'list<string>',
            'target': 'string',
            'universal_video_id': 'string',
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
            'captions_file': 'file',
            'default_locale': 'string',
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
            'live_filter': 'live_filter_enum',
            'order': 'order_enum',
            'since': 'datetime',
        }
        enums = {
            'filter_enum': Comment.Filter.__dict__.values(),
            'live_filter_enum': Comment.LiveFilter.__dict__.values(),
            'order_enum': Comment.Order.__dict__.values(),
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
            'attachment_id': 'string',
            'attachment_share_url': 'string',
            'attachment_url': 'string',
            'comment_privacy_value': 'comment_privacy_value_enum',
            'facepile_mentioned_ids': 'list<string>',
            'feedback_source': 'string',
            'is_offline': 'bool',
            'message': 'string',
            'nectar_module': 'string',
            'object_id': 'string',
            'parent_comment_id': 'Object',
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

    def create_gaming_clip_create(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'duration_seconds': 'float',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/gaming_clip_create',
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
            'feedback_source': 'string',
            'nectar_module': 'string',
            'notify': 'bool',
            'tracking': 'string',
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

    def get_poll_settings(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/poll_settings',
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
            'close_after_voting': 'bool',
            'correct_option': 'unsigned int',
            'default_open': 'bool',
            'options': 'list<string>',
            'question': 'string',
            'show_gradient': 'bool',
            'show_results': 'bool',
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

    def get_tags(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/tags',
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

    def create_tag(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'tag_uid': 'int',
            'uid': 'int',
            'vid': 'string',
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
            'is_preferred': 'bool',
            'source': 'file',
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
        'copyright': 'VideoCopyright',
        'copyright_monitoring_status': 'string',
        'created_time': 'datetime',
        'custom_labels': 'list<string>',
        'description': 'string',
        'embed_html': 'Object',
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
        'is_reference_only': 'bool',
        'length': 'float',
        'live_audience_count': 'unsigned int',
        'live_status': 'string',
        'music_video_copyright': 'MusicVideoCopyright',
        'permalink_url': 'Object',
        'picture': 'string',
        'place': 'Place',
        'post_views': 'unsigned int',
        'premiere_living_room_status': 'string',
        'privacy': 'Privacy',
        'published': 'bool',
        'scheduled_publish_time': 'datetime',
        'source': 'string',
        'spherical': 'bool',
        'status': 'Object',
        'title': 'string',
        'universal_video_id': 'string',
        'updated_time': 'datetime',
        'views': 'unsigned int',
        'adaptive_type': 'string',
        'animated_effect_id': 'unsigned int',
        'application_id': 'string',
        'asked_fun_fact_prompt_id': 'unsigned int',
        'audio_story_wave_animation_handle': 'string',
        'chunk_session_id': 'string',
        'composer_entry_picker': 'string',
        'composer_entry_point': 'string',
        'composer_entry_time': 'unsigned int',
        'composer_session_events_log': 'string',
        'composer_session_id': 'string',
        'composer_source_surface': 'string',
        'composer_type': 'string',
        'container_type': 'ContainerType',
        'creative_tools': 'string',
        'end_offset': 'unsigned int',
        'fbuploader_video_file_chunk': 'string',
        'file_size': 'unsigned int',
        'file_url': 'string',
        'fisheye_video_cropped': 'bool',
        'formatting': 'Formatting',
        'fov': 'unsigned int',
        'front_z_rotation': 'float',
        'fun_fact_prompt_id': 'unsigned int',
        'fun_fact_toastee_id': 'unsigned int',
        'guide': 'list<list<unsigned int>>',
        'guide_enabled': 'bool',
        'has_nickname': 'bool',
        'holiday_card': 'string',
        'initial_heading': 'unsigned int',
        'initial_pitch': 'unsigned int',
        'instant_game_entry_point_data': 'string',
        'is_boost_intended': 'bool',
        'is_group_linking_post': 'bool',
        'is_voice_clip': 'bool',
        'location_source_id': 'string',
        'name': 'string',
        'offer_like_post_id': 'unsigned int',
        'og_action_type_id': 'string',
        'og_icon_id': 'string',
        'og_object_id': 'string',
        'og_phrase': 'string',
        'og_suggestion_mechanism': 'string',
        'original_fov': 'unsigned int',
        'original_projection_type': 'OriginalProjectionType',
        'publish_event_id': 'unsigned int',
        'react_mode_metadata': 'string',
        'referenced_sticker_id': 'string',
        'replace_video_id': 'string',
        'slideshow_spec': 'map',
        'source_instagram_media_id': 'string',
        'start_offset': 'unsigned int',
        'swap_mode': 'SwapMode',
        'text_format_metadata': 'string',
        'throwback_camera_roll_media': 'string',
        'thumb': 'file',
        'time_since_original_post': 'unsigned int',
        'transcode_setting_properties': 'string',
        'unpublished_content_type': 'UnpublishedContentType',
        'upload_phase': 'UploadPhase',
        'upload_session_id': 'string',
        'upload_setting_properties': 'string',
        'video_file_chunk': 'string',
        'video_id_original': 'string',
        'video_start_time_ms': 'unsigned int',
        'waterfall_id': 'string',
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
