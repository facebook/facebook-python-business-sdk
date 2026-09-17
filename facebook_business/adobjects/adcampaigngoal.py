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

class AdCampaignGoal(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCampaignGoal, self).__init__()
        self._isAdCampaignGoal = True
        self._api = api

    class Field(AbstractObject.Field):
        engaged_audiences_audience_label_exclusions = 'engaged_audiences_audience_label_exclusions'
        engaged_audiences_audience_label_inclusions = 'engaged_audiences_audience_label_inclusions'
        engaged_audiences_exclusions = 'engaged_audiences_exclusions'
        engaged_audiences_inclusions = 'engaged_audiences_inclusions'
        existing_customers_audience_label_exclusions = 'existing_customers_audience_label_exclusions'
        existing_customers_audience_label_inclusions = 'existing_customers_audience_label_inclusions'
        existing_customers_auto_exclusion_retention_days = 'existing_customers_auto_exclusion_retention_days'
        existing_customers_exclusion_auto_selection_state = 'existing_customers_exclusion_auto_selection_state'
        existing_customers_exclusions = 'existing_customers_exclusions'
        existing_customers_inclusions = 'existing_customers_inclusions'
        is_ca_expansion_enabled = 'is_ca_expansion_enabled'
        is_lookalike_inclusion_enabled = 'is_lookalike_inclusion_enabled'
        lookalike_inclusions = 'lookalike_inclusions'
        type = 'type'

    _field_types = {
        'engaged_audiences_audience_label_exclusions': 'list<string>',
        'engaged_audiences_audience_label_inclusions': 'list<string>',
        'engaged_audiences_exclusions': 'list<string>',
        'engaged_audiences_inclusions': 'list<string>',
        'existing_customers_audience_label_exclusions': 'list<string>',
        'existing_customers_audience_label_inclusions': 'list<string>',
        'existing_customers_auto_exclusion_retention_days': 'int',
        'existing_customers_exclusion_auto_selection_state': 'int',
        'existing_customers_exclusions': 'list<string>',
        'existing_customers_inclusions': 'list<string>',
        'is_ca_expansion_enabled': 'bool',
        'is_lookalike_inclusion_enabled': 'bool',
        'lookalike_inclusions': 'list<string>',
        'type': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


