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

class PageSavedFilter(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPageSavedFilter = True
        super(PageSavedFilter, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        display_name = 'display_name'
        filters = 'filters'
        id = 'id'
        page_id = 'page_id'
        section = 'section'
        time_created = 'time_created'
        time_updated = 'time_updated'

    class Section:
        active_fundraisers = 'ACTIVE_FUNDRAISERS'
        ads_canvas = 'ADS_CANVAS'
        ads_posts = 'ADS_POSTS'
        allowed = 'ALLOWED'
        all_reference_files = 'ALL_REFERENCE_FILES'
        archived_events = 'ARCHIVED_EVENTS'
        attributions = 'ATTRIBUTIONS'
        audio_releases = 'AUDIO_RELEASES'
        blocked = 'BLOCKED'
        branded_content = 'BRANDED_CONTENT'
        branded_content_creator = 'BRANDED_CONTENT_CREATOR'
        broadcasted_messages = 'BROADCASTED_MESSAGES'
        candidate_videos = 'CANDIDATE_VIDEOS'
        chex_completed_orders = 'CHEX_COMPLETED_ORDERS'
        chex_pending_orders = 'CHEX_PENDING_ORDERS'
        claimed = 'CLAIMED'
        commerce_collections = 'COMMERCE_COLLECTIONS'
        commerce_merchant_settings = 'COMMERCE_MERCHANT_SETTINGS'
        commerce_past_orders = 'COMMERCE_PAST_ORDERS'
        commerce_pending_orders = 'COMMERCE_PENDING_ORDERS'
        commerce_platform_settings = 'COMMERCE_PLATFORM_SETTINGS'
        commerce_products = 'COMMERCE_PRODUCTS'
        commerce_shop_link = 'COMMERCE_SHOP_LINK'
        content_tests = 'CONTENT_TESTS'
        creator_studio = 'CREATOR_STUDIO'
        creator_studio_all_reference_files = 'CREATOR_STUDIO_ALL_REFERENCE_FILES'
        creator_studio_blocked = 'CREATOR_STUDIO_BLOCKED'
        creator_studio_disputes = 'CREATOR_STUDIO_DISPUTES'
        creator_studio_published_all_reference_files = 'CREATOR_STUDIO_PUBLISHED_ALL_REFERENCE_FILES'
        creator_studio_published_blocked = 'CREATOR_STUDIO_PUBLISHED_BLOCKED'
        creator_studio_published_disputes = 'CREATOR_STUDIO_PUBLISHED_DISPUTES'
        creator_studio_published_manual_review = 'CREATOR_STUDIO_PUBLISHED_MANUAL_REVIEW'
        creator_studio_published_tracked = 'CREATOR_STUDIO_PUBLISHED_TRACKED'
        creator_studio_reference_conflicts = 'CREATOR_STUDIO_REFERENCE_CONFLICTS'
        creator_studio_reference_possible_conflicts = 'CREATOR_STUDIO_REFERENCE_POSSIBLE_CONFLICTS'
        creator_studio_reference_resolutions = 'CREATOR_STUDIO_REFERENCE_RESOLUTIONS'
        creator_studio_takedowns = 'CREATOR_STUDIO_TAKEDOWNS'
        creator_studio_tracked = 'CREATOR_STUDIO_TRACKED'
        crossposted_videos = 'CROSSPOSTED_VIDEOS'
        disputes = 'DISPUTES'
        donations_settings = 'DONATIONS_SETTINGS'
        drafts = 'DRAFTS'
        draft_events = 'DRAFT_EVENTS'
        draft_fundraisers = 'DRAFT_FUNDRAISERS'
        ended_fundraisers = 'ENDED_FUNDRAISERS'
        expired_posts = 'EXPIRED_POSTS'
        expiring_posts = 'EXPIRING_POSTS'
        gem_producer_dashboard = 'GEM_PRODUCER_DASHBOARD'
        ia_regiwall_settings = 'IA_REGIWALL_SETTINGS'
        instant_articles = 'INSTANT_ARTICLES'
        instant_articles_cta_management = 'INSTANT_ARTICLES_CTA_MANAGEMENT'
        instant_articles_development = 'INSTANT_ARTICLES_DEVELOPMENT'
        instant_articles_monetization = 'INSTANT_ARTICLES_MONETIZATION'
        instant_articles_sample = 'INSTANT_ARTICLES_SAMPLE'
        instant_articles_settings = 'INSTANT_ARTICLES_SETTINGS'
        instant_articles_sign_up = 'INSTANT_ARTICLES_SIGN_UP'
        instant_articles_traffic_lift = 'INSTANT_ARTICLES_TRAFFIC_LIFT'
        invoices_active = 'INVOICES_ACTIVE'
        invoices_history = 'INVOICES_HISTORY'
        job_applications = 'JOB_APPLICATIONS'
        job_posts = 'JOB_POSTS'
        lead_ads_crm_setup = 'LEAD_ADS_CRM_SETUP'
        lead_ads_custom_crm_setup = 'LEAD_ADS_CUSTOM_CRM_SETUP'
        lead_ads_draft_forms = 'LEAD_ADS_DRAFT_FORMS'
        lead_ads_forms = 'LEAD_ADS_FORMS'
        live_broadcasts = 'LIVE_BROADCASTS'
        manual_claims = 'MANUAL_CLAIMS'
        manual_claim_facebook_videos = 'MANUAL_CLAIM_FACEBOOK_VIDEOS'
        manual_claim_instagram_videos = 'MANUAL_CLAIM_INSTAGRAM_VIDEOS'
        manual_review = 'MANUAL_REVIEW'
        match_rules = 'MATCH_RULES'
        monetized_videos = 'MONETIZED_VIDEOS'
        news_subscriptions = 'NEWS_SUBSCRIPTIONS'
        news_subscriptions_publisher_asset_management = 'NEWS_SUBSCRIPTIONS_PUBLISHER_ASSET_MANAGEMENT'
        news_subscriptions_publisher_developer_tools = 'NEWS_SUBSCRIPTIONS_PUBLISHER_DEVELOPER_TOOLS'
        news_subscriptions_publisher_insights = 'NEWS_SUBSCRIPTIONS_PUBLISHER_INSIGHTS'
        news_subscriptions_publisher_offer_management = 'NEWS_SUBSCRIPTIONS_PUBLISHER_OFFER_MANAGEMENT'
        news_subscriptions_publisher_test_users = 'NEWS_SUBSCRIPTIONS_PUBLISHER_TEST_USERS'
        news_subscriptions_publisher_tools = 'NEWS_SUBSCRIPTIONS_PUBLISHER_TOOLS'
        new_matches = 'NEW_MATCHES'
        pending_profile_picture_frames = 'PENDING_PROFILE_PICTURE_FRAMES'
        playlists = 'PLAYLISTS'
        playlist_details = 'PLAYLIST_DETAILS'
        polls_composer = 'POLLS_COMPOSER'
        posts_config = 'POSTS_CONFIG'
        post_ideas = 'POST_IDEAS'
        premium_music_videos = 'PREMIUM_MUSIC_VIDEOS'
        published_events = 'PUBLISHED_EVENTS'
        published_posts = 'PUBLISHED_POSTS'
        published_profile_picture_frames = 'PUBLISHED_PROFILE_PICTURE_FRAMES'
        qr_code = 'QR_CODE'
        ready_fundraisers = 'READY_FUNDRAISERS'
        reference_conflicts = 'REFERENCE_CONFLICTS'
        reference_files = 'REFERENCE_FILES'
        reference_possible_conflicts = 'REFERENCE_POSSIBLE_CONFLICTS'
        reference_resolutions = 'REFERENCE_RESOLUTIONS'
        registrations = 'REGISTRATIONS'
        reported = 'REPORTED'
        reward_program = 'REWARD_PROGRAM'
        scheduled_events = 'SCHEDULED_EVENTS'
        scheduled_posts = 'SCHEDULED_POSTS'
        seasons = 'SEASONS'
        season_details = 'SEASON_DETAILS'
        sounds_collection = 'SOUNDS_COLLECTION'
        sound_recordings = 'SOUND_RECORDINGS'
        story_archive = 'STORY_ARCHIVE'
        takedowns = 'TAKEDOWNS'
        tours = 'TOURS'
        tracked = 'TRACKED'
        unsent_reports = 'UNSENT_REPORTS'
        videos = 'VIDEOS'
        videos_copyright = 'VIDEOS_COPYRIGHT'

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
            target_class=PageSavedFilter,
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

    _field_types = {
        'display_name': 'string',
        'filters': 'list<Object>',
        'id': 'string',
        'page_id': 'string',
        'section': 'string',
        'time_created': 'int',
        'time_updated': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Section'] = PageSavedFilter.Section.__dict__.values()
        return field_enum_info


