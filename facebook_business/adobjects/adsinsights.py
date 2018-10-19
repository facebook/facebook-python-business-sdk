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
from facebook_business.adobjects.helpers.adsinsightsmixin import AdsInsightsMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdsInsights(
    AdsInsightsMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsInsights = True
        super(AdsInsights, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_currency = 'account_currency'
        account_id = 'account_id'
        account_name = 'account_name'
        action_values = 'action_values'
        actions = 'actions'
        activity_recency = 'activity_recency'
        ad_click_actions = 'ad_click_actions'
        ad_format_asset = 'ad_format_asset'
        ad_id = 'ad_id'
        ad_impression_actions = 'ad_impression_actions'
        ad_name = 'ad_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        age = 'age'
        age_targeting = 'age_targeting'
        bid_type = 'bid_type'
        body_asset = 'body_asset'
        buying_type = 'buying_type'
        call_to_action_asset = 'call_to_action_asset'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        canvas_avg_view_percent = 'canvas_avg_view_percent'
        canvas_avg_view_time = 'canvas_avg_view_time'
        canvas_component_avg_pct_view = 'canvas_component_avg_pct_view'
        clicks = 'clicks'
        cost_per_10_sec_video_view = 'cost_per_10_sec_video_view'
        cost_per_15_sec_video_view = 'cost_per_15_sec_video_view'
        cost_per_2_sec_continuous_video_view = 'cost_per_2_sec_continuous_video_view'
        cost_per_action_type = 'cost_per_action_type'
        cost_per_ad_click = 'cost_per_ad_click'
        cost_per_dda_countby_convs = 'cost_per_dda_countby_convs'
        cost_per_estimated_ad_recallers = 'cost_per_estimated_ad_recallers'
        cost_per_inline_link_click = 'cost_per_inline_link_click'
        cost_per_inline_post_engagement = 'cost_per_inline_post_engagement'
        cost_per_one_thousand_ad_impression = 'cost_per_one_thousand_ad_impression'
        cost_per_outbound_click = 'cost_per_outbound_click'
        cost_per_thruplay = 'cost_per_thruplay'
        cost_per_unique_action_type = 'cost_per_unique_action_type'
        cost_per_unique_click = 'cost_per_unique_click'
        cost_per_unique_inline_link_click = 'cost_per_unique_inline_link_click'
        cost_per_unique_outbound_click = 'cost_per_unique_outbound_click'
        country = 'country'
        cpc = 'cpc'
        cpm = 'cpm'
        cpp = 'cpp'
        created_time = 'created_time'
        creative_fingerprint = 'creative_fingerprint'
        ctr = 'ctr'
        date_start = 'date_start'
        date_stop = 'date_stop'
        dda_countby_convs = 'dda_countby_convs'
        description_asset = 'description_asset'
        device_platform = 'device_platform'
        dma = 'dma'
        estimated_ad_recall_rate = 'estimated_ad_recall_rate'
        estimated_ad_recall_rate_lower_bound = 'estimated_ad_recall_rate_lower_bound'
        estimated_ad_recall_rate_upper_bound = 'estimated_ad_recall_rate_upper_bound'
        estimated_ad_recallers = 'estimated_ad_recallers'
        estimated_ad_recallers_lower_bound = 'estimated_ad_recallers_lower_bound'
        estimated_ad_recallers_upper_bound = 'estimated_ad_recallers_upper_bound'
        frequency = 'frequency'
        frequency_value = 'frequency_value'
        gender = 'gender'
        gender_targeting = 'gender_targeting'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        image_asset = 'image_asset'
        impression_device = 'impression_device'
        impressions = 'impressions'
        impressions_dummy = 'impressions_dummy'
        inline_link_click_ctr = 'inline_link_click_ctr'
        inline_link_clicks = 'inline_link_clicks'
        inline_post_engagement = 'inline_post_engagement'
        labels = 'labels'
        link_url_asset = 'link_url_asset'
        location = 'location'
        media_asset = 'media_asset'
        mobile_app_purchase_roas = 'mobile_app_purchase_roas'
        objective = 'objective'
        outbound_clicks = 'outbound_clicks'
        outbound_clicks_ctr = 'outbound_clicks_ctr'
        place_page_id = 'place_page_id'
        place_page_name = 'place_page_name'
        placement = 'placement'
        platform_position = 'platform_position'
        product_format = 'product_format'
        product_id = 'product_id'
        publisher_platform = 'publisher_platform'
        purchasing_interface = 'purchasing_interface'
        reach = 'reach'
        region = 'region'
        relevance_score = 'relevance_score'
        social_spend = 'social_spend'
        spend = 'spend'
        title_asset = 'title_asset'
        total_action_value = 'total_action_value'
        unique_actions = 'unique_actions'
        unique_clicks = 'unique_clicks'
        unique_ctr = 'unique_ctr'
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
        video_avg_percent_watched_actions = 'video_avg_percent_watched_actions'
        video_avg_time_watched_actions = 'video_avg_time_watched_actions'
        video_continuous_2_sec_watched_actions = 'video_continuous_2_sec_watched_actions'
        video_p100_watched_actions = 'video_p100_watched_actions'
        video_p25_watched_actions = 'video_p25_watched_actions'
        video_p50_watched_actions = 'video_p50_watched_actions'
        video_p75_watched_actions = 'video_p75_watched_actions'
        video_p95_watched_actions = 'video_p95_watched_actions'
        video_play_actions = 'video_play_actions'
        video_play_retention_0_to_15s_actions = 'video_play_retention_0_to_15s_actions'
        video_play_retention_20_to_60s_actions = 'video_play_retention_20_to_60s_actions'
        video_play_retention_graph_actions = 'video_play_retention_graph_actions'
        video_thruplay_watched_actions = 'video_thruplay_watched_actions'
        video_time_watched_actions = 'video_time_watched_actions'
        website_ctr = 'website_ctr'
        website_purchase_roas = 'website_purchase_roas'
        id = 'id'

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

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'insights'

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
            target_class=AdsInsights,
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
        'account_currency': 'string',
        'account_id': 'string',
        'account_name': 'string',
        'action_values': 'list<AdsActionStats>',
        'actions': 'list<AdsActionStats>',
        'activity_recency': 'string',
        'ad_click_actions': 'list<AdsActionStats>',
        'ad_format_asset': 'string',
        'ad_id': 'string',
        'ad_impression_actions': 'list<AdsActionStats>',
        'ad_name': 'string',
        'adset_id': 'string',
        'adset_name': 'string',
        'age': 'string',
        'age_targeting': 'string',
        'bid_type': 'string',
        'body_asset': 'Object',
        'buying_type': 'string',
        'call_to_action_asset': 'Object',
        'campaign_id': 'string',
        'campaign_name': 'string',
        'canvas_avg_view_percent': 'string',
        'canvas_avg_view_time': 'string',
        'canvas_component_avg_pct_view': 'list<AdsActionStats>',
        'clicks': 'string',
        'cost_per_10_sec_video_view': 'list<AdsActionStats>',
        'cost_per_15_sec_video_view': 'list<AdsActionStats>',
        'cost_per_2_sec_continuous_video_view': 'list<AdsActionStats>',
        'cost_per_action_type': 'list<AdsActionStats>',
        'cost_per_ad_click': 'list<AdsActionStats>',
        'cost_per_dda_countby_convs': 'string',
        'cost_per_estimated_ad_recallers': 'string',
        'cost_per_inline_link_click': 'string',
        'cost_per_inline_post_engagement': 'string',
        'cost_per_one_thousand_ad_impression': 'list<AdsActionStats>',
        'cost_per_outbound_click': 'list<AdsActionStats>',
        'cost_per_thruplay': 'list<AdsActionStats>',
        'cost_per_unique_action_type': 'list<AdsActionStats>',
        'cost_per_unique_click': 'string',
        'cost_per_unique_inline_link_click': 'string',
        'cost_per_unique_outbound_click': 'list<AdsActionStats>',
        'country': 'string',
        'cpc': 'string',
        'cpm': 'string',
        'cpp': 'string',
        'created_time': 'string',
        'creative_fingerprint': 'string',
        'ctr': 'string',
        'date_start': 'string',
        'date_stop': 'string',
        'dda_countby_convs': 'string',
        'description_asset': 'Object',
        'device_platform': 'string',
        'dma': 'string',
        'estimated_ad_recall_rate': 'string',
        'estimated_ad_recall_rate_lower_bound': 'string',
        'estimated_ad_recall_rate_upper_bound': 'string',
        'estimated_ad_recallers': 'string',
        'estimated_ad_recallers_lower_bound': 'string',
        'estimated_ad_recallers_upper_bound': 'string',
        'frequency': 'string',
        'frequency_value': 'string',
        'gender': 'string',
        'gender_targeting': 'string',
        'hourly_stats_aggregated_by_advertiser_time_zone': 'string',
        'hourly_stats_aggregated_by_audience_time_zone': 'string',
        'image_asset': 'Object',
        'impression_device': 'string',
        'impressions': 'string',
        'impressions_dummy': 'string',
        'inline_link_click_ctr': 'string',
        'inline_link_clicks': 'string',
        'inline_post_engagement': 'string',
        'labels': 'string',
        'link_url_asset': 'Object',
        'location': 'string',
        'media_asset': 'Object',
        'mobile_app_purchase_roas': 'list<AdsActionStats>',
        'objective': 'string',
        'outbound_clicks': 'list<AdsActionStats>',
        'outbound_clicks_ctr': 'list<AdsActionStats>',
        'place_page_id': 'string',
        'place_page_name': 'string',
        'placement': 'string',
        'platform_position': 'string',
        'product_format': 'string',
        'product_id': 'string',
        'publisher_platform': 'string',
        'purchasing_interface': 'string',
        'reach': 'string',
        'region': 'string',
        'relevance_score': 'AdgroupRelevanceScore',
        'social_spend': 'string',
        'spend': 'string',
        'title_asset': 'Object',
        'total_action_value': 'string',
        'unique_actions': 'list<AdsActionStats>',
        'unique_clicks': 'string',
        'unique_ctr': 'string',
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
        'video_avg_percent_watched_actions': 'list<AdsActionStats>',
        'video_avg_time_watched_actions': 'list<AdsActionStats>',
        'video_continuous_2_sec_watched_actions': 'list<AdsActionStats>',
        'video_p100_watched_actions': 'list<AdsActionStats>',
        'video_p25_watched_actions': 'list<AdsActionStats>',
        'video_p50_watched_actions': 'list<AdsActionStats>',
        'video_p75_watched_actions': 'list<AdsActionStats>',
        'video_p95_watched_actions': 'list<AdsActionStats>',
        'video_play_actions': 'list<AdsActionStats>',
        'video_play_retention_0_to_15s_actions': 'list<Object>',
        'video_play_retention_20_to_60s_actions': 'list<Object>',
        'video_play_retention_graph_actions': 'list<Object>',
        'video_thruplay_watched_actions': 'list<AdsActionStats>',
        'video_time_watched_actions': 'list<AdsActionStats>',
        'website_ctr': 'list<AdsActionStats>',
        'website_purchase_roas': 'list<AdsActionStats>',
        'id': 'string',
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


