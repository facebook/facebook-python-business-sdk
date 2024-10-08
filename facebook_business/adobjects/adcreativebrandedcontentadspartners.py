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

class AdCreativeBrandedContentAdsPartners(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeBrandedContentAdsPartners, self).__init__()
        self._isAdCreativeBrandedContentAdsPartners = True
        self._api = api

    class Field(AbstractObject.Field):
        fb_page_id = 'fb_page_id'
        has_create_ads_access = 'has_create_ads_access'
        identity_type = 'identity_type'
        ig_asset_id = 'ig_asset_id'
        ig_user_id = 'ig_user_id'

    _field_types = {
        'fb_page_id': 'string',
        'has_create_ads_access': 'bool',
        'identity_type': 'string',
        'ig_asset_id': 'string',
        'ig_user_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


