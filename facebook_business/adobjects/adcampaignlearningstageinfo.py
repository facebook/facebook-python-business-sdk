# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCampaignLearningStageInfo(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCampaignLearningStageInfo, self).__init__()
        self._isAdCampaignLearningStageInfo = True
        self._api = api

    class Field(AbstractObject.Field):
        attribution_windows = 'attribution_windows'
        cas_segment = 'cas_segment'
        conversions = 'conversions'
        current_budget_prediction = 'current_budget_prediction'
        dynamic_lp_conversions_threshold = 'dynamic_lp_conversions_threshold'
        dynamic_lp_days_threshold = 'dynamic_lp_days_threshold'
        dynamic_lp_status = 'dynamic_lp_status'
        is_one_to_one_cbo_budget = 'is_one_to_one_cbo_budget'
        last_sig_edit_ts = 'last_sig_edit_ts'
        recommended_budget_prediction = 'recommended_budget_prediction'
        sigedit_removal = 'sigedit_removal'
        status = 'status'

    _field_types = {
        'attribution_windows': 'list<string>',
        'cas_segment': 'string',
        'conversions': 'unsigned int',
        'current_budget_prediction': 'Object',
        'dynamic_lp_conversions_threshold': 'unsigned int',
        'dynamic_lp_days_threshold': 'unsigned int',
        'dynamic_lp_status': 'string',
        'is_one_to_one_cbo_budget': 'bool',
        'last_sig_edit_ts': 'int',
        'recommended_budget_prediction': 'Object',
        'sigedit_removal': 'bool',
        'status': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


