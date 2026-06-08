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

class ProductGroupGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductGroupGet = True
        super(ProductGroupGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        id = 'id'
        mini_shops_product_sets_count = 'mini_shops_product_sets_count'
        product_catalog = 'product_catalog'
        products = 'products'
        representative_item_id = 'representative_item_id'
        retailer_id = 'retailer_id'
        variants = 'variants'

    _field_types = {
        'id': 'int',
        'mini_shops_product_sets_count': 'int',
        'product_catalog': 'object',
        'products': 'object',
        'representative_item_id': 'string',
        'retailer_id': 'string',
        'variants': 'list<object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


