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
        actions_per_impression = 'actions_per_impression'
        actions_results = 'actions_results'
        activity_recency = 'activity_recency'
        ad_bid_type = 'ad_bid_type'
        ad_bid_value = 'ad_bid_value'
        ad_click_actions = 'ad_click_actions'
        ad_delivery = 'ad_delivery'
        ad_format_asset = 'ad_format_asset'
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
        age = 'age'
        age_targeting = 'age_targeting'
        amount_in_catalog_currency = 'amount_in_catalog_currency'
        app_store_clicks = 'app_store_clicks'
        attention_events_per_impression = 'attention_events_per_impression'
        attention_events_unq_per_reach = 'attention_events_unq_per_reach'
        auction_bid = 'auction_bid'
        auction_competitiveness = 'auction_competitiveness'
        auction_max_competitor_bid = 'auction_max_competitor_bid'
        body_asset = 'body_asset'
        buying_type = 'buying_type'
        call_to_action_asset = 'call_to_action_asset'
        call_to_action_clicks = 'call_to_action_clicks'
        campaign_delivery = 'campaign_delivery'
        campaign_end = 'campaign_end'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        campaign_start = 'campaign_start'
        cancel_subscription_actions = 'cancel_subscription_actions'
        canvas_avg_view_percent = 'canvas_avg_view_percent'
        canvas_avg_view_time = 'canvas_avg_view_time'
        card_views = 'card_views'
        catalog_segment_actions = 'catalog_segment_actions'
        catalog_segment_value_in_catalog_currency = 'catalog_segment_value_in_catalog_currency'
        catalog_segment_value_mobile_purchase_roas = 'catalog_segment_value_mobile_purchase_roas'
        catalog_segment_value_website_purchase_roas = 'catalog_segment_value_website_purchase_roas'
        clicks = 'clicks'
        conditional_time_spent_ms_over_10s_actions = 'conditional_time_spent_ms_over_10s_actions'
        conditional_time_spent_ms_over_15s_actions = 'conditional_time_spent_ms_over_15s_actions'
        conditional_time_spent_ms_over_2s_actions = 'conditional_time_spent_ms_over_2s_actions'
        conditional_time_spent_ms_over_3s_actions = 'conditional_time_spent_ms_over_3s_actions'
        conditional_time_spent_ms_over_6s_actions = 'conditional_time_spent_ms_over_6s_actions'
        contact_actions = 'contact_actions'
        contact_value = 'contact_value'
        conversion_rate_ranking = 'conversion_rate_ranking'
        conversion_values = 'conversion_values'
        conversions = 'conversions'
        cost_per_10_sec_video_view = 'cost_per_10_sec_video_view'
        cost_per_15_sec_video_view = 'cost_per_15_sec_video_view'
        cost_per_2_sec_continuous_video_view = 'cost_per_2_sec_continuous_video_view'
        cost_per_action_result = 'cost_per_action_result'
        cost_per_action_type = 'cost_per_action_type'
        cost_per_ad_click = 'cost_per_ad_click'
        cost_per_completed_video_view = 'cost_per_completed_video_view'
        cost_per_contact = 'cost_per_contact'
        cost_per_conversion = 'cost_per_conversion'
        cost_per_customize_product = 'cost_per_customize_product'
        cost_per_dda_countby_convs = 'cost_per_dda_countby_convs'
        cost_per_donate = 'cost_per_donate'
        cost_per_dwell = 'cost_per_dwell'
        cost_per_dwell_3_sec = 'cost_per_dwell_3_sec'
        cost_per_dwell_5_sec = 'cost_per_dwell_5_sec'
        cost_per_dwell_7_sec = 'cost_per_dwell_7_sec'
        cost_per_estimated_ad_recallers = 'cost_per_estimated_ad_recallers'
        cost_per_find_location = 'cost_per_find_location'
        cost_per_inline_link_click = 'cost_per_inline_link_click'
        cost_per_inline_post_engagement = 'cost_per_inline_post_engagement'
        cost_per_one_thousand_ad_impression = 'cost_per_one_thousand_ad_impression'
        cost_per_outbound_click = 'cost_per_outbound_click'
        cost_per_schedule = 'cost_per_schedule'
        cost_per_start_trial = 'cost_per_start_trial'
        cost_per_submit_application = 'cost_per_submit_application'
        cost_per_subscribe = 'cost_per_subscribe'
        cost_per_thruplay = 'cost_per_thruplay'
        cost_per_total_action = 'cost_per_total_action'
        cost_per_unique_action_type = 'cost_per_unique_action_type'
        cost_per_unique_click = 'cost_per_unique_click'
        cost_per_unique_conversion = 'cost_per_unique_conversion'
        cost_per_unique_inline_link_click = 'cost_per_unique_inline_link_click'
        cost_per_unique_outbound_click = 'cost_per_unique_outbound_click'
        country = 'country'
        cpc = 'cpc'
        cpm = 'cpm'
        cpp = 'cpp'
        created_time = 'created_time'
        creative_fingerprint = 'creative_fingerprint'
        ctr = 'ctr'
        customize_product_actions = 'customize_product_actions'
        customize_product_value = 'customize_product_value'
        date_start = 'date_start'
        date_stop = 'date_stop'
        dda_countby_convs = 'dda_countby_convs'
        deduping_1st_source_ratio = 'deduping_1st_source_ratio'
        deduping_2nd_source_ratio = 'deduping_2nd_source_ratio'
        deduping_3rd_source_ratio = 'deduping_3rd_source_ratio'
        deduping_ratio = 'deduping_ratio'
        deeplink_clicks = 'deeplink_clicks'
        description_asset = 'description_asset'
        device_platform = 'device_platform'
        dma = 'dma'
        donate_actions = 'donate_actions'
        donate_value = 'donate_value'
        dwell_3_sec = 'dwell_3_sec'
        dwell_5_sec = 'dwell_5_sec'
        dwell_7_sec = 'dwell_7_sec'
        dwell_rate = 'dwell_rate'
        earned_impression = 'earned_impression'
        engagement_rate_ranking = 'engagement_rate_ranking'
        estimated_ad_recall_rate = 'estimated_ad_recall_rate'
        estimated_ad_recall_rate_lower_bound = 'estimated_ad_recall_rate_lower_bound'
        estimated_ad_recall_rate_upper_bound = 'estimated_ad_recall_rate_upper_bound'
        estimated_ad_recallers = 'estimated_ad_recallers'
        estimated_ad_recallers_lower_bound = 'estimated_ad_recallers_lower_bound'
        estimated_ad_recallers_upper_bound = 'estimated_ad_recallers_upper_bound'
        find_location_actions = 'find_location_actions'
        find_location_value = 'find_location_value'
        frequency = 'frequency'
        frequency_value = 'frequency_value'
        full_view_impressions = 'full_view_impressions'
        full_view_reach = 'full_view_reach'
        gender = 'gender'
        gender_targeting = 'gender_targeting'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        image_asset = 'image_asset'
        impression_device = 'impression_device'
        impressions = 'impressions'
        impressions_auto_refresh = 'impressions_auto_refresh'
        impressions_gross = 'impressions_gross'
        inline_link_click_ctr = 'inline_link_click_ctr'
        inline_link_clicks = 'inline_link_clicks'
        inline_post_engagement = 'inline_post_engagement'
        instant_experience_clicks_to_open = 'instant_experience_clicks_to_open'
        instant_experience_clicks_to_start = 'instant_experience_clicks_to_start'
        instant_experience_outbound_clicks = 'instant_experience_outbound_clicks'
        interactive_component_tap = 'interactive_component_tap'
        labels = 'labels'
        link_url_asset = 'link_url_asset'
        location = 'location'
        media_asset = 'media_asset'
        mobile_app_purchase_roas = 'mobile_app_purchase_roas'
        newsfeed_avg_position = 'newsfeed_avg_position'
        newsfeed_clicks = 'newsfeed_clicks'
        newsfeed_impressions = 'newsfeed_impressions'
        objective = 'objective'
        optimization_goal = 'optimization_goal'
        outbound_clicks = 'outbound_clicks'
        outbound_clicks_ctr = 'outbound_clicks_ctr'
        performance_indicator = 'performance_indicator'
        place_page_id = 'place_page_id'
        place_page_name = 'place_page_name'
        placement = 'placement'
        platform_position = 'platform_position'
        product_id = 'product_id'
        publisher_platform = 'publisher_platform'
        purchase_roas = 'purchase_roas'
        quality_ranking = 'quality_ranking'
        quality_score_ectr = 'quality_score_ectr'
        quality_score_ecvr = 'quality_score_ecvr'
        quality_score_enfbr = 'quality_score_enfbr'
        quality_score_organic = 'quality_score_organic'
        reach = 'reach'
        recurring_subscription_payment_actions = 'recurring_subscription_payment_actions'
        region = 'region'
        relevance_score = 'relevance_score'
        rule_asset = 'rule_asset'
        schedule_actions = 'schedule_actions'
        schedule_value = 'schedule_value'
        social_spend = 'social_spend'
        spend = 'spend'
        start_trial_actions = 'start_trial_actions'
        start_trial_value = 'start_trial_value'
        submit_application_actions = 'submit_application_actions'
        submit_application_value = 'submit_application_value'
        subscribe_actions = 'subscribe_actions'
        subscribe_value = 'subscribe_value'
        thumb_stops = 'thumb_stops'
        title_asset = 'title_asset'
        today_spend = 'today_spend'
        total_action_value = 'total_action_value'
        total_actions = 'total_actions'
        total_unique_actions = 'total_unique_actions'
        unique_actions = 'unique_actions'
        unique_clicks = 'unique_clicks'
        unique_conversions = 'unique_conversions'
        unique_ctr = 'unique_ctr'
        unique_impressions = 'unique_impressions'
        unique_inline_link_click_ctr = 'unique_inline_link_click_ctr'
        unique_inline_link_clicks = 'unique_inline_link_clicks'
        unique_link_clicks_ctr = 'unique_link_clicks_ctr'
        unique_outbound_clicks = 'unique_outbound_clicks'
        unique_outbound_clicks_ctr = 'unique_outbound_clicks_ctr'
        unique_video_continuous_2_sec_watched_actions = 'unique_video_continuous_2_sec_watched_actions'
        unique_video_view_10_sec = 'unique_video_view_10_sec'
        unique_video_view_15_sec = 'unique_video_view_15_sec'
        updated_time = 'updated_time'
        video_10_sec_watched_actions = 'video_10_sec_watched_actions'
        video_15_sec_watched_actions = 'video_15_sec_watched_actions'
        video_30_sec_watched_actions = 'video_30_sec_watched_actions'
        video_asset = 'video_asset'
        video_avg_time_watched_actions = 'video_avg_time_watched_actions'
        video_complete_watched_actions = 'video_complete_watched_actions'
        video_completed_view_or_15s_passed_actions = 'video_completed_view_or_15s_passed_actions'
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
        website_clicks = 'website_clicks'
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
        value_default = 'default'

    class ActionBreakdowns:
        action_canvas_component_name = 'action_canvas_component_name'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_converted_product_id = 'action_converted_product_id'
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
        action_converted_product_id = 'action_converted_product_id'
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
        'actions_per_impression': 'string',
        'actions_results': 'AdsActionStats',
        'activity_recency': 'string',
        'ad_bid_type': 'string',
        'ad_bid_value': 'string',
        'ad_click_actions': 'list<AdsActionStats>',
        'ad_delivery': 'string',
        'ad_format_asset': 'string',
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
        'age': 'string',
        'age_targeting': 'string',
        'amount_in_catalog_currency': 'list<AdsActionStats>',
        'app_store_clicks': 'string',
        'attention_events_per_impression': 'string',
        'attention_events_unq_per_reach': 'string',
        'auction_bid': 'string',
        'auction_competitiveness': 'string',
        'auction_max_competitor_bid': 'string',
        'body_asset': 'Object',
        'buying_type': 'string',
        'call_to_action_asset': 'Object',
        'call_to_action_clicks': 'string',
        'campaign_delivery': 'string',
        'campaign_end': 'string',
        'campaign_id': 'string',
        'campaign_name': 'string',
        'campaign_start': 'string',
        'cancel_subscription_actions': 'list<AdsActionStats>',
        'canvas_avg_view_percent': 'string',
        'canvas_avg_view_time': 'string',
        'card_views': 'string',
        'catalog_segment_actions': 'list<AdsActionStats>',
        'catalog_segment_value_in_catalog_currency': 'list<AdsActionStats>',
        'catalog_segment_value_mobile_purchase_roas': 'list<AdsActionStats>',
        'catalog_segment_value_website_purchase_roas': 'list<AdsActionStats>',
        'clicks': 'string',
        'conditional_time_spent_ms_over_10s_actions': 'list<AdsActionStats>',
        'conditional_time_spent_ms_over_15s_actions': 'list<AdsActionStats>',
        'conditional_time_spent_ms_over_2s_actions': 'list<AdsActionStats>',
        'conditional_time_spent_ms_over_3s_actions': 'list<AdsActionStats>',
        'conditional_time_spent_ms_over_6s_actions': 'list<AdsActionStats>',
        'contact_actions': 'list<AdsActionStats>',
        'contact_value': 'list<AdsActionStats>',
        'conversion_rate_ranking': 'string',
        'conversion_values': 'list<AdsActionStats>',
        'conversions': 'list<AdsActionStats>',
        'cost_per_10_sec_video_view': 'list<AdsActionStats>',
        'cost_per_15_sec_video_view': 'list<AdsActionStats>',
        'cost_per_2_sec_continuous_video_view': 'list<AdsActionStats>',
        'cost_per_action_result': 'AdsActionStats',
        'cost_per_action_type': 'list<AdsActionStats>',
        'cost_per_ad_click': 'list<AdsActionStats>',
        'cost_per_completed_video_view': 'list<AdsActionStats>',
        'cost_per_contact': 'list<AdsActionStats>',
        'cost_per_conversion': 'list<AdsActionStats>',
        'cost_per_customize_product': 'list<AdsActionStats>',
        'cost_per_dda_countby_convs': 'string',
        'cost_per_donate': 'list<AdsActionStats>',
        'cost_per_dwell': 'string',
        'cost_per_dwell_3_sec': 'string',
        'cost_per_dwell_5_sec': 'string',
        'cost_per_dwell_7_sec': 'string',
        'cost_per_estimated_ad_recallers': 'string',
        'cost_per_find_location': 'list<AdsActionStats>',
        'cost_per_inline_link_click': 'string',
        'cost_per_inline_post_engagement': 'string',
        'cost_per_one_thousand_ad_impression': 'list<AdsActionStats>',
        'cost_per_outbound_click': 'list<AdsActionStats>',
        'cost_per_schedule': 'list<AdsActionStats>',
        'cost_per_start_trial': 'list<AdsActionStats>',
        'cost_per_submit_application': 'list<AdsActionStats>',
        'cost_per_subscribe': 'list<AdsActionStats>',
        'cost_per_thruplay': 'list<AdsActionStats>',
        'cost_per_total_action': 'string',
        'cost_per_unique_action_type': 'list<AdsActionStats>',
        'cost_per_unique_click': 'string',
        'cost_per_unique_conversion': 'list<AdsActionStats>',
        'cost_per_unique_inline_link_click': 'string',
        'cost_per_unique_outbound_click': 'list<AdsActionStats>',
        'country': 'string',
        'cpc': 'string',
        'cpm': 'string',
        'cpp': 'string',
        'created_time': 'string',
        'creative_fingerprint': 'string',
        'ctr': 'string',
        'customize_product_actions': 'list<AdsActionStats>',
        'customize_product_value': 'list<AdsActionStats>',
        'date_start': 'string',
        'date_stop': 'string',
        'dda_countby_convs': 'string',
        'deduping_1st_source_ratio': 'string',
        'deduping_2nd_source_ratio': 'string',
        'deduping_3rd_source_ratio': 'string',
        'deduping_ratio': 'string',
        'deeplink_clicks': 'string',
        'description_asset': 'Object',
        'device_platform': 'string',
        'dma': 'string',
        'donate_actions': 'list<AdsActionStats>',
        'donate_value': 'list<AdsActionStats>',
        'dwell_3_sec': 'string',
        'dwell_5_sec': 'string',
        'dwell_7_sec': 'string',
        'dwell_rate': 'string',
        'earned_impression': 'string',
        'engagement_rate_ranking': 'string',
        'estimated_ad_recall_rate': 'string',
        'estimated_ad_recall_rate_lower_bound': 'string',
        'estimated_ad_recall_rate_upper_bound': 'string',
        'estimated_ad_recallers': 'string',
        'estimated_ad_recallers_lower_bound': 'string',
        'estimated_ad_recallers_upper_bound': 'string',
        'find_location_actions': 'list<AdsActionStats>',
        'find_location_value': 'list<AdsActionStats>',
        'frequency': 'string',
        'frequency_value': 'string',
        'full_view_impressions': 'string',
        'full_view_reach': 'string',
        'gender': 'string',
        'gender_targeting': 'string',
        'hourly_stats_aggregated_by_advertiser_time_zone': 'string',
        'hourly_stats_aggregated_by_audience_time_zone': 'string',
        'image_asset': 'Object',
        'impression_device': 'string',
        'impressions': 'string',
        'impressions_auto_refresh': 'string',
        'impressions_gross': 'string',
        'inline_link_click_ctr': 'string',
        'inline_link_clicks': 'string',
        'inline_post_engagement': 'string',
        'instant_experience_clicks_to_open': 'string',
        'instant_experience_clicks_to_start': 'string',
        'instant_experience_outbound_clicks': 'string',
        'interactive_component_tap': 'list<AdsActionStats>',
        'labels': 'string',
        'link_url_asset': 'Object',
        'location': 'string',
        'media_asset': 'Object',
        'mobile_app_purchase_roas': 'list<AdsActionStats>',
        'newsfeed_avg_position': 'string',
        'newsfeed_clicks': 'string',
        'newsfeed_impressions': 'string',
        'objective': 'string',
        'optimization_goal': 'string',
        'outbound_clicks': 'list<AdsActionStats>',
        'outbound_clicks_ctr': 'list<AdsActionStats>',
        'performance_indicator': 'string',
        'place_page_id': 'string',
        'place_page_name': 'string',
        'placement': 'string',
        'platform_position': 'string',
        'product_id': 'string',
        'publisher_platform': 'string',
        'purchase_roas': 'list<AdsActionStats>',
        'quality_ranking': 'string',
        'quality_score_ectr': 'string',
        'quality_score_ecvr': 'string',
        'quality_score_enfbr': 'string',
        'quality_score_organic': 'string',
        'reach': 'string',
        'recurring_subscription_payment_actions': 'list<AdsActionStats>',
        'region': 'string',
        'relevance_score': 'AdgroupRelevanceScore',
        'rule_asset': 'Object',
        'schedule_actions': 'list<AdsActionStats>',
        'schedule_value': 'list<AdsActionStats>',
        'social_spend': 'string',
        'spend': 'string',
        'start_trial_actions': 'list<AdsActionStats>',
        'start_trial_value': 'list<AdsActionStats>',
        'submit_application_actions': 'list<AdsActionStats>',
        'submit_application_value': 'list<AdsActionStats>',
        'subscribe_actions': 'list<AdsActionStats>',
        'subscribe_value': 'list<AdsActionStats>',
        'thumb_stops': 'string',
        'title_asset': 'Object',
        'today_spend': 'string',
        'total_action_value': 'string',
        'total_actions': 'string',
        'total_unique_actions': 'string',
        'unique_actions': 'list<AdsActionStats>',
        'unique_clicks': 'string',
        'unique_conversions': 'list<AdsActionStats>',
        'unique_ctr': 'string',
        'unique_impressions': 'string',
        'unique_inline_link_click_ctr': 'string',
        'unique_inline_link_clicks': 'string',
        'unique_link_clicks_ctr': 'string',
        'unique_outbound_clicks': 'list<AdsActionStats>',
        'unique_outbound_clicks_ctr': 'list<AdsActionStats>',
        'unique_video_continuous_2_sec_watched_actions': 'list<AdsActionStats>',
        'unique_video_view_10_sec': 'list<AdsActionStats>',
        'unique_video_view_15_sec': 'list<AdsActionStats>',
        'updated_time': 'string',
        'video_10_sec_watched_actions': 'list<AdsActionStats>',
        'video_15_sec_watched_actions': 'list<AdsActionStats>',
        'video_30_sec_watched_actions': 'list<AdsActionStats>',
        'video_asset': 'Object',
        'video_avg_time_watched_actions': 'list<AdsActionStats>',
        'video_complete_watched_actions': 'list<AdsActionStats>',
        'video_completed_view_or_15s_passed_actions': 'list<AdsActionStats>',
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
        'website_clicks': 'string',
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


