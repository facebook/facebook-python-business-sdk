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

class AdCampaignActivity(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCampaignActivity = True
        super(AdCampaignActivity, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        auto_create_lookalike_new = 'auto_create_lookalike_new'
        auto_create_lookalike_old = 'auto_create_lookalike_old'
        bid_adjustments_spec_new = 'bid_adjustments_spec_new'
        bid_adjustments_spec_old = 'bid_adjustments_spec_old'
        bid_amount_new = 'bid_amount_new'
        bid_amount_old = 'bid_amount_old'
        bid_constraints_new = 'bid_constraints_new'
        bid_constraints_old = 'bid_constraints_old'
        bid_info_new = 'bid_info_new'
        bid_info_old = 'bid_info_old'
        bid_strategy_new = 'bid_strategy_new'
        bid_strategy_old = 'bid_strategy_old'
        bid_type_new = 'bid_type_new'
        bid_type_old = 'bid_type_old'
        billing_event_new = 'billing_event_new'
        billing_event_old = 'billing_event_old'
        brande_audience_id_new = 'brande_audience_id_new'
        brande_audience_id_old = 'brande_audience_id_old'
        budget_limit_new = 'budget_limit_new'
        budget_limit_old = 'budget_limit_old'
        created_time = 'created_time'
        daily_impressions_new = 'daily_impressions_new'
        daily_impressions_old = 'daily_impressions_old'
        dco_mode_new = 'dco_mode_new'
        dco_mode_old = 'dco_mode_old'
        delivery_behavior_new = 'delivery_behavior_new'
        delivery_behavior_old = 'delivery_behavior_old'
        destination_type_new = 'destination_type_new'
        destination_type_old = 'destination_type_old'
        event_time = 'event_time'
        event_type = 'event_type'
        id = 'id'
        invoicing_limit_new = 'invoicing_limit_new'
        invoicing_limit_old = 'invoicing_limit_old'
        min_spend_target_new = 'min_spend_target_new'
        min_spend_target_old = 'min_spend_target_old'
        name_new = 'name_new'
        name_old = 'name_old'
        optimization_goal_new = 'optimization_goal_new'
        optimization_goal_old = 'optimization_goal_old'
        pacing_type_new = 'pacing_type_new'
        pacing_type_old = 'pacing_type_old'
        run_status_new = 'run_status_new'
        run_status_old = 'run_status_old'
        schedule_new = 'schedule_new'
        schedule_old = 'schedule_old'
        spend_cap_new = 'spend_cap_new'
        spend_cap_old = 'spend_cap_old'
        start_time_new = 'start_time_new'
        start_time_old = 'start_time_old'
        stop_time_new = 'stop_time_new'
        stop_time_old = 'stop_time_old'
        targeting_expansion_new = 'targeting_expansion_new'
        targeting_expansion_old = 'targeting_expansion_old'
        updated_time_new = 'updated_time_new'
        updated_time_old = 'updated_time_old'

    class BidStrategyNew:
        lowest_cost_without_cap = 'LOWEST_COST_WITHOUT_CAP'
        lowest_cost_with_bid_cap = 'LOWEST_COST_WITH_BID_CAP'
        target_cost = 'TARGET_COST'

    class BidStrategyOld:
        lowest_cost_without_cap = 'LOWEST_COST_WITHOUT_CAP'
        lowest_cost_with_bid_cap = 'LOWEST_COST_WITH_BID_CAP'
        target_cost = 'TARGET_COST'

    class BillingEventNew:
        app_installs = 'APP_INSTALLS'
        clicks = 'CLICKS'
        impressions = 'IMPRESSIONS'
        link_clicks = 'LINK_CLICKS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        video_views = 'VIDEO_VIEWS'

    class BillingEventOld:
        app_installs = 'APP_INSTALLS'
        clicks = 'CLICKS'
        impressions = 'IMPRESSIONS'
        link_clicks = 'LINK_CLICKS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        video_views = 'VIDEO_VIEWS'

    class OptimizationGoalNew:
        none = 'NONE'
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        ad_recall_lift = 'AD_RECALL_LIFT'
        clicks = 'CLICKS'
        engaged_users = 'ENGAGED_USERS'
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
        app_downloads = 'APP_DOWNLOADS'
        landing_page_views = 'LANDING_PAGE_VIEWS'
        value = 'VALUE'
        replies = 'REPLIES'

    class OptimizationGoalOld:
        none = 'NONE'
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        ad_recall_lift = 'AD_RECALL_LIFT'
        clicks = 'CLICKS'
        engaged_users = 'ENGAGED_USERS'
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
        app_downloads = 'APP_DOWNLOADS'
        landing_page_views = 'LANDING_PAGE_VIEWS'
        value = 'VALUE'
        replies = 'REPLIES'

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
            target_class=AdCampaignActivity,
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

    _field_types = {
        'auto_create_lookalike_new': 'bool',
        'auto_create_lookalike_old': 'bool',
        'bid_adjustments_spec_new': 'string',
        'bid_adjustments_spec_old': 'string',
        'bid_amount_new': 'int',
        'bid_amount_old': 'int',
        'bid_constraints_new': 'Object',
        'bid_constraints_old': 'Object',
        'bid_info_new': 'list<Object>',
        'bid_info_old': 'list<Object>',
        'bid_strategy_new': 'BidStrategyNew',
        'bid_strategy_old': 'BidStrategyOld',
        'bid_type_new': 'string',
        'bid_type_old': 'string',
        'billing_event_new': 'BillingEventNew',
        'billing_event_old': 'BillingEventOld',
        'brande_audience_id_new': 'string',
        'brande_audience_id_old': 'string',
        'budget_limit_new': 'Object',
        'budget_limit_old': 'Object',
        'created_time': 'datetime',
        'daily_impressions_new': 'int',
        'daily_impressions_old': 'int',
        'dco_mode_new': 'string',
        'dco_mode_old': 'string',
        'delivery_behavior_new': 'string',
        'delivery_behavior_old': 'string',
        'destination_type_new': 'string',
        'destination_type_old': 'string',
        'event_time': 'datetime',
        'event_type': 'string',
        'id': 'string',
        'invoicing_limit_new': 'int',
        'invoicing_limit_old': 'int',
        'min_spend_target_new': 'Object',
        'min_spend_target_old': 'Object',
        'name_new': 'string',
        'name_old': 'string',
        'optimization_goal_new': 'OptimizationGoalNew',
        'optimization_goal_old': 'OptimizationGoalOld',
        'pacing_type_new': 'int',
        'pacing_type_old': 'int',
        'run_status_new': 'string',
        'run_status_old': 'string',
        'schedule_new': 'list<Object>',
        'schedule_old': 'list<Object>',
        'spend_cap_new': 'Object',
        'spend_cap_old': 'Object',
        'start_time_new': 'datetime',
        'start_time_old': 'datetime',
        'stop_time_new': 'datetime',
        'stop_time_old': 'datetime',
        'targeting_expansion_new': 'Object',
        'targeting_expansion_old': 'Object',
        'updated_time_new': 'datetime',
        'updated_time_old': 'datetime',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BidStrategyNew'] = AdCampaignActivity.BidStrategyNew.__dict__.values()
        field_enum_info['BidStrategyOld'] = AdCampaignActivity.BidStrategyOld.__dict__.values()
        field_enum_info['BillingEventNew'] = AdCampaignActivity.BillingEventNew.__dict__.values()
        field_enum_info['BillingEventOld'] = AdCampaignActivity.BillingEventOld.__dict__.values()
        field_enum_info['OptimizationGoalNew'] = AdCampaignActivity.OptimizationGoalNew.__dict__.values()
        field_enum_info['OptimizationGoalOld'] = AdCampaignActivity.OptimizationGoalOld.__dict__.values()
        return field_enum_info


