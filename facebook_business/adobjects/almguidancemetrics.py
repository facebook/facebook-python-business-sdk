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

class ALMGuidanceMetrics(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ALMGuidanceMetrics, self).__init__()
        self._isALMGuidanceMetrics = True
        self._api = api

    class Field(AbstractObject.Field):
        ad_account_id = 'ad_account_id'
        adopted_objects = 'adopted_objects'
        guidance_name = 'guidance_name'
        guidance_type = 'guidance_type'
        l28_adoption = 'l28_adoption'
        l28_available = 'l28_available'
        l28_click = 'l28_click'
        l28_conversion = 'l28_conversion'
        l28_impression = 'l28_impression'
        l28_pitch = 'l28_pitch'
        last_pitch_ds = 'last_pitch_ds'
        parent_advertiser_id = 'parent_advertiser_id'
        report_ds = 'report_ds'

    _field_types = {
        'ad_account_id': 'string',
        'adopted_objects': 'list<Object>',
        'guidance_name': 'string',
        'guidance_type': 'string',
        'l28_adoption': 'int',
        'l28_available': 'int',
        'l28_click': 'int',
        'l28_conversion': 'int',
        'l28_impression': 'int',
        'l28_pitch': 'int',
        'last_pitch_ds': 'string',
        'parent_advertiser_id': 'string',
        'report_ds': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


