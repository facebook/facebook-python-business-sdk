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

class ProductSetProducts(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductSetProducts = True
        super(ProductSetProducts, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        id = 'id'

    def genget(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.productsetproductsget import ProductSetProductsGet
        param_types = {
            'after': 'string',
            'before': 'string',
            'dedupe_by_group_id_for_small_catalogs': 'string',
            'dedupe_items_by_group': 'string',
            'display_format': 'display_format_enum',
            'enable_typeahead': 'string',
            'error_priority': 'error_priority_enum',
            'error_type': 'error_type_enum',
            'fields': 'string',
            'filter': 'string',
            'limit': 'int',
            'sort': 'string',
            'summary': 'string',
        }
        enums = {
            'display_format_enum': ProductSetProductsGet.DisplayFormat.__dict__.values(),
            'error_priority_enum': ProductSetProductsGet.ErrorPriority.__dict__.values(),
            'error_type_enum': ProductSetProductsGet.ErrorType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/products',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductSetProductsGet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductSetProductsGet, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


