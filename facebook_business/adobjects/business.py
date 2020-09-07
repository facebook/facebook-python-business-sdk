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
        admin_required = 'admin_required'
        all_required = 'all_required'
        none = 'none'

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
        health = 'HEALTH'
        luxury = 'LUXURY'
        marketing = 'MARKETING'
        non_profit = 'NON_PROFIT'
        organizations_and_associations = 'ORGANIZATIONS_AND_ASSOCIATIONS'
        other = 'OTHER'
        professional_services = 'PROFESSIONAL_SERVICES'
        restaurant = 'RESTAURANT'
        retail = 'RETAIL'
        technology = 'TECHNOLOGY'
        telecom = 'TELECOM'
        travel = 'TRAVEL'

    class PermittedTasks:
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'
        manage = 'MANAGE'

    class SurveyBusinessType:
        advertiser = 'ADVERTISER'
        agency = 'AGENCY'
        app_developer = 'APP_DEVELOPER'
        publisher = 'PUBLISHER'

    class PagePermittedTasks:
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'
        cashier_role = 'CASHIER_ROLE'
        create_content = 'CREATE_CONTENT'
        manage = 'MANAGE'
        manage_jobs = 'MANAGE_JOBS'
        manage_leads = 'MANAGE_LEADS'
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
            target_class=Business,
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
            'name': 'string',
            'primary_page': 'string',
            'timezone_id': 'unsigned int',
            'two_factor_type': 'two_factor_type_enum',
            'vertical': 'vertical_enum',
        }
        enums = {
            'two_factor_type_enum': Business.TwoFactorType.__dict__.values(),
            'vertical_enum': Business.Vertical.__dict__.values(),
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_access_token(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'app_id': 'string',
            'scope': 'list<Permission>',
            'system_user_name': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_studies(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ad_study(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adstudy import AdStudy
        param_types = {
            'cells': 'list<Object>',
            'client_business': 'string',
            'confidence_level': 'float',
            'cooldown_start_time': 'int',
            'description': 'string',
            'end_time': 'int',
            'name': 'string',
            'objectives': 'list<Object>',
            'observation_end_time': 'int',
            'start_time': 'int',
            'type': 'type_enum',
            'viewers': 'list<int>',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ad_account(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
            'ad_account_created_from_bm_flag': 'bool',
            'currency': 'string',
            'end_advertiser': 'Object',
            'funding_id': 'string',
            'invoice': 'bool',
            'invoice_group_id': 'string',
            'invoicing_emails': 'list<string>',
            'io': 'bool',
            'media_agency': 'string',
            'name': 'string',
            'partner': 'string',
            'po_number': 'string',
            'timezone_id': 'unsigned int',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_network_analytics(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adnetworkanalyticssyncqueryresult import AdNetworkAnalyticsSyncQueryResult
        param_types = {
            'aggregation_period': 'aggregation_period_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'filters': 'list<map>',
            'limit': 'unsigned int',
            'metrics': 'list<metrics_enum>',
            'ordering_column': 'ordering_column_enum',
            'ordering_type': 'ordering_type_enum',
            'since': 'datetime',
            'until': 'datetime',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ad_network_analytic(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adnetworkanalyticssyncqueryresult import AdNetworkAnalyticsSyncQueryResult
        param_types = {
            'aggregation_period': 'aggregation_period_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'filters': 'list<Object>',
            'limit': 'int',
            'metrics': 'list<metrics_enum>',
            'ordering_column': 'ordering_column_enum',
            'ordering_type': 'ordering_type_enum',
            'since': 'datetime',
            'until': 'datetime',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_network_analytics_results(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ads_pixels(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adspixel import AdsPixel
        param_types = {
            'id_filter': 'string',
            'name_filter': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_ads_pixel(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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

    def get_an_placements(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adplacement import AdPlacement
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/an_placements',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPlacement,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPlacement, api=self._api),
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

    def create_block_list_draft(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_asset_groups(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.businessassetgroup import BusinessAssetGroup
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_asset_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessAssetGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAssetGroup, api=self._api),
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

    def get_business_invoices(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.oracletransaction import OracleTransaction
        param_types = {
            'end_date': 'string',
            'invoice_id': 'unsigned int',
            'issue_end_date': 'string',
            'issue_start_date': 'string',
            'root_id': 'unsigned int',
            'start_date': 'string',
            'type': 'type_enum',
        }
        enums = {
            'type_enum': OracleTransaction.Type.__dict__.values(),
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_units(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_business_unit(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.businessunit import BusinessUnit
        param_types = {
            'business_units': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_users(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_business_user(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_claim_custom_conversion(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_ad_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_client_ad_account(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_apps(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_client_app(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_pages(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_client_page(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_pixels(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_client_product_catalogs(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_clients(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_clients(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/clients',
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

    def get_content_delivery_report(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.contentdeliveryreport import ContentDeliveryReport
        param_types = {
            'end_date': 'datetime',
            'page_id': 'unsigned int',
            'platform': 'platform_enum',
            'position': 'position_enum',
            'start_date': 'datetime',
            'summary': 'bool',
        }
        enums = {
            'platform_enum': ContentDeliveryReport.Platform.__dict__.values(),
            'position_enum': ContentDeliveryReport.Position.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/content_delivery_report',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ContentDeliveryReport,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ContentDeliveryReport, api=self._api),
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

    def create_custom_conversion(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
            'advanced_rule': 'string',
            'custom_event_type': 'custom_event_type_enum',
            'default_conversion_value': 'float',
            'description': 'string',
            'event_source_id': 'string',
            'name': 'string',
            'rule': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_event_source_groups(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_event_source_group(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_extended_credits(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.extendedcredit import ExtendedCredit
        param_types = {
            'order_by_is_owned_credential': 'bool',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_initiated_audience_sharing_requests(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_initiated_sharing_agreements(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_instagram_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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

    def delete_managed_businesses(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'existing_client_business_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/managed_businesses',
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

    def create_managed_business(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'existing_client_business_id': 'string',
            'name': 'string',
            'sales_rep_email': 'string',
            'survey_business_type': 'survey_business_type_enum',
            'survey_num_assets': 'unsigned int',
            'survey_num_people': 'unsigned int',
            'timezone_id': 'unsigned int',
            'vertical': 'vertical_enum',
        }
        enums = {
            'survey_business_type_enum': Business.SurveyBusinessType.__dict__.values(),
            'vertical_enum': Business.Vertical.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/managed_businesses',
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

    def create_move_asset(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'asset_id': 'string',
            'client_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/move_asset',
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

    def get_offline_conversion_data_sets(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_offline_conversion_data_set(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
        param_types = {
            'auto_assign_to_new_accounts_only': 'bool',
            'description': 'string',
            'enable_auto_assign_to_accounts': 'bool',
            'is_mta_use': 'bool',
            'name': 'string',
        }
        enums = {
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_ad_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_owned_ad_account(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_apps(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_owned_app(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_owned_businesses(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'client_id': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_businesses(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'client_user_id': 'int',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_owned_business(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'name': 'string',
            'page_permitted_tasks': 'list<page_permitted_tasks_enum>',
            'sales_rep_email': 'string',
            'shared_page_id': 'string',
            'survey_business_type': 'survey_business_type_enum',
            'survey_num_assets': 'unsigned int',
            'survey_num_people': 'unsigned int',
            'timezone_id': 'unsigned int',
            'vertical': 'vertical_enum',
        }
        enums = {
            'page_permitted_tasks_enum': Business.PagePermittedTasks.__dict__.values(),
            'survey_business_type_enum': Business.SurveyBusinessType.__dict__.values(),
            'vertical_enum': Business.Vertical.__dict__.values(),
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_instagram_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_pages(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_owned_page(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'code': 'string',
            'page_id': 'int',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_pixels(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_owned_product_catalogs(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_owned_product_catalog(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
            'commerce_merchant_settings': 'Object',
            'da_display_settings': 'Object',
            'destination_catalog_settings': 'map',
            'flight_catalog_settings': 'map',
            'name': 'string',
            'onsite_commerce_merchant': 'Object',
            'store_catalog_settings': 'map',
            'vertical': 'vertical_enum',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_pages(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_client_ad_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_client_apps(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_client_pages(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_owned_ad_accounts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.businessadaccountrequest import BusinessAdAccountRequest
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
            target_class=BusinessAdAccountRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessAdAccountRequest, api=self._api),
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

    def get_pending_owned_pages(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_users(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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

    def create_pixel_to(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/pixel_tos',
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

    def get_received_audience_sharing_requests(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_received_sharing_agreements(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.businessagreement import BusinessAgreement
        param_types = {
            'request_status': 'request_status_enum',
            'requesting_business_id': 'string',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_system_users(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_system_user(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.systemuser import SystemUser
        param_types = {
            'name': 'string',
            'role': 'role_enum',
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_third_party_measurement_report_dataset(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.thirdpartymeasurementreportdataset import ThirdPartyMeasurementReportDataset
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/third_party_measurement_report_dataset',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ThirdPartyMeasurementReportDataset,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ThirdPartyMeasurementReportDataset, api=self._api),
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

    def create_upload_event(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.measurementuploadevent import MeasurementUploadEvent
        param_types = {
            'aggregation_level': 'aggregation_level_enum',
            'conversion_end_date': 'string',
            'conversion_start_date': 'string',
            'event_status': 'event_status_enum',
            'lookback_window': 'lookback_window_enum',
            'match_universe': 'match_universe_enum',
            'timezone': 'timezone_enum',
            'upload_tag': 'string',
        }
        enums = {
            'aggregation_level_enum': MeasurementUploadEvent.AggregationLevel.__dict__.values(),
            'event_status_enum': MeasurementUploadEvent.EventStatus.__dict__.values(),
            'lookback_window_enum': MeasurementUploadEvent.LookbackWindow.__dict__.values(),
            'match_universe_enum': MeasurementUploadEvent.MatchUniverse.__dict__.values(),
            'timezone_enum': MeasurementUploadEvent.Timezone.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/upload_event',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MeasurementUploadEvent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MeasurementUploadEvent, api=self._api),
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
        field_enum_info['PermittedTasks'] = Business.PermittedTasks.__dict__.values()
        field_enum_info['SurveyBusinessType'] = Business.SurveyBusinessType.__dict__.values()
        field_enum_info['PagePermittedTasks'] = Business.PagePermittedTasks.__dict__.values()
        return field_enum_info


