# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

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

class AdsInsightsCampaign(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsInsightsCampaign = True
        super(AdsInsightsCampaign, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        id = 'id'

    def genget(self, fields=None, params=None, is_async=False, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.adsinsightscampaignget import AdsInsightsCampaignGet
        if is_async:
          return self.get_insights_async(fields, params, batch, success, failure, pending)
        param_types = {
            'action_attribution_windows': 'string',
            'action_breakdowns': 'string',
            'action_report_time': 'string',
            'after': 'string',
            'am_call_tags': 'string',
            'before': 'string',
            'breakdowns': 'string',
            'comparison_fields': 'string',
            'comparison_time_ranges': 'string',
            'date_preset': 'string',
            'debug_enable_trace': 'bool',
            'default_attribution_windows': 'string',
            'default_summary': 'bool',
            'e2e_scenario_run_id': 'string',
            'export_columns': 'string',
            'export_format': 'string',
            'export_name': 'string',
            'fields': 'string',
            'filtering': 'string',
            'flog': 'string',
            'graph_cache': 'bool',
            'include_zeros': 'bool',
            'level': 'string',
            'limit': 'int',
            'meta_breakdowns': 'string',
            'product_id_limit': 'int',
            'round_up_level': 'string',
            'run_id': 'string',
            'saber_setsuna_perf_request_id': 'string',
            'sort': 'string',
            'summary': 'string',
            'summary_action_breakdowns': 'string',
            'time_increment': 'string',
            'time_range': 'string',
            'time_ranges': 'string',
            'use_account_attribution_setting': 'bool',
            'use_unified_attribution_setting': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsInsightsCampaignGet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsInsightsCampaignGet, api=self._api),
            include_summary=False,
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
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


