# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAccountAdVolume(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdAccountAdVolume, self).__init__()
        self._isAdAccountAdVolume = True
        self._api = api

    class Field(AbstractObject.Field):
        actor_id = 'actor_id'
        actor_name = 'actor_name'
        ad_limit_scope_business = 'ad_limit_scope_business'
        ad_limit_scope_business_manager_id = 'ad_limit_scope_business_manager_id'
        ad_limit_set_by_page_admin = 'ad_limit_set_by_page_admin'
        ads_running_or_in_review_count = 'ads_running_or_in_review_count'
        ads_running_or_in_review_count_subject_to_limit_set_by_page = 'ads_running_or_in_review_count_subject_to_limit_set_by_page'
        current_account_ads_running_or_in_review_count = 'current_account_ads_running_or_in_review_count'
        future_limit_activation_date = 'future_limit_activation_date'
        future_limit_on_ads_running_or_in_review = 'future_limit_on_ads_running_or_in_review'
        limit_on_ads_running_or_in_review = 'limit_on_ads_running_or_in_review'
        recommendations = 'recommendations'

    class RecommendationType:
        ab_test = 'AB_TEST'
        aco_toggle = 'ACO_TOGGLE'
        ads_reporting = 'ADS_REPORTING'
        advantage_plus_creative = 'ADVANTAGE_PLUS_CREATIVE'
        ad_objective = 'AD_OBJECTIVE'
        aem_v2_ineligible = 'AEM_V2_INELIGIBLE'
        aggregated_bid_limited = 'AGGREGATED_BID_LIMITED'
        aggregated_budget_limited = 'AGGREGATED_BUDGET_LIMITED'
        aggregated_cost_limited = 'AGGREGATED_COST_LIMITED'
        auction_overlap = 'AUCTION_OVERLAP'
        auction_overlap_consolidation = 'AUCTION_OVERLAP_CONSOLIDATION'
        audience_expansion = 'AUDIENCE_EXPANSION'
        autoflow_opt_in = 'AUTOFLOW_OPT_IN'
        automatic_placements = 'AUTOMATIC_PLACEMENTS'
        auto_bid = 'AUTO_BID'
        broad_targeting = 'BROAD_TARGETING'
        capi = 'CAPI'
        connect_facebook_page_to_instagram = 'CONNECT_FACEBOOK_PAGE_TO_INSTAGRAM'
        connect_facebook_page_to_whatsapp = 'CONNECT_FACEBOOK_PAGE_TO_WHATSAPP'
        cost_goal = 'COST_GOAL'
        cost_goal_budget_limited = 'COST_GOAL_BUDGET_LIMITED'
        cost_goal_cpa_limited = 'COST_GOAL_CPA_LIMITED'
        creative_badge = 'CREATIVE_BADGE'
        creative_fatigue = 'CREATIVE_FATIGUE'
        creative_fatigue_hourly = 'CREATIVE_FATIGUE_HOURLY'
        creative_limited = 'CREATIVE_LIMITED'
        creative_limited_hourly = 'CREATIVE_LIMITED_HOURLY'
        dead_link = 'DEAD_LINK'
        ecosystem_bid_reduce_l1_cardinality = 'ECOSYSTEM_BID_REDUCE_L1_CARDINALITY'
        fragmentation = 'FRAGMENTATION'
        ges_test = 'GES_TEST'
        learning_limited = 'LEARNING_LIMITED'
        low_outcome = 'LOW_OUTCOME'
        mmt_carousel_to_video = 'MMT_CAROUSEL_TO_VIDEO'
        mobile_first_video = 'MOBILE_FIRST_VIDEO'
        multi_text = 'MULTI_TEXT'
        music = 'MUSIC'
        optimal_spend = 'OPTIMAL_SPEND'
        payment_method = 'PAYMENT_METHOD'
        pfr_l1_inline_mmt = 'PFR_L1_INLINE_MMT'
        predictive_creative_limited = 'PREDICTIVE_CREATIVE_LIMITED'
        predictive_creative_limited_hourly = 'PREDICTIVE_CREATIVE_LIMITED_HOURLY'
        revert = 'REVERT'
        scale_good_campaign = 'SCALE_GOOD_CAMPAIGN'
        semantic_based_audience_expansion = 'SEMANTIC_BASED_AUDIENCE_EXPANSION'
        setup_pixel = 'SETUP_PIXEL'
        shops_ads = 'SHOPS_ADS'
        signals_growth_capi = 'SIGNALS_GROWTH_CAPI'
        six_plus_manual_placements = 'SIX_PLUS_MANUAL_PLACEMENTS'
        spend_limit = 'SPEND_LIMIT'
        syd_test_mode = 'SYD_TEST_MODE'
        top_adsets_with_ads_under_cap = 'TOP_ADSETS_WITH_ADS_UNDER_CAP'
        top_campaigns_with_ads_under_cap = 'TOP_CAMPAIGNS_WITH_ADS_UNDER_CAP'
        uneconomical_ads_throttling = 'UNECONOMICAL_ADS_THROTTLING'
        unused_budget = 'UNUSED_BUDGET'
        zero_impression = 'ZERO_IMPRESSION'

    _field_types = {
        'actor_id': 'string',
        'actor_name': 'string',
        'ad_limit_scope_business': 'Business',
        'ad_limit_scope_business_manager_id': 'string',
        'ad_limit_set_by_page_admin': 'unsigned int',
        'ads_running_or_in_review_count': 'unsigned int',
        'ads_running_or_in_review_count_subject_to_limit_set_by_page': 'unsigned int',
        'current_account_ads_running_or_in_review_count': 'unsigned int',
        'future_limit_activation_date': 'string',
        'future_limit_on_ads_running_or_in_review': 'unsigned int',
        'limit_on_ads_running_or_in_review': 'unsigned int',
        'recommendations': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['RecommendationType'] = AdAccountAdVolume.RecommendationType.__dict__.values()
        return field_enum_info


