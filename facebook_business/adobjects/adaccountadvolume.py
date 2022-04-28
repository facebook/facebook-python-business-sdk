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
        aco_toggle = 'ACO_TOGGLE'
        aggregated_bid_limited = 'AGGREGATED_BID_LIMITED'
        aggregated_budget_limited = 'AGGREGATED_BUDGET_LIMITED'
        aggregated_cost_limited = 'AGGREGATED_COST_LIMITED'
        auction_overlap = 'AUCTION_OVERLAP'
        audience_expansion = 'AUDIENCE_EXPANSION'
        autoflow_opt_in = 'AUTOFLOW_OPT_IN'
        creative_fatigue = 'CREATIVE_FATIGUE'
        creative_limited = 'CREATIVE_LIMITED'
        dead_link = 'DEAD_LINK'
        ecosystem_bid_reduce_l1_cardinality = 'ECOSYSTEM_BID_REDUCE_L1_CARDINALITY'
        fragmentation = 'FRAGMENTATION'
        learning_limited = 'LEARNING_LIMITED'
        syd_test_mode = 'SYD_TEST_MODE'
        top_adsets_with_ads_under_cap = 'TOP_ADSETS_WITH_ADS_UNDER_CAP'
        top_campaigns_with_ads_under_cap = 'TOP_CAMPAIGNS_WITH_ADS_UNDER_CAP'
        uneconomical_ads_throttling = 'UNECONOMICAL_ADS_THROTTLING'
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


