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

class HighDemandPeriodGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isHighDemandPeriodGet = True
        super(HighDemandPeriodGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_object_id = 'ad_object_id'
        budget_value = 'budget_value'
        budget_value_type = 'budget_value_type'
        id = 'id'
        recurrence_type = 'recurrence_type'
        time_end = 'time_end'
        time_start = 'time_start'
        weekly_schedule = 'weekly_schedule'

    _field_types = {
        'ad_object_id': 'string',
        'budget_value': 'int',
        'budget_value_type': 'string',
        'id': 'string',
        'recurrence_type': 'string',
        'time_end': 'string',
        'time_start': 'string',
        'weekly_schedule': 'list<object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


