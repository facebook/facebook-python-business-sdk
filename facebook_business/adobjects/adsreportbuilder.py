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

class AdsReportBuilder(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsReportBuilder = True
        super(AdsReportBuilder, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        headers = 'headers'
        rows = 'rows'
        id = 'id'

    class AttributionWindows:
        value_1d_view = '1d_view'
        value_7d_view = '7d_view'
        value_28d_view = '28d_view'
        value_1d_click = '1d_click'
        value_7d_click = '7d_click'
        value_28d_click = '28d_click'
        value_default = 'default'

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

    class DimensionGroups:
        age = 'age'
        country = 'country'
        gender = 'gender'
        region = 'region'
        region_id = 'region_id'
        dma = 'dma'
        impression_device = 'impression_device'
        publisher_platform = 'publisher_platform'
        device_platform = 'device_platform'
        platform_position = 'platform_position'
        activity_recency = 'activity_recency'
        place_page_id = 'place_page_id'
        household_composition = 'household_composition'
        household_income = 'household_income'
        product_id = 'product_id'
        frequency_value = 'frequency_value'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        ad_variation = 'ad_variation'
        image_asset = 'image_asset'
        image_asset_value = 'image_asset_value'
        video_asset = 'video_asset'
        video_asset_value = 'video_asset_value'
        link_url_asset = 'link_url_asset'
        link_url_asset_value = 'link_url_asset_value'
        body_asset = 'body_asset'
        body_asset_value = 'body_asset_value'
        title_asset = 'title_asset'
        title_asset_value = 'title_asset_value'
        description_asset = 'description_asset'
        description_asset_value = 'description_asset_value'
        call_to_action_asset = 'call_to_action_asset'
        call_to_action_asset_value = 'call_to_action_asset_value'
        action_device = 'action_device'
        action_reaction = 'action_reaction'
        action_destination = 'action_destination'
        action_event_channel = 'action_event_channel'
        action_link_click_destination = 'action_link_click_destination'
        action_video_type = 'action_video_type'
        action_video_sound = 'action_video_sound'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_canvas_component_id = 'action_canvas_component_id'
        action_canvas_component_name = 'action_canvas_component_name'
        ad_id = 'ad_id'
        ad_name = 'ad_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        creative_fingerprint = 'creative_fingerprint'
        adset_bid_type = 'adset_bid_type'
        adset_bid_value = 'adset_bid_value'
        budget_type = 'budget_type'
        budget_value = 'budget_value'
        adset_budget_type = 'adset_budget_type'
        adset_budget_value = 'adset_budget_value'
        campaign_budget_type = 'campaign_budget_type'
        campaign_budget_value = 'campaign_budget_value'
        buying_type = 'buying_type'
        delivery_info = 'delivery_info'
        objective = 'objective'
        delivery_start = 'delivery_start'
        delivery_end = 'delivery_end'
        ad_delivery = 'ad_delivery'
        adset_delivery = 'adset_delivery'
        campaign_delivery = 'campaign_delivery'
        days_1 = 'days_1'
        days_7 = 'days_7'
        days_14 = 'days_14'
        monthly = 'monthly'
        all_days = 'all_days'

    class Dimensions:
        age = 'age'
        country = 'country'
        gender = 'gender'
        region = 'region'
        region_id = 'region_id'
        dma = 'dma'
        impression_device = 'impression_device'
        publisher_platform = 'publisher_platform'
        device_platform = 'device_platform'
        platform_position = 'platform_position'
        activity_recency = 'activity_recency'
        place_page_id = 'place_page_id'
        household_composition = 'household_composition'
        household_income = 'household_income'
        product_id = 'product_id'
        frequency_value = 'frequency_value'
        hourly_stats_aggregated_by_advertiser_time_zone = 'hourly_stats_aggregated_by_advertiser_time_zone'
        hourly_stats_aggregated_by_audience_time_zone = 'hourly_stats_aggregated_by_audience_time_zone'
        ad_variation = 'ad_variation'
        image_asset = 'image_asset'
        image_asset_value = 'image_asset_value'
        video_asset = 'video_asset'
        video_asset_value = 'video_asset_value'
        link_url_asset = 'link_url_asset'
        link_url_asset_value = 'link_url_asset_value'
        body_asset = 'body_asset'
        body_asset_value = 'body_asset_value'
        title_asset = 'title_asset'
        title_asset_value = 'title_asset_value'
        description_asset = 'description_asset'
        description_asset_value = 'description_asset_value'
        call_to_action_asset = 'call_to_action_asset'
        call_to_action_asset_value = 'call_to_action_asset_value'
        action_device = 'action_device'
        action_reaction = 'action_reaction'
        action_destination = 'action_destination'
        action_event_channel = 'action_event_channel'
        action_link_click_destination = 'action_link_click_destination'
        action_video_type = 'action_video_type'
        action_video_sound = 'action_video_sound'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_canvas_component_id = 'action_canvas_component_id'
        action_canvas_component_name = 'action_canvas_component_name'
        ad_id = 'ad_id'
        ad_name = 'ad_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        creative_fingerprint = 'creative_fingerprint'
        adset_bid_type = 'adset_bid_type'
        adset_bid_value = 'adset_bid_value'
        budget_type = 'budget_type'
        budget_value = 'budget_value'
        adset_budget_type = 'adset_budget_type'
        adset_budget_value = 'adset_budget_value'
        campaign_budget_type = 'campaign_budget_type'
        campaign_budget_value = 'campaign_budget_value'
        buying_type = 'buying_type'
        delivery_info = 'delivery_info'
        objective = 'objective'
        delivery_start = 'delivery_start'
        delivery_end = 'delivery_end'
        ad_delivery = 'ad_delivery'
        adset_delivery = 'adset_delivery'
        campaign_delivery = 'campaign_delivery'
        days_1 = 'days_1'
        days_7 = 'days_7'
        days_14 = 'days_14'
        monthly = 'monthly'
        all_days = 'all_days'

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
            target_class=AdsReportBuilder,
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
        'headers': 'Object',
        'rows': 'list<Object>',
        'id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AttributionWindows'] = AdsReportBuilder.AttributionWindows.__dict__.values()
        field_enum_info['DatePreset'] = AdsReportBuilder.DatePreset.__dict__.values()
        field_enum_info['DimensionGroups'] = AdsReportBuilder.DimensionGroups.__dict__.values()
        field_enum_info['Dimensions'] = AdsReportBuilder.Dimensions.__dict__.values()
        return field_enum_info
