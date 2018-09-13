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

class AtlasCompany(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAtlasCompany = True
        super(AtlasCompany, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        created_by = 'created_by'
        created_date = 'created_date'
        created_time = 'created_time'
        cumulative_edited_date = 'cumulative_edited_date'
        id = 'id'
        is_mta = 'is_mta'
        last_modified_by = 'last_modified_by'
        last_modified_date = 'last_modified_date'
        last_modified_time = 'last_modified_time'
        login_security = 'login_security'
        name = 'name'
        version = 'version'
        visibility_type = 'visibility_type'

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
            target_class=AtlasCompany,
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

    def get_action_tags(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/action_tags',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_advertisers(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/advertisers',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_atlas_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.atlasuser import AtlasUser
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/atlas_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AtlasUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AtlasUser, api=self._api),
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

    def get_branches(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/branches',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_campaigns(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.atlascampaign import AtlasCampaign
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/campaigns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AtlasCampaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AtlasCampaign, api=self._api),
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

    def get_channels(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/channels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_clients(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/clients',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_connected_fb_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/connected_fb_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_custom_dimensions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/custom_dimensions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_in_product_metrics_by_campaign(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'additional_filter_value_sets': 'list<list<string>>',
            'columns': 'list<columns_enum>',
            'date_range': 'Object',
            'dimension_columns': 'list<dimension_columns_enum>',
            'filter_by': 'string',
            'filter_value_sets': 'list<list<string>>',
            'granularity': 'granularity_enum',
            'join_column': 'join_column_enum',
            'order_by': 'string',
            'requested_columns': 'list<requested_columns_enum>',
            'should_include_empty_metrics_rows': 'bool',
            'should_include_prior_period': 'bool',
            'should_summarize_over_date_range': 'bool',
            'time_period': 'time_period_enum',
            'view': 'view_enum',
        }
        enums = {
            'columns_enum': [
                'attributed_clicks_count',
                'attributed_impressions_count',
                'action_tag_id',
                'ad_id',
                'ad_set_id',
                'alias',
                'action_requests',
                'advertiser_id',
                'campaign_id',
                'campaign_group_id',
                'channel_id',
                'click_through_rate',
                'click_lookback_window',
                'click_lookback_window_in_minutes',
                'clicks',
                'company_id',
                'connection_id',
                'conversion_device_type',
                'conversion_event_id',
                'contributor_device_path_type',
                'age_range',
                'gender',
                'country',
                'dma_code',
                'dma_name',
                'device_os',
                'cost_per_1k_impressions',
                'cost_per_click',
                'cost_per_visit',
                'CUSTOM_BUCKET_BOOL_1',
                'CUSTOM_BUCKET_BOOL_2',
                'CUSTOM_BUCKET_BOOL_3',
                'CUSTOM_BUCKET_BOOL_4',
                'CUSTOM_BUCKET_INT_1',
                'CUSTOM_BUCKET_INT_2',
                'CUSTOM_BUCKET_INT_3',
                'CUSTOM_BUCKET_INT_4',
                'CUSTOM_BUCKET_STR_1',
                'CUSTOM_BUCKET_STR_2',
                'CUSTOM_BUCKET_STR_3',
                'CUSTOM_BUCKET_STR_4',
                'device_type',
                'days_from_conversion',
                'id',
                'data_driven_convs',
                'data_driven_convs_per_1k_impress',
                'data_driven_convs_per_100_clicks',
                'data_driven_convs_per_click',
                'data_driven_convs_per_visit',
                'data_driven_cpa',
                'data_driven_nullable_convs',
                'data_driven_roas',
                'data_driven_revenue',
                'dimension_group_ruleset',
                'even_credit_convs',
                'even_credit_convs_per_1k_impress',
                'even_credit_convs_per_100_clicks',
                'even_credit_convs_per_click',
                'even_credit_convs_per_visit',
                'even_credit_cpa',
                'even_credit_roas',
                'even_credit_revenue',
                'fb_identity_frequency',
                'fb_identity_reach',
                'first_click_convs',
                'first_click_revenue',
                'first_touch_convs',
                'first_touch_revenue',
                'first_touchpoints',
                'impression',
                'impressions',
                'last_click_convs',
                'last_click_convs_per_1k_impress',
                'last_click_convs_per_100_clicks',
                'last_click_convs_per_click',
                'last_click_convs_per_visit',
                'last_click_cpa',
                'last_click_roas',
                'last_click_revenue',
                'last_click_with_extrapolation_convs',
                'last_click_with_extrapolation_convs_per_1k_impress',
                'last_click_with_extrapolation_convs_per_100_clicks',
                'last_click_with_extrapolation_convs_per_click',
                'last_click_with_extrapolation_convs_per_visit',
                'last_click_with_extrapolation_cpa',
                'last_click_with_extrapolation_roas',
                'last_click_with_extrapolation_revenue',
                'last_click_with_cookies_convs',
                'last_click_with_cookies_convs_per_1k_impress',
                'last_click_with_cookies_convs_per_100_clicks',
                'last_click_with_cookies_convs_per_click',
                'last_click_with_cookies_convs_per_visit',
                'last_click_with_cookies_cpa',
                'last_click_with_cookies_roas',
                'last_click_with_cookies_revenue',
                'last_touch_convs',
                'last_touch_convs_per_1k_impress',
                'last_touch_convs_per_100_clicks',
                'last_touch_convs_per_click',
                'last_touch_convs_per_visit',
                'last_touch_cpa',
                'last_touch_roas',
                'last_touch_revenue',
                'first_view_convs',
                'first_view_revenue',
                'last_view_convs',
                'last_view_revenue',
                'last_touch_with_extrapolation_convs',
                'last_touch_with_extrapolation_convs_per_1k_impress',
                'last_touch_with_extrapolation_convs_per_100_clicks',
                'last_touch_with_extrapolation_convs_per_click',
                'last_touch_with_extrapolation_convs_per_visit',
                'last_touch_with_extrapolation_cpa',
                'last_touch_with_extrapolation_roas',
                'last_touch_with_extrapolation_revenue',
                'last_touchpoints',
                'lookback_window',
                'fraud_impressions',
                'metric_conversions',
                'metric_desktop_contributors',
                'metric_mobile_contributors',
                'non_fraud_impressions',
                'non_fraud_included_impressions',
                'off_screen_impressions',
                'positional_20fl_convs',
                'positional_20fl_convs_per_1k_impress',
                'positional_20fl_convs_per_100_clicks',
                'positional_20fl_convs_per_click',
                'positional_20fl_convs_per_visit',
                'positional_20fl_cpa',
                'positional_20fl_roas',
                'positional_20fl_revenue',
                'positional_30fl_convs',
                'positional_30fl_convs_per_1k_impress',
                'positional_30fl_convs_per_100_clicks',
                'positional_30fl_convs_per_click',
                'positional_30fl_convs_per_visit',
                'positional_30fl_cpa',
                'positional_30fl_roas',
                'positional_30fl_revenue',
                'positional_40fl_convs',
                'positional_40fl_convs_per_1k_impress',
                'positional_40fl_convs_per_100_clicks',
                'positional_40fl_convs_per_click',
                'positional_40fl_convs_per_visit',
                'positional_40fl_cpa',
                'positional_40fl_roas',
                'positional_40fl_revenue',
                'measurable_impressions',
                'name',
                'net_media_cost',
                'placement_id',
                'publisher_id',
                'raw_impressions',
                'reach',
                'reach_by_frequency_1',
                'reach_by_frequency_2',
                'reach_by_frequency_3',
                'reach_by_frequency_4',
                'reach_by_frequency_5',
                'reach_by_frequency_6',
                'reach_by_frequency_7',
                'reach_by_frequency_8',
                'reach_by_frequency_9',
                'reach_by_frequency_10',
                'reach_by_frequency_11',
                'reach_by_frequency_12',
                'reach_by_frequency_13',
                'reach_by_frequency_14',
                'reach_by_frequency_15_plus',
                'reach_excluded_impressions',
                'reach_included_impressions',
                'reach_frequency',
                'report_click_through_rate',
                'report_clicks',
                'report_impressions',
                'report_visits',
                'report_visits_for_virtual_column',
                'search_clicks',
                'source_channel',
                'stats_model_convs',
                'stats_model_convs_per_1k_impress',
                'stats_model_convs_per_100_clicks',
                'stats_model_convs_per_click',
                'stats_model_convs_per_visit',
                'stats_model_cpa',
                'stats_model_roas',
                'stats_model_revenue',
                'sum_legal_price',
                'tactic_id',
                'time_decay_1day_convs',
                'time_decay_1day_convs_per_1k_impress',
                'time_decay_1day_convs_per_100_clicks',
                'time_decay_1day_convs_per_click',
                'time_decay_1day_convs_per_visit',
                'time_decay_1day_cpa',
                'time_decay_1day_roas',
                'time_decay_1day_revenue',
                'time_decay_2day_convs',
                'time_decay_2day_convs_per_1k_impress',
                'time_decay_2day_convs_per_100_clicks',
                'time_decay_2day_convs_per_click',
                'time_decay_2day_convs_per_visit',
                'time_decay_2day_cpa',
                'time_decay_2day_roas',
                'time_decay_2day_revenue',
                'time_decay_7day_convs',
                'time_decay_7day_convs_per_1k_impress',
                'time_decay_7day_convs_per_100_clicks',
                'time_decay_7day_convs_per_click',
                'time_decay_7day_convs_per_visit',
                'time_decay_7day_cpa',
                'time_decay_7day_roas',
                'time_decay_7day_revenue',
                'time_decay_14day_convs',
                'time_decay_14day_convs_per_1k_impress',
                'time_decay_14day_convs_per_100_clicks',
                'time_decay_14day_convs_per_click',
                'time_decay_14day_convs_per_visit',
                'time_decay_14day_cpa',
                'time_decay_14day_roas',
                'time_decay_14day_revenue',
                'timestamp',
                'total_comparable_conversions',
                'total_comparable_revenue',
                'total_conversions',
                'total_measurable_impressions',
                'total_non_fraud_impressions',
                'total_raw_impressions',
                'total_revenue',
                'total_viewable_impressions',
                'total_wasted_impressions',
                'unique_reach',
                'url_without_params',
                'version_id',
                'view_lookback_window',
                'view_lookback_window_in_minutes',
                'viewable_impressions',
                'wasted_impressions',
            ],
            'dimension_columns_enum': [
                'attributed_clicks_count',
                'attributed_impressions_count',
                'action_tag_id',
                'ad_id',
                'ad_set_id',
                'alias',
                'action_requests',
                'advertiser_id',
                'campaign_id',
                'campaign_group_id',
                'channel_id',
                'click_through_rate',
                'click_lookback_window',
                'click_lookback_window_in_minutes',
                'clicks',
                'company_id',
                'connection_id',
                'conversion_device_type',
                'conversion_event_id',
                'contributor_device_path_type',
                'age_range',
                'gender',
                'country',
                'dma_code',
                'dma_name',
                'device_os',
                'cost_per_1k_impressions',
                'cost_per_click',
                'cost_per_visit',
                'CUSTOM_BUCKET_BOOL_1',
                'CUSTOM_BUCKET_BOOL_2',
                'CUSTOM_BUCKET_BOOL_3',
                'CUSTOM_BUCKET_BOOL_4',
                'CUSTOM_BUCKET_INT_1',
                'CUSTOM_BUCKET_INT_2',
                'CUSTOM_BUCKET_INT_3',
                'CUSTOM_BUCKET_INT_4',
                'CUSTOM_BUCKET_STR_1',
                'CUSTOM_BUCKET_STR_2',
                'CUSTOM_BUCKET_STR_3',
                'CUSTOM_BUCKET_STR_4',
                'device_type',
                'days_from_conversion',
                'id',
                'data_driven_convs',
                'data_driven_convs_per_1k_impress',
                'data_driven_convs_per_100_clicks',
                'data_driven_convs_per_click',
                'data_driven_convs_per_visit',
                'data_driven_cpa',
                'data_driven_nullable_convs',
                'data_driven_roas',
                'data_driven_revenue',
                'dimension_group_ruleset',
                'even_credit_convs',
                'even_credit_convs_per_1k_impress',
                'even_credit_convs_per_100_clicks',
                'even_credit_convs_per_click',
                'even_credit_convs_per_visit',
                'even_credit_cpa',
                'even_credit_roas',
                'even_credit_revenue',
                'fb_identity_frequency',
                'fb_identity_reach',
                'first_click_convs',
                'first_click_revenue',
                'first_touch_convs',
                'first_touch_revenue',
                'first_touchpoints',
                'impression',
                'impressions',
                'last_click_convs',
                'last_click_convs_per_1k_impress',
                'last_click_convs_per_100_clicks',
                'last_click_convs_per_click',
                'last_click_convs_per_visit',
                'last_click_cpa',
                'last_click_roas',
                'last_click_revenue',
                'last_click_with_extrapolation_convs',
                'last_click_with_extrapolation_convs_per_1k_impress',
                'last_click_with_extrapolation_convs_per_100_clicks',
                'last_click_with_extrapolation_convs_per_click',
                'last_click_with_extrapolation_convs_per_visit',
                'last_click_with_extrapolation_cpa',
                'last_click_with_extrapolation_roas',
                'last_click_with_extrapolation_revenue',
                'last_click_with_cookies_convs',
                'last_click_with_cookies_convs_per_1k_impress',
                'last_click_with_cookies_convs_per_100_clicks',
                'last_click_with_cookies_convs_per_click',
                'last_click_with_cookies_convs_per_visit',
                'last_click_with_cookies_cpa',
                'last_click_with_cookies_roas',
                'last_click_with_cookies_revenue',
                'last_touch_convs',
                'last_touch_convs_per_1k_impress',
                'last_touch_convs_per_100_clicks',
                'last_touch_convs_per_click',
                'last_touch_convs_per_visit',
                'last_touch_cpa',
                'last_touch_roas',
                'last_touch_revenue',
                'first_view_convs',
                'first_view_revenue',
                'last_view_convs',
                'last_view_revenue',
                'last_touch_with_extrapolation_convs',
                'last_touch_with_extrapolation_convs_per_1k_impress',
                'last_touch_with_extrapolation_convs_per_100_clicks',
                'last_touch_with_extrapolation_convs_per_click',
                'last_touch_with_extrapolation_convs_per_visit',
                'last_touch_with_extrapolation_cpa',
                'last_touch_with_extrapolation_roas',
                'last_touch_with_extrapolation_revenue',
                'last_touchpoints',
                'lookback_window',
                'fraud_impressions',
                'metric_conversions',
                'metric_desktop_contributors',
                'metric_mobile_contributors',
                'non_fraud_impressions',
                'non_fraud_included_impressions',
                'off_screen_impressions',
                'positional_20fl_convs',
                'positional_20fl_convs_per_1k_impress',
                'positional_20fl_convs_per_100_clicks',
                'positional_20fl_convs_per_click',
                'positional_20fl_convs_per_visit',
                'positional_20fl_cpa',
                'positional_20fl_roas',
                'positional_20fl_revenue',
                'positional_30fl_convs',
                'positional_30fl_convs_per_1k_impress',
                'positional_30fl_convs_per_100_clicks',
                'positional_30fl_convs_per_click',
                'positional_30fl_convs_per_visit',
                'positional_30fl_cpa',
                'positional_30fl_roas',
                'positional_30fl_revenue',
                'positional_40fl_convs',
                'positional_40fl_convs_per_1k_impress',
                'positional_40fl_convs_per_100_clicks',
                'positional_40fl_convs_per_click',
                'positional_40fl_convs_per_visit',
                'positional_40fl_cpa',
                'positional_40fl_roas',
                'positional_40fl_revenue',
                'measurable_impressions',
                'name',
                'net_media_cost',
                'placement_id',
                'publisher_id',
                'raw_impressions',
                'reach',
                'reach_by_frequency_1',
                'reach_by_frequency_2',
                'reach_by_frequency_3',
                'reach_by_frequency_4',
                'reach_by_frequency_5',
                'reach_by_frequency_6',
                'reach_by_frequency_7',
                'reach_by_frequency_8',
                'reach_by_frequency_9',
                'reach_by_frequency_10',
                'reach_by_frequency_11',
                'reach_by_frequency_12',
                'reach_by_frequency_13',
                'reach_by_frequency_14',
                'reach_by_frequency_15_plus',
                'reach_excluded_impressions',
                'reach_included_impressions',
                'reach_frequency',
                'report_click_through_rate',
                'report_clicks',
                'report_impressions',
                'report_visits',
                'report_visits_for_virtual_column',
                'search_clicks',
                'source_channel',
                'stats_model_convs',
                'stats_model_convs_per_1k_impress',
                'stats_model_convs_per_100_clicks',
                'stats_model_convs_per_click',
                'stats_model_convs_per_visit',
                'stats_model_cpa',
                'stats_model_roas',
                'stats_model_revenue',
                'sum_legal_price',
                'tactic_id',
                'time_decay_1day_convs',
                'time_decay_1day_convs_per_1k_impress',
                'time_decay_1day_convs_per_100_clicks',
                'time_decay_1day_convs_per_click',
                'time_decay_1day_convs_per_visit',
                'time_decay_1day_cpa',
                'time_decay_1day_roas',
                'time_decay_1day_revenue',
                'time_decay_2day_convs',
                'time_decay_2day_convs_per_1k_impress',
                'time_decay_2day_convs_per_100_clicks',
                'time_decay_2day_convs_per_click',
                'time_decay_2day_convs_per_visit',
                'time_decay_2day_cpa',
                'time_decay_2day_roas',
                'time_decay_2day_revenue',
                'time_decay_7day_convs',
                'time_decay_7day_convs_per_1k_impress',
                'time_decay_7day_convs_per_100_clicks',
                'time_decay_7day_convs_per_click',
                'time_decay_7day_convs_per_visit',
                'time_decay_7day_cpa',
                'time_decay_7day_roas',
                'time_decay_7day_revenue',
                'time_decay_14day_convs',
                'time_decay_14day_convs_per_1k_impress',
                'time_decay_14day_convs_per_100_clicks',
                'time_decay_14day_convs_per_click',
                'time_decay_14day_convs_per_visit',
                'time_decay_14day_cpa',
                'time_decay_14day_roas',
                'time_decay_14day_revenue',
                'timestamp',
                'total_comparable_conversions',
                'total_comparable_revenue',
                'total_conversions',
                'total_measurable_impressions',
                'total_non_fraud_impressions',
                'total_raw_impressions',
                'total_revenue',
                'total_viewable_impressions',
                'total_wasted_impressions',
                'unique_reach',
                'url_without_params',
                'version_id',
                'view_lookback_window',
                'view_lookback_window_in_minutes',
                'viewable_impressions',
                'wasted_impressions',
            ],
            'granularity_enum': [
                'hour',
                'day',
                'week',
                'month',
                'year',
                'lifetime',
            ],
            'join_column_enum': [
                'attributed_clicks_count',
                'attributed_impressions_count',
                'action_tag_id',
                'ad_id',
                'ad_set_id',
                'alias',
                'action_requests',
                'advertiser_id',
                'campaign_id',
                'campaign_group_id',
                'channel_id',
                'click_through_rate',
                'click_lookback_window',
                'click_lookback_window_in_minutes',
                'clicks',
                'company_id',
                'connection_id',
                'conversion_device_type',
                'conversion_event_id',
                'contributor_device_path_type',
                'age_range',
                'gender',
                'country',
                'dma_code',
                'dma_name',
                'device_os',
                'cost_per_1k_impressions',
                'cost_per_click',
                'cost_per_visit',
                'CUSTOM_BUCKET_BOOL_1',
                'CUSTOM_BUCKET_BOOL_2',
                'CUSTOM_BUCKET_BOOL_3',
                'CUSTOM_BUCKET_BOOL_4',
                'CUSTOM_BUCKET_INT_1',
                'CUSTOM_BUCKET_INT_2',
                'CUSTOM_BUCKET_INT_3',
                'CUSTOM_BUCKET_INT_4',
                'CUSTOM_BUCKET_STR_1',
                'CUSTOM_BUCKET_STR_2',
                'CUSTOM_BUCKET_STR_3',
                'CUSTOM_BUCKET_STR_4',
                'device_type',
                'days_from_conversion',
                'id',
                'data_driven_convs',
                'data_driven_convs_per_1k_impress',
                'data_driven_convs_per_100_clicks',
                'data_driven_convs_per_click',
                'data_driven_convs_per_visit',
                'data_driven_cpa',
                'data_driven_nullable_convs',
                'data_driven_roas',
                'data_driven_revenue',
                'dimension_group_ruleset',
                'even_credit_convs',
                'even_credit_convs_per_1k_impress',
                'even_credit_convs_per_100_clicks',
                'even_credit_convs_per_click',
                'even_credit_convs_per_visit',
                'even_credit_cpa',
                'even_credit_roas',
                'even_credit_revenue',
                'fb_identity_frequency',
                'fb_identity_reach',
                'first_click_convs',
                'first_click_revenue',
                'first_touch_convs',
                'first_touch_revenue',
                'first_touchpoints',
                'impression',
                'impressions',
                'last_click_convs',
                'last_click_convs_per_1k_impress',
                'last_click_convs_per_100_clicks',
                'last_click_convs_per_click',
                'last_click_convs_per_visit',
                'last_click_cpa',
                'last_click_roas',
                'last_click_revenue',
                'last_click_with_extrapolation_convs',
                'last_click_with_extrapolation_convs_per_1k_impress',
                'last_click_with_extrapolation_convs_per_100_clicks',
                'last_click_with_extrapolation_convs_per_click',
                'last_click_with_extrapolation_convs_per_visit',
                'last_click_with_extrapolation_cpa',
                'last_click_with_extrapolation_roas',
                'last_click_with_extrapolation_revenue',
                'last_click_with_cookies_convs',
                'last_click_with_cookies_convs_per_1k_impress',
                'last_click_with_cookies_convs_per_100_clicks',
                'last_click_with_cookies_convs_per_click',
                'last_click_with_cookies_convs_per_visit',
                'last_click_with_cookies_cpa',
                'last_click_with_cookies_roas',
                'last_click_with_cookies_revenue',
                'last_touch_convs',
                'last_touch_convs_per_1k_impress',
                'last_touch_convs_per_100_clicks',
                'last_touch_convs_per_click',
                'last_touch_convs_per_visit',
                'last_touch_cpa',
                'last_touch_roas',
                'last_touch_revenue',
                'first_view_convs',
                'first_view_revenue',
                'last_view_convs',
                'last_view_revenue',
                'last_touch_with_extrapolation_convs',
                'last_touch_with_extrapolation_convs_per_1k_impress',
                'last_touch_with_extrapolation_convs_per_100_clicks',
                'last_touch_with_extrapolation_convs_per_click',
                'last_touch_with_extrapolation_convs_per_visit',
                'last_touch_with_extrapolation_cpa',
                'last_touch_with_extrapolation_roas',
                'last_touch_with_extrapolation_revenue',
                'last_touchpoints',
                'lookback_window',
                'fraud_impressions',
                'metric_conversions',
                'metric_desktop_contributors',
                'metric_mobile_contributors',
                'non_fraud_impressions',
                'non_fraud_included_impressions',
                'off_screen_impressions',
                'positional_20fl_convs',
                'positional_20fl_convs_per_1k_impress',
                'positional_20fl_convs_per_100_clicks',
                'positional_20fl_convs_per_click',
                'positional_20fl_convs_per_visit',
                'positional_20fl_cpa',
                'positional_20fl_roas',
                'positional_20fl_revenue',
                'positional_30fl_convs',
                'positional_30fl_convs_per_1k_impress',
                'positional_30fl_convs_per_100_clicks',
                'positional_30fl_convs_per_click',
                'positional_30fl_convs_per_visit',
                'positional_30fl_cpa',
                'positional_30fl_roas',
                'positional_30fl_revenue',
                'positional_40fl_convs',
                'positional_40fl_convs_per_1k_impress',
                'positional_40fl_convs_per_100_clicks',
                'positional_40fl_convs_per_click',
                'positional_40fl_convs_per_visit',
                'positional_40fl_cpa',
                'positional_40fl_roas',
                'positional_40fl_revenue',
                'measurable_impressions',
                'name',
                'net_media_cost',
                'placement_id',
                'publisher_id',
                'raw_impressions',
                'reach',
                'reach_by_frequency_1',
                'reach_by_frequency_2',
                'reach_by_frequency_3',
                'reach_by_frequency_4',
                'reach_by_frequency_5',
                'reach_by_frequency_6',
                'reach_by_frequency_7',
                'reach_by_frequency_8',
                'reach_by_frequency_9',
                'reach_by_frequency_10',
                'reach_by_frequency_11',
                'reach_by_frequency_12',
                'reach_by_frequency_13',
                'reach_by_frequency_14',
                'reach_by_frequency_15_plus',
                'reach_excluded_impressions',
                'reach_included_impressions',
                'reach_frequency',
                'report_click_through_rate',
                'report_clicks',
                'report_impressions',
                'report_visits',
                'report_visits_for_virtual_column',
                'search_clicks',
                'source_channel',
                'stats_model_convs',
                'stats_model_convs_per_1k_impress',
                'stats_model_convs_per_100_clicks',
                'stats_model_convs_per_click',
                'stats_model_convs_per_visit',
                'stats_model_cpa',
                'stats_model_roas',
                'stats_model_revenue',
                'sum_legal_price',
                'tactic_id',
                'time_decay_1day_convs',
                'time_decay_1day_convs_per_1k_impress',
                'time_decay_1day_convs_per_100_clicks',
                'time_decay_1day_convs_per_click',
                'time_decay_1day_convs_per_visit',
                'time_decay_1day_cpa',
                'time_decay_1day_roas',
                'time_decay_1day_revenue',
                'time_decay_2day_convs',
                'time_decay_2day_convs_per_1k_impress',
                'time_decay_2day_convs_per_100_clicks',
                'time_decay_2day_convs_per_click',
                'time_decay_2day_convs_per_visit',
                'time_decay_2day_cpa',
                'time_decay_2day_roas',
                'time_decay_2day_revenue',
                'time_decay_7day_convs',
                'time_decay_7day_convs_per_1k_impress',
                'time_decay_7day_convs_per_100_clicks',
                'time_decay_7day_convs_per_click',
                'time_decay_7day_convs_per_visit',
                'time_decay_7day_cpa',
                'time_decay_7day_roas',
                'time_decay_7day_revenue',
                'time_decay_14day_convs',
                'time_decay_14day_convs_per_1k_impress',
                'time_decay_14day_convs_per_100_clicks',
                'time_decay_14day_convs_per_click',
                'time_decay_14day_convs_per_visit',
                'time_decay_14day_cpa',
                'time_decay_14day_roas',
                'time_decay_14day_revenue',
                'timestamp',
                'total_comparable_conversions',
                'total_comparable_revenue',
                'total_conversions',
                'total_measurable_impressions',
                'total_non_fraud_impressions',
                'total_raw_impressions',
                'total_revenue',
                'total_viewable_impressions',
                'total_wasted_impressions',
                'unique_reach',
                'url_without_params',
                'version_id',
                'view_lookback_window',
                'view_lookback_window_in_minutes',
                'viewable_impressions',
                'wasted_impressions',
            ],
            'requested_columns_enum': [
                'attributed_clicks_count',
                'attributed_impressions_count',
                'action_tag_id',
                'ad_id',
                'ad_set_id',
                'alias',
                'action_requests',
                'advertiser_id',
                'campaign_id',
                'campaign_group_id',
                'channel_id',
                'click_through_rate',
                'click_lookback_window',
                'click_lookback_window_in_minutes',
                'clicks',
                'company_id',
                'connection_id',
                'conversion_device_type',
                'conversion_event_id',
                'contributor_device_path_type',
                'age_range',
                'gender',
                'country',
                'dma_code',
                'dma_name',
                'device_os',
                'cost_per_1k_impressions',
                'cost_per_click',
                'cost_per_visit',
                'CUSTOM_BUCKET_BOOL_1',
                'CUSTOM_BUCKET_BOOL_2',
                'CUSTOM_BUCKET_BOOL_3',
                'CUSTOM_BUCKET_BOOL_4',
                'CUSTOM_BUCKET_INT_1',
                'CUSTOM_BUCKET_INT_2',
                'CUSTOM_BUCKET_INT_3',
                'CUSTOM_BUCKET_INT_4',
                'CUSTOM_BUCKET_STR_1',
                'CUSTOM_BUCKET_STR_2',
                'CUSTOM_BUCKET_STR_3',
                'CUSTOM_BUCKET_STR_4',
                'device_type',
                'days_from_conversion',
                'id',
                'data_driven_convs',
                'data_driven_convs_per_1k_impress',
                'data_driven_convs_per_100_clicks',
                'data_driven_convs_per_click',
                'data_driven_convs_per_visit',
                'data_driven_cpa',
                'data_driven_nullable_convs',
                'data_driven_roas',
                'data_driven_revenue',
                'dimension_group_ruleset',
                'even_credit_convs',
                'even_credit_convs_per_1k_impress',
                'even_credit_convs_per_100_clicks',
                'even_credit_convs_per_click',
                'even_credit_convs_per_visit',
                'even_credit_cpa',
                'even_credit_roas',
                'even_credit_revenue',
                'fb_identity_frequency',
                'fb_identity_reach',
                'first_click_convs',
                'first_click_revenue',
                'first_touch_convs',
                'first_touch_revenue',
                'first_touchpoints',
                'impression',
                'impressions',
                'last_click_convs',
                'last_click_convs_per_1k_impress',
                'last_click_convs_per_100_clicks',
                'last_click_convs_per_click',
                'last_click_convs_per_visit',
                'last_click_cpa',
                'last_click_roas',
                'last_click_revenue',
                'last_click_with_extrapolation_convs',
                'last_click_with_extrapolation_convs_per_1k_impress',
                'last_click_with_extrapolation_convs_per_100_clicks',
                'last_click_with_extrapolation_convs_per_click',
                'last_click_with_extrapolation_convs_per_visit',
                'last_click_with_extrapolation_cpa',
                'last_click_with_extrapolation_roas',
                'last_click_with_extrapolation_revenue',
                'last_click_with_cookies_convs',
                'last_click_with_cookies_convs_per_1k_impress',
                'last_click_with_cookies_convs_per_100_clicks',
                'last_click_with_cookies_convs_per_click',
                'last_click_with_cookies_convs_per_visit',
                'last_click_with_cookies_cpa',
                'last_click_with_cookies_roas',
                'last_click_with_cookies_revenue',
                'last_touch_convs',
                'last_touch_convs_per_1k_impress',
                'last_touch_convs_per_100_clicks',
                'last_touch_convs_per_click',
                'last_touch_convs_per_visit',
                'last_touch_cpa',
                'last_touch_roas',
                'last_touch_revenue',
                'first_view_convs',
                'first_view_revenue',
                'last_view_convs',
                'last_view_revenue',
                'last_touch_with_extrapolation_convs',
                'last_touch_with_extrapolation_convs_per_1k_impress',
                'last_touch_with_extrapolation_convs_per_100_clicks',
                'last_touch_with_extrapolation_convs_per_click',
                'last_touch_with_extrapolation_convs_per_visit',
                'last_touch_with_extrapolation_cpa',
                'last_touch_with_extrapolation_roas',
                'last_touch_with_extrapolation_revenue',
                'last_touchpoints',
                'lookback_window',
                'fraud_impressions',
                'metric_conversions',
                'metric_desktop_contributors',
                'metric_mobile_contributors',
                'non_fraud_impressions',
                'non_fraud_included_impressions',
                'off_screen_impressions',
                'positional_20fl_convs',
                'positional_20fl_convs_per_1k_impress',
                'positional_20fl_convs_per_100_clicks',
                'positional_20fl_convs_per_click',
                'positional_20fl_convs_per_visit',
                'positional_20fl_cpa',
                'positional_20fl_roas',
                'positional_20fl_revenue',
                'positional_30fl_convs',
                'positional_30fl_convs_per_1k_impress',
                'positional_30fl_convs_per_100_clicks',
                'positional_30fl_convs_per_click',
                'positional_30fl_convs_per_visit',
                'positional_30fl_cpa',
                'positional_30fl_roas',
                'positional_30fl_revenue',
                'positional_40fl_convs',
                'positional_40fl_convs_per_1k_impress',
                'positional_40fl_convs_per_100_clicks',
                'positional_40fl_convs_per_click',
                'positional_40fl_convs_per_visit',
                'positional_40fl_cpa',
                'positional_40fl_roas',
                'positional_40fl_revenue',
                'measurable_impressions',
                'name',
                'net_media_cost',
                'placement_id',
                'publisher_id',
                'raw_impressions',
                'reach',
                'reach_by_frequency_1',
                'reach_by_frequency_2',
                'reach_by_frequency_3',
                'reach_by_frequency_4',
                'reach_by_frequency_5',
                'reach_by_frequency_6',
                'reach_by_frequency_7',
                'reach_by_frequency_8',
                'reach_by_frequency_9',
                'reach_by_frequency_10',
                'reach_by_frequency_11',
                'reach_by_frequency_12',
                'reach_by_frequency_13',
                'reach_by_frequency_14',
                'reach_by_frequency_15_plus',
                'reach_excluded_impressions',
                'reach_included_impressions',
                'reach_frequency',
                'report_click_through_rate',
                'report_clicks',
                'report_impressions',
                'report_visits',
                'report_visits_for_virtual_column',
                'search_clicks',
                'source_channel',
                'stats_model_convs',
                'stats_model_convs_per_1k_impress',
                'stats_model_convs_per_100_clicks',
                'stats_model_convs_per_click',
                'stats_model_convs_per_visit',
                'stats_model_cpa',
                'stats_model_roas',
                'stats_model_revenue',
                'sum_legal_price',
                'tactic_id',
                'time_decay_1day_convs',
                'time_decay_1day_convs_per_1k_impress',
                'time_decay_1day_convs_per_100_clicks',
                'time_decay_1day_convs_per_click',
                'time_decay_1day_convs_per_visit',
                'time_decay_1day_cpa',
                'time_decay_1day_roas',
                'time_decay_1day_revenue',
                'time_decay_2day_convs',
                'time_decay_2day_convs_per_1k_impress',
                'time_decay_2day_convs_per_100_clicks',
                'time_decay_2day_convs_per_click',
                'time_decay_2day_convs_per_visit',
                'time_decay_2day_cpa',
                'time_decay_2day_roas',
                'time_decay_2day_revenue',
                'time_decay_7day_convs',
                'time_decay_7day_convs_per_1k_impress',
                'time_decay_7day_convs_per_100_clicks',
                'time_decay_7day_convs_per_click',
                'time_decay_7day_convs_per_visit',
                'time_decay_7day_cpa',
                'time_decay_7day_roas',
                'time_decay_7day_revenue',
                'time_decay_14day_convs',
                'time_decay_14day_convs_per_1k_impress',
                'time_decay_14day_convs_per_100_clicks',
                'time_decay_14day_convs_per_click',
                'time_decay_14day_convs_per_visit',
                'time_decay_14day_cpa',
                'time_decay_14day_roas',
                'time_decay_14day_revenue',
                'timestamp',
                'total_comparable_conversions',
                'total_comparable_revenue',
                'total_conversions',
                'total_measurable_impressions',
                'total_non_fraud_impressions',
                'total_raw_impressions',
                'total_revenue',
                'total_viewable_impressions',
                'total_wasted_impressions',
                'unique_reach',
                'url_without_params',
                'version_id',
                'view_lookback_window',
                'view_lookback_window_in_minutes',
                'viewable_impressions',
                'wasted_impressions',
            ],
            'time_period_enum': [
                'all_available',
                'all_dates',
                'custom',
                'date_range',
                'fifteen_days',
                'last_fourteen_days',
                'last_hundred_fourty_four_hours',
                'last_month',
                'last_ninety_days',
                'last_quarter',
                'last_seven_days',
                'last_sixty_days',
                'last_thirty_days',
                'last_twenty_four_hours',
                'last_year',
                'month_to_date',
                'quarter_to_date',
                'seven_days',
                'thirty_days',
                'this_month_whole_days',
                'today',
                'week_to_date',
                'year_to_date',
                'yesterday',
            ],
            'view_enum': [
                'none',
                'adset/connection/advertiser',
                'advertiser',
                'advertiser/version',
                'advertiser/version/campaign',
                'campaign',
                'campaign/device',
                'campaign/placement',
                'campaign/publisher',
                'campaign/version',
                'campaign/version/publisher',
                'company/campaign',
                'connection/advertiser',
                'connection/advertiser/adset',
                'connection/advertiser/campaign',
                'connection/advertiser/campaign/placement',
                'conversion_event/campaign',
                'conversion_event/channel',
                'conversion_event/publisher',
                'conversion_event/tactic',
                'placement',
                'placement/advertiser',
                'placement/device',
                'publisher',
                'publisher/campaign',
                'publisher/device',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/in_product_metrics_by_campaign',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_permissions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/permissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_report_columns(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/report_columns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_report_runs(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/report_runs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_reports(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reports',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_roles(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/roles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_tactics(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tactics',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_tracking_connections(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filter_by': 'string',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tracking_connections',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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
        'created_by': 'Object',
        'created_date': 'datetime',
        'created_time': 'datetime',
        'cumulative_edited_date': 'datetime',
        'id': 'string',
        'is_mta': 'bool',
        'last_modified_by': 'Object',
        'last_modified_date': 'datetime',
        'last_modified_time': 'datetime',
        'login_security': 'string',
        'name': 'string',
        'version': 'string',
        'visibility_type': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
