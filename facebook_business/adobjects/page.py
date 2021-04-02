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

class Page(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPage = True
        super(Page, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        about = 'about'
        access_token = 'access_token'
        ad_campaign = 'ad_campaign'
        affiliation = 'affiliation'
        app_id = 'app_id'
        artists_we_like = 'artists_we_like'
        attire = 'attire'
        awards = 'awards'
        band_interests = 'band_interests'
        band_members = 'band_members'
        best_page = 'best_page'
        bio = 'bio'
        birthday = 'birthday'
        booking_agent = 'booking_agent'
        built = 'built'
        business = 'business'
        can_checkin = 'can_checkin'
        can_post = 'can_post'
        category = 'category'
        category_list = 'category_list'
        checkins = 'checkins'
        company_overview = 'company_overview'
        connected_instagram_account = 'connected_instagram_account'
        connected_page_backed_instagram_account = 'connected_page_backed_instagram_account'
        contact_address = 'contact_address'
        copyright_whitelisted_ig_partners = 'copyright_whitelisted_ig_partners'
        country_page_likes = 'country_page_likes'
        cover = 'cover'
        culinary_team = 'culinary_team'
        current_location = 'current_location'
        delivery_and_pickup_option_info = 'delivery_and_pickup_option_info'
        description = 'description'
        description_html = 'description_html'
        differently_open_offerings = 'differently_open_offerings'
        directed_by = 'directed_by'
        display_subtext = 'display_subtext'
        displayed_message_response_time = 'displayed_message_response_time'
        emails = 'emails'
        engagement = 'engagement'
        fan_count = 'fan_count'
        featured_video = 'featured_video'
        features = 'features'
        followers_count = 'followers_count'
        food_styles = 'food_styles'
        founded = 'founded'
        general_info = 'general_info'
        general_manager = 'general_manager'
        genre = 'genre'
        global_brand_page_name = 'global_brand_page_name'
        global_brand_root_id = 'global_brand_root_id'
        has_added_app = 'has_added_app'
        has_whatsapp_business_number = 'has_whatsapp_business_number'
        has_whatsapp_number = 'has_whatsapp_number'
        hometown = 'hometown'
        hours = 'hours'
        id = 'id'
        impressum = 'impressum'
        influences = 'influences'
        instagram_business_account = 'instagram_business_account'
        instant_articles_review_status = 'instant_articles_review_status'
        is_always_open = 'is_always_open'
        is_chain = 'is_chain'
        is_community_page = 'is_community_page'
        is_eligible_for_branded_content = 'is_eligible_for_branded_content'
        is_messenger_bot_get_started_enabled = 'is_messenger_bot_get_started_enabled'
        is_messenger_platform_bot = 'is_messenger_platform_bot'
        is_owned = 'is_owned'
        is_permanently_closed = 'is_permanently_closed'
        is_published = 'is_published'
        is_unclaimed = 'is_unclaimed'
        is_verified = 'is_verified'
        is_webhooks_subscribed = 'is_webhooks_subscribed'
        keywords = 'keywords'
        leadgen_tos_acceptance_time = 'leadgen_tos_acceptance_time'
        leadgen_tos_accepted = 'leadgen_tos_accepted'
        leadgen_tos_accepting_user = 'leadgen_tos_accepting_user'
        link = 'link'
        location = 'location'
        members = 'members'
        merchant_id = 'merchant_id'
        merchant_review_status = 'merchant_review_status'
        messenger_ads_default_icebreakers = 'messenger_ads_default_icebreakers'
        messenger_ads_default_page_welcome_message = 'messenger_ads_default_page_welcome_message'
        messenger_ads_default_quick_replies = 'messenger_ads_default_quick_replies'
        messenger_ads_quick_replies_type = 'messenger_ads_quick_replies_type'
        mission = 'mission'
        mpg = 'mpg'
        name = 'name'
        name_with_location_descriptor = 'name_with_location_descriptor'
        network = 'network'
        new_like_count = 'new_like_count'
        offer_eligible = 'offer_eligible'
        overall_star_rating = 'overall_star_rating'
        page_token = 'page_token'
        parent_page = 'parent_page'
        parking = 'parking'
        payment_options = 'payment_options'
        personal_info = 'personal_info'
        personal_interests = 'personal_interests'
        pharma_safety_info = 'pharma_safety_info'
        phone = 'phone'
        pickup_options = 'pickup_options'
        place_type = 'place_type'
        plot_outline = 'plot_outline'
        preferred_audience = 'preferred_audience'
        press_contact = 'press_contact'
        price_range = 'price_range'
        privacy_info_url = 'privacy_info_url'
        produced_by = 'produced_by'
        products = 'products'
        promotion_eligible = 'promotion_eligible'
        promotion_ineligible_reason = 'promotion_ineligible_reason'
        public_transit = 'public_transit'
        rating_count = 'rating_count'
        recipient = 'recipient'
        record_label = 'record_label'
        release_date = 'release_date'
        restaurant_services = 'restaurant_services'
        restaurant_specialties = 'restaurant_specialties'
        schedule = 'schedule'
        screenplay_by = 'screenplay_by'
        season = 'season'
        single_line_address = 'single_line_address'
        starring = 'starring'
        start_info = 'start_info'
        store_code = 'store_code'
        store_location_descriptor = 'store_location_descriptor'
        store_number = 'store_number'
        studio = 'studio'
        supports_donate_button_in_live_video = 'supports_donate_button_in_live_video'
        supports_instant_articles = 'supports_instant_articles'
        talking_about_count = 'talking_about_count'
        temporary_status = 'temporary_status'
        unread_message_count = 'unread_message_count'
        unread_notif_count = 'unread_notif_count'
        unseen_message_count = 'unseen_message_count'
        username = 'username'
        verification_status = 'verification_status'
        voip_info = 'voip_info'
        website = 'website'
        were_here_count = 'were_here_count'
        whatsapp_number = 'whatsapp_number'
        written_by = 'written_by'

    class Attire:
        casual = 'Casual'
        dressy = 'Dressy'
        unspecified = 'Unspecified'

    class FoodStyles:
        afghani = 'Afghani'
        american_new_ = 'American (New)'
        american_traditional_ = 'American (Traditional)'
        asian_fusion = 'Asian Fusion'
        barbeque = 'Barbeque'
        brazilian = 'Brazilian'
        breakfast = 'Breakfast'
        british = 'British'
        brunch = 'Brunch'
        buffets = 'Buffets'
        burgers = 'Burgers'
        burmese = 'Burmese'
        cajun_creole = 'Cajun/Creole'
        caribbean = 'Caribbean'
        chinese = 'Chinese'
        creperies = 'Creperies'
        cuban = 'Cuban'
        delis = 'Delis'
        diners = 'Diners'
        ethiopian = 'Ethiopian'
        fast_food = 'Fast Food'
        filipino = 'Filipino'
        fondue = 'Fondue'
        food_stands = 'Food Stands'
        french = 'French'
        german = 'German'
        greek_and_mediterranean = 'Greek and Mediterranean'
        hawaiian = 'Hawaiian'
        himalayan_nepalese = 'Himalayan/Nepalese'
        hot_dogs = 'Hot Dogs'
        indian_pakistani = 'Indian/Pakistani'
        irish = 'Irish'
        italian = 'Italian'
        japanese = 'Japanese'
        korean = 'Korean'
        latin_american = 'Latin American'
        mexican = 'Mexican'
        middle_eastern = 'Middle Eastern'
        moroccan = 'Moroccan'
        pizza = 'Pizza'
        russian = 'Russian'
        sandwiches = 'Sandwiches'
        seafood = 'Seafood'
        singaporean = 'Singaporean'
        soul_food = 'Soul Food'
        southern = 'Southern'
        spanish_basque = 'Spanish/Basque'
        steakhouses = 'Steakhouses'
        sushi_bars = 'Sushi Bars'
        taiwanese = 'Taiwanese'
        tapas_bars = 'Tapas Bars'
        tex_mex = 'Tex-Mex'
        thai = 'Thai'
        turkish = 'Turkish'
        vegan = 'Vegan'
        vegetarian = 'Vegetarian'
        vietnamese = 'Vietnamese'

    class PickupOptions:
        curbside = 'CURBSIDE'
        in_store = 'IN_STORE'
        other = 'OTHER'

    class TemporaryStatus:
        differently_open = 'DIFFERENTLY_OPEN'
        no_data = 'NO_DATA'
        operating_as_usual = 'OPERATING_AS_USUAL'
        temporarily_closed = 'TEMPORARILY_CLOSED'

    class PermittedTasks:
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'
        cashier_role = 'CASHIER_ROLE'
        create_content = 'CREATE_CONTENT'
        manage = 'MANAGE'
        manage_jobs = 'MANAGE_JOBS'
        manage_leads = 'MANAGE_LEADS'
        messaging = 'MESSAGING'
        moderate = 'MODERATE'
        moderate_community = 'MODERATE_COMMUNITY'
        pages_messaging = 'PAGES_MESSAGING'
        pages_messaging_subscriptions = 'PAGES_MESSAGING_SUBSCRIPTIONS'
        profile_plus_advertise = 'PROFILE_PLUS_ADVERTISE'
        profile_plus_analyze = 'PROFILE_PLUS_ANALYZE'
        profile_plus_create_content = 'PROFILE_PLUS_CREATE_CONTENT'
        profile_plus_manage = 'PROFILE_PLUS_MANAGE'
        profile_plus_messaging = 'PROFILE_PLUS_MESSAGING'
        profile_plus_moderate = 'PROFILE_PLUS_MODERATE'
        read_page_mailboxes = 'READ_PAGE_MAILBOXES'
        view_monetization_insights = 'VIEW_MONETIZATION_INSIGHTS'

    class Tasks:
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'
        cashier_role = 'CASHIER_ROLE'
        create_content = 'CREATE_CONTENT'
        manage = 'MANAGE'
        manage_jobs = 'MANAGE_JOBS'
        manage_leads = 'MANAGE_LEADS'
        messaging = 'MESSAGING'
        moderate = 'MODERATE'
        moderate_community = 'MODERATE_COMMUNITY'
        pages_messaging = 'PAGES_MESSAGING'
        pages_messaging_subscriptions = 'PAGES_MESSAGING_SUBSCRIPTIONS'
        profile_plus_advertise = 'PROFILE_PLUS_ADVERTISE'
        profile_plus_analyze = 'PROFILE_PLUS_ANALYZE'
        profile_plus_create_content = 'PROFILE_PLUS_CREATE_CONTENT'
        profile_plus_manage = 'PROFILE_PLUS_MANAGE'
        profile_plus_messaging = 'PROFILE_PLUS_MESSAGING'
        profile_plus_moderate = 'PROFILE_PLUS_MODERATE'
        read_page_mailboxes = 'READ_PAGE_MAILBOXES'
        view_monetization_insights = 'VIEW_MONETIZATION_INSIGHTS'

    class BackdatedTimeGranularity:
        day = 'day'
        hour = 'hour'
        min = 'min'
        month = 'month'
        none = 'none'
        year = 'year'

    class CheckinEntryPoint:
        branding_checkin = 'BRANDING_CHECKIN'
        branding_other = 'BRANDING_OTHER'
        branding_photo = 'BRANDING_PHOTO'
        branding_status = 'BRANDING_STATUS'

    class Formatting:
        markdown = 'MARKDOWN'
        plaintext = 'PLAINTEXT'

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
        disabled = 'disabled'
        enabled = 'enabled'

    class TargetSurface:
        story = 'STORY'
        timeline = 'TIMELINE'

    class UnpublishedContentType:
        ads_post = 'ADS_POST'
        draft = 'DRAFT'
        inline_created = 'INLINE_CREATED'
        published = 'PUBLISHED'
        reviewable_branded_content = 'REVIEWABLE_BRANDED_CONTENT'
        scheduled = 'SCHEDULED'
        scheduled_recurring = 'SCHEDULED_RECURRING'

    class PublishStatus:
        draft = 'DRAFT'
        live = 'LIVE'

    class MessagingType:
        message_tag = 'MESSAGE_TAG'
        response = 'RESPONSE'
        update = 'UPDATE'

    class NotificationType:
        no_push = 'NO_PUSH'
        regular = 'REGULAR'
        silent_push = 'SILENT_PUSH'

    class SenderAction:
        mark_seen = 'MARK_SEEN'
        react = 'REACT'
        typing_off = 'TYPING_OFF'
        typing_on = 'TYPING_ON'
        unreact = 'UNREACT'

    class Model:
        arabic = 'ARABIC'
        chinese = 'CHINESE'
        croatian = 'CROATIAN'
        custom = 'CUSTOM'
        danish = 'DANISH'
        dutch = 'DUTCH'
        english = 'ENGLISH'
        french_standard = 'FRENCH_STANDARD'
        georgian = 'GEORGIAN'
        german_standard = 'GERMAN_STANDARD'
        greek = 'GREEK'
        hebrew = 'HEBREW'
        hungarian = 'HUNGARIAN'
        irish = 'IRISH'
        italian_standard = 'ITALIAN_STANDARD'
        korean = 'KOREAN'
        norwegian_bokmal = 'NORWEGIAN_BOKMAL'
        polish = 'POLISH'
        portuguese = 'PORTUGUESE'
        romanian = 'ROMANIAN'
        spanish = 'SPANISH'
        swedish = 'SWEDISH'
        vietnamese = 'VIETNAMESE'

    class SubscribedFields:
        affiliation = 'affiliation'
        attire = 'attire'
        awards = 'awards'
        bio = 'bio'
        birthday = 'birthday'
        branded_camera = 'branded_camera'
        category = 'category'
        checkins = 'checkins'
        company_overview = 'company_overview'
        conversations = 'conversations'
        culinary_team = 'culinary_team'
        current_location = 'current_location'
        description = 'description'
        email = 'email'
        feature_access_list = 'feature_access_list'
        feed = 'feed'
        founded = 'founded'
        general_info = 'general_info'
        general_manager = 'general_manager'
        hometown = 'hometown'
        hours = 'hours'
        inbox_labels = 'inbox_labels'
        invoice_access_invoice_change = 'invoice_access_invoice_change'
        invoice_access_onboarding_status_active = 'invoice_access_onboarding_status_active'
        leadgen = 'leadgen'
        leadgen_fat = 'leadgen_fat'
        live_videos = 'live_videos'
        local_delivery = 'local_delivery'
        location = 'location'
        mcom_invoice_change = 'mcom_invoice_change'
        members = 'members'
        mention = 'mention'
        merchant_review = 'merchant_review'
        message_deliveries = 'message_deliveries'
        message_echoes = 'message_echoes'
        message_mention = 'message_mention'
        message_reactions = 'message_reactions'
        message_reads = 'message_reads'
        messages = 'messages'
        messaging_account_linking = 'messaging_account_linking'
        messaging_appointments = 'messaging_appointments'
        messaging_checkout_updates = 'messaging_checkout_updates'
        messaging_direct_sends = 'messaging_direct_sends'
        messaging_fblogin_account_linking = 'messaging_fblogin_account_linking'
        messaging_feedback = 'messaging_feedback'
        messaging_game_plays = 'messaging_game_plays'
        messaging_handovers = 'messaging_handovers'
        messaging_optins = 'messaging_optins'
        messaging_optouts = 'messaging_optouts'
        messaging_page_feedback = 'messaging_page_feedback'
        messaging_payments = 'messaging_payments'
        messaging_policy_enforcement = 'messaging_policy_enforcement'
        messaging_postbacks = 'messaging_postbacks'
        messaging_pre_checkouts = 'messaging_pre_checkouts'
        messaging_referrals = 'messaging_referrals'
        mission = 'mission'
        name = 'name'
        page_about_story = 'page_about_story'
        page_change_proposal = 'page_change_proposal'
        page_upcoming_change = 'page_upcoming_change'
        parking = 'parking'
        payment_options = 'payment_options'
        personal_info = 'personal_info'
        personal_interests = 'personal_interests'
        phone = 'phone'
        picture = 'picture'
        price_range = 'price_range'
        product_review = 'product_review'
        products = 'products'
        public_transit = 'public_transit'
        publisher_subscriptions = 'publisher_subscriptions'
        ratings = 'ratings'
        registration = 'registration'
        standby = 'standby'
        user_action = 'user_action'
        video_text_question_responses = 'video_text_question_responses'
        videos = 'videos'
        website = 'website'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'accounts'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'account_linking_token': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
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
            'about': 'string',
            'accept_crossposting_handshake': 'list<map>',
            'allow_spherical_photo': 'bool',
            'attire': 'attire_enum',
            'begin_crossposting_handshake': 'list<map>',
            'bio': 'string',
            'category_list': 'list<string>',
            'company_overview': 'string',
            'contact_address': 'Object',
            'cover': 'string',
            'culinary_team': 'string',
            'delivery_and_pickup_option_info': 'list<string>',
            'description': 'string',
            'differently_open_offerings': 'map',
            'directed_by': 'string',
            'displayed_message_response_time': 'string',
            'emails': 'list<string>',
            'focus_x': 'float',
            'focus_y': 'float',
            'food_styles': 'list<food_styles_enum>',
            'general_info': 'string',
            'general_manager': 'string',
            'genre': 'string',
            'hours': 'map',
            'ignore_coordinate_warnings': 'bool',
            'impressum': 'string',
            'instant_articles_submit_for_review': 'bool',
            'is_always_open': 'bool',
            'is_permanently_closed': 'bool',
            'is_published': 'bool',
            'is_webhooks_subscribed': 'bool',
            'location': 'Object',
            'menu': 'string',
            'mission': 'string',
            'no_feed_story': 'bool',
            'no_notification': 'bool',
            'offset_x': 'int',
            'offset_y': 'int',
            'parking': 'map',
            'payment_options': 'map',
            'phone': 'string',
            'pickup_options': 'list<pickup_options_enum>',
            'plot_outline': 'string',
            'price_range': 'string',
            'public_transit': 'string',
            'restaurant_services': 'map',
            'restaurant_specialties': 'map',
            'scrape': 'bool',
            'service_details': 'string',
            'spherical_metadata': 'map',
            'start_info': 'Object',
            'store_location_descriptor': 'string',
            'temporary_status': 'temporary_status_enum',
            'website': 'string',
            'zoom_scale_x': 'float',
            'zoom_scale_y': 'float',
        }
        enums = {
            'attire_enum': Page.Attire.__dict__.values(),
            'food_styles_enum': Page.FoodStyles.__dict__.values(),
            'pickup_options_enum': Page.PickupOptions.__dict__.values(),
            'temporary_status_enum': Page.TemporaryStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
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

    def create_acknowledge_order(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'idempotency_key': 'string',
            'orders': 'list<map>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/acknowledge_orders',
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

    def get_ads_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'exclude_dynamic_ads': 'bool',
            'include_inline_create': 'bool',
            'since': 'datetime',
            'until': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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

    def delete_agencies(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/agencies',
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

    def get_agencies(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Business,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Business, api=self._api),
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

    def create_agency(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'business': 'string',
            'permitted_tasks': 'list<permitted_tasks_enum>',
        }
        enums = {
            'permitted_tasks_enum': Page.PermittedTasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/agencies',
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

    def get_albums(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_assigned_users(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/assigned_users',
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

    def get_assigned_users(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.assigneduser import AssignedUser
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AssignedUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AssignedUser, api=self._api),
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

    def create_assigned_user(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'tasks': 'list<tasks_enum>',
            'user': 'int',
        }
        enums = {
            'tasks_enum': Page.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/assigned_users',
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

    def delete_blocked(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'asid': 'string',
            'psid': 'int',
            'uid': 'int',
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/blocked',
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

    def get_blocked(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.profile import Profile
        param_types = {
            'uid': 'int',
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/blocked',
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

    def create_blocked(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'asid': 'list',
            'psid': 'list<int>',
            'uid': 'list',
            'user': 'list',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/blocked',
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

    def create_business_datum(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'data': 'list<string>',
            'partner_agent': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/business_data',
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

    def get_call_to_actions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagecalltoaction import PageCallToAction
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/call_to_actions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageCallToAction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageCallToAction, api=self._api),
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

    def get_canvas_elements(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.canvasbodyelement import CanvasBodyElement
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/canvas_elements',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CanvasBodyElement,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CanvasBodyElement, api=self._api),
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

    def create_canvas_element(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.canvasbodyelement import CanvasBodyElement
        param_types = {
            'canvas_button': 'Object',
            'canvas_carousel': 'Object',
            'canvas_footer': 'Object',
            'canvas_header': 'Object',
            'canvas_lead_form': 'Object',
            'canvas_photo': 'Object',
            'canvas_product_list': 'Object',
            'canvas_product_set': 'Object',
            'canvas_store_locator': 'Object',
            'canvas_text': 'Object',
            'canvas_video': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/canvas_elements',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CanvasBodyElement,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CanvasBodyElement, api=self._api),
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

    def get_canvases(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.canvas import Canvas
        param_types = {
            'is_hidden': 'bool',
            'is_published': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/canvases',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Canvas,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Canvas, api=self._api),
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

    def create_canvase(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.canvas import Canvas
        param_types = {
            'background_color': 'string',
            'body_element_ids': 'list<string>',
            'enable_swipe_to_open': 'bool',
            'is_hidden': 'bool',
            'is_published': 'bool',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/canvases',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Canvas,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Canvas, api=self._api),
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

    def get_claimed_urls(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.url import URL
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/claimed_urls',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=URL,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=URL, api=self._api),
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

    def get_commerce_eligibility(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagecommerceeligibility import PageCommerceEligibility
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_eligibility',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageCommerceEligibility,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageCommerceEligibility, api=self._api),
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

    def get_commerce_merchant_settings(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commercemerchantsettings import CommerceMerchantSettings
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_merchant_settings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceMerchantSettings,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceMerchantSettings, api=self._api),
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

    def get_commerce_orders(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commerceorder import CommerceOrder
        param_types = {
            'filters': 'list<filters_enum>',
            'state': 'list<state_enum>',
            'updated_after': 'datetime',
            'updated_before': 'datetime',
        }
        enums = {
            'filters_enum': CommerceOrder.Filters.__dict__.values(),
            'state_enum': CommerceOrder.State.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_orders',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceOrder,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceOrder, api=self._api),
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

    def get_commerce_payouts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commercepayout import CommercePayout
        param_types = {
            'end_time': 'datetime',
            'start_time': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_payouts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommercePayout,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommercePayout, api=self._api),
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

    def get_commerce_transactions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commerceordertransactiondetail import CommerceOrderTransactionDetail
        param_types = {
            'end_time': 'datetime',
            'payout_reference_id': 'string',
            'start_time': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_transactions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceOrderTransactionDetail,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceOrderTransactionDetail, api=self._api),
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

    def get_conversations(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'folder': 'string',
            'tags': 'list<string>',
            'user_id': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_copyright_manual_claim(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'action': 'action_enum',
            'action_reason': 'action_reason_enum',
            'countries': 'Object',
            'match_content_type': 'match_content_type_enum',
            'matched_asset_id': 'string',
            'reference_asset_id': 'string',
        }
        enums = {
            'action_enum': [
                'BLOCK',
                'CLAIM_AD_EARNINGS',
                'MANUAL_REVIEW',
                'MONITOR',
                'REQUEST_TAKEDOWN',
            ],
            'action_reason_enum': [
                'ARTIST_OBJECTION',
                'OBJECTIONABLE_CONTENT',
                'PREMIUM_MUSIC_VIDEO',
                'PRERELEASE_CONTENT',
                'PRODUCT_PARAMETERS',
                'RESTRICTED_CONTENT',
                'UNAUTHORIZED_COMMERCIAL_USE',
            ],
            'match_content_type_enum': [
                'AUDIO_ONLY',
                'VIDEO_AND_AUDIO',
                'VIDEO_ONLY',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/copyright_manual_claims',
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

    def get_copyright_whitelisted_partners(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/copyright_whitelisted_partners',
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

    def get_crosspost_whitelisted_pages(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/crosspost_whitelisted_pages',
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

    def get_custom_labels(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/custom_labels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageUserMessageThreadLabel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageUserMessageThreadLabel, api=self._api),
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

    def create_custom_label(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
        param_types = {
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/custom_labels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageUserMessageThreadLabel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageUserMessageThreadLabel, api=self._api),
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

    def delete_custom_user_settings(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'params': 'list<params_enum>',
            'psid': 'string',
        }
        enums = {
            'params_enum': [
                'PERSISTENT_MENU',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/custom_user_settings',
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

    def get_custom_user_settings(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.customusersettings import CustomUserSettings
        param_types = {
            'psid': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/custom_user_settings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomUserSettings,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomUserSettings, api=self._api),
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

    def create_custom_user_setting(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'persistent_menu': 'list<Object>',
            'psid': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/custom_user_settings',
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

    def get_events(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.event import Event
        param_types = {
            'event_state_filter': 'list<event_state_filter_enum>',
            'include_canceled': 'bool',
            'time_filter': 'time_filter_enum',
            'type': 'type_enum',
        }
        enums = {
            'event_state_filter_enum': Event.EventStateFilter.__dict__.values(),
            'time_filter_enum': Event.TimeFilter.__dict__.values(),
            'type_enum': Event.Type.__dict__.values(),
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_extend_thread_control(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'duration': 'unsigned int',
            'recipient': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/extend_thread_control',
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

    def get_feed(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'include_hidden': 'bool',
            'limit': 'unsigned int',
            'show_expired': 'bool',
            'with': 'with_enum',
        }
        enums = {
            'with_enum': PagePost.With.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/feed',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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
            'enforce_link_ownership': 'bool',
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
            'backdated_time_granularity_enum': Page.BackdatedTimeGranularity.__dict__.values(),
            'checkin_entry_point_enum': Page.CheckinEntryPoint.__dict__.values(),
            'formatting_enum': Page.Formatting.__dict__.values(),
            'place_attachment_setting_enum': Page.PlaceAttachmentSetting.__dict__.values(),
            'post_surfaces_blacklist_enum': Page.PostSurfacesBlacklist.__dict__.values(),
            'posting_to_redspace_enum': Page.PostingToRedspace.__dict__.values(),
            'target_surface_enum': Page.TargetSurface.__dict__.values(),
            'unpublished_content_type_enum': Page.UnpublishedContentType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/feed',
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

    def get_global_brand_children(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/global_brand_children',
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

    def get_image_copyrights(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.imagecopyright import ImageCopyright
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/image_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ImageCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ImageCopyright, api=self._api),
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

    def create_image_copyright(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.imagecopyright import ImageCopyright
        param_types = {
            'artist': 'string',
            'creator': 'string',
            'custom_id': 'string',
            'description': 'string',
            'filename': 'string',
            'geo_ownership': 'list<geo_ownership_enum>',
            'original_content_creation_date': 'unsigned int',
            'reference_photo': 'string',
            'title': 'string',
        }
        enums = {
            'geo_ownership_enum': ImageCopyright.GeoOwnership.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/image_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ImageCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ImageCopyright, api=self._api),
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

    def get_indexed_videos(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/indexed_videos',
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

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.insightsresult import InsightsResult
        if is_async:
          return self.get_insights_async(fields, params, batch, success, failure, pending)
        param_types = {
            'date_preset': 'date_preset_enum',
            'metric': 'list<Object>',
            'period': 'period_enum',
            'show_description_from_api_doc': 'bool',
            'since': 'datetime',
            'until': 'datetime',
        }
        enums = {
            'date_preset_enum': InsightsResult.DatePreset.__dict__.values(),
            'period_enum': InsightsResult.Period.__dict__.values(),
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_instagram_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.instagramuser import InstagramUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/instagram_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstagramUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstagramUser, api=self._api),
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

    def get_instant_articles(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.instantarticle import InstantArticle
        param_types = {
            'development_mode': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/instant_articles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstantArticle,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstantArticle, api=self._api),
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

    def create_instant_article(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.instantarticle import InstantArticle
        param_types = {
            'development_mode': 'bool',
            'html_source': 'string',
            'published': 'bool',
            'take_live': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/instant_articles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstantArticle,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstantArticle, api=self._api),
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

    def get_instant_articles_insights(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.instantarticleinsightsqueryresult import InstantArticleInsightsQueryResult
        param_types = {
            'breakdown': 'breakdown_enum',
            'metric': 'list<Object>',
            'period': 'period_enum',
            'since': 'datetime',
            'until': 'datetime',
        }
        enums = {
            'breakdown_enum': InstantArticleInsightsQueryResult.Breakdown.__dict__.values(),
            'period_enum': InstantArticleInsightsQueryResult.Period.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/instant_articles_insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstantArticleInsightsQueryResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstantArticleInsightsQueryResult, api=self._api),
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

    def create_instant_articles_publish(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'canonical_url': 'string',
            'publish_status': 'publish_status_enum',
        }
        enums = {
            'publish_status_enum': Page.PublishStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/instant_articles_publish',
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

    def get_lead_gen_forms(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.leadgenform import LeadgenForm
        param_types = {
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_lead_gen_form(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.leadgenform import LeadgenForm
        param_types = {
            'allow_organic_lead_retrieval': 'bool',
            'block_display_for_non_targeted_viewer': 'bool',
            'context_card': 'Object',
            'cover_photo': 'file',
            'custom_disclaimer': 'Object',
            'follow_up_action_url': 'string',
            'is_for_canvas': 'bool',
            'is_optimized_for_quality': 'bool',
            'locale': 'locale_enum',
            'name': 'string',
            'privacy_policy': 'Object',
            'question_page_custom_headline': 'string',
            'questions': 'list<Object>',
            'thank_you_page': 'Object',
            'tracking_parameters': 'map',
        }
        enums = {
            'locale_enum': LeadgenForm.Locale.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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
        param_types = {
            'target_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/likes',
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

    def get_live_encoders(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.liveencoder import LiveEncoder
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/live_encoders',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveEncoder,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LiveEncoder, api=self._api),
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

    def create_live_encoder(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.liveencoder import LiveEncoder
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
            target_class=LiveEncoder,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LiveEncoder, api=self._api),
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

    def get_live_videos(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            'crossposting_actions': 'list<map>',
            'custom_labels': 'list<string>',
            'description': 'string',
            'enable_backup_ingest': 'bool',
            'encoding_settings': 'string',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'game_show': 'map',
            'is_audio_only': 'bool',
            'is_spherical': 'bool',
            'live_encoders': 'list<string>',
            'original_fov': 'unsigned int',
            'planned_start_time': 'int',
            'privacy': 'string',
            'projection': 'projection_enum',
            'published': 'bool',
            'schedule_custom_profile_image': 'file',
            'spatial_audio_format': 'spatial_audio_format_enum',
            'status': 'status_enum',
            'stereoscopic_mode': 'stereoscopic_mode_enum',
            'stop_on_delete_stream': 'bool',
            'stream_type': 'stream_type_enum',
            'targeting': 'Object',
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

    def delete_locations(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'location_page_id': 'string',
            'store_number': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/locations',
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

    def get_locations(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/locations',
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

    def create_location(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'always_open': 'bool',
            'delivery_and_pickup_option_info': 'list<string>',
            'differently_open_offerings': 'map',
            'hours': 'map',
            'ignore_warnings': 'bool',
            'location': 'Object',
            'location_page_id': 'string',
            'old_store_number': 'unsigned int',
            'page_username': 'string',
            'permanently_closed': 'bool',
            'phone': 'string',
            'pickup_options': 'list<pickup_options_enum>',
            'place_topics': 'list<string>',
            'price_range': 'string',
            'store_code': 'string',
            'store_location_descriptor': 'string',
            'store_name': 'string',
            'store_number': 'unsigned int',
            'temporary_status': 'temporary_status_enum',
            'website': 'string',
        }
        enums = {
            'pickup_options_enum': Page.PickupOptions.__dict__.values(),
            'temporary_status_enum': Page.TemporaryStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/locations',
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

    def get_media_fingerprints(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.mediafingerprint import MediaFingerprint
        param_types = {
            'universal_content_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/media_fingerprints',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MediaFingerprint,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MediaFingerprint, api=self._api),
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

    def create_media_fingerprint(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.mediafingerprint import MediaFingerprint
        param_types = {
            'fingerprint_content_type': 'fingerprint_content_type_enum',
            'metadata': 'list',
            'source': 'string',
            'title': 'string',
            'universal_content_id': 'string',
        }
        enums = {
            'fingerprint_content_type_enum': MediaFingerprint.FingerprintContentType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/media_fingerprints',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MediaFingerprint,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MediaFingerprint, api=self._api),
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

    def create_message_attachment(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'message': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/message_attachments',
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

    def create_message(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'message': 'Object',
            'messaging_type': 'messaging_type_enum',
            'notification_type': 'notification_type_enum',
            'persona_id': 'string',
            'recipient': 'Object',
            'sender_action': 'sender_action_enum',
            'tag': 'Object',
        }
        enums = {
            'messaging_type_enum': Page.MessagingType.__dict__.values(),
            'notification_type_enum': Page.NotificationType.__dict__.values(),
            'sender_action_enum': Page.SenderAction.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/messages',
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

    def get_messaging_feature_review(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.messagingfeaturereview import MessagingFeatureReview
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/messaging_feature_review',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MessagingFeatureReview,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MessagingFeatureReview, api=self._api),
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

    def delete_messenger_profile(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'fields': 'list<fields_enum>',
        }
        enums = {
            'fields_enum': [
                'ACCOUNT_LINKING_URL',
                'GET_STARTED',
                'GREETING',
                'HOME_URL',
                'ICE_BREAKERS',
                'PAYMENT_SETTINGS',
                'PERSISTENT_MENU',
                'PLATFORM',
                'SUBJECT_TO_NEW_EU_PRIVACY_RULES',
                'TARGET_AUDIENCE',
                'WHITELISTED_DOMAINS',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/messenger_profile',
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

    def get_messenger_profile(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.messengerprofile import MessengerProfile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/messenger_profile',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MessengerProfile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MessengerProfile, api=self._api),
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

    def create_messenger_profile(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'account_linking_url': 'string',
            'get_started': 'Object',
            'greeting': 'list<Object>',
            'ice_breakers': 'list<map>',
            'payment_settings': 'Object',
            'persistent_menu': 'list<Object>',
            'target_audience': 'Object',
            'whitelisted_domains': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/messenger_profile',
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

    def get_native_offers(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.nativeoffer import NativeOffer
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/nativeoffers',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=NativeOffer,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=NativeOffer, api=self._api),
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

    def create_native_offer(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.nativeoffer import NativeOffer
        param_types = {
            'barcode_photo': 'unsigned int',
            'barcode_type': 'barcode_type_enum',
            'barcode_value': 'string',
            'block_reshares': 'bool',
            'commerce_product_item': 'string',
            'commerce_store': 'string',
            'commerce_store_collection': 'string',
            'details': 'string',
            'disable_location': 'bool',
            'discounts': 'list<Object>',
            'expiration_time': 'datetime',
            'instore_code': 'string',
            'location_type': 'location_type_enum',
            'max_save_count': 'unsigned int',
            'online_code': 'string',
            'page_set_id': 'string',
            'redemption_code': 'string',
            'redemption_link': 'string',
            'terms': 'string',
            'unique_barcodes': 'unsigned int',
            'unique_codes': 'unsigned int',
        }
        enums = {
            'barcode_type_enum': NativeOffer.BarcodeType.__dict__.values(),
            'location_type_enum': NativeOffer.LocationType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/nativeoffers',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=NativeOffer,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=NativeOffer, api=self._api),
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

    def create_nlp_config(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'api_version': 'Object',
            'custom_token': 'string',
            'model': 'model_enum',
            'n_best': 'unsigned int',
            'nlp_enabled': 'bool',
            'other_language_support': 'map',
            'verbose': 'bool',
        }
        enums = {
            'model_enum': Page.Model.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/nlp_configs',
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

    def get_page_backed_instagram_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.instagramuser import InstagramUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/page_backed_instagram_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstagramUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstagramUser, api=self._api),
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

    def create_page_backed_instagram_account(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.instagramuser import InstagramUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/page_backed_instagram_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstagramUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstagramUser, api=self._api),
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

    def create_page_whatsapp_number_verification(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'verification_code': 'string',
            'whatsapp_number': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/page_whatsapp_number_verification',
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

    def create_pass_thread_control(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'metadata': 'string',
            'recipient': 'Object',
            'target_app_id': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/pass_thread_control',
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

    def create_pass_thread_metadatum(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'metadata': 'string',
            'recipient': 'Object',
            'target_app_id': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/pass_thread_metadata',
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

    def get_personas(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.persona import Persona
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/personas',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Persona,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Persona, api=self._api),
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

    def create_persona(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.persona import Persona
        param_types = {
            'name': 'string',
            'profile_picture_url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/personas',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Persona,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Persona, api=self._api),
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

    def get_photos(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.photo import Photo
        param_types = {
            'biz_tag_id': 'unsigned int',
            'business_id': 'string',
            'type': 'type_enum',
        }
        enums = {
            'type_enum': Photo.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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
            'is_visual_search': 'bool',
            'location_source_id': 'string',
            'manual_privacy': 'bool',
            'message': 'string',
            'name': 'string',
            'nectar_module': 'string',
            'no_story': 'bool',
            'offline_id': 'unsigned int',
            'og_action_type_id': 'string',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'parent_media_id': 'unsigned int',
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
            'temporary': 'bool',
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
            'breaking_change': 'breaking_change_enum',
            'height': 'int',
            'redirect': 'bool',
            'type': 'type_enum',
            'width': 'int',
        }
        enums = {
            'breaking_change_enum': ProfilePictureSource.BreakingChange.__dict__.values(),
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

    def create_picture(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.profilepicturesource import ProfilePictureSource
        param_types = {
            'android_key_hash': 'string',
            'burn_media_effect': 'bool',
            'caption': 'string',
            'composer_session_id': 'string',
            'has_umg': 'bool',
            'height': 'unsigned int',
            'ios_bundle_id': 'string',
            'media_effect_ids': 'list<int>',
            'media_effect_source_object_id': 'int',
            'msqrd_mask_id': 'string',
            'photo': 'string',
            'picture': 'string',
            'profile_pic_method': 'string',
            'profile_pic_source': 'string',
            'proxied_app_id': 'int',
            'qn': 'string',
            'reuse': 'bool',
            'scaled_crop_rect': 'Object',
            'set_profile_photo_shield': 'string',
            'sticker_id': 'int',
            'sticker_source_object_id': 'int',
            'suppress_stories': 'bool',
            'width': 'unsigned int',
            'x': 'unsigned int',
            'y': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def get_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'include_hidden': 'bool',
            'limit': 'unsigned int',
            'q': 'string',
            'show_expired': 'bool',
            'with': 'with_enum',
        }
        enums = {
            'with_enum': PagePost.With.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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

    def get_product_catalogs(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_catalogs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_published_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'since': 'datetime',
            'until': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/published_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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

    def get_ratings(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.recommendation import Recommendation
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ratings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Recommendation,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Recommendation, api=self._api),
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

    def create_release_thread_control(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'recipient': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/release_thread_control',
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

    def create_request_thread_control(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'metadata': 'string',
            'recipient': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/request_thread_control',
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

    def get_roles(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.user import User
        param_types = {
            'include_deactivated': 'bool',
            'uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/roles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=User,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=User, api=self._api),
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

    def get_rtb_dynamic_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.rtbdynamicpost import RTBDynamicPost
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/rtb_dynamic_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=RTBDynamicPost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=RTBDynamicPost, api=self._api),
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

    def get_scheduled_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/scheduled_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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

    def get_secondary_receivers(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.application import Application
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/secondary_receivers',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Application,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Application, api=self._api),
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

    def get_settings(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagesettings import PageSettings
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/settings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageSettings,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageSettings, api=self._api),
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

    def create_setting(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'option': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/settings',
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

    def get_shop_setup_status(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commercemerchantsettingssetupstatus import CommerceMerchantSettingsSetupStatus
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shop_setup_status',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceMerchantSettingsSetupStatus,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceMerchantSettingsSetupStatus, api=self._api),
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

    def delete_subscribed_apps(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/subscribed_apps',
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

    def get_subscribed_apps(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.application import Application
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/subscribed_apps',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Application,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Application, api=self._api),
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

    def create_subscribed_app(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'subscribed_fields': 'list<subscribed_fields_enum>',
        }
        enums = {
            'subscribed_fields_enum': Page.SubscribedFields.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/subscribed_apps',
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

    def get_tabs(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.tab import Tab
        param_types = {
            'tab': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tabs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Tab,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Tab, api=self._api),
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

    def create_tab(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'app_id': 'int',
            'custom_image_url': 'string',
            'custom_name': 'string',
            'is_non_connection_landing_tab': 'bool',
            'position': 'int',
            'tab': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/tabs',
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

    def get_tagged(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tagged',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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

    def create_take_thread_control(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'metadata': 'string',
            'recipient': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/take_thread_control',
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

    def get_thread_owner(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagethreadowner import PageThreadOwner
        param_types = {
            'recipient': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/thread_owner',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageThreadOwner,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageThreadOwner, api=self._api),
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

    def get_threads(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'folder': 'string',
            'tags': 'list<string>',
            'user_id': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_tours(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/tours',
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

    def create_unlink_account(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'psid': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/unlink_accounts',
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

    def get_video_copyright_rules(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.videocopyrightrule import VideoCopyrightRule
        param_types = {
            'selected_rule_id': 'string',
            'source': 'source_enum',
        }
        enums = {
            'source_enum': VideoCopyrightRule.Source.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_copyright_rules',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoCopyrightRule,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoCopyrightRule, api=self._api),
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

    def create_video_copyright_rule(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.videocopyrightrule import VideoCopyrightRule
        param_types = {
            'condition_groups': 'list<Object>',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/video_copyright_rules',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoCopyrightRule,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoCopyrightRule, api=self._api),
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

    def create_video_copyright(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.videocopyright import VideoCopyright
        param_types = {
            'attribution_id': 'string',
            'content_category': 'content_category_enum',
            'copyright_content_id': 'string',
            'excluded_ownership_countries': 'list<string>',
            'excluded_ownership_segments': 'list<Object>',
            'is_reference_disabled': 'bool',
            'is_reference_video': 'bool',
            'monitoring_type': 'monitoring_type_enum',
            'ownership_countries': 'list<string>',
            'rule_id': 'string',
            'tags': 'list<string>',
            'whitelisted_ids': 'list<string>',
            'whitelisted_ig_user_ids': 'list<string>',
        }
        enums = {
            'content_category_enum': VideoCopyright.ContentCategory.__dict__.values(),
            'monitoring_type_enum': VideoCopyright.MonitoringType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/video_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoCopyright, api=self._api),
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

    def get_video_lists(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.videolist import VideoList
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_lists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoList, api=self._api),
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

    def get_videos(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_video(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'ad_breaks': 'list',
            'adaptive_type': 'string',
            'animated_effect_id': 'unsigned int',
            'application_id': 'string',
            'asked_fun_fact_prompt_id': 'unsigned int',
            'audio_story_wave_animation_handle': 'string',
            'backdated_post': 'list',
            'call_to_action': 'Object',
            'composer_entry_picker': 'string',
            'composer_entry_point': 'string',
            'composer_entry_time': 'unsigned int',
            'composer_session_events_log': 'string',
            'composer_session_id': 'string',
            'composer_source_surface': 'string',
            'composer_type': 'string',
            'container_type': 'container_type_enum',
            'content_category': 'content_category_enum',
            'content_tags': 'list<string>',
            'creative_tools': 'string',
            'crossposted_video_id': 'string',
            'custom_labels': 'list<string>',
            'description': 'string',
            'direct_share_status': 'unsigned int',
            'embeddable': 'bool',
            'end_offset': 'unsigned int',
            'expiration': 'Object',
            'fbuploader_video_file_chunk': 'string',
            'feed_targeting': 'Object',
            'file_size': 'unsigned int',
            'file_url': 'string',
            'fisheye_video_cropped': 'bool',
            'formatting': 'formatting_enum',
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
            'is_explicit_share': 'bool',
            'is_group_linking_post': 'bool',
            'is_voice_clip': 'bool',
            'location_source_id': 'string',
            'manual_privacy': 'bool',
            'multilingual_data': 'list<Object>',
            'no_story': 'bool',
            'offer_like_post_id': 'unsigned int',
            'og_action_type_id': 'string',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_suggestion_mechanism': 'string',
            'original_fov': 'unsigned int',
            'original_projection_type': 'original_projection_type_enum',
            'publish_event_id': 'unsigned int',
            'published': 'bool',
            'react_mode_metadata': 'string',
            'reference_only': 'bool',
            'referenced_sticker_id': 'string',
            'replace_video_id': 'string',
            'sales_promo_id': 'unsigned int',
            'scheduled_publish_time': 'unsigned int',
            'secret': 'bool',
            'slideshow_spec': 'map',
            'social_actions': 'bool',
            'source': 'string',
            'source_instagram_media_id': 'string',
            'specified_dialect': 'string',
            'spherical': 'bool',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'start_offset': 'unsigned int',
            'swap_mode': 'swap_mode_enum',
            'targeting': 'Object',
            'text_format_metadata': 'string',
            'throwback_camera_roll_media': 'string',
            'thumb': 'file',
            'time_since_original_post': 'unsigned int',
            'title': 'string',
            'transcode_setting_properties': 'string',
            'universal_video_id': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'upload_phase': 'upload_phase_enum',
            'upload_session_id': 'string',
            'upload_setting_properties': 'string',
            'video_asset_id': 'string',
            'video_file_chunk': 'string',
            'video_id_original': 'string',
            'video_start_time_ms': 'unsigned int',
            'waterfall_id': 'string',
        }
        enums = {
            'container_type_enum': AdVideo.ContainerType.__dict__.values(),
            'content_category_enum': AdVideo.ContentCategory.__dict__.values(),
            'formatting_enum': AdVideo.Formatting.__dict__.values(),
            'original_projection_type_enum': AdVideo.OriginalProjectionType.__dict__.values(),
            'swap_mode_enum': AdVideo.SwapMode.__dict__.values(),
            'unpublished_content_type_enum': AdVideo.UnpublishedContentType.__dict__.values(),
            'upload_phase_enum': AdVideo.UploadPhase.__dict__.values(),
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_visitor_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'include_hidden': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/visitor_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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
        'about': 'string',
        'access_token': 'string',
        'ad_campaign': 'AdSet',
        'affiliation': 'string',
        'app_id': 'string',
        'artists_we_like': 'string',
        'attire': 'string',
        'awards': 'string',
        'band_interests': 'string',
        'band_members': 'string',
        'best_page': 'Page',
        'bio': 'string',
        'birthday': 'string',
        'booking_agent': 'string',
        'built': 'string',
        'business': 'Object',
        'can_checkin': 'bool',
        'can_post': 'bool',
        'category': 'string',
        'category_list': 'list<PageCategory>',
        'checkins': 'unsigned int',
        'company_overview': 'string',
        'connected_instagram_account': 'IGUser',
        'connected_page_backed_instagram_account': 'IGUser',
        'contact_address': 'MailingAddress',
        'copyright_whitelisted_ig_partners': 'list<string>',
        'country_page_likes': 'unsigned int',
        'cover': 'CoverPhoto',
        'culinary_team': 'string',
        'current_location': 'string',
        'delivery_and_pickup_option_info': 'list<string>',
        'description': 'string',
        'description_html': 'string',
        'differently_open_offerings': 'map<string, bool>',
        'directed_by': 'string',
        'display_subtext': 'string',
        'displayed_message_response_time': 'string',
        'emails': 'list<string>',
        'engagement': 'Engagement',
        'fan_count': 'unsigned int',
        'featured_video': 'AdVideo',
        'features': 'string',
        'followers_count': 'unsigned int',
        'food_styles': 'list<string>',
        'founded': 'string',
        'general_info': 'string',
        'general_manager': 'string',
        'genre': 'string',
        'global_brand_page_name': 'string',
        'global_brand_root_id': 'string',
        'has_added_app': 'bool',
        'has_whatsapp_business_number': 'bool',
        'has_whatsapp_number': 'bool',
        'hometown': 'string',
        'hours': 'map<string, string>',
        'id': 'string',
        'impressum': 'string',
        'influences': 'string',
        'instagram_business_account': 'IGUser',
        'instant_articles_review_status': 'string',
        'is_always_open': 'bool',
        'is_chain': 'bool',
        'is_community_page': 'bool',
        'is_eligible_for_branded_content': 'bool',
        'is_messenger_bot_get_started_enabled': 'bool',
        'is_messenger_platform_bot': 'bool',
        'is_owned': 'bool',
        'is_permanently_closed': 'bool',
        'is_published': 'bool',
        'is_unclaimed': 'bool',
        'is_verified': 'bool',
        'is_webhooks_subscribed': 'bool',
        'keywords': 'Object',
        'leadgen_tos_acceptance_time': 'datetime',
        'leadgen_tos_accepted': 'bool',
        'leadgen_tos_accepting_user': 'User',
        'link': 'string',
        'location': 'Location',
        'members': 'string',
        'merchant_id': 'string',
        'merchant_review_status': 'string',
        'messenger_ads_default_icebreakers': 'list<string>',
        'messenger_ads_default_page_welcome_message': 'MessengerDestinationPageWelcomeMessage',
        'messenger_ads_default_quick_replies': 'list<string>',
        'messenger_ads_quick_replies_type': 'string',
        'mission': 'string',
        'mpg': 'string',
        'name': 'string',
        'name_with_location_descriptor': 'string',
        'network': 'string',
        'new_like_count': 'unsigned int',
        'offer_eligible': 'bool',
        'overall_star_rating': 'float',
        'page_token': 'string',
        'parent_page': 'Page',
        'parking': 'PageParking',
        'payment_options': 'PagePaymentOptions',
        'personal_info': 'string',
        'personal_interests': 'string',
        'pharma_safety_info': 'string',
        'phone': 'string',
        'pickup_options': 'list<string>',
        'place_type': 'string',
        'plot_outline': 'string',
        'preferred_audience': 'Targeting',
        'press_contact': 'string',
        'price_range': 'string',
        'privacy_info_url': 'string',
        'produced_by': 'string',
        'products': 'string',
        'promotion_eligible': 'bool',
        'promotion_ineligible_reason': 'string',
        'public_transit': 'string',
        'rating_count': 'unsigned int',
        'recipient': 'string',
        'record_label': 'string',
        'release_date': 'string',
        'restaurant_services': 'PageRestaurantServices',
        'restaurant_specialties': 'PageRestaurantSpecialties',
        'schedule': 'string',
        'screenplay_by': 'string',
        'season': 'string',
        'single_line_address': 'string',
        'starring': 'string',
        'start_info': 'PageStartInfo',
        'store_code': 'string',
        'store_location_descriptor': 'string',
        'store_number': 'unsigned int',
        'studio': 'string',
        'supports_donate_button_in_live_video': 'bool',
        'supports_instant_articles': 'bool',
        'talking_about_count': 'unsigned int',
        'temporary_status': 'string',
        'unread_message_count': 'unsigned int',
        'unread_notif_count': 'unsigned int',
        'unseen_message_count': 'unsigned int',
        'username': 'string',
        'verification_status': 'string',
        'voip_info': 'VoipInfo',
        'website': 'string',
        'were_here_count': 'unsigned int',
        'whatsapp_number': 'string',
        'written_by': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Attire'] = Page.Attire.__dict__.values()
        field_enum_info['FoodStyles'] = Page.FoodStyles.__dict__.values()
        field_enum_info['PickupOptions'] = Page.PickupOptions.__dict__.values()
        field_enum_info['TemporaryStatus'] = Page.TemporaryStatus.__dict__.values()
        field_enum_info['PermittedTasks'] = Page.PermittedTasks.__dict__.values()
        field_enum_info['Tasks'] = Page.Tasks.__dict__.values()
        field_enum_info['BackdatedTimeGranularity'] = Page.BackdatedTimeGranularity.__dict__.values()
        field_enum_info['CheckinEntryPoint'] = Page.CheckinEntryPoint.__dict__.values()
        field_enum_info['Formatting'] = Page.Formatting.__dict__.values()
        field_enum_info['PlaceAttachmentSetting'] = Page.PlaceAttachmentSetting.__dict__.values()
        field_enum_info['PostSurfacesBlacklist'] = Page.PostSurfacesBlacklist.__dict__.values()
        field_enum_info['PostingToRedspace'] = Page.PostingToRedspace.__dict__.values()
        field_enum_info['TargetSurface'] = Page.TargetSurface.__dict__.values()
        field_enum_info['UnpublishedContentType'] = Page.UnpublishedContentType.__dict__.values()
        field_enum_info['PublishStatus'] = Page.PublishStatus.__dict__.values()
        field_enum_info['MessagingType'] = Page.MessagingType.__dict__.values()
        field_enum_info['NotificationType'] = Page.NotificationType.__dict__.values()
        field_enum_info['SenderAction'] = Page.SenderAction.__dict__.values()
        field_enum_info['Model'] = Page.Model.__dict__.values()
        field_enum_info['SubscribedFields'] = Page.SubscribedFields.__dict__.values()
        return field_enum_info


