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

class Application(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isApplication = True
        super(Application, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        an_ad_space_limit = 'an_ad_space_limit'
        an_platforms = 'an_platforms'
        android_key_hash = 'android_key_hash'
        android_sdk_error_categories = 'android_sdk_error_categories'
        app_domains = 'app_domains'
        app_events_feature_bitmask = 'app_events_feature_bitmask'
        app_events_session_timeout = 'app_events_session_timeout'
        app_install_tracked = 'app_install_tracked'
        app_name = 'app_name'
        app_signals_binding_ios = 'app_signals_binding_ios'
        app_type = 'app_type'
        auth_dialog_data_help_url = 'auth_dialog_data_help_url'
        auth_dialog_headline = 'auth_dialog_headline'
        auth_dialog_perms_explanation = 'auth_dialog_perms_explanation'
        auth_referral_default_activity_privacy = 'auth_referral_default_activity_privacy'
        auth_referral_enabled = 'auth_referral_enabled'
        auth_referral_extended_perms = 'auth_referral_extended_perms'
        auth_referral_friend_perms = 'auth_referral_friend_perms'
        auth_referral_response_type = 'auth_referral_response_type'
        auth_referral_user_perms = 'auth_referral_user_perms'
        auto_event_mapping_android = 'auto_event_mapping_android'
        auto_event_mapping_ios = 'auto_event_mapping_ios'
        auto_event_setup_enabled = 'auto_event_setup_enabled'
        business = 'business'
        canvas_fluid_height = 'canvas_fluid_height'
        canvas_fluid_width = 'canvas_fluid_width'
        canvas_url = 'canvas_url'
        category = 'category'
        client_config = 'client_config'
        company = 'company'
        configured_ios_sso = 'configured_ios_sso'
        contact_email = 'contact_email'
        context = 'context'
        created_time = 'created_time'
        creator_uid = 'creator_uid'
        daily_active_users = 'daily_active_users'
        daily_active_users_rank = 'daily_active_users_rank'
        deauth_callback_url = 'deauth_callback_url'
        default_share_mode = 'default_share_mode'
        description = 'description'
        financial_id = 'financial_id'
        gdpv4_chrome_custom_tabs_enabled = 'gdpv4_chrome_custom_tabs_enabled'
        gdpv4_enabled = 'gdpv4_enabled'
        gdpv4_nux_content = 'gdpv4_nux_content'
        gdpv4_nux_enabled = 'gdpv4_nux_enabled'
        groups_app_settings = 'groups_app_settings'
        has_messenger_product = 'has_messenger_product'
        hosting_url = 'hosting_url'
        icon_url = 'icon_url'
        id = 'id'
        ios_bundle_id = 'ios_bundle_id'
        ios_sdk_dialog_flows = 'ios_sdk_dialog_flows'
        ios_sdk_error_categories = 'ios_sdk_error_categories'
        ios_sfvc_attr = 'ios_sfvc_attr'
        ios_supports_native_proxy_auth_flow = 'ios_supports_native_proxy_auth_flow'
        ios_supports_system_auth = 'ios_supports_system_auth'
        ipad_app_store_id = 'ipad_app_store_id'
        iphone_app_store_id = 'iphone_app_store_id'
        is_viewer_admin = 'is_viewer_admin'
        latest_sdk_version = 'latest_sdk_version'
        link = 'link'
        logging_token = 'logging_token'
        login_secret = 'login_secret'
        logo_url = 'logo_url'
        migrations = 'migrations'
        mobile_profile_section_url = 'mobile_profile_section_url'
        mobile_web_url = 'mobile_web_url'
        monthly_active_users = 'monthly_active_users'
        monthly_active_users_rank = 'monthly_active_users_rank'
        name = 'name'
        namespace = 'namespace'
        object_store_urls = 'object_store_urls'
        page_tab_default_name = 'page_tab_default_name'
        page_tab_url = 'page_tab_url'
        photo_url = 'photo_url'
        privacy_policy_url = 'privacy_policy_url'
        profile_section_url = 'profile_section_url'
        property_id = 'property_id'
        real_time_mode_devices = 'real_time_mode_devices'
        restrictions = 'restrictions'
        sdk_update_message = 'sdk_update_message'
        seamless_login = 'seamless_login'
        secure_canvas_url = 'secure_canvas_url'
        secure_page_tab_url = 'secure_page_tab_url'
        server_ip_whitelist = 'server_ip_whitelist'
        smart_login_bookmark_icon_url = 'smart_login_bookmark_icon_url'
        smart_login_menu_icon_url = 'smart_login_menu_icon_url'
        social_discovery = 'social_discovery'
        subcategory = 'subcategory'
        supported_platforms = 'supported_platforms'
        supports_apprequests_fast_app_switch = 'supports_apprequests_fast_app_switch'
        supports_attribution = 'supports_attribution'
        supports_implicit_sdk_logging = 'supports_implicit_sdk_logging'
        suppress_native_ios_gdp = 'suppress_native_ios_gdp'
        terms_of_service_url = 'terms_of_service_url'
        url_scheme_suffix = 'url_scheme_suffix'
        user_support_email = 'user_support_email'
        user_support_url = 'user_support_url'
        website_url = 'website_url'
        weekly_active_users = 'weekly_active_users'

    class SupportedPlatforms:
        web = 'WEB'
        canvas = 'CANVAS'
        mobile_web = 'MOBILE_WEB'
        iphone = 'IPHONE'
        ipad = 'IPAD'
        android = 'ANDROID'
        windows = 'WINDOWS'
        amazon = 'AMAZON'
        supplementary_images = 'SUPPLEMENTARY_IMAGES'
        gameroom = 'GAMEROOM'
        instant_game = 'INSTANT_GAME'

    class AnPlatforms:
        ios = 'IOS'
        android = 'ANDROID'
        mobile_web = 'MOBILE_WEB'
        desktop = 'DESKTOP'
        instant_articles = 'INSTANT_ARTICLES'
        unknown = 'UNKNOWN'

    class AggregationPeriod:
        hour = 'HOUR'
        day = 'DAY'
        total = 'TOTAL'

    class Breakdowns:
        age = 'AGE'
        app = 'APP'
        country = 'COUNTRY'
        delivery_method = 'DELIVERY_METHOD'
        display_format = 'DISPLAY_FORMAT'
        deal = 'DEAL'
        deal_ad = 'DEAL_AD'
        deal_page = 'DEAL_PAGE'
        gender = 'GENDER'
        placement = 'PLACEMENT'
        platform = 'PLATFORM'
        property = 'PROPERTY'
        clicked_view_tag = 'CLICKED_VIEW_TAG'
        no_fill_reason = 'NO_FILL_REASON'

    class Metrics:
        fb_ad_network_bidding_request = 'FB_AD_NETWORK_BIDDING_REQUEST'
        fb_ad_network_bidding_response = 'FB_AD_NETWORK_BIDDING_RESPONSE'
        fb_ad_network_bidding_bid_rate = 'FB_AD_NETWORK_BIDDING_BID_RATE'
        fb_ad_network_bidding_win_rate = 'FB_AD_NETWORK_BIDDING_WIN_RATE'
        fb_ad_network_request = 'FB_AD_NETWORK_REQUEST'
        fb_ad_network_filled_request = 'FB_AD_NETWORK_FILLED_REQUEST'
        fb_ad_network_fill_rate = 'FB_AD_NETWORK_FILL_RATE'
        fb_ad_network_imp = 'FB_AD_NETWORK_IMP'
        fb_ad_network_show_rate = 'FB_AD_NETWORK_SHOW_RATE'
        fb_ad_network_click = 'FB_AD_NETWORK_CLICK'
        fb_ad_network_ctr = 'FB_AD_NETWORK_CTR'
        fb_ad_network_bidding_revenue = 'FB_AD_NETWORK_BIDDING_REVENUE'
        fb_ad_network_revenue = 'FB_AD_NETWORK_REVENUE'
        fb_ad_network_cpm = 'FB_AD_NETWORK_CPM'
        fb_ad_network_video_guarantee_revenue = 'FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE'
        fb_ad_network_video_view = 'FB_AD_NETWORK_VIDEO_VIEW'
        fb_ad_network_video_view_rate = 'FB_AD_NETWORK_VIDEO_VIEW_RATE'
        fb_ad_network_video_mrc = 'FB_AD_NETWORK_VIDEO_MRC'
        fb_ad_network_video_mrc_rate = 'FB_AD_NETWORK_VIDEO_MRC_RATE'
        fb_ad_network_win_rate = 'FB_AD_NETWORK_WIN_RATE'
        fb_ad_network_direct_total_revenue = 'FB_AD_NETWORK_DIRECT_TOTAL_REVENUE'
        fb_ad_network_direct_publisher_bill = 'FB_AD_NETWORK_DIRECT_PUBLISHER_BILL'
        fb_ad_network_fast_click_rate = 'FB_AD_NETWORK_FAST_CLICK_RATE'
        fb_ad_network_fast_return_rate = 'FB_AD_NETWORK_FAST_RETURN_RATE'
        fb_ad_network_click_value_score = 'FB_AD_NETWORK_CLICK_VALUE_SCORE'
        fb_ad_network_fast_click_numerator = 'FB_AD_NETWORK_FAST_CLICK_NUMERATOR'
        fb_ad_network_fast_click_denominator = 'FB_AD_NETWORK_FAST_CLICK_DENOMINATOR'
        fb_ad_network_fast_return_numerator = 'FB_AD_NETWORK_FAST_RETURN_NUMERATOR'
        fb_ad_network_fast_return_denominator = 'FB_AD_NETWORK_FAST_RETURN_DENOMINATOR'
        fb_ad_network_click_value_score_numerator = 'FB_AD_NETWORK_CLICK_VALUE_SCORE_NUMERATOR'
        fb_ad_network_click_value_score_denominator = 'FB_AD_NETWORK_CLICK_VALUE_SCORE_DENOMINATOR'
        fb_ad_network_no_fill = 'FB_AD_NETWORK_NO_FILL'

    class OrderingColumn:
        time = 'TIME'
        value = 'VALUE'
        metric = 'METRIC'

    class OrderingType:
        ascending = 'ASCENDING'
        descending = 'DESCENDING'

    class Platform:
        android = 'ANDROID'
        ios = 'IOS'

    class RequestType:
        app_indexing = 'APP_INDEXING'
        plugin = 'PLUGIN'
        button_sampling = 'BUTTON_SAMPLING'

    class MutationMethod:
        replace = 'REPLACE'
        add = 'ADD'
        delete = 'DELETE'

    class ScoreType:
        custom = 'CUSTOM'
        numeric = 'NUMERIC'
        time = 'TIME'

    class SortOrder:
        higher_is_better = 'HIGHER_IS_BETTER'
        lower_is_better = 'LOWER_IS_BETTER'

    class Role:
        administrators = 'administrators'
        developers = 'developers'
        testers = 'testers'
        insights_users = 'insights users'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'advertiser_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Application,
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
            'migrations': 'string',
            'restrictions': 'string',
            'android_key_hash': 'list<string>',
            'an_platforms': 'list<an_platforms_enum>',
            'app_name': 'string',
            'app_type': 'bool',
            'auth_dialog_headline': 'string',
            'auth_dialog_perms_explanation': 'string',
            'auth_referral_default_activity_privacy': 'string',
            'auth_referral_enabled': 'bool',
            'auth_referral_extended_perms': 'list<string>',
            'auth_referral_response_type': 'string',
            'auth_referral_user_perms': 'list<string>',
            'auth_referral_friend_perms': 'list<string>',
            'canvas_fluid_height': 'bool',
            'canvas_fluid_width': 'bool',
            'category': 'string',
            'configured_ios_sso': 'bool',
            'ios_bundle_id': 'list<string>',
            'ipad_app_store_id': 'string',
            'iphone_app_store_id': 'string',
            'page_tab_default_name': 'string',
            'social_discovery': 'bool',
            'subcategory': 'string',
            'android_package_name': 'string',
            'android_class_name': 'string',
            'android_key_hashes': 'list<string>',
            'android_sso': 'bool',
            'app_domains': 'list<string>',
            'auth_dialog_data_help_url': 'string',
            'canvas_url': 'string',
            'contact_email': 'string',
            'created_time': 'Object',
            'creator_uid': 'int',
            'deauth_callback_url': 'string',
            'hosting_url': 'string',
            'mobile_web_url': 'string',
            'namespace': 'string',
            'page_tab_url': 'string',
            'privacy_policy_url': 'string',
            'secure_canvas_url': 'string',
            'secure_page_tab_url': 'string',
            'server_ip_whitelist': 'list<string>',
            'terms_of_service_url': 'string',
            'url_scheme_suffix': 'string',
            'user_support_email': 'string',
            'user_support_url': 'string',
            'website_url': 'string',
        }
        enums = {
            'an_platforms_enum': Application.AnPlatforms.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Application,
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

    def create_Local_Service_Booking_Test(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'api_name': 'api_name_enum',
        }
        enums = {
            'api_name_enum': [
                'AVAILABILITY',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/LocalServiceBookingTest',
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

    def delete_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'type': 'type_enum',
            'uid': 'int',
        }
        enums = {
            'type_enum': [
                'test-users',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
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

    def get_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': [
                'test-users',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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

    def create_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
            'owner_access_token': 'string',
            'installed': 'bool',
            'permissions': 'Object',
            'name': 'string',
            'minor': 'bool',
            'type': 'type_enum',
        }
        enums = {
            'type_enum': [
                'test-users',
            ],
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

    def get_achievements(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.opengraphobject import OpenGraphObject
        param_types = {
            'achievement': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/achievements',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OpenGraphObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OpenGraphObject, api=self._api),
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
            'event': 'event_enum',
            'attribution': 'string',
            'advertiser_id': 'string',
            'anon_id': 'string',
            'advertiser_tracking_enabled': 'bool',
            'application_tracking_enabled': 'bool',
            'extinfo': 'Object',
            'bundle_id': 'string',
            'bundle_version': 'string',
            'bundle_short_version': 'string',
            'auto_publish': 'bool',
            'custom_events': 'list<Object>',
            'custom_events_file': 'file',
            'installer_package': 'string',
            'migration_bundle': 'string',
            'url_schemes': 'list<string>',
            'device_token': 'string',
            'windows_attribution_id': 'string',
            'consider_views': 'bool',
            'include_video_data': 'bool',
            'include_dwell_data': 'bool',
            'page_id': 'unsigned int',
            'page_scoped_user_id': 'unsigned int',
            'ud': 'map',
            'user_id': 'string',
            'user_id_type': 'user_id_type_enum',
            'app_user_id': 'string',
            'receipt_data': 'string',
        }
        enums = {
            'event_enum': [
                'MOBILE_APP_INSTALL',
                'CUSTOM_APP_EVENTS',
                'DEFERRED_APP_LINK',
            ],
            'user_id_type_enum': [
                'INSTANT_GAMES_PLAYER_ID',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/activities',
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

    def get_ad_network_analytics(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adnetworkanalyticssyncqueryresult import AdNetworkAnalyticsSyncQueryResult
        param_types = {
            'aggregation_period': 'aggregation_period_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'filters': 'list<map>',
            'limit': 'unsigned int',
            'metrics': 'list<metrics_enum>',
            'ordering_column': 'ordering_column_enum',
            'ordering_type': 'ordering_type_enum',
            'since': 'Object',
            'until': 'Object',
        }
        enums = {
            'aggregation_period_enum': Application.AggregationPeriod.__dict__.values(),
            'breakdowns_enum': Application.Breakdowns.__dict__.values(),
            'metrics_enum': Application.Metrics.__dict__.values(),
            'ordering_column_enum': Application.OrderingColumn.__dict__.values(),
            'ordering_type_enum': Application.OrderingType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adnetworkanalytics',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdNetworkAnalyticsSyncQueryResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdNetworkAnalyticsSyncQueryResult, api=self._api),
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

    def create_ad_network_analytic(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'aggregation_period': 'aggregation_period_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'metrics': 'list<metrics_enum>',
            'filters': 'list<Object>',
            'limit': 'int',
            'ordering_column': 'ordering_column_enum',
            'ordering_type': 'ordering_type_enum',
            'since': 'Object',
            'until': 'Object',
        }
        enums = {
            'aggregation_period_enum': Application.AggregationPeriod.__dict__.values(),
            'breakdowns_enum': Application.Breakdowns.__dict__.values(),
            'metrics_enum': Application.Metrics.__dict__.values(),
            'ordering_column_enum': Application.OrderingColumn.__dict__.values(),
            'ordering_type_enum': Application.OrderingType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adnetworkanalytics',
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

    def get_ad_network_analytics_results(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adnetworkanalyticsasyncqueryresult import AdNetworkAnalyticsAsyncQueryResult
        param_types = {
            'query_ids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adnetworkanalytics_results',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdNetworkAnalyticsAsyncQueryResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdNetworkAnalyticsAsyncQueryResult, api=self._api),
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

    def get_ads_app_insights(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'metric': 'metric_enum',
            'since': 'datetime',
            'until': 'datetime',
            'details': 'details_enum',
            'filters': 'Object',
            'breakdowns': 'list<breakdowns_enum>',
            'limit': 'unsigned int',
            'timeseries': 'bool',
        }
        enums = {
            'metric_enum': [
                'ads_api_call',
                'ads_api_error',
                'ads_api_error_rate',
            ],
            'details_enum': [
                'daily',
                'hourly',
            ],
            'breakdowns_enum': [
                'none',
                'ad_account_id',
                'method',
                'version',
                'error',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads_app_insights',
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

    def get_ads_app_insights_dimensions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'dimension': 'dimension_enum',
            'since': 'datetime',
            'until': 'datetime',
            'details': 'details_enum',
            'limit': 'unsigned int',
        }
        enums = {
            'dimension_enum': [
                'ad_account_id',
                'method',
                'version',
            ],
            'details_enum': [
                'daily',
                'hourly',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads_app_insights_dimensions',
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

    def get_android_dialog_configs(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/android_dialog_configs',
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

    def get_app_event_types(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/app_event_types',
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

    def create_app_indexing(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_version': 'string',
            'platform': 'platform_enum',
            'tree': 'map',
            'extra_info': 'string',
            'request_type': 'request_type_enum',
            'device_session_id': 'string',
        }
        enums = {
            'platform_enum': Application.Platform.__dict__.values(),
            'request_type_enum': Application.RequestType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/app_indexing',
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

    def create_app_indexing_session(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'device_session_id': 'string',
            'extinfo': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/app_indexing_session',
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

    def get_app_insights(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'metric_key': 'string',
            'period': 'period_enum',
            'since': 'datetime',
            'until': 'datetime',
            'breakdowns': 'list<string>',
            'aggregateBy': 'aggregateBy_enum',
            'event_name': 'string',
            'ecosystem': 'ecosystem_enum',
            'intervals_to_aggregate': 'int',
        }
        enums = {
            'period_enum': [
                'mins_15',
                'hourly',
                'daily',
                'weekly',
                'monthly',
                'lifetime',
                'days_28',
                'range',
            ],
            'aggregateBy_enum': [
                'COUNT',
                'COUNT_IDENTIFIED_USERS',
                'USERS',
                'TOPK',
                'SUM',
                'SUM_PER_EVENT',
                'SUM_IDENTIFIED_USERS',
                'USD_SUM',
                'USD_SUM_PER_EVENT',
                'USD_SUM_IDENTIFIED_USERS',
                'USD_SUM_PER_USER',
                'UNKNOWN_USERS',
                'SCORE',
                'MEDIAN_VALUE',
                'MEDIAN_VALUE_PER_USER',
                'DAU',
                'WAU',
                'MAU',
                'PERCENTILES_COUNT',
                'PERCENTILES_VALUE',
                'PERCENTILES_USD_VALUE',
                'OVERLAP',
                'COUNT_PER_USER',
                'VALUE_PER_USER',
                'USD_VALUE_PER_USER',
                'SESSIONS_PER_JOURNEY',
                'CONVERTED_JOURNEY_PERCENT',
                'MEDIAN_JOURNEY_LENGTH',
                'AVERAGE_JOURNEY_LENGTH',
                'JOURNEY_CHANNEL_INCLUSION',
                'EVENT_SOURCE_IDS',
                'SESSION_BOUNCE_RATE',
                'JOURNEY_INCLUSION',
                'USER_PROPERTY_USER_COUNT',
            ],
            'ecosystem_enum': [
                'GAME',
                'NON_GAME',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/app_insights',
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

    def get_app_installed_groups(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.group import Group
        param_types = {
            'group_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/app_installed_groups',
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

    def create_app_link_host(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'android': 'Object',
            'ios': 'Object',
            'ipad': 'Object',
            'iphone': 'Object',
            'web': 'Object',
            'windows_phone': 'Object',
            'windows': 'Object',
            'windows_universal': 'Object',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/app_link_hosts',
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

    def create_app_push_device_token(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'device_id': 'string',
            'device_token': 'string',
            'platform': 'platform_enum',
        }
        enums = {
            'platform_enum': Application.Platform.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/app_push_device_token',
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

    def get_app_assets(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/appassets',
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

    def create_asset(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'asset': 'file',
            'comment': 'string',
            'type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/assets',
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

    def get_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudience import CustomAudience
        param_types = {
            'ad_account': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/audiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudience, api=self._api),
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

    def delete_authorized_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/authorized_adaccounts',
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

    def get_authorized_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/authorized_adaccounts',
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

    def create_authorized_ad_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/authorized_adaccounts',
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

    def delete_banned(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uids': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/banned',
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

    def get_banned(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
            'uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/banned',
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

    def create_banned(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
            'uids': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/banned',
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

    def get_button_auto_detection_device_selection(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'device_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/button_auto_detection_device_selection',
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

    def create_button_indexing(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_version': 'string',
            'indexed_button_list': 'list<map>',
            'device_id': 'string',
            'extinfo': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/button_indexing',
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

    def create_codeless_event_binding(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'mutation_method': 'mutation_method_enum',
            'platform': 'platform_enum',
            'bindings': 'list<map>',
        }
        enums = {
            'mutation_method_enum': Application.MutationMethod.__dict__.values(),
            'platform_enum': Application.Platform.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/codeless_event_bindings',
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

    def create_codeless_event_mapping(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'mutation_method': 'mutation_method_enum',
            'platform': 'platform_enum',
            'mappings': 'list<map>',
        }
        enums = {
            'mutation_method_enum': Application.MutationMethod.__dict__.values(),
            'platform_enum': Application.Platform.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/codeless_event_mappings',
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

    def get_connections(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/connections',
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

    def get_custom_audience_third_party_id(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'limit_event_usage': 'bool',
            'udid': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/custom_audience_third_party_id',
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

    def get_da_checks(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.dacheck import DACheck
        param_types = {
            'checks': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/da_checks',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DACheck,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DACheck, api=self._api),
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

    def get_direct_deals(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.directdeal import DirectDeal
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/direct_deals',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DirectDeal,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DirectDeal, api=self._api),
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
        }
        enums = {
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_food_drink_orders(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'order_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/food_drink_orders',
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

    def create_food_drink_order(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'order_id': 'string',
            'status': 'status_enum',
        }
        enums = {
            'status_enum': [
                'CREATED',
                'CONFIRMED',
                'CANCELLED',
                'DELIVERED',
                'READY_FOR_PICKUP',
                'OUT_FOR_DELIVERY',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/food_drink_orders',
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

    def get_full_app_indexing_infos(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_version': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/full_app_indexing_infos',
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

    def create_full_app_indexing_info(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_version': 'string',
            'full_app_indexing_info_classes': 'list<map>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/full_app_indexing_infos',
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

    def create_groups_app_setting(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'post_install_url': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/groups_app_settings',
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

    def get_insights_event_labels(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'add': 'list<string>',
            'delete': 'unsigned int',
            'ecosystem': 'bool',
            'since': 'datetime',
            'until': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights_event_labels',
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

    def get_ios_dialog_configs(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ios_dialog_configs',
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

    def create_leaderboards_create(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'context_id': 'string',
            'sort_order': 'sort_order_enum',
            'score_type': 'score_type_enum',
            'decimal_offset': 'unsigned int',
            'unit': 'string',
        }
        enums = {
            'sort_order_enum': Application.SortOrder.__dict__.values(),
            'score_type_enum': Application.ScoreType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leaderboards_create',
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

    def create_leaderboards_delete_entry(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'player_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leaderboards_delete_entry',
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

    def create_leaderboards_reset(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'reset_time': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leaderboards_reset',
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

    def create_leaderboards_set_score(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'score': 'unsigned int',
            'player_id': 'Object',
            'extra_data': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/leaderboards_set_score',
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

    def get_local_service_booking_config(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/local_service_booking_config',
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

    def create_local_service_booking_config(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'base_url': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/local_service_booking_config',
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

    def create_machine(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/machines',
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

    def create_mmp_auditing(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'event': 'string',
            'is_fb': 'bool',
            'fb_ad_id': 'unsigned int',
            'attribution': 'string',
            'advertiser_id': 'string',
            'fb_click_time': 'unsigned int',
            'fb_view_time': 'unsigned int',
            'event_reported_time': 'unsigned int',
            'attribution_model': 'string',
            'click_attr_window': 'unsigned int',
            'view_attr_window': 'unsigned int',
            'decline_reason': 'string',
            'auditing_token': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/mmp_auditing',
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

    def get_mobile_sdk_gk(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'device_id': 'string',
            'platform': 'platform_enum',
            'sdk_version': 'string',
        }
        enums = {
            'platform_enum': [
                'ANDROID',
                'IOS',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/mobile_sdk_gk',
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

    def get_moods_for_application(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/moods_for_application',
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

    def get_object_types(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/object_types',
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

    def get_objects(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.opengraphobject import OpenGraphObject
        param_types = {
            'type': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/objects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OpenGraphObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OpenGraphObject, api=self._api),
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

    def create_object(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.opengraphobject import OpenGraphObject
        param_types = {
            'object': 'Object',
            'type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/objects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OpenGraphObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OpenGraphObject, api=self._api),
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

    def create_occludes_popup(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'unity': 'bool',
            'flash': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/occludespopups',
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

    def get_ozone_release(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ozone_release',
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

    def create_ozone_release(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'release_name': 'string',
            'changelog': 'string',
            'rollout_percentage': 'float',
            'auto_push_to_prod': 'bool',
            'channel_id': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/ozone_release',
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

    def delete_payment_currencies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'currency_url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/payment_currencies',
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

    def create_payment_currency(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'currency_url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/payment_currencies',
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

    def delete_payments_test_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uids': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/payments_test_users',
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

    def get_payments_test_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/payments_test_users',
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

    def create_payments_test_user(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uids': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/payments_test_users',
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

    def get_permissions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'permission': 'Object',
            'status': 'list<status_enum>',
            'android_key_hash': 'string',
            'ios_bundle_id': 'string',
            'proxied_app_id': 'int',
        }
        enums = {
            'status_enum': [
                'live',
                'unapproved',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/permissions',
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

    def get_pixel_helper_debugging_info(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.externaleventsourcepixelhelperdebugginginfo import ExternalEventSourcePixelHelperDebuggingInfo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pixel_helper_debugging_info',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExternalEventSourcePixelHelperDebuggingInfo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExternalEventSourcePixelHelperDebuggingInfo, api=self._api),
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

    def get_products(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'product_ids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/products',
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

    def get_purchases(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'is_premium': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/purchases',
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

    def get_recent_debuggings(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.externaleventsourcedebugging import ExternalEventSourceDebugging
        param_types = {
            'event_name': 'string',
            'diagnostic': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/recent_debuggings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExternalEventSourceDebugging,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExternalEventSourceDebugging, api=self._api),
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

    def delete_roles(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/roles',
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

    def get_roles(self, fields=None, params=None, batch=None, pending=False):
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

    def create_role(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'role': 'role_enum',
        }
        enums = {
            'role_enum': Application.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/roles',
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

    def create_staging_resource(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'file': 'file',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/stagingresources',
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

    def get_subscribed_domains(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/subscribed_domains',
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

    def create_subscribed_domain(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'subscribe': 'list<string>',
            'unsubscribe': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/subscribed_domains',
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

    def get_subscribed_domains_phishing(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/subscribed_domains_phishing',
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

    def create_subscribed_domains_phishing(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'subscribe': 'list<string>',
            'unsubscribe': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/subscribed_domains_phishing',
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

    def delete_subscriptions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'object': 'string',
            'fields': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
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

    def create_upload(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'session_type': 'session_type_enum',
            'file_type': 'string',
            'file_length': 'unsigned int',
            'file_name': 'string',
        }
        enums = {
            'session_type_enum': [
                'attachment',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/uploads',
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

    def create_user_property(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'data': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/user_properties',
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
        'an_ad_space_limit': 'unsigned int',
        'an_platforms': 'list<string>',
        'android_key_hash': 'list<string>',
        'android_sdk_error_categories': 'list<Object>',
        'app_domains': 'list<string>',
        'app_events_feature_bitmask': 'unsigned int',
        'app_events_session_timeout': 'unsigned int',
        'app_install_tracked': 'bool',
        'app_name': 'string',
        'app_signals_binding_ios': 'list<Object>',
        'app_type': 'unsigned int',
        'auth_dialog_data_help_url': 'string',
        'auth_dialog_headline': 'string',
        'auth_dialog_perms_explanation': 'string',
        'auth_referral_default_activity_privacy': 'string',
        'auth_referral_enabled': 'unsigned int',
        'auth_referral_extended_perms': 'list<string>',
        'auth_referral_friend_perms': 'list<string>',
        'auth_referral_response_type': 'string',
        'auth_referral_user_perms': 'list<string>',
        'auto_event_mapping_android': 'list<Object>',
        'auto_event_mapping_ios': 'list<Object>',
        'auto_event_setup_enabled': 'bool',
        'business': 'Business',
        'canvas_fluid_height': 'bool',
        'canvas_fluid_width': 'unsigned int',
        'canvas_url': 'string',
        'category': 'string',
        'client_config': 'map',
        'company': 'string',
        'configured_ios_sso': 'bool',
        'contact_email': 'string',
        'context': 'Object',
        'created_time': 'datetime',
        'creator_uid': 'string',
        'daily_active_users': 'string',
        'daily_active_users_rank': 'unsigned int',
        'deauth_callback_url': 'string',
        'default_share_mode': 'string',
        'description': 'string',
        'financial_id': 'string',
        'gdpv4_chrome_custom_tabs_enabled': 'bool',
        'gdpv4_enabled': 'bool',
        'gdpv4_nux_content': 'string',
        'gdpv4_nux_enabled': 'bool',
        'groups_app_settings': 'Object',
        'has_messenger_product': 'bool',
        'hosting_url': 'string',
        'icon_url': 'string',
        'id': 'string',
        'ios_bundle_id': 'list<string>',
        'ios_sdk_dialog_flows': 'Object',
        'ios_sdk_error_categories': 'list<Object>',
        'ios_sfvc_attr': 'bool',
        'ios_supports_native_proxy_auth_flow': 'bool',
        'ios_supports_system_auth': 'bool',
        'ipad_app_store_id': 'string',
        'iphone_app_store_id': 'string',
        'is_viewer_admin': 'bool',
        'latest_sdk_version': 'Object',
        'link': 'string',
        'logging_token': 'string',
        'login_secret': 'string',
        'logo_url': 'string',
        'migrations': 'map<string, bool>',
        'mobile_profile_section_url': 'string',
        'mobile_web_url': 'string',
        'monthly_active_users': 'string',
        'monthly_active_users_rank': 'unsigned int',
        'name': 'string',
        'namespace': 'string',
        'object_store_urls': 'Object',
        'page_tab_default_name': 'string',
        'page_tab_url': 'string',
        'photo_url': 'string',
        'privacy_policy_url': 'string',
        'profile_section_url': 'string',
        'property_id': 'string',
        'real_time_mode_devices': 'list<string>',
        'restrictions': 'Object',
        'sdk_update_message': 'string',
        'seamless_login': 'int',
        'secure_canvas_url': 'string',
        'secure_page_tab_url': 'string',
        'server_ip_whitelist': 'string',
        'smart_login_bookmark_icon_url': 'string',
        'smart_login_menu_icon_url': 'string',
        'social_discovery': 'unsigned int',
        'subcategory': 'string',
        'supported_platforms': 'list<SupportedPlatforms>',
        'supports_apprequests_fast_app_switch': 'Object',
        'supports_attribution': 'bool',
        'supports_implicit_sdk_logging': 'bool',
        'suppress_native_ios_gdp': 'bool',
        'terms_of_service_url': 'string',
        'url_scheme_suffix': 'string',
        'user_support_email': 'string',
        'user_support_url': 'string',
        'website_url': 'string',
        'weekly_active_users': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['SupportedPlatforms'] = Application.SupportedPlatforms.__dict__.values()
        field_enum_info['AnPlatforms'] = Application.AnPlatforms.__dict__.values()
        field_enum_info['AggregationPeriod'] = Application.AggregationPeriod.__dict__.values()
        field_enum_info['Breakdowns'] = Application.Breakdowns.__dict__.values()
        field_enum_info['Metrics'] = Application.Metrics.__dict__.values()
        field_enum_info['OrderingColumn'] = Application.OrderingColumn.__dict__.values()
        field_enum_info['OrderingType'] = Application.OrderingType.__dict__.values()
        field_enum_info['Platform'] = Application.Platform.__dict__.values()
        field_enum_info['RequestType'] = Application.RequestType.__dict__.values()
        field_enum_info['MutationMethod'] = Application.MutationMethod.__dict__.values()
        field_enum_info['ScoreType'] = Application.ScoreType.__dict__.values()
        field_enum_info['SortOrder'] = Application.SortOrder.__dict__.values()
        field_enum_info['Role'] = Application.Role.__dict__.values()
        return field_enum_info


