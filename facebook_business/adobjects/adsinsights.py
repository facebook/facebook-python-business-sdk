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
from facebook_business.adobjects.helpers.adsinsightsmixin import AdsInsightsMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdsInsights(
    AdsInsightsMixin,
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdsInsights, self).__init__()
        self._isAdsInsights = True
        self._api = api

    class Field(AbstractObject.Field):
        account_currency = 'account_currency'
        account_id = 'account_id'
        account_name = 'account_name'
        action_values = 'action_values'
        actions = 'actions'
        ad_bid_type = 'ad_bid_type'
        ad_bid_value = 'ad_bid_value'
        ad_click_actions = 'ad_click_actions'
        ad_delivery = 'ad_delivery'
        ad_id = 'ad_id'
        ad_impression_actions = 'ad_impression_actions'
        ad_name = 'ad_name'
        adset_bid_type = 'adset_bid_type'
        adset_bid_value = 'adset_bid_value'
        adset_budget_type = 'adset_budget_type'
        adset_budget_value = 'adset_budget_value'
        adset_delivery = 'adset_delivery'
        adset_end = 'adset_end'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        adset_start = 'adset_start'
        age_targeting = 'age_targeting'
        auction_bid = 'auction_bid'
        auction_competitiveness = 'auction_competitiveness'
        auction_max_competitor_bid = 'auction_max_competitor_bid'
        buying_type = 'buying_type'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        canvas_avg_view_percent = 'canvas_avg_view_percent'
        canvas_avg_view_time = 'canvas_avg_view_time'
        catalog_segment_actions = 'catalog_segment_actions'
        catalog_segment_value = 'catalog_segment_value'
        catalog_segment_value_mobile_purchase_roas = 'catalog_segment_value_mobile_purchase_roas'
        catalog_segment_value_omni_purchase_roas = 'catalog_segment_value_omni_purchase_roas'
        catalog_segment_value_website_purchase_roas = 'catalog_segment_value_website_purchase_roas'
        clicks = 'clicks'
        conversion_rate_ranking = 'conversion_rate_ranking'
        conversion_values = 'conversion_values'
        conversions = 'conversions'
        converted_product_quantity = 'converted_product_quantity'
        converted_product_value = 'converted_product_value'
        cost_per_15_sec_video_view = 'cost_per_15_sec_video_view'
        cost_per_2_sec_continuous_video_view = 'cost_per_2_sec_continuous_video_view'
        cost_per_action_type = 'cost_per_action_type'
        cost_per_ad_click = 'cost_per_ad_click'
        cost_per_conversion = 'cost_per_conversion'
        cost_per_dda_countby_convs = 'cost_per_dda_countby_convs'
        cost_per_estimated_ad_recallers = 'cost_per_estimated_ad_recallers'
        cost_per_inline_link_click = 'cost_per_inline_link_click'
        cost_per_inline_post_engagement = 'cost_per_inline_post_engagement'
        cost_per_one_thousand_ad_impression = 'cost_per_one_thousand_ad_impression'
        cost_per_outbound_click = 'cost_per_outbound_click'
        cost_per_store_visit_action = 'cost_per_store_visit_action'
        cost_per_thruplay = 'cost_per_thruplay'
        cost_per_unique_action_type = 'cost_per_unique_action_type'
        cost_per_unique_click = 'cost_per_unique_click'
        cost_per_unique_conversion = 'cost_per_unique_conversion'
        cost_per_unique_inline_link_click = 'cost_per_unique_inline_link_click'
        cost_per_unique_outbound_click = 'cost_per_unique_outbound_click'
        cpc = 'cpc'
        cpm = 'cpm'
        cpp = 'cpp'
        created_time = 'created_time'
        ctr = 'ctr'
        date_start = 'date_start'
        date_stop = 'date_stop'
        dda_countby_convs = 'dda_countby_convs'
        engagement_rate_ranking = 'engagement_rate_ranking'
        estimated_ad_recall_rate = 'estimated_ad_recall_rate'
        estimated_ad_recall_rate_lower_bound = 'estimated_ad_recall_rate_lower_bound'
        estimated_ad_recall_rate_upper_bound = 'estimated_ad_recall_rate_upper_bound'
        estimated_ad_recallers = 'estimated_ad_recallers'
        estimated_ad_recallers_lower_bound = 'estimated_ad_recallers_lower_bound'
        estimated_ad_recallers_upper_bound = 'estimated_ad_recallers_upper_bound'
        frequency = 'frequency'
        full_view_impressions = 'full_view_impressions'
        full_view_reach = 'full_view_reach'
        gender_targeting = 'gender_targeting'
        impressions = 'impressions'
        inline_link_click_ctr = 'inline_link_click_ctr'
        inline_link_clicks = 'inline_link_clicks'
        inline_post_engagement = 'inline_post_engagement'
        instant_experience_clicks_to_open = 'instant_experience_clicks_to_open'
        instant_experience_clicks_to_start = 'instant_experience_clicks_to_start'
        instant_experience_outbound_clicks = 'instant_experience_outbound_clicks'
        interactive_component_tap = 'interactive_component_tap'
        labels = 'labels'
        location = 'location'
        mobile_app_purchase_roas = 'mobile_app_purchase_roas'
        objective = 'objective'
        outbound_clicks = 'outbound_clicks'
        outbound_clicks_ctr = 'outbound_clicks_ctr'
        place_page_name = 'place_page_name'
        purchase_roas = 'purchase_roas'
        qualifying_question_qualify_answer_rate = 'qualifying_question_qualify_answer_rate'
        quality_ranking = 'quality_ranking'
        quality_score_ectr = 'quality_score_ectr'
        quality_score_ecvr = 'quality_score_ecvr'
        quality_score_organic = 'quality_score_organic'
        reach = 'reach'
        social_spend = 'social_spend'
        spend = 'spend'
        store_visit_actions = 'store_visit_actions'
        unique_actions = 'unique_actions'
        unique_clicks = 'unique_clicks'
        unique_conversions = 'unique_conversions'
        unique_ctr = 'unique_ctr'
        unique_inline_link_click_ctr = 'unique_inline_link_click_ctr'
        unique_inline_link_clicks = 'unique_inline_link_clicks'
        unique_link_clicks_ctr = 'unique_link_clicks_ctr'
        unique_outbound_clicks = 'unique_outbound_clicks'
        unique_outbound_clicks_ctr = 'unique_outbound_clicks_ctr'
        unique_video_continuous_2_sec_watched_actions = 'unique_video_continuous_2_sec_watched_actions'
        unique_video_view_15_sec = 'unique_video_view_15_sec'
        updated_time = 'updated_time'
        video_15_sec_watched_actions = 'video_15_sec_watched_actions'
        video_30_sec_watched_actions = 'video_30_sec_watched_actions'
        video_avg_time_watched_actions = 'video_avg_time_watched_actions'
        video_continuous_2_sec_watched_actions = 'video_continuous_2_sec_watched_actions'
        video_p100_watched_actions = 'video_p100_watched_actions'
        video_p25_watched_actions = 'video_p25_watched_actions'
        video_p50_watched_actions = 'video_p50_watched_actions'
        video_p75_watched_actions = 'video_p75_watched_actions'
        video_p95_watched_actions = 'video_p95_watched_actions'
        video_play_actions = 'video_play_actions'
        video_play_curve_actions = 'video_play_curve_actions'
        video_play_retention_0_to_15s_actions = 'video_play_retention_0_to_15s_actions'
        video_play_retention_20_to_60s_actions = 'video_play_retention_20_to_60s_actions'
        video_play_retention_graph_actions = 'video_play_retention_graph_actions'
        video_thruplay_watched_actions = 'video_thruplay_watched_actions'
        video_time_watched_actions = 'video_time_watched_actions'
        website_ctr = 'website_ctr'
        website_purchase_roas = 'website_purchase_roas'
        wish_bid = 'wish_bid'

    class ActionAttributionWindows:
        value_1d_click = '1d_click'
        value_1d_view = '1d_view'
        value_28d_click = '28d_click'
        value_28d_view = '28d_view'
        value_7d_click = '7d_click'
        value_7d_view = '7d_view'
        dda = 'dda'
        value_default = 'default'

    class ActionBreakdowns:
        action_canvas_component_name = 'action_canvas_component_name'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_reaction = 'action_reaction'
        action_target_id = 'action_target_id'
        action_type = 'action_type'
        action_video_sound = 'action_video_sound'
        action_video_type = 'action_video_type'

    class ActionReportTime:
        conversion = 'conversion'
        impression = 'impression'

    class Breakdowns:
        ad_format_asset = 'ad_format_asset'
        age = 'age'
        body_asset = 'body_asset'
        call_to_action_asset = 'call_to_action_asset'
        country = 'country'
        description_asset = 'description_asset'
        device_platform = 'device_platform'
        dma = 'dma'
        frequency_value = 'frequency_value'
        gender = 'gender'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        image_asset = 'image_asset'
        impression_device = 'impression_device'
        link_url_asset = 'link_url_asset'
        place_page_id = 'place_page_id'
        platform_position = 'platform_position'
        product_id = 'product_id'
        publisher_platform = 'publisher_platform'
        region = 'region'
        title_asset = 'title_asset'
        video_asset = 'video_asset'

    class DatePreset:
        last_14d = 'last_14d'
        last_28d = 'last_28d'
        last_30d = 'last_30d'
        last_3d = 'last_3d'
        last_7d = 'last_7d'
        last_90d = 'last_90d'
        last_month = 'last_month'
        last_quarter = 'last_quarter'
        last_week_mon_sun = 'last_week_mon_sun'
        last_week_sun_sat = 'last_week_sun_sat'
        last_year = 'last_year'
        lifetime = 'lifetime'
        this_month = 'this_month'
        this_quarter = 'this_quarter'
        this_week_mon_today = 'this_week_mon_today'
        this_week_sun_today = 'this_week_sun_today'
        this_year = 'this_year'
        today = 'today'
        yesterday = 'yesterday'

    class Level:
        account = 'account'
        ad = 'ad'
        adset = 'adset'
        campaign = 'campaign'

    class SummaryActionBreakdowns:
        action_canvas_component_name = 'action_canvas_component_name'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_reaction = 'action_reaction'
        action_target_id = 'action_target_id'
        action_type = 'action_type'
        action_video_sound = 'action_video_sound'
        action_video_type = 'action_video_type'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'insights'

    _field_types = {
        'account_currency': 'string',
        'account_id': 'string',
        'account_name': 'string',
        'action_values': 'list<AdsActionStats>',
        'actions': 'list<AdsActionStats>',
        'ad_bid_type': 'string',
        'ad_bid_value': 'string',
        'ad_click_actions': 'list<AdsActionStats>',
        'ad_delivery': 'string',
        'ad_id': 'string',
        'ad_impression_actions': 'list<AdsActionStats>',
        'ad_name': 'string',
        'adset_bid_type': 'string',
        'adset_bid_value': 'string',
        'adset_budget_type': 'string',
        'adset_budget_value': 'string',
        'adset_delivery': 'string',
        'adset_end': 'string',
        'adset_id': 'string',
        'adset_name': 'string',
        'adset_start': 'string',
        'age_targeting': 'string',
        'auction_bid': 'string',
        'auction_competitiveness': 'string',
        'auction_max_competitor_bid': 'string',
        'buying_type': 'string',
        'campaign_id': 'string',
        'campaign_name': 'string',
        'canvas_avg_view_percent': 'string',
        'canvas_avg_view_time': 'string',
        'catalog_segment_actions': 'list<AdsActionStats>',
        'catalog_segment_value': 'list<AdsActionStats>',
        'catalog_segment_value_mobile_purchase_roas': 'list<AdsActionStats>',
        'catalog_segment_value_omni_purchase_roas': 'list<AdsActionStats>',
        'catalog_segment_value_website_purchase_roas': 'list<AdsActionStats>',
        'clicks': 'string',
        'conversion_rate_ranking': 'string',
        'conversion_values': 'list<AdsActionStats>',
        'conversions': 'list<AdsActionStats>',
        'converted_product_quantity': 'list<AdsActionStats>',
        'converted_product_value': 'list<AdsActionStats>',
        'cost_per_15_sec_video_view': 'list<AdsActionStats>',
        'cost_per_2_sec_continuous_video_view': 'list<AdsActionStats>',
        'cost_per_action_type': 'list<AdsActionStats>',
        'cost_per_ad_click': 'list<AdsActionStats>',
        'cost_per_conversion': 'list<AdsActionStats>',
        'cost_per_dda_countby_convs': 'string',
        'cost_per_estimated_ad_recallers': 'string',
        'cost_per_inline_link_click': 'string',
        'cost_per_inline_post_engagement': 'string',
        'cost_per_one_thousand_ad_impression': 'list<AdsActionStats>',
        'cost_per_outbound_click': 'list<AdsActionStats>',
        'cost_per_store_visit_action': 'list<AdsActionStats>',
        'cost_per_thruplay': 'list<AdsActionStats>',
        'cost_per_unique_action_type': 'list<AdsActionStats>',
        'cost_per_unique_click': 'string',
        'cost_per_unique_conversion': 'list<AdsActionStats>',
        'cost_per_unique_inline_link_click': 'string',
        'cost_per_unique_outbound_click': 'list<AdsActionStats>',
        'cpc': 'string',
        'cpm': 'string',
        'cpp': 'string',
        'created_time': 'string',
        'ctr': 'string',
        'date_start': 'string',
        'date_stop': 'string',
        'dda_countby_convs': 'string',
        'engagement_rate_ranking': 'string',
        'estimated_ad_recall_rate': 'string',
        'estimated_ad_recall_rate_lower_bound': 'string',
        'estimated_ad_recall_rate_upper_bound': 'string',
        'estimated_ad_recallers': 'string',
        'estimated_ad_recallers_lower_bound': 'string',
        'estimated_ad_recallers_upper_bound': 'string',
        'frequency': 'string',
        'full_view_impressions': 'string',
        'full_view_reach': 'string',
        'gender_targeting': 'string',
        'impressions': 'string',
        'inline_link_click_ctr': 'string',
        'inline_link_clicks': 'string',
        'inline_post_engagement': 'string',
        'instant_experience_clicks_to_open': 'string',
        'instant_experience_clicks_to_start': 'string',
        'instant_experience_outbound_clicks': 'string',
        'interactive_component_tap': 'list<AdsActionStats>',
        'labels': 'string',
        'location': 'string',
        'mobile_app_purchase_roas': 'list<AdsActionStats>',
        'objective': 'string',
        'outbound_clicks': 'list<AdsActionStats>',
        'outbound_clicks_ctr': 'list<AdsActionStats>',
        'place_page_name': 'string',
        'purchase_roas': 'list<AdsActionStats>',
        'qualifying_question_qualify_answer_rate': 'string',
        'quality_ranking': 'string',
        'quality_score_ectr': 'string',
        'quality_score_ecvr': 'string',
        'quality_score_organic': 'string',
        'reach': 'string',
        'social_spend': 'string',
        'spend': 'string',
        'store_visit_actions': 'list<AdsActionStats>',
        'unique_actions': 'list<AdsActionStats>',
        'unique_clicks': 'string',
        'unique_conversions': 'list<AdsActionStats>',
        'unique_ctr': 'string',
        'unique_inline_link_click_ctr': 'string',
        'unique_inline_link_clicks': 'string',
        'unique_link_clicks_ctr': 'string',
        'unique_outbound_clicks': 'list<AdsActionStats>',
        'unique_outbound_clicks_ctr': 'list<AdsActionStats>',
        'unique_video_continuous_2_sec_watched_actions': 'list<AdsActionStats>',
        'unique_video_view_15_sec': 'list<AdsActionStats>',
        'updated_time': 'string',
        'video_15_sec_watched_actions': 'list<AdsActionStats>',
        'video_30_sec_watched_actions': 'list<AdsActionStats>',
        'video_avg_time_watched_actions': 'list<AdsActionStats>',
        'video_continuous_2_sec_watched_actions': 'list<AdsActionStats>',
        'video_p100_watched_actions': 'list<AdsActionStats>',
        'video_p25_watched_actions': 'list<AdsActionStats>',
        'video_p50_watched_actions': 'list<AdsActionStats>',
        'video_p75_watched_actions': 'list<AdsActionStats>',
        'video_p95_watched_actions': 'list<AdsActionStats>',
        'video_play_actions': 'list<AdsActionStats>',
        'video_play_curve_actions': 'list<Object>',
        'video_play_retention_0_to_15s_actions': 'list<Object>',
        'video_play_retention_20_to_60s_actions': 'list<Object>',
        'video_play_retention_graph_actions': 'list<Object>',
        'video_thruplay_watched_actions': 'list<AdsActionStats>',
        'video_time_watched_actions': 'list<AdsActionStats>',
        'website_ctr': 'list<AdsActionStats>',
        'website_purchase_roas': 'list<AdsActionStats>',
        'wish_bid': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ActionAttributionWindows'] = AdsInsights.ActionAttributionWindows.__dict__.values()
        field_enum_info['ActionBreakdowns'] = AdsInsights.ActionBreakdowns.__dict__.values()
        field_enum_info['ActionReportTime'] = AdsInsights.ActionReportTime.__dict__.values()
        field_enum_info['Breakdowns'] = AdsInsights.Breakdowns.__dict__.values()
        field_enum_info['DatePreset'] = AdsInsights.DatePreset.__dict__.values()
        field_enum_info['Level'] = AdsInsights.Level.__dict__.values()
        field_enum_info['SummaryActionBreakdowns'] = AdsInsights.SummaryActionBreakdowns.__dict__.values()
        return field_enum_info


