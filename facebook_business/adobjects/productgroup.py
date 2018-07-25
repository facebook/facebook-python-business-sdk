# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

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

class ProductGroup(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductGroup = True
        super(ProductGroup, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        id = 'id'
        product_catalog = 'product_catalog'
        retailer_id = 'retailer_id'
        variants = 'variants'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'product_groups'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_product_group(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductGroup,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'default_product_id': 'string',
            'variants': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductGroup,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_products(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productitem import ProductItem
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/products',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductItem, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_product(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productitem import ProductItem
        param_types = {
            'additional_image_urls': 'list<string>',
            'additional_variant_attributes': 'Object',
            'android_app_name': 'string',
            'android_class': 'string',
            'android_package': 'string',
            'android_url': 'string',
            'availability': 'availability_enum',
            'brand': 'string',
            'category': 'string',
            'checkout_url': 'string',
            'color': 'string',
            'condition': 'condition_enum',
            'currency': 'string',
            'custom_data': 'map',
            'custom_label_0': 'string',
            'custom_label_1': 'string',
            'custom_label_2': 'string',
            'custom_label_3': 'string',
            'custom_label_4': 'string',
            'description': 'string',
            'expiration_date': 'string',
            'gender': 'gender_enum',
            'gtin': 'string',
            'image_url': 'Object',
            'inventory': 'unsigned int',
            'ios_app_name': 'string',
            'ios_app_store_id': 'unsigned int',
            'ios_url': 'string',
            'ipad_app_name': 'string',
            'ipad_app_store_id': 'unsigned int',
            'ipad_url': 'string',
            'iphone_app_name': 'string',
            'iphone_app_store_id': 'unsigned int',
            'iphone_url': 'string',
            'manufacturer_part_number': 'string',
            'material': 'string',
            'mobile_link': 'Object',
            'name': 'string',
            'offer_price_amount': 'unsigned int',
            'offer_price_end_date': 'Object',
            'offer_price_start_date': 'Object',
            'ordering_index': 'unsigned int',
            'pattern': 'string',
            'price': 'unsigned int',
            'product_type': 'string',
            'retailer_id': 'string',
            'sale_price': 'unsigned int',
            'sale_price_end_date': 'datetime',
            'sale_price_start_date': 'datetime',
            'short_description': 'string',
            'size': 'string',
            'start_date': 'string',
            'url': 'Object',
            'visibility': 'visibility_enum',
            'windows_phone_app_id': 'string',
            'windows_phone_app_name': 'string',
            'windows_phone_url': 'string',
        }
        enums = {
            'availability_enum': ProductItem.Availability.__dict__.values(),
            'condition_enum': ProductItem.Condition.__dict__.values(),
            'gender_enum': ProductItem.Gender.__dict__.values(),
            'visibility_enum': ProductItem.Visibility.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/products',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductItem, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'id': 'string',
        'product_catalog': 'ProductCatalog',
        'retailer_id': 'string',
        'variants': 'list<ProductVariant>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
