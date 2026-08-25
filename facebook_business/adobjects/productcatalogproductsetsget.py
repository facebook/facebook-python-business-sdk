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

class ProductCatalogProductSetsGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductCatalogProductSetsGet, self).__init__()
        self._isProductCatalogProductSetsGet = True
        self._api = api

    class Field(AbstractObject.Field):
        data = 'data'
        paging = 'paging'
        summary = 'summary'

    class IntegratedCheckoutEligibility:
        eligible = 'ELIGIBLE'
        not_eligible = 'NOT_ELIGIBLE'

    class IntegratedCheckoutPartner:
        amazon = 'AMAZON'
        jest_e2e_amazon = 'JEST_E2E_AMAZON'
        lowes = 'LOWES'
        meli = 'MELI'
        none = 'NONE'
        shein = 'SHEIN'
        shopee_id = 'SHOPEE_ID'
        shopee_my = 'SHOPEE_MY'
        shopee_ph = 'SHOPEE_PH'
        shopee_sg = 'SHOPEE_SG'
        shopee_th = 'SHOPEE_TH'
        shopee_tw = 'SHOPEE_TW'
        shopee_vn = 'SHOPEE_VN'
        walmart = 'WALMART'
        zalando = 'ZALANDO'

    _field_types = {
        'data': 'list<object>',
        'paging': 'object',
        'summary': 'object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['IntegratedCheckoutEligibility'] = ProductCatalogProductSetsGet.IntegratedCheckoutEligibility.__dict__.values()
        field_enum_info['IntegratedCheckoutPartner'] = ProductCatalogProductSetsGet.IntegratedCheckoutPartner.__dict__.values()
        return field_enum_info


