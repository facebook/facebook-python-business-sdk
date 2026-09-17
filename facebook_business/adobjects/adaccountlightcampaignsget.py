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

class AdAccountLightCampaignsGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdAccountLightCampaignsGet, self).__init__()
        self._isAdAccountLightCampaignsGet = True
        self._api = api

    class Field(AbstractObject.Field):
        data = 'data'
        paging = 'paging'
        summary = 'summary'

    class DatePreset:
        data_maximum = 'DATA_MAXIMUM'
        last_14d = 'LAST_14D'
        last_14_days = 'LAST_14_DAYS'
        last_180_days = 'LAST_180_DAYS'
        last_24m = 'LAST_24M'
        last_28d = 'LAST_28D'
        last_28_days = 'LAST_28_DAYS'
        last_2d = 'LAST_2D'
        last_2_days = 'LAST_2_DAYS'
        last_30d = 'LAST_30D'
        last_30_days = 'LAST_30_DAYS'
        last_3d = 'LAST_3D'
        last_3_days = 'LAST_3_DAYS'
        last_3_months = 'LAST_3_MONTHS'
        last_40d = 'LAST_40D'
        last_7d = 'LAST_7D'
        last_7_days = 'LAST_7_DAYS'
        last_8_days = 'LAST_8_DAYS'
        last_90d = 'LAST_90D'
        last_90_days = 'LAST_90_DAYS'
        last_month = 'LAST_MONTH'
        last_nd_3_2 = 'LAST_ND_3_2'
        last_nd_4_3 = 'LAST_ND_4_3'
        last_nd_5_4 = 'LAST_ND_5_4'
        last_nd_6_5 = 'LAST_ND_6_5'
        last_nd_7_6 = 'LAST_ND_7_6'
        last_nd_8_7 = 'LAST_ND_8_7'
        last_nm_1_0 = 'LAST_NM_1_0'
        last_nm_2_0 = 'LAST_NM_2_0'
        last_nm_3_0 = 'LAST_NM_3_0'
        last_nm_3_2 = 'LAST_NM_3_2'
        last_nm_4_3 = 'LAST_NM_4_3'
        last_nm_5_4 = 'LAST_NM_5_4'
        last_nq_2_0 = 'LAST_NQ_2_0'
        last_nq_2_1 = 'LAST_NQ_2_1'
        last_nq_3_0 = 'LAST_NQ_3_0'
        last_nq_3_1 = 'LAST_NQ_3_1'
        last_quarter = 'LAST_QUARTER'
        last_week = 'LAST_WEEK'
        last_week_mon_sun = 'LAST_WEEK_MON_SUN'
        last_week_sun_sat = 'LAST_WEEK_SUN_SAT'
        last_year = 'LAST_YEAR'
        lifetime = 'LIFETIME'
        maximum = 'MAXIMUM'
        none = 'NONE'
        this_month = 'THIS_MONTH'
        this_month_no_today = 'THIS_MONTH_NO_TODAY'
        this_quarter = 'THIS_QUARTER'
        this_week = 'THIS_WEEK'
        this_week_mon_no_today = 'THIS_WEEK_MON_NO_TODAY'
        this_week_mon_today = 'THIS_WEEK_MON_TODAY'
        this_week_sun_no_today = 'THIS_WEEK_SUN_NO_TODAY'
        this_week_sun_today = 'THIS_WEEK_SUN_TODAY'
        this_year = 'THIS_YEAR'
        today = 'TODAY'
        yesterday = 'YESTERDAY'

    _field_types = {
        'data': 'list<object>',
        'paging': 'object',
        'summary': 'object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DatePreset'] = AdAccountLightCampaignsGet.DatePreset.__dict__.values()
        return field_enum_info


