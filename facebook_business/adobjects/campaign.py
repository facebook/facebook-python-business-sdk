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
from facebook_business.mixins import HasAdLabels
from facebook_business.mixins import CanValidate

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class Campaign(
    AbstractCrudObject,
    HasAdLabels,
    CanValidate,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCampaign = True
        super(Campaign, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        adlabels = 'adlabels'
        bid_strategy = 'bid_strategy'
        boosted_object_id = 'boosted_object_id'
        brand_lift_studies = 'brand_lift_studies'
        budget_rebalance_flag = 'budget_rebalance_flag'
        budget_remaining = 'budget_remaining'
        buying_type = 'buying_type'
        can_create_brand_lift_study = 'can_create_brand_lift_study'
        can_use_spend_cap = 'can_use_spend_cap'
        configured_status = 'configured_status'
        created_time = 'created_time'
        daily_budget = 'daily_budget'
        effective_status = 'effective_status'
        id = 'id'
        is_autobid = 'is_autobid'
        is_average_price_pacing = 'is_average_price_pacing'
        kpi_custom_conversion_id = 'kpi_custom_conversion_id'
        kpi_type = 'kpi_type'
        last_budget_toggling_time = 'last_budget_toggling_time'
        lifetime_budget = 'lifetime_budget'
        name = 'name'
        objective = 'objective'
        pacing_type = 'pacing_type'
        promoted_object = 'promoted_object'
        recommendations = 'recommendations'
        source_campaign = 'source_campaign'
        source_campaign_id = 'source_campaign_id'
        spend_cap = 'spend_cap'
        start_time = 'start_time'
        status = 'status'
        stop_time = 'stop_time'
        topline_id = 'topline_id'
        updated_time = 'updated_time'
        adbatch = 'adbatch'
        execution_options = 'execution_options'
        upstream_events = 'upstream_events'
        iterative_split_test_configs = 'iterative_split_test_configs'

    class BidStrategy:
        lowest_cost_without_cap = 'LOWEST_COST_WITHOUT_CAP'
        lowest_cost_with_bid_cap = 'LOWEST_COST_WITH_BID_CAP'
        target_cost = 'TARGET_COST'

    class ConfiguredStatus:
        active = 'ACTIVE'
        paused = 'PAUSED'
        deleted = 'DELETED'
        archived = 'ARCHIVED'

    class EffectiveStatus:
        active = 'ACTIVE'
        paused = 'PAUSED'
        deleted = 'DELETED'
        pending_review = 'PENDING_REVIEW'
        disapproved = 'DISAPPROVED'
        preapproved = 'PREAPPROVED'
        pending_billing_info = 'PENDING_BILLING_INFO'
        campaign_paused = 'CAMPAIGN_PAUSED'
        archived = 'ARCHIVED'
        adset_paused = 'ADSET_PAUSED'

    class Status:
        active = 'ACTIVE'
        paused = 'PAUSED'
        deleted = 'DELETED'
        archived = 'ARCHIVED'

    class DatePreset:
        today = 'today'
        yesterday = 'yesterday'
        this_month = 'this_month'
        last_month = 'last_month'
        this_quarter = 'this_quarter'
        lifetime = 'lifetime'
        last_3d = 'last_3d'
        last_7d = 'last_7d'
        last_14d = 'last_14d'
        last_28d = 'last_28d'
        last_30d = 'last_30d'
        last_90d = 'last_90d'
        last_week_mon_sun = 'last_week_mon_sun'
        last_week_sun_sat = 'last_week_sun_sat'
        last_quarter = 'last_quarter'
        last_year = 'last_year'
        this_week_mon_today = 'this_week_mon_today'
        this_week_sun_today = 'this_week_sun_today'
        this_year = 'this_year'

    class ExecutionOptions:
        validate_only = 'validate_only'
        include_recommendations = 'include_recommendations'

    class Objective:
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        conversions = 'CONVERSIONS'
        event_responses = 'EVENT_RESPONSES'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        local_awareness = 'LOCAL_AWARENESS'
        messages = 'MESSAGES'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        reach = 'REACH'
        video_views = 'VIDEO_VIEWS'

    class Operator:
        all = 'ALL'
        any = 'ANY'

    class StatusOption:
        active = 'ACTIVE'
        paused = 'PAUSED'
        inherited_from_source = 'INHERITED_FROM_SOURCE'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'campaigns'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_campaign(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'date_preset': 'date_preset_enum',
            'from_adtable': 'bool',
            'time_range': 'Object',
        }
        enums = {
            'date_preset_enum': [
                'today',
                'yesterday',
                'this_month',
                'last_month',
                'this_quarter',
                'lifetime',
                'last_3d',
                'last_7d',
                'last_14d',
                'last_28d',
                'last_30d',
                'last_90d',
                'last_week_mon_sun',
                'last_week_sun_sat',
                'last_quarter',
                'last_year',
                'this_week_mon_today',
                'this_week_sun_today',
                'this_year',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
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
            'objective': 'objective_enum',
            'status': 'status_enum',
            'bid_strategy': 'bid_strategy_enum',
            'budget_rebalance_flag': 'bool',
            'daily_budget': 'unsigned int',
            'lifetime_budget': 'unsigned int',
            'pacing_type': 'list<string>',
            'promoted_object': 'Object',
            'spend_cap': 'unsigned int',
            'execution_options': 'list<execution_options_enum>',
            'upstream_events': 'map',
            'adlabels': 'list<Object>',
            'iterative_split_test_configs': 'list<Object>',
            'kpi_custom_conversion_id': 'string',
            'kpi_type': 'Object',
            'is_autobid': 'bool',
            'is_average_price_pacing': 'bool',
        }
        enums = {
            'objective_enum': Campaign.Objective.__dict__.values(),
            'status_enum': Campaign.Status.__dict__.values(),
            'bid_strategy_enum': Campaign.BidStrategy.__dict__.values(),
            'execution_options_enum': Campaign.ExecutionOptions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
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

    def delete_ad_labels(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adlabels': 'list<Object>',
            'execution_options': 'list<execution_options_enum>',
        }
        enums = {
            'execution_options_enum': Campaign.ExecutionOptions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adlabels',
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

    def create_ad_label(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adlabels': 'list<Object>',
            'execution_options': 'list<execution_options_enum>',
        }
        enums = {
            'execution_options_enum': Campaign.ExecutionOptions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.ad import Ad
        param_types = {
            'effective_status': 'list<string>',
            'date_preset': 'date_preset_enum',
            'include_deleted': 'bool',
            'time_range': 'Object',
            'updated_since': 'int',
            'ad_draft_id': 'string',
        }
        enums = {
            'date_preset_enum': Ad.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Ad,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Ad, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adset import AdSet
        param_types = {
            'effective_status': 'list<effective_status_enum>',
            'date_preset': 'date_preset_enum',
            'is_completed': 'bool',
            'time_range': 'Object',
            'ad_draft_id': 'string',
        }
        enums = {
            'effective_status_enum': AdSet.EffectiveStatus.__dict__.values(),
            'date_preset_enum': AdSet.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adsets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdSet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_copies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'effective_status': 'list<effective_status_enum>',
            'date_preset': 'date_preset_enum',
            'is_completed': 'bool',
            'time_range': 'Object',
        }
        enums = {
            'effective_status_enum': Campaign.EffectiveStatus.__dict__.values(),
            'date_preset_enum': Campaign.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/copies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_copy(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'deep_copy': 'bool',
            'rename_options': 'Object',
            'status_option': 'status_option_enum',
            'start_time': 'datetime',
            'end_time': 'datetime',
        }
        enums = {
            'status_option_enum': Campaign.StatusOption.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/copies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign, api=self._api),
        )
        request.add_params(params)
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
        from facebook_business.adobjects.adsinsights import AdsInsights
        if is_async:
          return self.get_insights_async(fields, params, batch, pending)
        param_types = {
            'default_summary': 'bool',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'summary': 'list<string>',
            'sort': 'list<string>',
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'Object',
            'time_ranges': 'list<Object>',
            'use_account_attribution_setting': 'bool',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'level_enum': AdsInsights.Level.__dict__.values(),
            'summary_action_breakdowns_enum': AdsInsights.SummaryActionBreakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsInsights,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsInsights, api=self._api),
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

    def get_insights_async(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adreportrun import AdReportRun
        from facebook_business.adobjects.adsinsights import AdsInsights
        param_types = {
            'default_summary': 'bool',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'summary': 'list<string>',
            'sort': 'list<string>',
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'Object',
            'time_ranges': 'list<Object>',
            'use_account_attribution_setting': 'bool',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'level_enum': AdsInsights.Level.__dict__.values(),
            'summary_action_breakdowns_enum': AdsInsights.SummaryActionBreakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdReportRun,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdReportRun, api=self._api),
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

    _field_types = {
        'account_id': 'string',
        'adlabels': 'list<AdLabel>',
        'bid_strategy': 'BidStrategy',
        'boosted_object_id': 'string',
        'brand_lift_studies': 'list<AdStudy>',
        'budget_rebalance_flag': 'bool',
        'budget_remaining': 'string',
        'buying_type': 'string',
        'can_create_brand_lift_study': 'bool',
        'can_use_spend_cap': 'bool',
        'configured_status': 'ConfiguredStatus',
        'created_time': 'datetime',
        'daily_budget': 'string',
        'effective_status': 'EffectiveStatus',
        'id': 'string',
        'is_autobid': 'bool',
        'is_average_price_pacing': 'bool',
        'kpi_custom_conversion_id': 'string',
        'kpi_type': 'string',
        'last_budget_toggling_time': 'datetime',
        'lifetime_budget': 'string',
        'name': 'string',
        'objective': 'string',
        'pacing_type': 'list<string>',
        'promoted_object': 'AdPromotedObject',
        'recommendations': 'list<AdRecommendation>',
        'source_campaign': 'Campaign',
        'source_campaign_id': 'string',
        'spend_cap': 'string',
        'start_time': 'datetime',
        'status': 'Status',
        'stop_time': 'datetime',
        'topline_id': 'string',
        'updated_time': 'datetime',
        'adbatch': 'list<Object>',
        'execution_options': 'list<ExecutionOptions>',
        'upstream_events': 'map',
        'iterative_split_test_configs': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BidStrategy'] = Campaign.BidStrategy.__dict__.values()
        field_enum_info['ConfiguredStatus'] = Campaign.ConfiguredStatus.__dict__.values()
        field_enum_info['EffectiveStatus'] = Campaign.EffectiveStatus.__dict__.values()
        field_enum_info['Status'] = Campaign.Status.__dict__.values()
        field_enum_info['DatePreset'] = Campaign.DatePreset.__dict__.values()
        field_enum_info['ExecutionOptions'] = Campaign.ExecutionOptions.__dict__.values()
        field_enum_info['Objective'] = Campaign.Objective.__dict__.values()
        field_enum_info['Operator'] = Campaign.Operator.__dict__.values()
        field_enum_info['StatusOption'] = Campaign.StatusOption.__dict__.values()
        return field_enum_info


