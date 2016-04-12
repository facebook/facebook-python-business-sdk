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

class Ad(
    AbstractCrudObject,
    HasAdLabels,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAd = True
        super(Ad, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        ad_review_feedback = 'ad_review_feedback'
        adlabels = 'adlabels'
        adset = 'adset'
        adset_id = 'adset_id'
        bid_amount = 'bid_amount'
        bid_info = 'bid_info'
        bid_type = 'bid_type'
        campaign = 'campaign'
        campaign_id = 'campaign_id'
        configured_status = 'configured_status'
        conversion_specs = 'conversion_specs'
        created_time = 'created_time'
        creative = 'creative'
        effective_status = 'effective_status'
        id = 'id'
        last_updated_by_app_id = 'last_updated_by_app_id'
        name = 'name'
        recommendations = 'recommendations'
        status = 'status'
        tracking_specs = 'tracking_specs'
        updated_time = 'updated_time'
        date_format = 'date_format'
        display_sequence = 'display_sequence'
        execution_options = 'execution_options'
        redownload = 'redownload'
        filename = 'filename'

    class BidType:
        cpc = 'CPC'
        cpm = 'CPM'
        multi_premium = 'MULTI_PREMIUM'
        absolute_ocpm = 'ABSOLUTE_OCPM'
        cpa = 'CPA'

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
        return 'ads'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
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
            target_class=Ad,
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
            'adlabels': 'list<Object>',
            'adset_id': 'unsigned int',
            'bid_amount': 'int',
            'creative': 'AdCreative',
            'display_sequence': 'unsigned int',
            'execution_options': 'list<execution_options_enum>',
            'name': 'string',
            'redownload': 'bool',
            'status': 'status_enum',
            'tracking_specs': 'Object',
        }
        enums = {
            'execution_options_enum': Ad.ExecutionOptions.__dict__.values(),
            'status_enum': Ad.Status.__dict__.values(),
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

    def get_keyword_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adkeywordstats import AdKeywordStats
        self.assure_call()
        param_types = {
            'date': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/keywordstats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdKeywordStats,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdKeywordStats),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_leads(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.lead import Lead
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Lead,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Lead),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_previews(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adpreview import AdPreview
        self.assure_call()
        param_types = {
            'ad_format': 'ad_format_enum',
            'height': 'unsigned int',
            'locale': 'string',
            'post': 'Object',
            'product_item_ids': 'list<int>',
            'width': 'unsigned int',
        }
        enums = {
            'ad_format_enum': AdPreview.AdFormat.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/previews',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPreview,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPreview),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_reach_estimate(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.reachestimate import ReachEstimate
        self.assure_call()
        param_types = {
            'currency': 'string',
            'daily_budget': 'float',
            'optimize_for': 'optimize_for_enum',
        }
        enums = {
            'optimize_for_enum': ReachEstimate.OptimizeFor.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reachestimate',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ReachEstimate,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ReachEstimate),
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
        'ad_review_feedback': 'AdgroupReviewFeedback',
        'adlabels': 'list<AdLabel>',
        'adset': 'AdSet',
        'adset_id': 'string',
        'bid_amount': 'int',
        'bid_info': 'map<string, unsigned int>',
        'bid_type': 'BidType',
        'campaign': 'Campaign',
        'campaign_id': 'string',
        'configured_status': 'ConfiguredStatus',
        'conversion_specs': 'list<ConversionActionQuery>',
        'created_time': 'datetime',
        'creative': 'AdCreative',
        'effective_status': 'EffectiveStatus',
        'id': 'string',
        'last_updated_by_app_id': 'string',
        'name': 'string',
        'recommendations': 'list<AdRecommendation>',
        'status': 'Status',
        'tracking_specs': 'list<ConversionActionQuery>',
        'updated_time': 'datetime',
        'date_format': 'string',
        'display_sequence': 'unsigned int',
        'execution_options': 'ExecutionOptions',
        'redownload': 'bool',
        'filename': 'file'
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BidType'] = Ad.BidType.__dict__.values()
        field_enum_info['ConfiguredStatus'] = Ad.ConfiguredStatus.__dict__.values()
        field_enum_info['EffectiveStatus'] = Ad.EffectiveStatus.__dict__.values()
        field_enum_info['Status'] = Ad.Status.__dict__.values()
        field_enum_info['DatePreset'] = Ad.DatePreset.__dict__.values()
        field_enum_info['ExecutionOptions'] = Ad.ExecutionOptions.__dict__.values()
        field_enum_info['Operator'] = Ad.Operator.__dict__.values()
        return field_enum_info
