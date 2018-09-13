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
from facebook_business.adobjects.helpers.adspixelmixin import AdsPixelMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdsPixel(
    AdsPixelMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsPixel = True
        super(AdsPixel, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        can_proxy = 'can_proxy'
        code = 'code'
        creation_time = 'creation_time'
        creator = 'creator'
        id = 'id'
        is_created_by_business = 'is_created_by_business'
        last_fired_time = 'last_fired_time'
        name = 'name'
        owner_ad_account = 'owner_ad_account'
        owner_business = 'owner_business'

    class SortBy:
        last_fired_time = 'LAST_FIRED_TIME'
        name = 'NAME'

    class Tasks:
        edit = 'EDIT'
        analyze = 'ANALYZE'

    class Type:
        primary = 'PRIMARY'
        secondary = 'SECONDARY'

    class RelationshipType:
        ad_manager = 'AD_MANAGER'
        audience_manager = 'AUDIENCE_MANAGER'
        agency = 'AGENCY'
        other = 'OTHER'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adspixels'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ads_pixel(fields, params, batch, pending)

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
            target_class=AdsPixel,
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
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
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

    def get_ads_pixel_traffic_anomaly_config(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixeltrafficanomalyconfig import AdsPixelTrafficAnomalyConfig
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads_pixel_traffic_anomaly_config',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelTrafficAnomalyConfig,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelTrafficAnomalyConfig, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_analytics_cohort_query(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.analyticscohortqueryresult import AnalyticsCohortQueryResult
        param_types = {
            'query_ids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/analytics_cohort_query',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsCohortQueryResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AnalyticsCohortQueryResult, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_analytics_entity_user_config(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.analyticsentityuserconfig import AnalyticsEntityUserConfig
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/analytics_entity_user_config',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsEntityUserConfig,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AnalyticsEntityUserConfig, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_analytics_event_types(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.analyticseventtypes import AnalyticsEventTypes
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/analytics_event_types',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsEventTypes,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AnalyticsEventTypes, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_analytics_funnel_query(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.analyticsfunnelqueryresult import AnalyticsFunnelQueryResult
        param_types = {
            'query_ids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/analytics_funnel_query',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsFunnelQueryResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AnalyticsFunnelQueryResult, api=self._api),
        )
        request.add_params(params)
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

    def get_analytics_segments(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.analyticssegment import AnalyticsSegment
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/analytics_segments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsSegment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AnalyticsSegment, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_assigned_partners(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_partners',
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

    def delete_assigned_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'business': 'string',
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
            'business': 'string',
        }
        enums = {
            'tasks_enum': AdsPixel.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/assigned_users',
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

    def create_create_server_to_server_key(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/create_server_to_server_keys',
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

    def get_custom_conversions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
            'ad_account': 'string',
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

    def get_da_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.externaleventsourcedastatsresult import ExternalEventSourceDAStatsResult
        param_types = {
            'event': 'event_enum',
        }
        enums = {
            'event_enum': ExternalEventSourceDAStatsResult.Event.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/da_stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExternalEventSourceDAStatsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExternalEventSourceDAStatsResult, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_domain_control_rule(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixeldomaincontrolrule import AdsPixelDomainControlRule
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': AdsPixelDomainControlRule.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/domain_control_rule',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelDomainControlRule,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelDomainControlRule, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_domain_last_fired_time(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixeldomainlastfiredtime import AdsPixelDomainLastFiredTime
        param_types = {
            'domain_name_list': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/domain_last_fired_time',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelDomainLastFiredTime,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelDomainLastFiredTime, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_event_last_fired_time(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixeleventlastfiredtime import AdsPixelEventLastFiredTime
        param_types = {
            'event': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/event_last_fired_time',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelEventLastFiredTime,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelEventLastFiredTime, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_event_prediction(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixeleventprediction import AdsPixelEventPrediction
        param_types = {
            'form_submission': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/event_prediction',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelEventPrediction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelEventPrediction, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_event_rules(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.calibratorexistingrule import CalibratorExistingRule
        param_types = {
            'event_type': 'string',
            'creation_source': 'list<creation_source_enum>',
        }
        enums = {
            'creation_source_enum': CalibratorExistingRule.CreationSource.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/event_rules',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CalibratorExistingRule,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CalibratorExistingRule, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_event_suggestion_rules(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixeleventsuggestionrule import AdsPixelEventSuggestionRule
        param_types = {
            'event_type': 'event_type_enum',
        }
        enums = {
            'event_type_enum': AdsPixelEventSuggestionRule.EventType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/event_suggestion_rules',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelEventSuggestionRule,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelEventSuggestionRule, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_microdata_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixelmicrodatastats import AdsPixelMicrodataStats
        param_types = {
            'catalog_id': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/microdata_stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelMicrodataStats,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelMicrodataStats, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_notification_settings(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.dognotificationsettings import DogNotificationSettings
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/notification_settings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DogNotificationSettings,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DogNotificationSettings, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_pending_share_d_agencies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_shared_agencies',
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

    def get_raw_fires(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixelrawfiresresult import AdsPixelRawFiresResult
        param_types = {
            'event': 'string',
            'filter': 'string',
            'filter_type': 'filter_type_enum',
        }
        enums = {
            'filter_type_enum': AdsPixelRawFiresResult.FilterType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/raw_fires',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelRawFiresResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelRawFiresResult, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_real_time_event_log(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixelrealtimeeventlogresult import AdsPixelRealTimeEventLogResult
        param_types = {
            'start_time': 'Object',
            'end_time': 'Object',
            'limit': 'unsigned int',
            'trace_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/real_time_event_log',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelRealTimeEventLogResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelRealTimeEventLogResult, api=self._api),
        )
        request.add_params(params)
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

    def get_recent_events(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixelrecenteventsresult import AdsPixelRecentEventsResult
        param_types = {
            'event': 'string',
            'lookback_window': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/recent_events',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelRecentEventsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelRecentEventsResult, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_reset_server_to_server_key(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': AdsPixel.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/reset_server_to_server_key',
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

    def get_segments(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adssegments import AdsSegments
        param_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'date_preset': 'string',
            'site_cpm': 'unsigned int',
            'sort': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/segments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsSegments,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsSegments, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_server_to_server_keys(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixelservertoserverkey import AdsPixelServerToServerKey
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/server_to_server_keys',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelServerToServerKey,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelServerToServerKey, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_share_d_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/shared_accounts',
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

    def get_share_d_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shared_accounts',
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

    def create_share_d_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/shared_accounts',
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

    def delete_share_d_agencies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'agency_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/shared_agencies',
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

    def get_share_d_agencies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shared_agencies',
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

    def create_share_d_agency(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'agency_id': 'string',
            'business': 'string',
            'relationship_type': 'list<relationship_type_enum>',
            'other_relationship': 'string',
        }
        enums = {
            'relationship_type_enum': AdsPixel.RelationshipType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/shared_agencies',
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

    def get_signals_iwl_nux(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixelsignalsiwlnux import AdsPixelSignalsIWLNux
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/signals_iwl_nux',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelSignalsIWLNux,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelSignalsIWLNux, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixelstatsresult import AdsPixelStatsResult
        param_types = {
            'start_time': 'Object',
            'end_time': 'Object',
            'aggregation': 'aggregation_enum',
            'event': 'string',
        }
        enums = {
            'aggregation_enum': AdsPixelStatsResult.Aggregation.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelStatsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelStatsResult, api=self._api),
        )
        request.add_params(params)
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
        'can_proxy': 'bool',
        'code': 'string',
        'creation_time': 'datetime',
        'creator': 'User',
        'id': 'string',
        'is_created_by_business': 'bool',
        'last_fired_time': 'datetime',
        'name': 'string',
        'owner_ad_account': 'AdAccount',
        'owner_business': 'Business',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['SortBy'] = AdsPixel.SortBy.__dict__.values()
        field_enum_info['Tasks'] = AdsPixel.Tasks.__dict__.values()
        field_enum_info['Type'] = AdsPixel.Type.__dict__.values()
        field_enum_info['RelationshipType'] = AdsPixel.RelationshipType.__dict__.values()
        return field_enum_info
