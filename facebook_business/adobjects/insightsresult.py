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

class InsightsResult(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isInsightsResult = True
        super(InsightsResult, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        description = 'description'
        description_from_api_doc = 'description_from_api_doc'
        id = 'id'
        name = 'name'
        period = 'period'
        title = 'title'
        values = 'values'

    class DatePreset:
        data_maximum = 'data_maximum'
        last_14d = 'last_14d'
        last_28d = 'last_28d'
        last_30d = 'last_30d'
        last_3d = 'last_3d'
        last_7d = 'last_7d'
        last_90d = 'last_90d'
        last_month = 'last_month'
        last_quarter = 'last_quarter'
        last_week_mon_sun = 'last_week_mon_sun'
        last_week_sun_sat = 'last_week_sun_sat'
        last_year = 'last_year'
        maximum = 'maximum'
        this_month = 'this_month'
        this_quarter = 'this_quarter'
        this_week_mon_today = 'this_week_mon_today'
        this_week_sun_today = 'this_week_sun_today'
        this_year = 'this_year'
        today = 'today'
        yesterday = 'yesterday'

    class Period:
        day = 'day'
        days_28 = 'days_28'
        lifetime = 'lifetime'
        month = 'month'
        total_over_range = 'total_over_range'
        week = 'week'

    _field_types = {
        'description': 'string',
        'description_from_api_doc': 'string',
        'id': 'string',
        'name': 'string',
        'period': 'string',
        'title': 'string',
        'values': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DatePreset'] = InsightsResult.DatePreset.__dict__.values()
        field_enum_info['Period'] = InsightsResult.Period.__dict__.values()
        return field_enum_info


