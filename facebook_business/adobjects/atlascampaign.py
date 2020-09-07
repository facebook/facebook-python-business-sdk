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

class AtlasCampaign(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAtlasCampaign = True
        super(AtlasCampaign, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_platform = 'ad_platform'
        alias = 'alias'
        cost_per_1k_impressions = 'cost_per_1k_impressions'
        cost_per_click = 'cost_per_click'
        cost_per_visit = 'cost_per_visit'
        created_by = 'created_by'
        created_date = 'created_date'
        data_driven_convs = 'data_driven_convs'
        data_driven_convs_per_1k_impress = 'data_driven_convs_per_1k_impress'
        data_driven_convs_per_click = 'data_driven_convs_per_click'
        data_driven_convs_per_visit = 'data_driven_convs_per_visit'
        data_driven_cpa = 'data_driven_cpa'
        data_driven_nullable_convs = 'data_driven_nullable_convs'
        data_driven_revenue = 'data_driven_revenue'
        data_driven_roas = 'data_driven_roas'
        even_credit_convs = 'even_credit_convs'
        even_credit_convs_per_1k_impress = 'even_credit_convs_per_1k_impress'
        even_credit_convs_per_click = 'even_credit_convs_per_click'
        even_credit_convs_per_visit = 'even_credit_convs_per_visit'
        even_credit_cpa = 'even_credit_cpa'
        even_credit_revenue = 'even_credit_revenue'
        even_credit_roas = 'even_credit_roas'
        first_click_convs = 'first_click_convs'
        first_click_convs_per_1k_impress = 'first_click_convs_per_1k_impress'
        first_click_convs_per_click = 'first_click_convs_per_click'
        first_click_convs_per_visit = 'first_click_convs_per_visit'
        first_click_cpa = 'first_click_cpa'
        first_click_revenue = 'first_click_revenue'
        first_click_roas = 'first_click_roas'
        first_touch_convs = 'first_touch_convs'
        first_touch_convs_per_1k_impress = 'first_touch_convs_per_1k_impress'
        first_touch_convs_per_click = 'first_touch_convs_per_click'
        first_touch_convs_per_visit = 'first_touch_convs_per_visit'
        first_touch_cpa = 'first_touch_cpa'
        first_touch_revenue = 'first_touch_revenue'
        first_touch_roas = 'first_touch_roas'
        id = 'id'
        is_archived = 'is_archived'
        last_click_convs = 'last_click_convs'
        last_click_convs_per_1k_impress = 'last_click_convs_per_1k_impress'
        last_click_convs_per_click = 'last_click_convs_per_click'
        last_click_convs_per_visit = 'last_click_convs_per_visit'
        last_click_cpa = 'last_click_cpa'
        last_click_revenue = 'last_click_revenue'
        last_click_roas = 'last_click_roas'
        last_click_with_extrapolation_convs = 'last_click_with_extrapolation_convs'
        last_click_with_extrapolation_convs_per_100_clicks = 'last_click_with_extrapolation_convs_per_100_clicks'
        last_click_with_extrapolation_convs_per_1k_impress = 'last_click_with_extrapolation_convs_per_1k_impress'
        last_click_with_extrapolation_convs_per_click = 'last_click_with_extrapolation_convs_per_click'
        last_click_with_extrapolation_convs_per_visit = 'last_click_with_extrapolation_convs_per_visit'
        last_click_with_extrapolation_cpa = 'last_click_with_extrapolation_cpa'
        last_click_with_extrapolation_revenue = 'last_click_with_extrapolation_revenue'
        last_click_with_extrapolation_roas = 'last_click_with_extrapolation_roas'
        last_click_with_extrapolation_unattributed = 'last_click_with_extrapolation_unattributed'
        last_modified_by = 'last_modified_by'
        last_modified_date = 'last_modified_date'
        last_touch_convs = 'last_touch_convs'
        last_touch_convs_per_1k_impress = 'last_touch_convs_per_1k_impress'
        last_touch_convs_per_click = 'last_touch_convs_per_click'
        last_touch_convs_per_visit = 'last_touch_convs_per_visit'
        last_touch_cpa = 'last_touch_cpa'
        last_touch_revenue = 'last_touch_revenue'
        last_touch_roas = 'last_touch_roas'
        name = 'name'
        net_media_cost = 'net_media_cost'
        positional_30fl_convs = 'positional_30fl_convs'
        positional_30fl_convs_per_1k_impress = 'positional_30fl_convs_per_1k_impress'
        positional_30fl_convs_per_click = 'positional_30fl_convs_per_click'
        positional_30fl_convs_per_visit = 'positional_30fl_convs_per_visit'
        positional_30fl_cpa = 'positional_30fl_cpa'
        positional_30fl_revenue = 'positional_30fl_revenue'
        positional_30fl_roas = 'positional_30fl_roas'
        positional_40fl_convs = 'positional_40fl_convs'
        positional_40fl_convs_per_1k_impress = 'positional_40fl_convs_per_1k_impress'
        positional_40fl_convs_per_click = 'positional_40fl_convs_per_click'
        positional_40fl_convs_per_visit = 'positional_40fl_convs_per_visit'
        positional_40fl_cpa = 'positional_40fl_cpa'
        positional_40fl_revenue = 'positional_40fl_revenue'
        positional_40fl_roas = 'positional_40fl_roas'
        report_click_through_rate = 'report_click_through_rate'
        report_clicks = 'report_clicks'
        report_impressions = 'report_impressions'
        report_visits = 'report_visits'
        time_decay_1day_convs = 'time_decay_1day_convs'
        time_decay_1day_convs_per_1k_impress = 'time_decay_1day_convs_per_1k_impress'
        time_decay_1day_convs_per_click = 'time_decay_1day_convs_per_click'
        time_decay_1day_convs_per_visit = 'time_decay_1day_convs_per_visit'
        time_decay_1day_cpa = 'time_decay_1day_cpa'
        time_decay_1day_revenue = 'time_decay_1day_revenue'
        time_decay_1day_roas = 'time_decay_1day_roas'
        time_decay_7day_convs = 'time_decay_7day_convs'
        time_decay_7day_convs_per_1k_impress = 'time_decay_7day_convs_per_1k_impress'
        time_decay_7day_convs_per_click = 'time_decay_7day_convs_per_click'
        time_decay_7day_convs_per_visit = 'time_decay_7day_convs_per_visit'
        time_decay_7day_cpa = 'time_decay_7day_cpa'
        time_decay_7day_revenue = 'time_decay_7day_revenue'
        time_decay_7day_roas = 'time_decay_7day_roas'
        type = 'type'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'metric_scope': 'map',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AtlasCampaign,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_sets(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'filter_by': 'string',
            'metric_scope': 'map',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ad_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_business_unit(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.businessunit import BusinessUnit
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_unit',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessUnit,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessUnit, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_metrics_breakdown(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'dimensions': 'list<dimensions_enum>',
            'granularity': 'granularity_enum',
            'metric_scope': 'map',
            'order_by': 'list',
        }
        enums = {
            'dimensions_enum': [
                'AD_ID',
                'AD_SET_ID',
                'CAMPAIGN_ID',
                'DEVICE_TYPE',
                'SOURCE_CHANNEL',
            ],
            'granularity_enum': [
                'DAY',
                'HOUR',
                'MONTH',
                'WEEK_SUNDAY',
                'YEAR',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/metrics_breakdown',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_sources(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'filter_by': 'string',
            'metric_scope': 'map',
            'order_by': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sources',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'ad_platform': 'Object',
        'alias': 'string',
        'cost_per_1k_impressions': 'float',
        'cost_per_click': 'float',
        'cost_per_visit': 'float',
        'created_by': 'Object',
        'created_date': 'datetime',
        'data_driven_convs': 'float',
        'data_driven_convs_per_1k_impress': 'float',
        'data_driven_convs_per_click': 'float',
        'data_driven_convs_per_visit': 'float',
        'data_driven_cpa': 'float',
        'data_driven_nullable_convs': 'float',
        'data_driven_revenue': 'float',
        'data_driven_roas': 'float',
        'even_credit_convs': 'float',
        'even_credit_convs_per_1k_impress': 'float',
        'even_credit_convs_per_click': 'float',
        'even_credit_convs_per_visit': 'float',
        'even_credit_cpa': 'float',
        'even_credit_revenue': 'float',
        'even_credit_roas': 'float',
        'first_click_convs': 'float',
        'first_click_convs_per_1k_impress': 'float',
        'first_click_convs_per_click': 'float',
        'first_click_convs_per_visit': 'float',
        'first_click_cpa': 'float',
        'first_click_revenue': 'float',
        'first_click_roas': 'float',
        'first_touch_convs': 'float',
        'first_touch_convs_per_1k_impress': 'float',
        'first_touch_convs_per_click': 'float',
        'first_touch_convs_per_visit': 'float',
        'first_touch_cpa': 'float',
        'first_touch_revenue': 'float',
        'first_touch_roas': 'float',
        'id': 'string',
        'is_archived': 'bool',
        'last_click_convs': 'float',
        'last_click_convs_per_1k_impress': 'float',
        'last_click_convs_per_click': 'float',
        'last_click_convs_per_visit': 'float',
        'last_click_cpa': 'float',
        'last_click_revenue': 'float',
        'last_click_roas': 'float',
        'last_click_with_extrapolation_convs': 'float',
        'last_click_with_extrapolation_convs_per_100_clicks': 'float',
        'last_click_with_extrapolation_convs_per_1k_impress': 'float',
        'last_click_with_extrapolation_convs_per_click': 'float',
        'last_click_with_extrapolation_convs_per_visit': 'float',
        'last_click_with_extrapolation_cpa': 'float',
        'last_click_with_extrapolation_revenue': 'float',
        'last_click_with_extrapolation_roas': 'float',
        'last_click_with_extrapolation_unattributed': 'float',
        'last_modified_by': 'Object',
        'last_modified_date': 'datetime',
        'last_touch_convs': 'float',
        'last_touch_convs_per_1k_impress': 'float',
        'last_touch_convs_per_click': 'float',
        'last_touch_convs_per_visit': 'float',
        'last_touch_cpa': 'float',
        'last_touch_revenue': 'float',
        'last_touch_roas': 'float',
        'name': 'string',
        'net_media_cost': 'float',
        'positional_30fl_convs': 'float',
        'positional_30fl_convs_per_1k_impress': 'float',
        'positional_30fl_convs_per_click': 'float',
        'positional_30fl_convs_per_visit': 'float',
        'positional_30fl_cpa': 'float',
        'positional_30fl_revenue': 'float',
        'positional_30fl_roas': 'float',
        'positional_40fl_convs': 'float',
        'positional_40fl_convs_per_1k_impress': 'float',
        'positional_40fl_convs_per_click': 'float',
        'positional_40fl_convs_per_visit': 'float',
        'positional_40fl_cpa': 'float',
        'positional_40fl_revenue': 'float',
        'positional_40fl_roas': 'float',
        'report_click_through_rate': 'float',
        'report_clicks': 'int',
        'report_impressions': 'int',
        'report_visits': 'int',
        'time_decay_1day_convs': 'float',
        'time_decay_1day_convs_per_1k_impress': 'float',
        'time_decay_1day_convs_per_click': 'float',
        'time_decay_1day_convs_per_visit': 'float',
        'time_decay_1day_cpa': 'float',
        'time_decay_1day_revenue': 'float',
        'time_decay_1day_roas': 'float',
        'time_decay_7day_convs': 'float',
        'time_decay_7day_convs_per_1k_impress': 'float',
        'time_decay_7day_convs_per_click': 'float',
        'time_decay_7day_convs_per_visit': 'float',
        'time_decay_7day_cpa': 'float',
        'time_decay_7day_revenue': 'float',
        'time_decay_7day_roas': 'float',
        'type': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


