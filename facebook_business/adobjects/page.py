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
        app_links = 'app_links'
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
        contact_address = 'contact_address'
        context = 'context'
        copyright_attribution_insights = 'copyright_attribution_insights'
        copyright_whitelisted_ig_partners = 'copyright_whitelisted_ig_partners'
        country_page_likes = 'country_page_likes'
        cover = 'cover'
        culinary_team = 'culinary_team'
        current_location = 'current_location'
        description = 'description'
        description_html = 'description_html'
        directed_by = 'directed_by'
        display_subtext = 'display_subtext'
        displayed_message_response_time = 'displayed_message_response_time'
        emails = 'emails'
        engagement = 'engagement'
        fan_count = 'fan_count'
        featured_video = 'featured_video'
        features = 'features'
        food_styles = 'food_styles'
        founded = 'founded'
        general_info = 'general_info'
        general_manager = 'general_manager'
        genre = 'genre'
        global_brand_page_name = 'global_brand_page_name'
        global_brand_parent_page = 'global_brand_parent_page'
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
        leadgen_form_preview_details = 'leadgen_form_preview_details'
        leadgen_has_crm_integration = 'leadgen_has_crm_integration'
        leadgen_has_fat_ping_crm_integration = 'leadgen_has_fat_ping_crm_integration'
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
        place_type = 'place_type'
        plot_outline = 'plot_outline'
        preferred_audience = 'preferred_audience'
        press_contact = 'press_contact'
        price_range = 'price_range'
        produced_by = 'produced_by'
        products = 'products'
        promotion_eligible = 'promotion_eligible'
        promotion_ineligible_reason = 'promotion_ineligible_reason'
        public_transit = 'public_transit'
        publisher_space = 'publisher_space'
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
        supports_instant_articles = 'supports_instant_articles'
        talking_about_count = 'talking_about_count'
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
        unspecified = 'Unspecified'
        casual = 'Casual'
        dressy = 'Dressy'

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

    class Setting:
        post_as_self = 'POST_AS_SELF'
        email_notif = 'EMAIL_NOTIF'
        mobile_notif = 'MOBILE_NOTIF'

    class Audience:
        grouper = 'GROUPER'
        ncpp = 'NCPP'
        custom_audience = 'CUSTOM_AUDIENCE'
        lookalike = 'LOOKALIKE'
        fans = 'FANS'
        local = 'LOCAL'
        ig_promoted_post_auto = 'IG_PROMOTED_POST_AUTO'
        saved_audience = 'SAVED_AUDIENCE'
        event_engagement = 'EVENT_ENGAGEMENT'
        district = 'DISTRICT'
        smart_audience = 'SMART_AUDIENCE'
        create_new = 'CREATE_NEW'
        auto_lookalike = 'AUTO_LOOKALIKE'
        mult_custom_audiences = 'MULT_CUSTOM_AUDIENCES'
        event_custom_audiences = 'EVENT_CUSTOM_AUDIENCES'

    class PermittedTasks:
        manage = 'MANAGE'
        create_content = 'CREATE_CONTENT'
        moderate = 'MODERATE'
        moderate_community = 'MODERATE_COMMUNITY'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class Tasks:
        manage = 'MANAGE'
        create_content = 'CREATE_CONTENT'
        moderate = 'MODERATE'
        moderate_community = 'MODERATE_COMMUNITY'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class MessagingType:
        response = 'RESPONSE'
        update = 'UPDATE'
        message_tag = 'MESSAGE_TAG'

    class NotificationType:
        regular = 'REGULAR'
        silent_push = 'SILENT_PUSH'
        no_push = 'NO_PUSH'

    class PublishStatus:
        draft = 'DRAFT'
        live = 'LIVE'

    class SenderAction:
        mark_seen = 'MARK_SEEN'
        typing_on = 'TYPING_ON'
        typing_off = 'TYPING_OFF'

    class Type:
        standard = 'STANDARD'
        ref = 'REF'

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

    class Filtering:
        groups = 'groups'
        groups_social = 'groups_social'
        ema = 'ema'

    class SubscribedFields:
        feed = 'feed'
        mention = 'mention'
        name = 'name'
        picture = 'picture'
        category = 'category'
        description = 'description'
        conversations = 'conversations'
        branded_camera = 'branded_camera'
        feature_access_list = 'feature_access_list'
        standby = 'standby'
        messages = 'messages'
        messaging_account_linking = 'messaging_account_linking'
        messaging_checkout_updates = 'messaging_checkout_updates'
        message_echoes = 'message_echoes'
        message_deliveries = 'message_deliveries'
        messaging_game_plays = 'messaging_game_plays'
        messaging_optins = 'messaging_optins'
        messaging_optouts = 'messaging_optouts'
        messaging_payments = 'messaging_payments'
        messaging_postbacks = 'messaging_postbacks'
        messaging_pre_checkouts = 'messaging_pre_checkouts'
        message_reads = 'message_reads'
        messaging_referrals = 'messaging_referrals'
        messaging_handovers = 'messaging_handovers'
        messaging_policy_enforcement = 'messaging_policy_enforcement'
        messaging_page_feedback = 'messaging_page_feedback'
        messaging_appointments = 'messaging_appointments'
        founded = 'founded'
        company_overview = 'company_overview'
        mission = 'mission'
        products = 'products'
        general_info = 'general_info'
        leadgen = 'leadgen'
        leadgen_fat = 'leadgen_fat'
        location = 'location'
        hours = 'hours'
        parking = 'parking'
        public_transit = 'public_transit'
        phone = 'phone'
        email = 'email'
        website = 'website'
        ratings = 'ratings'
        attire = 'attire'
        payment_options = 'payment_options'
        culinary_team = 'culinary_team'
        general_manager = 'general_manager'
        price_range = 'price_range'
        awards = 'awards'
        hometown = 'hometown'
        current_location = 'current_location'
        bio = 'bio'
        affiliation = 'affiliation'
        birthday = 'birthday'
        personal_info = 'personal_info'
        personal_interests = 'personal_interests'
        publisher_subscriptions = 'publisher_subscriptions'
        members = 'members'
        checkins = 'checkins'
        page_upcoming_change = 'page_upcoming_change'
        page_change_proposal = 'page_change_proposal'
        merchant_review = 'merchant_review'
        product_review = 'product_review'
        videos = 'videos'
        live_videos = 'live_videos'
        registration = 'registration'

    class DomainActionType:
        add = 'ADD'
        remove = 'REMOVE'

    class PaymentDevModeAction:
        add = 'ADD'
        remove = 'REMOVE'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'accounts'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'allow_spherical_photo': 'bool',
            'spherical_metadata': 'map',
            'offset_y': 'int',
            'offset_x': 'int',
            'focus_y': 'float',
            'focus_x': 'float',
            'zoom_scale_x': 'float',
            'zoom_scale_y': 'float',
            'no_feed_story': 'bool',
            'no_notification': 'bool',
            'cover': 'string',
            'about': 'string',
            'bio': 'string',
            'company_overview': 'string',
            'description': 'string',
            'directed_by': 'string',
            'general_info': 'string',
            'impressum': 'string',
            'mission': 'string',
            'phone': 'string',
            'website': 'string',
            'parking': 'map',
            'hours': 'map',
            'location': 'Object',
            'price_range': 'string',
            'payment_options': 'map',
            'restaurant_services': 'map',
            'restaurant_specialties': 'map',
            'emails': 'list<string>',
            'food_styles': 'list<food_styles_enum>',
            'attire': 'attire_enum',
            'public_transit': 'string',
            'general_manager': 'string',
            'culinary_team': 'string',
            'start_info': 'Object',
            'genre': 'string',
            'plot_outline': 'string',
            'scrape': 'bool',
            'category_list': 'list<string>',
            'is_always_open': 'bool',
            'is_published': 'bool',
            'is_webhooks_subscribed': 'bool',
            'contact_address': 'Object',
            'instant_articles_submit_for_review': 'bool',
            'is_permanently_closed': 'bool',
            'ignore_coordinate_warnings': 'bool',
            'crossposting_pages': 'list<Object>',
            'begin_crossposting_handshake': 'list<map>',
            'accept_crossposting_handshake': 'list<map>',
            'displayed_message_response_time': 'string',
            'store_location_descriptor': 'string',
            'service_details': 'string',
            'menu': 'string',
        }
        enums = {
            'food_styles_enum': Page.FoodStyles.__dict__.values(),
            'attire_enum': Page.Attire.__dict__.values(),
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_activity(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'page_scoped_user_id': 'unsigned int',
            'user_ref': 'string',
            'advertiser_tracking_enabled': 'bool',
            'custom_events': 'list<Object>',
            'app_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/activities',
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

    def get_admin_notes(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pageadminnote import PageAdminNote
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/admin_notes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageAdminNote,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageAdminNote, api=self._api),
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

    def create_admin_note(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pageadminnote import PageAdminNote
        param_types = {
            'body': 'string',
            'user_id': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/admin_notes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageAdminNote,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageAdminNote, api=self._api),
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

    def create_admin_setting(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'setting': 'setting_enum',
            'value': 'bool',
        }
        enums = {
            'setting_enum': Page.Setting.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/admin_settings',
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

    def delete_admins(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'trusted': 'bool',
            'admin_id': 'int',
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
        from facebook_business.adobjects.user import User
        param_types = {
            'trusted': 'bool',
            'admin_id': 'int',
            'tasks': 'list<tasks_enum>',
        }
        enums = {
            'tasks_enum': User.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/admins',
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

    def create_admin_sticky_setting(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'budget': 'unsigned int',
            'currency': 'string',
            'ad_account_id': 'string',
            'audience': 'audience_enum',
            'targeting': 'Targeting',
            'campaign_length': 'datetime',
        }
        enums = {
            'audience_enum': Page.Audience.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adminstickysettings',
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

    def delete_agencies(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_agencies(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_agency(self, fields=None, params=None, batch=None, pending=False):
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

    def get_asset3_ds(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.withasset3d import WithAsset3D
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/asset3ds',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=WithAsset3D,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=WithAsset3D, api=self._api),
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

    def delete_assigned_users(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_assigned_users(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_assigned_user(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'tasks': 'list<tasks_enum>',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_audio_copyrights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.audiocopyright import AudioCopyright
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/audio_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AudioCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AudioCopyright, api=self._api),
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

    def get_audio_media_copyrights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.audiocopyright import AudioCopyright
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/audio_media_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AudioCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AudioCopyright, api=self._api),
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

    def delete_blocked(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
            'user': 'int',
            'asid': 'int',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_blocked(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_blocked(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'list<string>',
            'uid': 'list<string>',
            'asid': 'Object',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_broadcast_messages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagebroadcast import PageBroadcast
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/broadcast_messages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageBroadcast,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageBroadcast, api=self._api),
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

    def create_broadcast_message(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'message_creative_id': 'string',
            'notification_type': 'notification_type_enum',
            'tag': 'Object',
            'messaging_type': 'messaging_type_enum',
            'targeting': 'Object',
            'custom_label_id': 'int',
            'schedule_time': 'Object',
            'schedule_local_time': 'string',
        }
        enums = {
            'notification_type_enum': Page.NotificationType.__dict__.values(),
            'messaging_type_enum': Page.MessagingType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/broadcast_messages',
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

    def create_broadcast_reach_estimation(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'custom_label_id': 'int',
            'targeting': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/broadcast_reach_estimations',
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

    def get_business_activities(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessactivitylogevent import BusinessActivityLogEvent
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_activities',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessActivityLogEvent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessActivityLogEvent, api=self._api),
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

    def create_business(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/businesses',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Business,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Business, api=self._api),
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

    def get_business_projects(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessproject import BusinessProject
        param_types = {
            'business': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/businessprojects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessProject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessProject, api=self._api),
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

    def get_business_setting_logs(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesssettinglogsdata import BusinessSettingLogsData
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/businesssettinglogs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessSettingLogsData,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessSettingLogsData, api=self._api),
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

    def get_call_to_actions(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_call_to_action(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagecalltoaction import PageCallToAction
        param_types = {
            'type': 'type_enum',
            'web_destination_type': 'web_destination_type_enum',
            'android_destination_type': 'android_destination_type_enum',
            'iphone_destination_type': 'iphone_destination_type_enum',
            'intl_number_with_plus': 'string',
            'web_url': 'string',
            'android_app_id': 'int',
            'android_deeplink': 'string',
            'android_package_name': 'string',
            'android_url': 'string',
            'iphone_app_id': 'int',
            'iphone_deeplink': 'string',
            'iphone_url': 'string',
            'email_address': 'string',
        }
        enums = {
            'type_enum': PageCallToAction.Type.__dict__.values(),
            'web_destination_type_enum': PageCallToAction.WebDestinationType.__dict__.values(),
            'android_destination_type_enum': PageCallToAction.AndroidDestinationType.__dict__.values(),
            'iphone_destination_type_enum': PageCallToAction.IphoneDestinationType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_canvas_elements(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_canvas_element(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.canvasbodyelement import CanvasBodyElement
        param_types = {
            'canvas_photo': 'Object',
            'canvas_video': 'Object',
            'canvas_text': 'Object',
            'canvas_button': 'Object',
            'canvas_footer': 'Object',
            'canvas_carousel': 'Object',
            'canvas_header': 'Object',
            'canvas_product_list': 'Object',
            'canvas_product_set': 'Object',
            'canvas_store_locator': 'Object',
            'canvas_lead_form': 'Object',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_canvases(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.canvas import Canvas
        param_types = {
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_canvase(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.canvas import Canvas
        param_types = {
            'body_element_ids': 'list<string>',
            'background_color': 'string',
            'is_published': 'bool',
            'is_hidden': 'bool',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_claimed_urls(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/claimed_urls',
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

    def get_conversations(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'tags': 'list<string>',
            'folder': 'string',
            'psid': 'Object',
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

    def create_copyright_manual_claim(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'reference_asset_id': 'string',
            'matched_asset_id': 'string',
            'match_content_type': 'match_content_type_enum',
            'action': 'action_enum',
            'countries': 'Object',
        }
        enums = {
            'match_content_type_enum': [
                'VIDEO_AND_AUDIO',
                'VIDEO_ONLY',
                'AUDIO_ONLY',
            ],
            'action_enum': [
                'MANUAL_REVIEW',
                'MONITOR',
                'BLOCK',
                'CLAIM_AD_EARNINGS',
                'REQUEST_TAKEDOWN',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_copyright_whitelisted_ig_partners(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'usernames': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/copyright_whitelisted_ig_partners',
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

    def create_copyright_whitelisted_ig_partner(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'usernames': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/copyright_whitelisted_ig_partners',
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

    def delete_copyright_whitelisted_partners(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'partner_ids': 'list<Object>',
            'urls': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/copyright_whitelisted_partners',
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

    def get_copyright_whitelisted_partners(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_copyright_whitelisted_partner(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'partner_ids': 'list<Object>',
            'urls': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/copyright_whitelisted_partners',
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

    def get_crosspost_pending_approval_pages(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/crosspost_pending_approval_pages',
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

    def get_crosspost_whitelisted_pages(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_custom_labels(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_custom_label(self, fields=None, params=None, batch=None, pending=False):
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
            'type': 'type_enum',
            'include_canceled': 'bool',
            'time_filter': 'time_filter_enum',
            'event_state_filter': 'list<event_state_filter_enum>',
        }
        enums = {
            'type_enum': Event.Type.__dict__.values(),
            'time_filter_enum': Event.TimeFilter.__dict__.values(),
            'event_state_filter_enum': Event.EventStateFilter.__dict__.values(),
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

    def create_event(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.event import Event
        param_types = {
            'event_info': 'Object',
            'action_context': 'Object',
            'app_context': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def get_expired_posts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.expirablepost import ExpirablePost
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/expired_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExpirablePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExpirablePost, api=self._api),
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

    def get_expiring_posts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.expirablepost import ExpirablePost
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/expiring_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExpirablePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExpirablePost, api=self._api),
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

    def get_feature_d_videos_collection(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/featured_videos_collection',
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

    def get_feed(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'include_hidden': 'bool',
            'with': 'with_enum',
            'show_expired': 'bool',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_feed(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagepost import PagePost
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
            'enforce_link_ownership': 'bool',
        }
        enums = {
            'backdated_time_granularity_enum': PagePost.BackdatedTimeGranularity.__dict__.values(),
            'unpublished_content_type_enum': PagePost.UnpublishedContentType.__dict__.values(),
            'posting_to_redspace_enum': PagePost.PostingToRedspace.__dict__.values(),
            'place_attachment_setting_enum': PagePost.PlaceAttachmentSetting.__dict__.values(),
            'checkin_entry_point_enum': PagePost.CheckinEntryPoint.__dict__.values(),
            'post_surfaces_blacklist_enum': PagePost.PostSurfacesBlacklist.__dict__.values(),
            'formatting_enum': PagePost.Formatting.__dict__.values(),
            'target_surface_enum': PagePost.TargetSurface.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_flag(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'page_id': 'int',
            'page_ids': 'list<int>',
            'flag': 'string',
            'value': 'bool',
            'entry_point': 'string',
            'endpoint': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/flags',
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

    def get_global_brand_children(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_indexed_video_copyrights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videocopyright import VideoCopyright
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/indexed_video_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoCopyright, api=self._api),
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

    def get_indexed_videos(self, fields=None, params=None, batch=None, pending=False):
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
            'show_description_from_api_doc': 'bool',
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

    def get_insights_exports(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pageinsightsasyncexportrun import PageInsightsAsyncExportRun
        param_types = {
            'data_level': 'list<string>',
            'from_creation_date': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights_exports',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageInsightsAsyncExportRun,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageInsightsAsyncExportRun, api=self._api),
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

    def get_instant_articles(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_instant_article(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.instantarticle import InstantArticle
        param_types = {
            'html_source': 'string',
            'development_mode': 'bool',
            'take_live': 'bool',
            'published': 'bool',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_instant_articles_insights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.instantarticleinsightsqueryresult import InstantArticleInsightsQueryResult
        param_types = {
            'metric': 'list<Object>',
            'period': 'period_enum',
            'since': 'datetime',
            'until': 'datetime',
            'breakdown': 'breakdown_enum',
        }
        enums = {
            'period_enum': InstantArticleInsightsQueryResult.Period.__dict__.values(),
            'breakdown_enum': InstantArticleInsightsQueryResult.Breakdown.__dict__.values(),
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_instant_articles_publish(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagelabel import PageLabel
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/labels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageLabel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageLabel, api=self._api),
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

    def create_label(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagelabel import PageLabel
        param_types = {
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/labels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageLabel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageLabel, api=self._api),
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

    def get_lead_gen_conditional_questions_group(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenconditionalquestionsgroup import LeadGenConditionalQuestionsGroup
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_conditional_questions_group',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenConditionalQuestionsGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenConditionalQuestionsGroup, api=self._api),
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

    def create_lead_gen_conditional_questions_group(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenconditionalquestionsgroup import LeadGenConditionalQuestionsGroup
        param_types = {
            'conditional_questions_group_csv': 'file',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leadgen_conditional_questions_group',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenConditionalQuestionsGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenConditionalQuestionsGroup, api=self._api),
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

    def get_lead_gen_context_cards(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgencontextcard import LeadGenContextCard
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_context_cards',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenContextCard,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenContextCard, api=self._api),
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

    def create_lead_gen_context_card(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgencontextcard import LeadGenContextCard
        param_types = {
            'title': 'string',
            'style': 'style_enum',
            'content': 'list<string>',
            'button_text': 'string',
            'cover_photo': 'file',
            'cover_photo_id': 'string',
            'status': 'status_enum',
        }
        enums = {
            'style_enum': LeadGenContextCard.Style.__dict__.values(),
            'status_enum': LeadGenContextCard.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leadgen_context_cards',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenContextCard,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenContextCard, api=self._api),
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

    def get_lead_gen_draft_forms(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgendatadraft import LeadGenDataDraft
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_draft_forms',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenDataDraft,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenDataDraft, api=self._api),
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

    def create_lead_gen_draft_form(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgendatadraft import LeadGenDataDraft
        param_types = {
            'name': 'string',
            'locale': 'locale_enum',
            'block_display_for_non_targeted_viewer': 'bool',
            'follow_up_action_url': 'string',
            'legal_content_id': 'string',
            'context_card_id': 'string',
            'questions': 'list<Object>',
            'privacy_policy': 'map',
            'custom_disclaimer': 'Object',
            'context_card': 'Object',
            'thank_you_page': 'map',
            'tracking_parameters': 'Object',
            'question_page_custom_headline': 'string',
            'is_optimized_for_quality': 'bool',
        }
        enums = {
            'locale_enum': LeadGenDataDraft.Locale.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leadgen_draft_forms',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenDataDraft,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenDataDraft, api=self._api),
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

    def create_lead_gen_form(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenform import LeadgenForm
        param_types = {
            'name': 'string',
            'locale': 'locale_enum',
            'allow_organic_lead_retrieval': 'bool',
            'block_display_for_non_targeted_viewer': 'bool',
            'follow_up_action_url': 'Object',
            'legal_content_id': 'Object',
            'context_card_id': 'Object',
            'thank_you_page_id': 'Object',
            'questions': 'list<Object>',
            'privacy_policy': 'Object',
            'custom_disclaimer': 'Object',
            'context_card': 'Object',
            'thank_you_page': 'Object',
            'tracking_parameters': 'Object',
            'cover_photo': 'file',
            'question_page_custom_headline': 'string',
            'is_optimized_for_quality': 'bool',
            'is_for_canvas': 'bool',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_lead_gen_legal_content(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenlegalcontent import LeadGenLegalContent
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_legal_content',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenLegalContent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenLegalContent, api=self._api),
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

    def create_lead_gen_legal_content(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenlegalcontent import LeadGenLegalContent
        param_types = {
            'privacy_policy': 'Object',
            'custom_disclaimer': 'Object',
            'status': 'status_enum',
        }
        enums = {
            'status_enum': LeadGenLegalContent.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leadgen_legal_content',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenLegalContent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenLegalContent, api=self._api),
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

    def get_lead_gen_qualifiers(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenqualifier import LeadGenQualifier
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_qualifiers',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadGenQualifier,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadGenQualifier, api=self._api),
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

    def create_lead_gen_thank_you_page(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'body': 'string',
            'business_phone_number': 'string',
            'button_text': 'string',
            'button_type': 'button_type_enum',
            'country_code': 'string',
            'enable_messenger': 'bool',
            'title': 'string',
            'website_url': 'string',
        }
        enums = {
            'button_type_enum': [
                'VIEW_WEBSITE',
                'CALL_BUSINESS',
                'MESSAGE_BUSINESS',
                'DOWNLOAD',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leadgen_thank_you_page',
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

    def delete_lead_gen_whitelisted_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/leadgen_whitelisted_users',
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

    def get_lead_gen_whitelisted_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_whitelisted_users',
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

    def create_lead_gen_whitelisted_user(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user_id': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leadgen_whitelisted_users',
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

    def get_likes(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_link(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.link import Link
        param_types = {
            'link': 'string',
            'message': 'string',
            'image': 'string',
            'tags': 'list<int>',
            'place': 'Object',
            'published': 'bool',
            'scheduled_publish_time': 'unsigned int',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'targeting': 'Object',
            'privacy': 'Object',
            'application_id': 'string',
            'is_explicit_share': 'bool',
        }
        enums = {
            'unpublished_content_type_enum': Link.UnpublishedContentType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/links',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Link,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Link, api=self._api),
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
            'custom_labels': 'list<string>',
            'targeting': 'Object',
            'product_items': 'list<string>',
            'crossposting_actions': 'list<map>',
            'game_show': 'map',
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

    def delete_locations(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'location_page_id': 'Object',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_locations(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_location(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'store_number': 'unsigned int',
            'location': 'Object',
            'place_topics': 'list<string>',
            'phone': 'string',
            'store_name': 'string',
            'hours': 'map',
            'page_username': 'string',
            'old_store_number': 'unsigned int',
            'permanently_closed': 'bool',
            'price_range': 'string',
            'store_location_descriptor': 'string',
            'location_page_id': 'Object',
            'ignore_warnings': 'bool',
            'website': 'Object',
            'always_open': 'bool',
            'store_code': 'string',
        }
        enums = {
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_media_fingerprints(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.mediafingerprint import MediaFingerprint
        param_types = {
            'universal_content_id': 'string',
            'fingerprint_validity': 'fingerprint_validity_enum',
        }
        enums = {
            'fingerprint_validity_enum': MediaFingerprint.FingerprintValidity.__dict__.values(),
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_media_fingerprint(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.mediafingerprint import MediaFingerprint
        param_types = {
            'fingerprint_content_type': 'fingerprint_content_type_enum',
            'title': 'string',
            'metadata': 'Object',
            'universal_content_id': 'string',
            'source': 'string',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_message_attachment(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_message_creative(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'messages': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/message_creatives',
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

    def create_message(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'recipient': 'Object',
            'message': 'Object',
            'sender_action': 'sender_action_enum',
            'notification_type': 'notification_type_enum',
            'tag': 'Object',
            'messaging_type': 'messaging_type_enum',
            'persona_id': 'Object',
        }
        enums = {
            'sender_action_enum': Page.SenderAction.__dict__.values(),
            'notification_type_enum': Page.NotificationType.__dict__.values(),
            'messaging_type_enum': Page.MessagingType.__dict__.values(),
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_messaging_feature_review(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_messenger_ads_page_welcome_messages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.messengerdestinationpagewelcomemessage import MessengerDestinationPageWelcomeMessage
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/messenger_ads_page_welcome_messages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MessengerDestinationPageWelcomeMessage,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MessengerDestinationPageWelcomeMessage, api=self._api),
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

    def create_messenger_code(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'type': 'type_enum',
            'data': 'string',
            'image_size': 'unsigned int',
        }
        enums = {
            'type_enum': Page.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/messenger_codes',
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

    def delete_messenger_profile(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'fields': 'list<fields_enum>',
        }
        enums = {
            'fields_enum': [
                'GET_STARTED',
                'PERSISTENT_MENU',
                'TARGET_AUDIENCE',
                'WHITELISTED_DOMAINS',
                'GREETING',
                'ACCOUNT_LINKING_URL',
                'PAYMENT_SETTINGS',
                'HOME_URL',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_messenger_profile(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_messenger_profile(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'get_started': 'Object',
            'persistent_menu': 'list<Object>',
            'target_audience': 'Object',
            'whitelisted_domains': 'list<string>',
            'greeting': 'list<Object>',
            'account_linking_url': 'string',
            'payment_settings': 'Object',
            'home_url': 'Object',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_milestones(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.lifeevent import LifeEvent
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/milestones',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LifeEvent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LifeEvent, api=self._api),
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

    def create_milestone(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.lifeevent import LifeEvent
        param_types = {
            'title': 'string',
            'description': 'string',
            'start_time': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/milestones',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LifeEvent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LifeEvent, api=self._api),
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

    def get_music_video_copyrights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.musicvideocopyright import MusicVideoCopyright
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/music_video_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MusicVideoCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MusicVideoCopyright, api=self._api),
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

    def get_music_video_media_copyrights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.musicvideocopyright import MusicVideoCopyright
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/music_video_media_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MusicVideoCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MusicVideoCopyright, api=self._api),
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

    def get_native_offers(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_native_offer(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.nativeoffer import NativeOffer
        param_types = {
            'discounts': 'list<Object>',
            'details': 'string',
            'terms': 'string',
            'redemption_code': 'string',
            'redemption_link': 'string',
            'max_save_count': 'unsigned int',
            'online_code': 'string',
            'instore_code': 'string',
            'expiration_time': 'datetime',
            'location_type': 'location_type_enum',
            'barcode_type': 'barcode_type_enum',
            'barcode_value': 'string',
            'barcode_photo': 'unsigned int',
            'unique_codes': 'unsigned int',
            'unique_barcodes': 'unsigned int',
            'block_reshares': 'bool',
            'disable_location': 'bool',
            'commerce_store': 'string',
            'commerce_store_collection': 'string',
            'commerce_product_item': 'string',
            'page_set_id': 'string',
        }
        enums = {
            'location_type_enum': NativeOffer.LocationType.__dict__.values(),
            'barcode_type_enum': NativeOffer.BarcodeType.__dict__.values(),
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_nlp_config(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'nlp_enabled': 'bool',
            'model': 'model_enum',
            'custom_token': 'string',
            'n_best': 'unsigned int',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_note(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'message': 'string',
            'subject': 'string',
            'privacy': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/notes',
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

    def create_notification(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'seen': 'bool',
            'read': 'bool',
            'notif_ids': 'list<string>',
            'filtering': 'list<filtering_enum>',
            'template': 'Object',
            'href': 'Object',
            'ref': 'string',
            'type': 'type_enum',
        }
        enums = {
            'filtering_enum': Page.Filtering.__dict__.values(),
            'type_enum': Page.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/notifications',
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

    def create_page_backed_instagram_account(self, fields=None, params=None, batch=None, pending=False):
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

    def create_pass_thread_control(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'recipient': 'Object',
            'target_app_id': 'int',
            'metadata': 'string',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_personas(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_persona(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.persona import Persona
        param_types = {
            'name': 'string',
            'profile_picture_url': 'Object',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_photos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.photo import Photo
        param_types = {
            'type': 'type_enum',
            'biz_tag_id': 'unsigned int',
            'business_id': 'string',
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
            'nectar_module': 'string',
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
            'temporary': 'bool',
            'location_source_id': 'string',
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

    def create_picture(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profilepicturesource import ProfilePictureSource
        param_types = {
            'composer_session_id': 'string',
            'qn': 'string',
            'photo': 'string',
            'reuse': 'bool',
            'x': 'unsigned int',
            'y': 'unsigned int',
            'width': 'unsigned int',
            'height': 'unsigned int',
            'scaled_crop_rect': 'Object',
            'profile_pic_source': 'string',
            'profile_pic_method': 'string',
            'sticker_id': 'int',
            'caption': 'string',
            'sticker_source_object_id': 'int',
            'msqrd_mask_id': 'string',
            'media_effect_ids': 'list<int>',
            'media_effect_source_object_id': 'int',
            'set_profile_photo_shield': 'string',
            'has_umg': 'bool',
            'android_key_hash': 'string',
            'ios_bundle_id': 'string',
            'proxied_app_id': 'int',
            'picture': 'string',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_place_topics(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.placetopic import PlaceTopic
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/place_topics',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PlaceTopic,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PlaceTopic, api=self._api),
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

    def get_posts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'include_hidden': 'bool',
            'with': 'with_enum',
            'show_expired': 'bool',
            'q': 'string',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_product_catalogs(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_promotable_posts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'include_hidden': 'bool',
            'with': 'with_enum',
            'show_expired': 'bool',
            'q': 'string',
            'is_published': 'bool',
            'include_inline': 'bool',
        }
        enums = {
            'with_enum': PagePost.With.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/promotable_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePost, api=self._api),
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
            'ad_account_id': 'string',
            'geo_level': 'string',
            'gender': 'unsigned int',
            'min_age': 'unsigned int',
            'max_age': 'unsigned int',
            'duration': 'string',
        }
        enums = {
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

    def get_published_posts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagepost import PagePost
        param_types = {
            'since': 'Object',
            'until': 'Object',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_question(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'question': 'string',
            'options': 'list<string>',
            'allow_new_options': 'bool',
            'choose_multiple_options': 'bool',
            'ranked_poll': 'bool',
            'published': 'bool',
            'scheduled_publish_time': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/questions',
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

    def get_ratings(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_request_thread_control(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'recipient': 'Object',
            'metadata': 'string',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_restaurant_orders(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.fooddrinkorder import FoodDrinkOrder
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/restaurant_orders',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FoodDrinkOrder,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=FoodDrinkOrder, api=self._api),
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

    def get_roles(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
            'uid': 'Object',
            'include_deactivated': 'bool',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_rtb_dynamic_posts(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_saved_filters(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagesavedfilter import PageSavedFilter
        param_types = {
            'section': 'section_enum',
        }
        enums = {
            'section_enum': PageSavedFilter.Section.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/saved_filters',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageSavedFilter,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageSavedFilter, api=self._api),
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

    def create_saved_filter(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagesavedfilter import PageSavedFilter
        param_types = {
            'display_name': 'string',
            'section': 'section_enum',
            'filters': 'list<Object>',
        }
        enums = {
            'section_enum': PageSavedFilter.Section.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/saved_filters',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageSavedFilter,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageSavedFilter, api=self._api),
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

    def get_saved_message_responses(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.savedmessageresponse import SavedMessageResponse
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/saved_message_responses',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SavedMessageResponse,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SavedMessageResponse, api=self._api),
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

    def create_saved_message_response(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.savedmessageresponse import SavedMessageResponse
        param_types = {
            'message': 'string',
            'category': 'category_enum',
            'is_enabled': 'bool',
            'title': 'string',
            'image': 'string',
        }
        enums = {
            'category_enum': SavedMessageResponse.Category.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/saved_message_responses',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SavedMessageResponse,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SavedMessageResponse, api=self._api),
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

    def get_schedule_d_posts(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_screen_names(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.screenname import ScreenName
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/screennames',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ScreenName,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ScreenName, api=self._api),
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

    def get_seasons(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videolist import VideoList
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/seasons',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoList, api=self._api),
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

    def get_secondary_receivers(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_settings(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_setting(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'setting': 'setting_enum',
            'value': 'bool',
            'option': 'Object',
        }
        enums = {
            'setting_enum': Page.Setting.__dict__.values(),
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_show_playlists(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videolist import VideoList
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/show_playlists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoList, api=self._api),
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

    def delete_subscribed_apps(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_subscribed_apps(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_subscribed_app(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_subscription(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'object': 'string',
            'fields': 'list<string>',
            'callback_url': 'Object',
            'verify_token': 'string',
            'include_values': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/subscriptions',
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

    def delete_tabs(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tab': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/tabs',
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

    def get_tabs(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_tab(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_id': 'int',
            'tab': 'string',
            'position': 'int',
            'custom_name': 'string',
            'custom_image_url': 'string',
            'is_non_connection_landing_tab': 'bool',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_tagged(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_take_thread_control(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'recipient': 'Object',
            'metadata': 'string',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_thread_owner(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagethreadowner import PageThreadOwner
        param_types = {
            'recipient': 'Object',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_thread_settings(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'setting_type': 'setting_type_enum',
            'thread_state': 'thread_state_enum',
        }
        enums = {
            'setting_type_enum': [
                'ACCOUNT_LINKING',
                'CALL_TO_ACTIONS',
                'GREETING',
                'DOMAIN_WHITELISTING',
                'PAYMENT',
            ],
            'thread_state_enum': [
                'NEW_THREAD',
                'EXISTING_THREAD',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/thread_settings',
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

    def get_thread_settings(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.threadsetting import ThreadSetting
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/thread_settings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ThreadSetting,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ThreadSetting, api=self._api),
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

    def create_thread_setting(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'setting_type': 'setting_type_enum',
            'thread_state': 'thread_state_enum',
            'call_to_actions': 'list<Object>',
            'greeting': 'Object',
            'account_linking_url': 'string',
            'payment_privacy_url': 'string',
            'whitelisted_domains': 'list<string>',
            'domain_action_type': 'domain_action_type_enum',
            'payment_public_key': 'string',
            'payment_dev_mode_action': 'payment_dev_mode_action_enum',
            'payment_testers': 'list<string>',
        }
        enums = {
            'setting_type_enum': [
                'ACCOUNT_LINKING',
                'CALL_TO_ACTIONS',
                'GREETING',
                'DOMAIN_WHITELISTING',
                'PAYMENT',
            ],
            'thread_state_enum': [
                'NEW_THREAD',
                'EXISTING_THREAD',
            ],
            'domain_action_type_enum': Page.DomainActionType.__dict__.values(),
            'payment_dev_mode_action_enum': Page.PaymentDevModeAction.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/thread_settings',
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

    def get_threads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'tags': 'list<string>',
            'folder': 'string',
            'psid': 'Object',
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

    def get_tours(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.eventtour import EventTour
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
            target_class=EventTour,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=EventTour, api=self._api),
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

    def create_unlink_account(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_user_permissions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'email': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/userpermissions',
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

    def create_user_permission(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'email': 'string',
            'business': 'string',
            'tasks': 'list<tasks_enum>',
        }
        enums = {
            'tasks_enum': Page.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/userpermissions',
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

    def get_video_broadcasts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.livevideo import LiveVideo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_broadcasts',
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

    def get_video_copyright_rules(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videocopyrightrule import VideoCopyrightRule
        param_types = {
            'source': 'source_enum',
            'selected_rule_id': 'string',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_video_copyright_rule(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videocopyrightrule import VideoCopyrightRule
        param_types = {
            'name': 'string',
            'condition_groups': 'list<Object>',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_video_copyrights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videocopyright import VideoCopyright
        param_types = {
            'use_fallback': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_video_copyright(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videocopyright import VideoCopyright
        param_types = {
            'monitoring_type': 'monitoring_type_enum',
            'rule_id': 'string',
            'whitelisted_ids': 'list<string>',
            'whitelisted_ig_user_ids': 'list<string>',
            'ownership_countries': 'list<string>',
            'excluded_ownership_countries': 'list<string>',
            'excluded_ownership_segments': 'list<Object>',
            'is_reference_disabled': 'bool',
            'content_category': 'content_category_enum',
            'attribution_id': 'string',
            'copyright_content_id': 'string',
            'is_reference_video': 'bool',
            'fingerprint_id': 'string',
        }
        enums = {
            'monitoring_type_enum': VideoCopyright.MonitoringType.__dict__.values(),
            'content_category_enum': VideoCopyright.ContentCategory.__dict__.values(),
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_video_lists(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'video_list_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/video_lists',
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

    def get_video_lists(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_video_list(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'title': 'string',
            'description': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/video_lists',
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

    def get_video_media_copyrights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videocopyright import VideoCopyright
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_media_copyrights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoCopyright,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoCopyright, api=self._api),
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
            'ad_breaks': 'Object',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'backdated_post': 'Object',
            'custom_labels': 'list<string>',
            'call_to_action': 'Object',
            'expiration': 'Object',
            'feed_targeting': 'Object',
            'published': 'bool',
            'scheduled_publish_time': 'unsigned int',
            'targeting': 'Object',
            'no_story': 'bool',
            'secret': 'bool',
            'social_actions': 'bool',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
            'sponsor_relationship': 'unsigned int',
            'content_tags': 'list<string>',
            'reference_only': 'bool',
            'video_asset_id': 'string',
            'universal_video_id': 'string',
            'multilingual_data': 'list<Object>',
            'specified_dialect': 'string',
            'crossposted_video_id': 'string',
        }
        enums = {
            'unpublished_content_type_enum': AdVideo.UnpublishedContentType.__dict__.values(),
            'original_projection_type_enum': AdVideo.OriginalProjectionType.__dict__.values(),
            'formatting_enum': AdVideo.Formatting.__dict__.values(),
            'upload_phase_enum': AdVideo.UploadPhase.__dict__.values(),
            'content_category_enum': AdVideo.ContentCategory.__dict__.values(),
            'container_type_enum': AdVideo.ContainerType.__dict__.values(),
            'swap_mode_enum': AdVideo.SwapMode.__dict__.values(),
            'backdated_time_granularity_enum': AdVideo.BackdatedTimeGranularity.__dict__.values(),
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

    def get_videos_you_can_use(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagevideosyoucanuse import PageVideosYouCanUse
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/videos_you_can_use',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageVideosYouCanUse,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageVideosYouCanUse, api=self._api),
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

    def get_visitor_posts(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_work_flows(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagesplatformcomponentflowserviceconfig import PagesPlatformComponentFlowServiceConfig
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/workflows',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagesPlatformComponentFlowServiceConfig,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagesPlatformComponentFlowServiceConfig, api=self._api),
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
        'access_token': 'string',
        'ad_campaign': 'AdSet',
        'affiliation': 'string',
        'app_id': 'string',
        'app_links': 'AppLinks',
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
        'connected_instagram_account': 'ShadowIGUser',
        'contact_address': 'MailingAddress',
        'context': 'OpenGraphContext',
        'copyright_attribution_insights': 'CopyrightAttributionInsights',
        'copyright_whitelisted_ig_partners': 'list<string>',
        'country_page_likes': 'unsigned int',
        'cover': 'CoverPhoto',
        'culinary_team': 'string',
        'current_location': 'string',
        'description': 'string',
        'description_html': 'string',
        'directed_by': 'string',
        'display_subtext': 'string',
        'displayed_message_response_time': 'string',
        'emails': 'list<string>',
        'engagement': 'Engagement',
        'fan_count': 'unsigned int',
        'featured_video': 'AdVideo',
        'features': 'string',
        'food_styles': 'list<string>',
        'founded': 'string',
        'general_info': 'string',
        'general_manager': 'string',
        'genre': 'string',
        'global_brand_page_name': 'string',
        'global_brand_parent_page': 'Page',
        'global_brand_root_id': 'string',
        'has_added_app': 'bool',
        'has_whatsapp_business_number': 'bool',
        'has_whatsapp_number': 'bool',
        'hometown': 'string',
        'hours': 'map<string, string>',
        'id': 'string',
        'impressum': 'string',
        'influences': 'string',
        'instagram_business_account': 'ShadowIGUser',
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
        'leadgen_form_preview_details': 'LeadGenFormPreviewDetails',
        'leadgen_has_crm_integration': 'bool',
        'leadgen_has_fat_ping_crm_integration': 'bool',
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
        'place_type': 'string',
        'plot_outline': 'string',
        'preferred_audience': 'Targeting',
        'press_contact': 'string',
        'price_range': 'string',
        'produced_by': 'string',
        'products': 'string',
        'promotion_eligible': 'bool',
        'promotion_ineligible_reason': 'string',
        'public_transit': 'string',
        'publisher_space': 'PublisherSpace',
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
        'supports_instant_articles': 'bool',
        'talking_about_count': 'unsigned int',
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
        field_enum_info['Setting'] = Page.Setting.__dict__.values()
        field_enum_info['Audience'] = Page.Audience.__dict__.values()
        field_enum_info['PermittedTasks'] = Page.PermittedTasks.__dict__.values()
        field_enum_info['Tasks'] = Page.Tasks.__dict__.values()
        field_enum_info['MessagingType'] = Page.MessagingType.__dict__.values()
        field_enum_info['NotificationType'] = Page.NotificationType.__dict__.values()
        field_enum_info['PublishStatus'] = Page.PublishStatus.__dict__.values()
        field_enum_info['SenderAction'] = Page.SenderAction.__dict__.values()
        field_enum_info['Type'] = Page.Type.__dict__.values()
        field_enum_info['Model'] = Page.Model.__dict__.values()
        field_enum_info['Filtering'] = Page.Filtering.__dict__.values()
        field_enum_info['SubscribedFields'] = Page.SubscribedFields.__dict__.values()
        field_enum_info['DomainActionType'] = Page.DomainActionType.__dict__.values()
        field_enum_info['PaymentDevModeAction'] = Page.PaymentDevModeAction.__dict__.values()
        return field_enum_info


