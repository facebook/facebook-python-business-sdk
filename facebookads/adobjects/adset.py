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

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker
from facebookads.mixins import HasAdLabels

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdSet(
    AbstractCrudObject,
    HasAdLabels,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdSet = True
        super(AdSet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        adlabels = 'adlabels'
        adset_schedule = 'adset_schedule'
        bid_amount = 'bid_amount'
        bid_info = 'bid_info'
        billing_event = 'billing_event'
        budget_remaining = 'budget_remaining'
        campaign = 'campaign'
        campaign_id = 'campaign_id'
        configured_status = 'configured_status'
        created_time = 'created_time'
        creative_sequence = 'creative_sequence'
        daily_budget = 'daily_budget'
        effective_status = 'effective_status'
        end_time = 'end_time'
        frequency_cap = 'frequency_cap'
        frequency_cap_reset_period = 'frequency_cap_reset_period'
        frequency_control_specs = 'frequency_control_specs'
        id = 'id'
        is_autobid = 'is_autobid'
        lifetime_budget = 'lifetime_budget'
        lifetime_frequency_cap = 'lifetime_frequency_cap'
        lifetime_imps = 'lifetime_imps'
        name = 'name'
        optimization_goal = 'optimization_goal'
        pacing_type = 'pacing_type'
        promoted_object = 'promoted_object'
        recommendations = 'recommendations'
        rf_prediction_id = 'rf_prediction_id'
        rtb_flag = 'rtb_flag'
        start_time = 'start_time'
        status = 'status'
        targeting = 'targeting'
        updated_time = 'updated_time'
        use_new_app_click = 'use_new_app_click'
        daily_imps = 'daily_imps'
        execution_options = 'execution_options'
        redownload = 'redownload'

    class BillingEvent:
        app_installs = 'APP_INSTALLS'
        clicks = 'CLICKS'
        impressions = 'IMPRESSIONS'
        link_clicks = 'LINK_CLICKS'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        video_views = 'VIDEO_VIEWS'

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

    class OptimizationGoal:
        none = 'NONE'
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        clicks = 'CLICKS'
        engaged_users = 'ENGAGED_USERS'
        external = 'EXTERNAL'
        event_responses = 'EVENT_RESPONSES'
        impressions = 'IMPRESSIONS'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        offer_claims = 'OFFER_CLAIMS'
        offsite_conversions = 'OFFSITE_CONVERSIONS'
        page_engagement = 'PAGE_ENGAGEMENT'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        reach = 'REACH'
        social_impressions = 'SOCIAL_IMPRESSIONS'
        video_views = 'VIDEO_VIEWS'

    class Status:
        active = 'ACTIVE'
        paused = 'PAUSED'
        deleted = 'DELETED'
        archived = 'ARCHIVED'

    class DatePreset:
        today = 'today'
        yesterday = 'yesterday'
        last_3_days = 'last_3_days'
        this_week = 'this_week'
        last_week = 'last_week'
        last_7_days = 'last_7_days'
        last_14_days = 'last_14_days'
        last_28_days = 'last_28_days'
        last_30_days = 'last_30_days'
        last_90_days = 'last_90_days'
        this_month = 'this_month'
        last_month = 'last_month'
        this_quarter = 'this_quarter'
        last_3_months = 'last_3_months'
        lifetime = 'lifetime'

    class ExecutionOptions:
        validate_only = 'VALIDATE_ONLY'
        synchronous_ad_review = 'SYNCHRONOUS_AD_REVIEW'
        include_recommendations = 'INCLUDE_RECOMMENDATIONS'

    class Operator:
        all = 'ALL'
        any = 'ANY'

    @classmethod
    def get_endpoint(cls):
        return 'adsets'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_set(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'account_id': 'string',
            'id': 'string',
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

        return request if pending else request.execute()

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
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
            target_class=AdSet,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'account_id': 'string',
            'adlabels': 'list<Object>',
            'adset_schedule': 'list<Object>',
            'bid_amount': 'int',
            'billing_event': 'billing_event_enum',
            'creative_sequence': 'list<string>',
            'daily_budget': 'unsigned int',
            'daily_imps': 'unsigned int',
            'end_time': 'datetime',
            'execution_options': 'list<execution_options_enum>',
            'id': 'string',
            'is_autobid': 'bool',
            'lifetime_budget': 'unsigned int',
            'lifetime_imps': 'unsigned int',
            'name': 'string',
            'optimization_goal': 'optimization_goal_enum',
            'pacing_type': 'list<string>',
            'promoted_object': 'Object',
            'redownload': 'bool',
            'rf_prediction_id': 'string',
            'start_time': 'datetime',
            'status': 'status_enum',
            'targeting': 'Targeting',
        }
        enums = {
            'billing_event_enum': AdSet.BillingEvent.__dict__.values(),
            'execution_options_enum': AdSet.ExecutionOptions.__dict__.values(),
            'optimization_goal_enum': AdSet.OptimizationGoal.__dict__.values(),
            'status_enum': AdSet.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

        return request if pending else request.execute()

    def get_activities(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adactivity import AdActivity
        self.assure_call()
        param_types = {
            'after': 'string',
            'business_id': 'string',
            'category': 'category_enum',
            'limit': 'int',
            'since': 'datetime',
            'uid': 'int',
            'until': 'datetime',
        }
        enums = {
            'category_enum': AdActivity.Category.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/activities',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdActivity,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdActivity),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_creatives(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adcreative import AdCreative
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adcreatives',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdCreative),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def delete_ad_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adlabel import AdLabel
        self.assure_call()
        param_types = {
            'adlabels': 'list<Object>',
            'execution_options': 'list<execution_options_enum>',
            'id': 'string',
        }
        enums = {
            'execution_options_enum': AdLabel.ExecutionOptions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_label(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adlabel import AdLabel
        self.assure_call()
        param_types = {
            'adlabels': 'list<Object>',
            'execution_options': 'list<execution_options_enum>',
            'id': 'string',
        }
        enums = {
            'execution_options_enum': AdLabel.ExecutionOptions.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ads(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.ad import Ad
        self.assure_call()
        param_types = {
            'ad_draft_id': 'string',
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<string>',
            'include_deleted': 'bool',
            'time_range': 'map',
            'updated_since': 'int',
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
            response_parser=ObjectParser(target_class=Ad),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_async_ad_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adasyncrequest import AdAsyncRequest
        self.assure_call()
        param_types = {
            'statuses': 'list<statuses_enum>',
        }
        enums = {
            'statuses_enum': AdAsyncRequest.Statuses.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/asyncadrequests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAsyncRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAsyncRequest),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_insights(self, fields=None, params=None, async=False, batch=None, pending=False):
        from facebookads.adobjects.adsinsights import AdsInsights
        if async:
          return self.get_insights_async(fields, params, batch, pending)
        self.assure_call()
        param_types = {
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'default_summary': 'bool',
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'sort': 'list<string>',
            'summary': 'list<summary_enum>',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'map',
            'time_ranges': 'list<map>',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'summary_enum': AdsInsights.Summary.__dict__.values(),
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
            response_parser=ObjectParser(target_class=AdsInsights),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_insights_async(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adreportrun import AdReportRun
        from facebookads.adobjects.adsinsights import AdsInsights
        self.assure_call()
        param_types = {
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'default_summary': 'bool',
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'sort': 'list<string>',
            'summary': 'list<summary_enum>',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'map',
            'time_ranges': 'list<map>',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'summary_enum': AdsInsights.Summary.__dict__.values(),
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
            response_parser=ObjectParser(target_class=AdReportRun),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_targeting_sentence_lines(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.targetingsentenceline import TargetingSentenceLine
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetingsentencelines',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=TargetingSentenceLine,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=TargetingSentenceLine),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    _field_types = {
        'account_id': 'string',
        'adlabels': 'list<AdLabel>',
        'adset_schedule': 'list<DayPart>',
        'bid_amount': 'unsigned int',
        'bid_info': 'map<string, unsigned int>',
        'billing_event': 'BillingEvent',
        'budget_remaining': 'string',
        'campaign': 'Campaign',
        'campaign_id': 'string',
        'configured_status': 'ConfiguredStatus',
        'created_time': 'datetime',
        'creative_sequence': 'list<string>',
        'daily_budget': 'string',
        'effective_status': 'EffectiveStatus',
        'end_time': 'datetime',
        'frequency_cap': 'unsigned int',
        'frequency_cap_reset_period': 'unsigned int',
        'frequency_control_specs': 'list<Object>',
        'id': 'string',
        'is_autobid': 'bool',
        'lifetime_budget': 'string',
        'lifetime_frequency_cap': 'unsigned int',
        'lifetime_imps': 'int',
        'name': 'string',
        'optimization_goal': 'OptimizationGoal',
        'pacing_type': 'list<string>',
        'promoted_object': 'AdPromotedObject',
        'recommendations': 'list<AdRecommendation>',
        'rf_prediction_id': 'string',
        'rtb_flag': 'bool',
        'start_time': 'datetime',
        'status': 'Status',
        'targeting': 'Targeting',
        'updated_time': 'datetime',
        'use_new_app_click': 'bool',
        'daily_imps': 'unsigned int',
        'execution_options': 'ExecutionOptions',
        'redownload': 'bool',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BillingEvent'] = AdSet.BillingEvent.__dict__.values()
        field_enum_info['ConfiguredStatus'] = AdSet.ConfiguredStatus.__dict__.values()
        field_enum_info['EffectiveStatus'] = AdSet.EffectiveStatus.__dict__.values()
        field_enum_info['OptimizationGoal'] = AdSet.OptimizationGoal.__dict__.values()
        field_enum_info['Status'] = AdSet.Status.__dict__.values()
        field_enum_info['DatePreset'] = AdSet.DatePreset.__dict__.values()
        field_enum_info['ExecutionOptions'] = AdSet.ExecutionOptions.__dict__.values()
        field_enum_info['Operator'] = AdSet.Operator.__dict__.values()
        return field_enum_info
