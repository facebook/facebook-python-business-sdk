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
from facebook_business.adobjects.helpers.businessmixin import BusinessMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class Business(
    BusinessMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusiness = True
        super(Business, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        block_offline_analytics = 'block_offline_analytics'
        created_by = 'created_by'
        created_time = 'created_time'
        extended_updated_time = 'extended_updated_time'
        id = 'id'
        is_hidden = 'is_hidden'
        is_instagram_enabled_in_fb_analytics = 'is_instagram_enabled_in_fb_analytics'
        link = 'link'
        name = 'name'
        payment_account_id = 'payment_account_id'
        primary_page = 'primary_page'
        profile_picture_uri = 'profile_picture_uri'
        timezone_id = 'timezone_id'
        two_factor_type = 'two_factor_type'
        updated_by = 'updated_by'
        updated_time = 'updated_time'
        verification_status = 'verification_status'
        vertical = 'vertical'
        vertical_id = 'vertical_id'

    class TwoFactorType:
        none = 'none'
        admin_required = 'admin_required'
        all_required = 'all_required'

    class Vertical:
        advertising = 'ADVERTISING'
        automotive = 'AUTOMOTIVE'
        consumer_packaged_goods = 'CONSUMER_PACKAGED_GOODS'
        ecommerce = 'ECOMMERCE'
        education = 'EDUCATION'
        energy_and_utilities = 'ENERGY_AND_UTILITIES'
        entertainment_and_media = 'ENTERTAINMENT_AND_MEDIA'
        financial_services = 'FINANCIAL_SERVICES'
        gaming = 'GAMING'
        government_and_politics = 'GOVERNMENT_AND_POLITICS'
        marketing = 'MARKETING'
        organizations_and_associations = 'ORGANIZATIONS_AND_ASSOCIATIONS'
        professional_services = 'PROFESSIONAL_SERVICES'
        retail = 'RETAIL'
        technology = 'TECHNOLOGY'
        telecom = 'TELECOM'
        travel = 'TRAVEL'
        non_profit = 'NON_PROFIT'
        restaurant = 'RESTAURANT'
        health = 'HEALTH'
        luxury = 'LUXURY'
        other = 'OTHER'

    class AccessType:
        owner = 'OWNER'
        agency = 'AGENCY'

    class PermittedTasks:
        manage = 'MANAGE'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class PagePermittedRoles:
        manager = 'MANAGER'
        content_creator = 'CONTENT_CREATOR'
        moderator = 'MODERATOR'
        advertiser = 'ADVERTISER'
        insights_analyst = 'INSIGHTS_ANALYST'

    class SurveyBusinessType:
        agency = 'AGENCY'
        advertiser = 'ADVERTISER'
        app_developer = 'APP_DEVELOPER'
        publisher = 'PUBLISHER'

    class PermittedRoles:
        manager = 'MANAGER'
        content_creator = 'CONTENT_CREATOR'
        moderator = 'MODERATOR'
        advertiser = 'ADVERTISER'
        insights_analyst = 'INSIGHTS_ANALYST'

    class Role:
        finance_editor = 'FINANCE_EDITOR'
        finance_analyst = 'FINANCE_ANALYST'
        ads_rights_reviewer = 'ADS_RIGHTS_REVIEWER'
        admin = 'ADMIN'
        employee = 'EMPLOYEE'
        fb_employee_sales_rep = 'FB_EMPLOYEE_SALES_REP'

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
            target_class=Business,
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
            'name': 'string',
            'vertical': 'vertical_enum',
            'timezone_id': 'unsigned int',
            'primary_page': 'string',
            'two_factor_type': 'two_factor_type_enum',
        }
        enums = {
            'vertical_enum': Business.Vertical.__dict__.values(),
            'two_factor_type_enum': Business.TwoFactorType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Business,
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

    def create_access_token(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_id': 'Object',
            'scope': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/access_token',
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

    def get_ad_monetization_properties(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.admonetizationproperty import AdMonetizationProperty
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ad_monetization_properties',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdMonetizationProperty,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdMonetizationProperty, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_studies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adstudy import AdStudy
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ad_studies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudy,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdStudy, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ad_study(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adstudy import AdStudy
        param_types = {
            'cells': 'list<Object>',
            'objectives': 'list<Object>',
            'end_time': 'int',
            'description': 'string',
            'name': 'string',
            'start_time': 'int',
            'viewers': 'list<int>',
            'cooldown_start_time': 'int',
            'observation_end_time': 'int',
            'confidence_level': 'float',
            'client_business': 'string',
            'type': 'type_enum',
        }
        enums = {
            'type_enum': AdStudy.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/ad_studies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudy,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdStudy, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ad_account(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
            'name': 'string',
            'currency': 'string',
            'timezone_id': 'unsigned int',
            'end_advertiser': 'Object',
            'funding_id': 'string',
            'media_agency': 'string',
            'partner': 'string',
            'invoice': 'bool',
            'po_number': 'string',
            'io': 'bool',
            'billing_address_id': 'Object',
            'sold_to_address_id': 'Object',
            'liable_address_id': 'Object',
            'invoice_group_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adaccount',
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

    def get_ad_account_creation_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountcreationrequest import AdAccountCreationRequest
        param_types = {
            'status': 'list<status_enum>',
        }
        enums = {
            'status_enum': AdAccountCreationRequest.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adaccountcreationrequests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountCreationRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountCreationRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ad_account_creation_request(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountcreationrequest import AdAccountCreationRequest
        param_types = {
            'extended_credit_id': 'Object',
            'ad_accounts_info': 'list<Object>',
            'business_registration': 'file',
            'planning_agency_business_id': 'string',
            'english_legal_entity_name': 'string',
            'legal_entity_name_in_local_language': 'string',
            'chinese_legal_entity_name': 'string',
            'address_in_chinese': 'string',
            'address_in_local_language': 'string',
            'address_in_english': 'Object',
            'official_website_url': 'Object',
            'business_registration_id': 'string',
            'vertical': 'vertical_enum',
            'subvertical': 'subvertical_enum',
            'promotable_page_urls': 'list<Object>',
            'promotable_page_ids': 'list<string>',
            'promotable_app_ids': 'list<string>',
            'promotable_urls': 'list<Object>',
            'contact': 'Object',
            'additional_comment': 'string',
            'is_smb': 'bool',
            'is_test': 'bool',
            'advertiser_business_id': 'string',
        }
        enums = {
            'vertical_enum': AdAccountCreationRequest.Vertical.__dict__.values(),
            'subvertical_enum': AdAccountCreationRequest.Subvertical.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adaccountcreationrequests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountCreationRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountCreationRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adaccount_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adaccounts',
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
            'aggregation_period_enum': AdNetworkAnalyticsSyncQueryResult.AggregationPeriod.__dict__.values(),
            'breakdowns_enum': AdNetworkAnalyticsSyncQueryResult.Breakdowns.__dict__.values(),
            'metrics_enum': AdNetworkAnalyticsSyncQueryResult.Metrics.__dict__.values(),
            'ordering_column_enum': AdNetworkAnalyticsSyncQueryResult.OrderingColumn.__dict__.values(),
            'ordering_type_enum': AdNetworkAnalyticsSyncQueryResult.OrderingType.__dict__.values(),
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
        from facebook_business.adobjects.adnetworkanalyticssyncqueryresult import AdNetworkAnalyticsSyncQueryResult
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
            'aggregation_period_enum': AdNetworkAnalyticsSyncQueryResult.AggregationPeriod.__dict__.values(),
            'breakdowns_enum': AdNetworkAnalyticsSyncQueryResult.Breakdowns.__dict__.values(),
            'metrics_enum': AdNetworkAnalyticsSyncQueryResult.Metrics.__dict__.values(),
            'ordering_column_enum': AdNetworkAnalyticsSyncQueryResult.OrderingColumn.__dict__.values(),
            'ordering_type_enum': AdNetworkAnalyticsSyncQueryResult.OrderingType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adnetworkanalytics',
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

    def get_ad_network_analytics_export(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adnetworkanalyticsasyncqueryexport import AdNetworkAnalyticsAsyncQueryExport
        param_types = {
            'query_ids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adnetworkanalytics_export',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdNetworkAnalyticsAsyncQueryExport,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdNetworkAnalyticsAsyncQueryExport, api=self._api),
        )
        request.add_params(params)
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

    def get_ads_reporting(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adsreportbuilder import AdsReportBuilder
        param_types = {
            'attribution_windows': 'list<attribution_windows_enum>',
            'dimensions': 'list<dimensions_enum>',
            'dimension_groups': 'list<list<businessads_reporting_dimension_groups_enum_param>>',
            'locked_dimensions': 'unsigned int',
            'metrics': 'list<string>',
            'filtering': 'Object',
            'sorting': 'list<map>',
            'date_preset': 'date_preset_enum',
            'time_range': 'Object',
            'default_summary': 'bool',
            'last_report_snapshot_id': 'unsigned int',
            'offset': 'unsigned int',
            'limit': 'int',
            'summary_count': 'bool',
        }
        enums = {
            'attribution_windows_enum': AdsReportBuilder.AttributionWindows.__dict__.values(),
            'dimensions_enum': AdsReportBuilder.Dimensions.__dict__.values(),
            'date_preset_enum': AdsReportBuilder.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads_reporting',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsReportBuilder,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsReportBuilder, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ads_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixel import AdsPixel
        param_types = {
            'name_filter': 'string',
            'id_filter': 'string',
            'sort_by': 'sort_by_enum',
        }
        enums = {
            'sort_by_enum': AdsPixel.SortBy.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adspixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ads_pixel(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixel import AdsPixel
        param_types = {
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adspixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_advertisable_applications(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessadvertisableapplicationsresult import BusinessAdvertisableApplicationsResult
        param_types = {
            'adaccount_id': 'unsigned int',
            'offset': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/advertisable_applications',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAdvertisableApplicationsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAdvertisableApplicationsResult, api=self._api),
        )
        request.add_params(params)
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

    def get_agency_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'agency_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/agency_pages',
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

    def get_an_publisher_block_list_apps(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.apppublisher import AppPublisher
        param_types = {
            'app_ids': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/an_publisher_blocklist_apps',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AppPublisher,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AppPublisher, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_an_publisher_block_list_categories(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.anblockedbicategory import ANBlockedBICategory
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/an_publisher_blocklist_categories',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ANBlockedBICategory,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ANBlockedBICategory, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_an_publisher_block_list_domains(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.webpublisher import WebPublisher
        param_types = {
            'domain_ids': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/an_publisher_blocklist_domains',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=WebPublisher,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=WebPublisher, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_an_publisher_block_list_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pagepublisher import PagePublisher
        param_types = {
            'page_ids': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/an_publisher_blocklist_pages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PagePublisher,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PagePublisher, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_analytics_query(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.analyticsqueryresult import AnalyticsQueryResult
        param_types = {
            'query_ids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/analytics_query',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsQueryResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AnalyticsQueryResult, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_analytics_query_export(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.analyticsqueryexportresult import AnalyticsQueryExportResult
        param_types = {
            'query_ids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/analytics_query_export',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsQueryExportResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AnalyticsQueryExportResult, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_apps(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_id': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/apps',
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

    def create_app(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_id': 'Object',
            'access_type': 'access_type_enum',
        }
        enums = {
            'access_type_enum': Business.AccessType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/apps',
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

    def get_assigned_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
            'user_id': 'int',
            'email': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_ad_accounts',
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

    def get_assigned_ad_images(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adimage import AdImage
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_adimages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdImage,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdImage, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_assigned_custom_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudience import CustomAudience
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_customaudiences',
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

    def get_assigned_monetization_properties(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.admonetizationproperty import AdMonetizationProperty
        param_types = {
            'user_id': 'int',
            'email': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_monetization_properties',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdMonetizationProperty,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdMonetizationProperty, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_assigned_page_photos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.photo import Photo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_pagephotos',
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

    def get_assigned_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'user_id': 'int',
            'email': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_pages',
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

    def get_assigned_product_catalogs(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
            'user_id': 'int',
            'email': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_product_catalogs',
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

    def get_assigned_saved_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.savedaudience import SavedAudience
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_savedaudiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SavedAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SavedAudience, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_big_data_upload(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.bigdatauploadsession import BigDataUploadSession
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/big_data_upload',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BigDataUploadSession,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BigDataUploadSession, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_block_list_draft(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'publisher_urls_file': 'file',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/block_list_drafts',
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

    def get_business_invoices(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.oracletransaction import OracleTransaction
        param_types = {
            'start_date': 'string',
            'end_date': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_invoices',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OracleTransaction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OracleTransaction, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_persona(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesspersona import BusinessPersona
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_persona',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessPersona,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessPersona, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_resource_groups(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessresourcegroup import BusinessResourceGroup
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_resource_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessResourceGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessResourceGroup, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_units(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessunit import BusinessUnit
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_units',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessUnit,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessUnit, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessuser import BusinessUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessUser, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_business_user(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessuser import BusinessUser
        param_types = {
            'email': 'string',
            'role': 'role_enum',
        }
        enums = {
            'role_enum': BusinessUser.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/business_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessUser, api=self._api),
        )
        request.add_params(params)
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

    def create_business_project(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessproject import BusinessProject
        param_types = {
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def get_catalog_segment_producer_tos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessproductcatalogtos import BusinessProductCatalogTOS
        param_types = {
            'catalog_segment_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/catalog_segment_producer_tos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessProductCatalogTOS,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessProductCatalogTOS, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_catalog_segment_producer_to(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'catalog_segment_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/catalog_segment_producer_tos',
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

    def create_claim_custom_conversion(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
            'custom_conversion_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/claim_custom_conversions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomConversion,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomConversion, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_ad_account_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessadaccountrequest import BusinessAdAccountRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_ad_account_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAdAccountRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAdAccountRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_ad_accounts',
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

    def create_client_ad_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adaccount_id': 'string',
            'permitted_tasks': 'list<permitted_tasks_enum>',
        }
        enums = {
            'permitted_tasks_enum': Business.PermittedTasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/client_ad_accounts',
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

    def get_client_apps(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.application import Application
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_apps',
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

    def create_client_app(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/client_apps',
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

    def get_client_leads_access(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pageleadsaccessconfig import PageLeadsAccessConfig
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_leads_access',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageLeadsAccessConfig,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageLeadsAccessConfig, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_objects(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessobject import BusinessObject
        param_types = {
            'type': 'type_enum',
            'owner_biz_id': 'string',
        }
        enums = {
            'type_enum': BusinessObject.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_objects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_page_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesspagerequest import BusinessPageRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_page_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessPageRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessPageRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_pages',
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

    def create_client_page(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'page_id': 'int',
            'permitted_tasks': 'list<permitted_tasks_enum>',
        }
        enums = {
            'permitted_tasks_enum': Business.PermittedTasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/client_pages',
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

    def get_client_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixel import AdsPixel
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_pixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_product_catalogs(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_product_catalogs',
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

    def get_client_publisher_block_lists(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.publisherblocklist import PublisherBlockList
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/client_publisher_block_lists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PublisherBlockList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PublisherBlockList, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_clients(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/clients',
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

    def get_commerce_tos_acceptance(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.commercemerchanttosacceptance import CommerceMerchantTOSAcceptance
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_tos_acceptance',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceMerchantTOSAcceptance,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceMerchantTOSAcceptance, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_custom_conversions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/customconversions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomConversion,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomConversion, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_custom_conversion(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
            'name': 'string',
            'description': 'string',
            'event_source_id': 'string',
            'rule': 'string',
            'default_conversion_value': 'float',
            'custom_event_type': 'custom_event_type_enum',
            'advanced_rule': 'string',
        }
        enums = {
            'custom_event_type_enum': CustomConversion.CustomEventType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/customconversions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomConversion,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomConversion, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_deal_shows_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/deal_shows_pages',
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

    def get_direct_deal_available_advertisers(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.directdealavailableadvertisers import DirectDealAvailableAdvertisers
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/direct_deal_available_advertisers',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DirectDealAvailableAdvertisers,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DirectDealAvailableAdvertisers, api=self._api),
        )
        request.add_params(params)
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
            'status': 'status_enum',
        }
        enums = {
            'status_enum': DirectDeal.Status.__dict__.values(),
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

    def get_direct_debits(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.directdebit import DirectDebit
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/direct_debits',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DirectDebit,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DirectDebit, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_event_source_groups(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.eventsourcegroup import EventSourceGroup
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/event_source_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=EventSourceGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=EventSourceGroup, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_event_source_group(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.eventsourcegroup import EventSourceGroup
        param_types = {
            'event_sources': 'list<string>',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/event_source_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=EventSourceGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=EventSourceGroup, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_extended_credit_applications(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.extendedcreditapplication import ExtendedCreditApplication
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/extendedcreditapplications',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExtendedCreditApplication,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExtendedCreditApplication, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_extended_credits(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.extendedcredit import ExtendedCredit
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/extendedcredits',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExtendedCredit,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExtendedCredit, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_finance_permissions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.financeobject import FinanceObject
        param_types = {
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/finance_permissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FinanceObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=FinanceObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_grp_plans(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
        param_types = {
            'status': 'status_enum',
        }
        enums = {
            'status_enum': ReachFrequencyPrediction.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/grp_plans',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ReachFrequencyPrediction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ReachFrequencyPrediction, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_initiated_audience_sharing_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessassetsharingagreement import BusinessAssetSharingAgreement
        param_types = {
            'recipient_id': 'string',
            'request_status': 'request_status_enum',
        }
        enums = {
            'request_status_enum': BusinessAssetSharingAgreement.RequestStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/initiated_audience_sharing_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAssetSharingAgreement,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAssetSharingAgreement, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_initiated_sharing_agreements(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessagreement import BusinessAgreement
        param_types = {
            'receiving_business_id': 'string',
            'request_status': 'request_status_enum',
        }
        enums = {
            'request_status_enum': BusinessAgreement.RequestStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/initiated_sharing_agreements',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAgreement,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAgreement, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_instagram_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'instagram_account': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/instagram_accounts',
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

    def get_instagram_accounts(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ip_permissions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.ipobject import IPObject
        param_types = {
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ip_permissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=IPObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=IPObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_matched_search_applications(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessmatchedsearchapplicationsedgedata import BusinessMatchedSearchApplicationsEdgeData
        param_types = {
            'app_store': 'app_store_enum',
            'app_store_country': 'string',
            'query_term': 'string',
            'allow_incomplete_app': 'bool',
        }
        enums = {
            'app_store_enum': BusinessMatchedSearchApplicationsEdgeData.AppStore.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/matched_search_applications',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessMatchedSearchApplicationsEdgeData,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessMatchedSearchApplicationsEdgeData, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_measurement_playground(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.measurementplayground import MeasurementPlayground
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/measurement_playground',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MeasurementPlayground,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MeasurementPlayground, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_measurement_reports(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.measurementreport import MeasurementReport
        param_types = {
            'report_type': 'report_type_enum',
            'filters': 'list<Object>',
        }
        enums = {
            'report_type_enum': MeasurementReport.ReportType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/measurement_reports',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MeasurementReport,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MeasurementReport, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_measurement_report(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.measurementreport import MeasurementReport
        param_types = {
            'report_type': 'report_type_enum',
            'metadata': 'string',
        }
        enums = {
            'report_type_enum': MeasurementReport.ReportType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/measurement_reports',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MeasurementReport,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MeasurementReport, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_m_hub_terms_of_service(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.mhubtermsofservice import MHubTermsOfService
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/mhub_terms_of_service',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MHubTermsOfService,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MHubTermsOfService, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_offline_conversion_data_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/offline_conversion_data_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OfflineConversionDataSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineConversionDataSet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_offline_conversion_data_set(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
        param_types = {
            'name': 'string',
            'description': 'string',
            'data_origin': 'data_origin_enum',
            'enable_auto_assign_to_accounts': 'bool',
            'auto_assign_to_new_accounts_only': 'bool',
        }
        enums = {
            'data_origin_enum': OfflineConversionDataSet.DataOrigin.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/offline_conversion_data_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OfflineConversionDataSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineConversionDataSet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_of_f_line_terms_of_service(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.offlinetermsofservice import OfflineTermsOfService
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/offline_terms_of_service',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OfflineTermsOfService,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineTermsOfService, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_order_id_attributions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.orderidattributions import OrderIDAttributions
        param_types = {
            'pixel_id': 'string',
            'app_id': 'string',
            'dataset_id': 'string',
            'since': 'int',
            'until': 'int',
            'simple_attribution': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/order_id_attributions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OrderIDAttributions,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OrderIDAttributions, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_ad_account_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.legacybusinessadaccountrequest import LegacyBusinessAdAccountRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_ad_account_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LegacyBusinessAdAccountRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LegacyBusinessAdAccountRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_ad_accounts',
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

    def create_owned_ad_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adaccount_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/owned_ad_accounts',
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

    def get_owned_apps(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.application import Application
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_apps',
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

    def create_owned_app(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/owned_apps',
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

    def delete_owned_businesses(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'client_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/owned_businesses',
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

    def get_owned_businesses(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'client_user_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_businesses',
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

    def create_owned_business(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'vertical': 'vertical_enum',
            'timezone_id': 'unsigned int',
            'survey_business_type': 'survey_business_type_enum',
            'survey_num_people': 'unsigned int',
            'survey_num_assets': 'unsigned int',
            'sales_rep_email': 'string',
            'shared_page_id': 'Object',
            'page_permitted_roles': 'list<page_permitted_roles_enum>',
        }
        enums = {
            'vertical_enum': Business.Vertical.__dict__.values(),
            'survey_business_type_enum': Business.SurveyBusinessType.__dict__.values(),
            'page_permitted_roles_enum': Business.PagePermittedRoles.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/owned_businesses',
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

    def get_owned_custom_conversions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_custom_conversions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomConversion,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomConversion, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_domains(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.owneddomain import OwnedDomain
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_domains',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OwnedDomain,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OwnedDomain, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_owned_domain(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.owneddomain import OwnedDomain
        param_types = {
            'domain_name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/owned_domains',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OwnedDomain,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OwnedDomain, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_instagram_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.instagramuser import InstagramUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_instagram_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstagramUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstagramUser, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_objects(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessobject import BusinessObject
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': BusinessObject.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_objects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_page_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesspagerequest import BusinessPageRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_page_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessPageRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessPageRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_pages',
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

    def create_owned_page(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'page_id': 'int',
            'ig_password': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/owned_pages',
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

    def get_owned_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixel import AdsPixel
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_pixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_product_catalogs(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_product_catalogs',
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

    def create_owned_product_catalog(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
            'name': 'string',
            'vertical': 'vertical_enum',
            'flight_catalog_settings': 'map',
            'destination_catalog_settings': 'map',
            'da_display_settings': 'Object',
        }
        enums = {
            'vertical_enum': ProductCatalog.Vertical.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/owned_product_catalogs',
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

    def get_owned_publisher_block_lists(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.publisherblocklist import PublisherBlockList
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owned_publisher_block_lists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PublisherBlockList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PublisherBlockList, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_pages(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'page_id': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/pages',
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

    def create_page(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'page_id': 'int',
            'access_type': 'access_type_enum',
            'permitted_roles': 'list<permitted_roles_enum>',
        }
        enums = {
            'access_type_enum': Business.AccessType.__dict__.values(),
            'permitted_roles_enum': Business.PermittedRoles.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/pages',
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

    def get_partner_integrations(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.partnerintegrationlinked import PartnerIntegrationLinked
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/partner_integrations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PartnerIntegrationLinked,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PartnerIntegrationLinked, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_partner_integration(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.partnerintegrationlinked import PartnerIntegrationLinked
        param_types = {
            'external_id': 'string',
            'gtm_account_id': 'string',
            'gtm_container_id': 'string',
            'name': 'string',
            'partner': 'partner_enum',
        }
        enums = {
            'partner_enum': PartnerIntegrationLinked.Partner.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/partner_integrations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PartnerIntegrationLinked,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PartnerIntegrationLinked, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_partner_ad_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'currency': 'string',
            'timezone_id': 'unsigned int',
            'end_advertiser': 'Object',
            'funding_id': 'string',
            'media_agency': 'string',
            'partner': 'string',
            'invoice': 'bool',
            'po_number': 'string',
            'io': 'bool',
            'billing_address_id': 'Object',
            'sold_to_address_id': 'Object',
            'liable_address_id': 'Object',
            'invoice_group_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/partneradaccount',
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

    def get_partners(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/partners',
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

    def get_pending_client_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessadaccountrequest import BusinessAdAccountRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_client_ad_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAdAccountRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAdAccountRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_client_apps(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessapplicationrequest import BusinessApplicationRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_client_apps',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessApplicationRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessApplicationRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_client_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesspagerequest import BusinessPageRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_client_pages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessPageRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessPageRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_owned_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.legacybusinessadaccountrequest import LegacyBusinessAdAccountRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_owned_ad_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LegacyBusinessAdAccountRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LegacyBusinessAdAccountRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_owned_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesspagerequest import BusinessPageRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_owned_pages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessPageRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessPageRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_share_d_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixel import AdsPixel
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_shared_pixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessrolerequest import BusinessRoleRequest
        param_types = {
            'email': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessRoleRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessRoleRequest, api=self._api),
        )
        request.add_params(params)
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

    def get_pixel_tos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesspixeltos import BusinessPixelTOS
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pixel_tos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessPixelTOS,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessPixelTOS, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_product_catalog_tos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessproductcatalogtos import BusinessProductCatalogTOS
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_catalog_tos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessProductCatalogTOS,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessProductCatalogTOS, api=self._api),
        )
        request.add_params(params)
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

    def create_product_catalog(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
            'name': 'string',
            'vertical': 'vertical_enum',
            'flight_catalog_settings': 'map',
            'destination_catalog_settings': 'map',
            'da_display_settings': 'Object',
        }
        enums = {
            'vertical_enum': ProductCatalog.Vertical.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def get_publisher_block_lists(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.publisherblocklist import PublisherBlockList
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/publisher_block_lists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PublisherBlockList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PublisherBlockList, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_received_audience_permissions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.audiencepermission import AudiencePermission
        param_types = {
            'partner_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/received_audience_permissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AudiencePermission,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AudiencePermission, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_received_audience_sharing_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessassetsharingagreement import BusinessAssetSharingAgreement
        param_types = {
            'initiator_id': 'string',
            'request_status': 'request_status_enum',
        }
        enums = {
            'request_status_enum': BusinessAssetSharingAgreement.RequestStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/received_audience_sharing_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAssetSharingAgreement,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAssetSharingAgreement, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_received_inprogress_on_behalf_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessownedobjectonbehalfofrequest import BusinessOwnedObjectOnBehalfOfRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/received_inprogress_onbehalf_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessOwnedObjectOnBehalfOfRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessOwnedObjectOnBehalfOfRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_received_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessrequest import BusinessRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/received_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_received_sharing_agreements(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessagreement import BusinessAgreement
        param_types = {
            'requesting_business_id': 'string',
            'request_status': 'request_status_enum',
        }
        enums = {
            'request_status_enum': BusinessAgreement.RequestStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/received_sharing_agreements',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAgreement,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAgreement, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_sent_inprogress_on_behalf_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessownedobjectonbehalfofrequest import BusinessOwnedObjectOnBehalfOfRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sent_inprogress_onbehalf_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessOwnedObjectOnBehalfOfRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessOwnedObjectOnBehalfOfRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_sent_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessrequest import BusinessRequest
        param_types = {
            'object_type': 'object_type_enum',
        }
        enums = {
            'object_type_enum': BusinessRequest.ObjectType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sent_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessRequest, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_share_d_audience_permissions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.audiencepermission import AudiencePermission
        param_types = {
            'partner_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shared_audience_permissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AudiencePermission,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AudiencePermission, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_share_d_objects(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessobject import BusinessObject
        param_types = {
            'type': 'type_enum',
            'partner_id': 'string',
        }
        enums = {
            'type_enum': BusinessObject.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shared_objects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_simple_attribution_webhook(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.simpleattributionwebhook import SimpleAttributionWebhook
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/simple_attribution_webhook',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SimpleAttributionWebhook,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SimpleAttributionWebhook, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_spaco_data_set_collections(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.spacodsdatacollection import SpacoDsDataCollection
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/spaco_dataset_collections',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SpacoDsDataCollection,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SpacoDsDataCollection, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_spaco_data_set_collection(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.spacodsdatacollection import SpacoDsDataCollection
        param_types = {
            'spaco_data_collections': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/spaco_dataset_collections',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SpacoDsDataCollection,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SpacoDsDataCollection, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_system_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.systemuser import SystemUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/system_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SystemUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SystemUser, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_system_user(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.systemuser import SystemUser
        param_types = {
            'role': 'role_enum',
            'name': 'string',
            'system_user_id': 'int',
        }
        enums = {
            'role_enum': SystemUser.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/system_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SystemUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SystemUser, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_tags(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businesstag import BusinessTag
        param_types = {
            'order': 'order_enum',
        }
        enums = {
            'order_enum': BusinessTag.Order.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tags',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessTag,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessTag, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_user_invitations(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'email': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/user_invitations',
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

    def get_user_invitations(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessrolerequest import BusinessRoleRequest
        param_types = {
            'status': 'status_enum',
            'email': 'string',
        }
        enums = {
            'status_enum': BusinessRoleRequest.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/user_invitations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessRoleRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessRoleRequest, api=self._api),
        )
        request.add_params(params)
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
            'role': 'role_enum',
        }
        enums = {
            'role_enum': Business.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/userpermissions',
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

    def get_video_metrics_report(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.videometricsreport import VideoMetricsReport
        param_types = {
            'start_date': 'Object',
            'end_date': 'Object',
            'upload_date': 'Object',
            'platform': 'platform_enum',
            'type': 'type_enum',
        }
        enums = {
            'platform_enum': VideoMetricsReport.Platform.__dict__.values(),
            'type_enum': VideoMetricsReport.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_metrics_report',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoMetricsReport,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=VideoMetricsReport, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_whats_app_business_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.whatsappbusinessaccount import WhatsAppBusinessAccount
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/whatsapp_business_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=WhatsAppBusinessAccount,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=WhatsAppBusinessAccount, api=self._api),
        )
        request.add_params(params)
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
        'block_offline_analytics': 'bool',
        'created_by': 'Object',
        'created_time': 'datetime',
        'extended_updated_time': 'datetime',
        'id': 'string',
        'is_hidden': 'bool',
        'is_instagram_enabled_in_fb_analytics': 'bool',
        'link': 'string',
        'name': 'string',
        'payment_account_id': 'string',
        'primary_page': 'Page',
        'profile_picture_uri': 'string',
        'timezone_id': 'unsigned int',
        'two_factor_type': 'string',
        'updated_by': 'Object',
        'updated_time': 'datetime',
        'verification_status': 'string',
        'vertical': 'string',
        'vertical_id': 'unsigned int',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['TwoFactorType'] = Business.TwoFactorType.__dict__.values()
        field_enum_info['Vertical'] = Business.Vertical.__dict__.values()
        field_enum_info['AccessType'] = Business.AccessType.__dict__.values()
        field_enum_info['PermittedTasks'] = Business.PermittedTasks.__dict__.values()
        field_enum_info['PagePermittedRoles'] = Business.PagePermittedRoles.__dict__.values()
        field_enum_info['SurveyBusinessType'] = Business.SurveyBusinessType.__dict__.values()
        field_enum_info['PermittedRoles'] = Business.PermittedRoles.__dict__.values()
        field_enum_info['Role'] = Business.Role.__dict__.values()
        return field_enum_info
