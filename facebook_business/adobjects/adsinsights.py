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
        ad_id = 'ad_id'
        ad_name = 'ad_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        buying_type = 'buying_type'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        canvas_avg_view_percent = 'canvas_avg_view_percent'
        canvas_avg_view_time = 'canvas_avg_view_time'
        clicks = 'clicks'
        cost_per_10_sec_video_view = 'cost_per_10_sec_video_view'
        cost_per_action_type = 'cost_per_action_type'
        cost_per_estimated_ad_recallers = 'cost_per_estimated_ad_recallers'
        cost_per_inline_link_click = 'cost_per_inline_link_click'
        cost_per_inline_post_engagement = 'cost_per_inline_post_engagement'
        cost_per_outbound_click = 'cost_per_outbound_click'
        cost_per_unique_action_type = 'cost_per_unique_action_type'
        cost_per_unique_click = 'cost_per_unique_click'
        cost_per_unique_inline_link_click = 'cost_per_unique_inline_link_click'
        cost_per_unique_outbound_click = 'cost_per_unique_outbound_click'
        cpc = 'cpc'
        cpm = 'cpm'
        cpp = 'cpp'
        ctr = 'ctr'
        date_start = 'date_start'
        date_stop = 'date_stop'
        estimated_ad_recall_rate = 'estimated_ad_recall_rate'
        estimated_ad_recallers = 'estimated_ad_recallers'
        frequency = 'frequency'
        impressions = 'impressions'
        inline_link_click_ctr = 'inline_link_click_ctr'
        inline_link_clicks = 'inline_link_clicks'
        inline_post_engagement = 'inline_post_engagement'
        mobile_app_purchase_roas = 'mobile_app_purchase_roas'
        objective = 'objective'
        outbound_clicks = 'outbound_clicks'
        outbound_clicks_ctr = 'outbound_clicks_ctr'
        place_page_name = 'place_page_name'
        reach = 'reach'
        relevance_score = 'relevance_score'
        social_impressions = 'social_impressions'
        social_spend = 'social_spend'
        spend = 'spend'
        total_action_value = 'total_action_value'
        unique_actions = 'unique_actions'
        unique_clicks = 'unique_clicks'
        unique_ctr = 'unique_ctr'
        unique_inline_link_click_ctr = 'unique_inline_link_click_ctr'
        unique_inline_link_clicks = 'unique_inline_link_clicks'
        unique_link_clicks_ctr = 'unique_link_clicks_ctr'
        unique_outbound_clicks = 'unique_outbound_clicks'
        unique_outbound_clicks_ctr = 'unique_outbound_clicks_ctr'
        video_10_sec_watched_actions = 'video_10_sec_watched_actions'
        video_30_sec_watched_actions = 'video_30_sec_watched_actions'
        video_avg_percent_watched_actions = 'video_avg_percent_watched_actions'
        video_avg_time_watched_actions = 'video_avg_time_watched_actions'
        video_p100_watched_actions = 'video_p100_watched_actions'
        video_p25_watched_actions = 'video_p25_watched_actions'
        video_p50_watched_actions = 'video_p50_watched_actions'
        video_p75_watched_actions = 'video_p75_watched_actions'
        video_p95_watched_actions = 'video_p95_watched_actions'
        website_ctr = 'website_ctr'
        website_purchase_roas = 'website_purchase_roas'

    class ActionAttributionWindows:
        value_1d_view = '1d_view'
        value_7d_view = '7d_view'
        value_28d_view = '28d_view'
        value_1d_click = '1d_click'
        value_7d_click = '7d_click'
        value_28d_click = '28d_click'
        value_default = 'default'

    class ActionBreakdowns:
        action_canvas_component_name = 'action_canvas_component_name'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_link_click_destination = 'action_link_click_destination'
        action_reaction = 'action_reaction'
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
        dma = 'dma'
        gender = 'gender'
        frequency_value = 'frequency_value'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        impression_device = 'impression_device'
        place_page_id = 'place_page_id'
        publisher_platform = 'publisher_platform'
        platform_position = 'platform_position'
        device_platform = 'device_platform'
        product_id = 'product_id'
        region = 'region'
        ad_format_asset = 'ad_format_asset'
        body_asset = 'body_asset'
        call_to_action_asset = 'call_to_action_asset'
        description_asset = 'description_asset'
        image_asset = 'image_asset'
        link_url_asset = 'link_url_asset'
        title_asset = 'title_asset'
        video_asset = 'video_asset'

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

    class Level:
        ad = 'ad'
        adset = 'adset'
        campaign = 'campaign'
        account = 'account'

    class SummaryActionBreakdowns:
        action_canvas_component_name = 'action_canvas_component_name'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_link_click_destination = 'action_link_click_destination'
        action_reaction = 'action_reaction'
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
        'ad_id': 'string',
        'ad_name': 'string',
        'adset_id': 'string',
        'adset_name': 'string',
        'buying_type': 'string',
        'campaign_id': 'string',
        'campaign_name': 'string',
        'canvas_avg_view_percent': 'string',
        'canvas_avg_view_time': 'string',
        'clicks': 'string',
        'cost_per_10_sec_video_view': 'list<AdsActionStats>',
        'cost_per_action_type': 'list<AdsActionStats>',
        'cost_per_estimated_ad_recallers': 'string',
        'cost_per_inline_link_click': 'string',
        'cost_per_inline_post_engagement': 'string',
        'cost_per_outbound_click': 'list<AdsActionStats>',
        'cost_per_unique_action_type': 'list<AdsActionStats>',
        'cost_per_unique_click': 'string',
        'cost_per_unique_inline_link_click': 'string',
        'cost_per_unique_outbound_click': 'list<AdsActionStats>',
        'cpc': 'string',
        'cpm': 'string',
        'cpp': 'string',
        'ctr': 'string',
        'date_start': 'string',
        'date_stop': 'string',
        'estimated_ad_recall_rate': 'string',
        'estimated_ad_recallers': 'string',
        'frequency': 'string',
        'impressions': 'string',
        'inline_link_click_ctr': 'string',
        'inline_link_clicks': 'string',
        'inline_post_engagement': 'string',
        'mobile_app_purchase_roas': 'list<AdsActionStats>',
        'objective': 'string',
        'outbound_clicks': 'list<AdsActionStats>',
        'outbound_clicks_ctr': 'list<AdsActionStats>',
        'place_page_name': 'string',
        'reach': 'string',
        'relevance_score': 'AdgroupRelevanceScore',
        'social_impressions': 'string',
        'social_spend': 'string',
        'spend': 'string',
        'total_action_value': 'string',
        'unique_actions': 'list<AdsActionStats>',
        'unique_clicks': 'string',
        'unique_ctr': 'string',
        'unique_inline_link_click_ctr': 'string',
        'unique_inline_link_clicks': 'string',
        'unique_link_clicks_ctr': 'string',
        'unique_outbound_clicks': 'list<AdsActionStats>',
        'unique_outbound_clicks_ctr': 'list<AdsActionStats>',
        'video_10_sec_watched_actions': 'list<AdsActionStats>',
        'video_30_sec_watched_actions': 'list<AdsActionStats>',
        'video_avg_percent_watched_actions': 'list<AdsActionStats>',
        'video_avg_time_watched_actions': 'list<AdsActionStats>',
        'video_p100_watched_actions': 'list<AdsActionStats>',
        'video_p25_watched_actions': 'list<AdsActionStats>',
        'video_p50_watched_actions': 'list<AdsActionStats>',
        'video_p75_watched_actions': 'list<AdsActionStats>',
        'video_p95_watched_actions': 'list<AdsActionStats>',
        'website_ctr': 'list<AdsActionStats>',
        'website_purchase_roas': 'list<AdsActionStats>',
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
