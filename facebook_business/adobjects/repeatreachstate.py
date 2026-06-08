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

class RepeatReachState(
    AbstractObject,
):

    def __init__(self, api=None):
        super(RepeatReachState, self).__init__()
        self._isRepeatReachState = True
        self._api = api

    class Field(AbstractObject.Field):
        current_saturation_level = 'current_saturation_level'
        forecasted_saturation_level = 'forecasted_saturation_level'
        high_saturation_threshold = 'high_saturation_threshold'
        should_display_cpr = 'should_display_cpr'

    _field_types = {
        'current_saturation_level': 'float',
        'forecasted_saturation_level': 'float',
        'high_saturation_threshold': 'float',
        'should_display_cpr': 'bool',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


