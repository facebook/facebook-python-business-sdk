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
from facebookads.adobjects.helpers.adsinsightsmixin import AdsInsightsMixin

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
        account_id = 'account_id'
        account_name = 'account_name'
        action_values = 'action_values'
        actions = 'actions'
        ad_id = 'ad_id'
        ad_name = 'ad_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        age = 'age'
        app_store_clicks = 'app_store_clicks'
        buying_type = 'buying_type'
        call_to_action_clicks = 'call_to_action_clicks'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        canvas_avg_view_percent = 'canvas_avg_view_percent'
        canvas_avg_view_time = 'canvas_avg_view_time'
        clicks = 'clicks'
        cost_per_10_sec_video_view = 'cost_per_10_sec_video_view'
        cost_per_action_type = 'cost_per_action_type'
        cost_per_inline_link_click = 'cost_per_inline_link_click'
        cost_per_inline_post_engagement = 'cost_per_inline_post_engagement'
        cost_per_total_action = 'cost_per_total_action'
        cost_per_unique_action_type = 'cost_per_unique_action_type'
        cost_per_unique_click = 'cost_per_unique_click'
        cost_per_unique_inline_link_click = 'cost_per_unique_inline_link_click'
        country = 'country'
        cpc = 'cpc'
        cpm = 'cpm'
        cpp = 'cpp'
        ctr = 'ctr'
        date_start = 'date_start'
        date_stop = 'date_stop'
        deeplink_clicks = 'deeplink_clicks'
        frequency = 'frequency'
        frequency_value = 'frequency_value'
        gender = 'gender'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        impression_device = 'impression_device'
        impressions = 'impressions'
        inline_link_click_ctr = 'inline_link_click_ctr'
        inline_link_clicks = 'inline_link_clicks'
        inline_post_engagement = 'inline_post_engagement'
        newsfeed_avg_position = 'newsfeed_avg_position'
        newsfeed_clicks = 'newsfeed_clicks'
        newsfeed_impressions = 'newsfeed_impressions'
        objective = 'objective'
        place_page_id = 'place_page_id'
        place_page_name = 'place_page_name'
        placement = 'placement'
        platform_position = 'platform_position'
        product_id = 'product_id'
        publisher_platform = 'publisher_platform'
        reach = 'reach'
        region = 'region'
        relevance_score = 'relevance_score'
        social_clicks = 'social_clicks'
        social_impressions = 'social_impressions'
        social_reach = 'social_reach'
        social_spend = 'social_spend'
        spend = 'spend'
        total_action_value = 'total_action_value'
        total_actions = 'total_actions'
        total_unique_actions = 'total_unique_actions'
        unique_actions = 'unique_actions'
        unique_clicks = 'unique_clicks'
        unique_ctr = 'unique_ctr'
        unique_impressions = 'unique_impressions'
        unique_inline_link_click_ctr = 'unique_inline_link_click_ctr'
        unique_inline_link_clicks = 'unique_inline_link_clicks'
        unique_link_clicks_ctr = 'unique_link_clicks_ctr'
        unique_social_clicks = 'unique_social_clicks'
        unique_social_impressions = 'unique_social_impressions'
        video_10_sec_watched_actions = 'video_10_sec_watched_actions'
        video_15_sec_watched_actions = 'video_15_sec_watched_actions'
        video_30_sec_watched_actions = 'video_30_sec_watched_actions'
        video_avg_pct_watched_actions = 'video_avg_pct_watched_actions'
        video_avg_sec_watched_actions = 'video_avg_sec_watched_actions'
        video_complete_watched_actions = 'video_complete_watched_actions'
        video_p100_watched_actions = 'video_p100_watched_actions'
        video_p25_watched_actions = 'video_p25_watched_actions'
        video_p50_watched_actions = 'video_p50_watched_actions'
        video_p75_watched_actions = 'video_p75_watched_actions'
        video_p95_watched_actions = 'video_p95_watched_actions'
        website_clicks = 'website_clicks'
        website_ctr = 'website_ctr'

    class ActionAttributionWindows:
        value_1d_view = '1d_view'
        value_7d_view = '7d_view'
        value_28d_view = '28d_view'
        value_1d_click = '1d_click'
        value_7d_click = '7d_click'
        value_28d_click = '28d_click'
        value_default = 'default'

    class ActionBreakdowns:
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_target_id = 'action_target_id'
        action_type = 'action_type'
        action_video_sound = 'action_video_sound'
        action_video_type = 'action_video_type'

    class ActionReportTime:
        impression = 'impression'
        conversion = 'conversion'

    class Breakdowns:
        age = 'age'
        country = 'country'
        gender = 'gender'
        frequency_value = 'frequency_value'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        impression_device = 'impression_device'
        place_page_id = 'place_page_id'
        placement = 'placement'
        product_id = 'product_id'
        region = 'region'

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

    class Level:
        ad = 'ad'
        adset = 'adset'
        campaign = 'campaign'
        account = 'account'

    class SummaryActionBreakdowns:
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_target_id = 'action_target_id'
        action_type = 'action_type'
        action_video_sound = 'action_video_sound'
        action_video_type = 'action_video_type'

    class Summary:
        id = 'id'
        account_id = 'account_id'
        async_percent_completion = 'async_percent_completion'
        async_status = 'async_status'
        date_start = 'date_start'
        date_stop = 'date_stop'
        emails = 'emails'
        friendly_name = 'friendly_name'
        is_bookmarked = 'is_bookmarked'
        is_running = 'is_running'
        schedule_id = 'schedule_id'
        time_completed = 'time_completed'
        time_ref = 'time_ref'

    @classmethod
    def get_endpoint(cls):
        return 'insights'

    _field_types = {
        'account_id': 'string',
        'account_name': 'string',
        'action_values': 'list<AdsActionStats>',
        'actions': 'list<AdsActionStats>',
        'ad_id': 'string',
        'ad_name': 'string',
        'adset_id': 'string',
        'adset_name': 'string',
        'age': 'string',
        'app_store_clicks': 'string',
        'buying_type': 'string',
        'call_to_action_clicks': 'string',
        'campaign_id': 'string',
        'campaign_name': 'string',
        'canvas_avg_view_percent': 'float',
        'canvas_avg_view_time': 'float',
        'clicks': 'string',
        'cost_per_10_sec_video_view': 'list<AdsActionStats>',
        'cost_per_action_type': 'list<AdsActionStats>',
        'cost_per_inline_link_click': 'float',
        'cost_per_inline_post_engagement': 'float',
        'cost_per_total_action': 'float',
        'cost_per_unique_action_type': 'list<AdsActionStats>',
        'cost_per_unique_click': 'float',
        'cost_per_unique_inline_link_click': 'float',
        'country': 'string',
        'cpc': 'float',
        'cpm': 'float',
        'cpp': 'float',
        'ctr': 'float',
        'date_start': 'string',
        'date_stop': 'string',
        'deeplink_clicks': 'string',
        'frequency': 'float',
        'frequency_value': 'string',
        'gender': 'string',
        'hourly_stats_aggregated_by_advertiser_time_zone': 'string',
        'hourly_stats_aggregated_by_audience_time_zone': 'string',
        'impression_device': 'string',
        'impressions': 'string',
        'inline_link_click_ctr': 'float',
        'inline_link_clicks': 'string',
        'inline_post_engagement': 'string',
        'newsfeed_avg_position': 'float',
        'newsfeed_clicks': 'string',
        'newsfeed_impressions': 'string',
        'objective': 'string',
        'place_page_id': 'string',
        'place_page_name': 'string',
        'placement': 'string',
        'platform_position': 'string',
        'product_id': 'string',
        'publisher_platform': 'string',
        'reach': 'string',
        'region': 'string',
        'relevance_score': 'AdgroupRelevanceScore',
        'social_clicks': 'string',
        'social_impressions': 'string',
        'social_reach': 'string',
        'social_spend': 'float',
        'spend': 'float',
        'total_action_value': 'float',
        'total_actions': 'string',
        'total_unique_actions': 'string',
        'unique_actions': 'list<AdsActionStats>',
        'unique_clicks': 'string',
        'unique_ctr': 'float',
        'unique_impressions': 'string',
        'unique_inline_link_click_ctr': 'float',
        'unique_inline_link_clicks': 'string',
        'unique_link_clicks_ctr': 'float',
        'unique_social_clicks': 'string',
        'unique_social_impressions': 'string',
        'video_10_sec_watched_actions': 'list<AdsActionStats>',
        'video_15_sec_watched_actions': 'list<AdsActionStats>',
        'video_30_sec_watched_actions': 'list<AdsActionStats>',
        'video_avg_pct_watched_actions': 'list<AdsActionStats>',
        'video_avg_sec_watched_actions': 'list<AdsActionStats>',
        'video_complete_watched_actions': 'list<AdsActionStats>',
        'video_p100_watched_actions': 'list<AdsActionStats>',
        'video_p25_watched_actions': 'list<AdsActionStats>',
        'video_p50_watched_actions': 'list<AdsActionStats>',
        'video_p75_watched_actions': 'list<AdsActionStats>',
        'video_p95_watched_actions': 'list<AdsActionStats>',
        'website_clicks': 'string',
        'website_ctr': 'list<AdsActionStats>',
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
        field_enum_info['Summary'] = AdsInsights.Summary.__dict__.values()
        return field_enum_info
