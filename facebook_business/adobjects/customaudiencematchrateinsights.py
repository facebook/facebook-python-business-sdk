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

class CustomAudienceMatchRateInsights(
    AbstractObject,
):

    def __init__(self, api=None):
        super(CustomAudienceMatchRateInsights, self).__init__()
        self._isCustomAudienceMatchRateInsights = True
        self._api = api

    class Field(AbstractObject.Field):
        email_quality = 'email_quality'
        email_upload_volume_pct = 'email_upload_volume_pct'
        is_eligible = 'is_eligible'
        madid_quality = 'madid_quality'
        madid_upload_volume_pct = 'madid_upload_volume_pct'
        match_rate_score = 'match_rate_score'
        phone_quality = 'phone_quality'
        phone_upload_volume_pct = 'phone_upload_volume_pct'

    _field_types = {
        'email_quality': 'string',
        'email_upload_volume_pct': 'float',
        'is_eligible': 'bool',
        'madid_quality': 'string',
        'madid_upload_volume_pct': 'float',
        'match_rate_score': 'float',
        'phone_quality': 'string',
        'phone_upload_volume_pct': 'float',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


