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

class AdCampaignGroupGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCampaignGroupGet = True
        super(AdCampaignGroupGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        advantage_state_info = 'advantage_state_info'
        bid_strategy = 'bid_strategy'
        budget_remaining = 'budget_remaining'
        buying_type = 'buying_type'
        configured_status = 'configured_status'
        created_time = 'created_time'
        daily_budget = 'daily_budget'
        effective_status = 'effective_status'
        id = 'id'
        lifetime_budget = 'lifetime_budget'
        name = 'name'
        objective = 'objective'
        promoted_object = 'promoted_object'
        special_ad_categories = 'special_ad_categories'
        spend_cap = 'spend_cap'
        start_time = 'start_time'
        status = 'status'
        stop_time = 'stop_time'
        updated_time = 'updated_time'

    _field_types = {
        'account_id': 'string',
        'advantage_state_info': 'object',
        'bid_strategy': 'string',
        'budget_remaining': 'string',
        'buying_type': 'string',
        'configured_status': 'string',
        'created_time': 'string',
        'daily_budget': 'string',
        'effective_status': 'string',
        'id': 'string',
        'lifetime_budget': 'string',
        'name': 'string',
        'objective': 'string',
        'promoted_object': 'object',
        'special_ad_categories': 'list<string>',
        'spend_cap': 'string',
        'start_time': 'string',
        'status': 'string',
        'stop_time': 'string',
        'updated_time': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


