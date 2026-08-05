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

class ProductCatalogHotelRoomsBatch(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductCatalogHotelRoomsBatch = True
        super(ProductCatalogHotelRoomsBatch, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        errors = 'errors'
        errors_total_count = 'errors_total_count'
        handle = 'handle'
        status = 'status'
        file = 'file'
        password = 'password'
        standard = 'standard'
        update_only = 'update_only'
        url = 'url'
        username = 'username'

    class Standard:
        google = 'google'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'hotel_rooms_batch'

    # @deprecated api_create is being deprecated
    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_hotel_rooms_batch(fields, params, batch, success, failure, pending)

    _field_types = {
        'errors': 'list<Object>',
        'errors_total_count': 'int',
        'handle': 'string',
        'status': 'string',
        'file': 'file',
        'password': 'string',
        'standard': 'Standard',
        'update_only': 'bool',
        'url': 'string',
        'username': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Standard'] = ProductCatalogHotelRoomsBatch.Standard.__dict__.values()
        return field_enum_info


