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

class PageCTXBudgetDFOBudgetRecommendation(
    AbstractObject,
):

    def __init__(self, api=None):
        super(PageCTXBudgetDFOBudgetRecommendation, self).__init__()
        self._isPageCTXBudgetDFOBudgetRecommendation = True
        self._api = api

    class Field(AbstractObject.Field):
        budget = 'budget'
        budget_leads = 'budget_leads'
        budget_new_model = 'budget_new_model'
        budget_purchases = 'budget_purchases'
        budget_value = 'budget_value'
        budget_without_threshold = 'budget_without_threshold'
        reported_conversion = 'reported_conversion'
        reported_conversion_leads = 'reported_conversion_leads'
        reported_conversion_purchases = 'reported_conversion_purchases'
        reported_conversion_value = 'reported_conversion_value'
        reported_conversions_new_model = 'reported_conversions_new_model'
        reported_conversions_without_threshold = 'reported_conversions_without_threshold'
        zo_budget = 'zo_budget'
        zo_budget_leads = 'zo_budget_leads'
        zo_budget_purchases = 'zo_budget_purchases'
        zo_budget_value = 'zo_budget_value'

    _field_types = {
        'budget': 'string',
        'budget_leads': 'string',
        'budget_new_model': 'string',
        'budget_purchases': 'string',
        'budget_value': 'string',
        'budget_without_threshold': 'string',
        'reported_conversion': 'string',
        'reported_conversion_leads': 'string',
        'reported_conversion_purchases': 'string',
        'reported_conversion_value': 'string',
        'reported_conversions_new_model': 'string',
        'reported_conversions_without_threshold': 'string',
        'zo_budget': 'string',
        'zo_budget_leads': 'string',
        'zo_budget_purchases': 'string',
        'zo_budget_value': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


