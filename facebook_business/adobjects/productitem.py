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

class ProductItem(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductItem = True
        super(ProductItem, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_image_cdn_urls = 'additional_image_cdn_urls'
        additional_image_urls = 'additional_image_urls'
        additional_variant_attributes = 'additional_variant_attributes'
        age_group = 'age_group'
        applinks = 'applinks'
        availability = 'availability'
        brand = 'brand'
        capability_to_review_status = 'capability_to_review_status'
        category = 'category'
        color = 'color'
        commerce_insights = 'commerce_insights'
        condition = 'condition'
        currency = 'currency'
        custom_data = 'custom_data'
        custom_label_0 = 'custom_label_0'
        custom_label_1 = 'custom_label_1'
        custom_label_2 = 'custom_label_2'
        custom_label_3 = 'custom_label_3'
        custom_label_4 = 'custom_label_4'
        description = 'description'
        expiration_date = 'expiration_date'
        gender = 'gender'
        gtin = 'gtin'
        id = 'id'
        image_cdn_urls = 'image_cdn_urls'
        image_url = 'image_url'
        inventory = 'inventory'
        manufacturer_part_number = 'manufacturer_part_number'
        material = 'material'
        mobile_link = 'mobile_link'
        name = 'name'
        ordering_index = 'ordering_index'
        pattern = 'pattern'
        price = 'price'
        product_catalog = 'product_catalog'
        product_feed = 'product_feed'
        product_group = 'product_group'
        product_type = 'product_type'
        retailer_id = 'retailer_id'
        retailer_product_group_id = 'retailer_product_group_id'
        review_rejection_reasons = 'review_rejection_reasons'
        review_status = 'review_status'
        sale_price = 'sale_price'
        sale_price_end_date = 'sale_price_end_date'
        sale_price_start_date = 'sale_price_start_date'
        shipping_weight_unit = 'shipping_weight_unit'
        shipping_weight_value = 'shipping_weight_value'
        short_description = 'short_description'
        size = 'size'
        start_date = 'start_date'
        url = 'url'
        visibility = 'visibility'
        checkout_url = 'checkout_url'
        offer_price_amount = 'offer_price_amount'
        offer_price_end_date = 'offer_price_end_date'
        offer_price_start_date = 'offer_price_start_date'
        ios_url = 'ios_url'
        ios_app_store_id = 'ios_app_store_id'
        ios_app_name = 'ios_app_name'
        iphone_url = 'iphone_url'
        iphone_app_store_id = 'iphone_app_store_id'
        iphone_app_name = 'iphone_app_name'
        ipad_url = 'ipad_url'
        ipad_app_store_id = 'ipad_app_store_id'
        ipad_app_name = 'ipad_app_name'
        android_url = 'android_url'
        android_package = 'android_package'
        android_class = 'android_class'
        android_app_name = 'android_app_name'
        windows_phone_url = 'windows_phone_url'
        windows_phone_app_id = 'windows_phone_app_id'
        windows_phone_app_name = 'windows_phone_app_name'

    class AgeGroup:
        adult = 'adult'
        all_ages = 'all ages'
        infant = 'infant'
        kids = 'kids'
        newborn = 'newborn'
        teen = 'teen'
        toddler = 'toddler'

    class Availability:
        available_for_order = 'available for order'
        discontinued = 'discontinued'
        in_stock = 'in stock'
        out_of_stock = 'out of stock'
        pending = 'pending'
        preorder = 'preorder'

    class Condition:
        cpo = 'cpo'
        new = 'new'
        open_box_new = 'open_box_new'
        refurbished = 'refurbished'
        used = 'used'

    class Gender:
        female = 'female'
        male = 'male'
        unisex = 'unisex'

    class ReviewStatus:
        approved = 'approved'
        outdated = 'outdated'
        pending = 'pending'
        rejected = 'rejected'

    class ShippingWeightUnit:
        value_g = 'g'
        kg = 'kg'
        lb = 'lb'
        oz = 'oz'

    class Visibility:
        published = 'published'
        staging = 'staging'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'products'

    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_product(fields, params, batch, success, failure, pending)

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'image_height': 'unsigned int',
            'image_width': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
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

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'availability': 'availability_enum',
            'brand': 'string',
            'category': 'string',
            'currency': 'string',
            'condition': 'condition_enum',
            'description': 'string',
            'image_url': 'string',
            'name': 'string',
            'price': 'unsigned int',
            'product_type': 'string',
            'url': 'string',
            'visibility': 'visibility_enum',
            'additional_image_urls': 'list<string>',
            'additional_variant_attributes': 'map',
            'checkout_url': 'string',
            'color': 'string',
            'custom_data': 'map',
            'custom_label_0': 'string',
            'custom_label_1': 'string',
            'custom_label_2': 'string',
            'custom_label_3': 'string',
            'custom_label_4': 'string',
            'expiration_date': 'string',
            'gender': 'gender_enum',
            'gtin': 'string',
            'inventory': 'unsigned int',
            'manufacturer_part_number': 'string',
            'mobile_link': 'string',
            'material': 'string',
            'offer_price_amount': 'unsigned int',
            'offer_price_end_date': 'datetime',
            'offer_price_start_date': 'datetime',
            'ordering_index': 'unsigned int',
            'pattern': 'string',
            'sale_price': 'unsigned int',
            'sale_price_end_date': 'datetime',
            'sale_price_start_date': 'datetime',
            'short_description': 'string',
            'size': 'string',
            'start_date': 'string',
            'ios_url': 'string',
            'ios_app_store_id': 'unsigned int',
            'ios_app_name': 'string',
            'iphone_url': 'string',
            'iphone_app_store_id': 'unsigned int',
            'iphone_app_name': 'string',
            'ipad_url': 'string',
            'ipad_app_store_id': 'unsigned int',
            'ipad_app_name': 'string',
            'android_url': 'string',
            'android_package': 'string',
            'android_class': 'string',
            'android_app_name': 'string',
            'windows_phone_url': 'string',
            'windows_phone_app_id': 'string',
            'windows_phone_app_name': 'string',
            'retailer_id': 'string',
        }
        enums = {
            'availability_enum': ProductItem.Availability.__dict__.values(),
            'condition_enum': ProductItem.Condition.__dict__.values(),
            'visibility_enum': ProductItem.Visibility.__dict__.values(),
            'gender_enum': ProductItem.Gender.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
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

    def create_comment(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.comment import Comment
        param_types = {
            'object_id': 'string',
            'parent_comment_id': 'Object',
            'nectar_module': 'string',
            'attachment_id': 'string',
            'attachment_url': 'string',
            'attachment_share_url': 'string',
            'feedback_source': 'string',
            'facepile_mentioned_ids': 'list<string>',
            'is_offline': 'bool',
            'comment_privacy_value': 'comment_privacy_value_enum',
            'message': 'string',
            'text': 'string',
            'tracking': 'string',
        }
        enums = {
            'comment_privacy_value_enum': Comment.CommentPrivacyValue.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
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

    def get_product_sets(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.productset import ProductSet
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductSet, api=self._api),
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
        'additional_image_cdn_urls': 'list<map<string, string>>',
        'additional_image_urls': 'list<string>',
        'additional_variant_attributes': 'map<string, string>',
        'age_group': 'AgeGroup',
        'applinks': 'AppLinks',
        'availability': 'Availability',
        'brand': 'string',
        'capability_to_review_status': 'map<Object, Object>',
        'category': 'string',
        'color': 'string',
        'commerce_insights': 'ProductItemCommerceInsights',
        'condition': 'Condition',
        'currency': 'string',
        'custom_data': 'map<string, string>',
        'custom_label_0': 'string',
        'custom_label_1': 'string',
        'custom_label_2': 'string',
        'custom_label_3': 'string',
        'custom_label_4': 'string',
        'description': 'string',
        'expiration_date': 'string',
        'gender': 'Gender',
        'gtin': 'string',
        'id': 'string',
        'image_cdn_urls': 'map<string, string>',
        'image_url': 'string',
        'inventory': 'int',
        'manufacturer_part_number': 'string',
        'material': 'string',
        'mobile_link': 'string',
        'name': 'string',
        'ordering_index': 'int',
        'pattern': 'string',
        'price': 'string',
        'product_catalog': 'ProductCatalog',
        'product_feed': 'ProductFeed',
        'product_group': 'ProductGroup',
        'product_type': 'string',
        'retailer_id': 'string',
        'retailer_product_group_id': 'string',
        'review_rejection_reasons': 'list<string>',
        'review_status': 'ReviewStatus',
        'sale_price': 'string',
        'sale_price_end_date': 'string',
        'sale_price_start_date': 'string',
        'shipping_weight_unit': 'ShippingWeightUnit',
        'shipping_weight_value': 'float',
        'short_description': 'string',
        'size': 'string',
        'start_date': 'string',
        'url': 'string',
        'visibility': 'Visibility',
        'checkout_url': 'string',
        'offer_price_amount': 'unsigned int',
        'offer_price_end_date': 'datetime',
        'offer_price_start_date': 'datetime',
        'ios_url': 'string',
        'ios_app_store_id': 'unsigned int',
        'ios_app_name': 'string',
        'iphone_url': 'string',
        'iphone_app_store_id': 'unsigned int',
        'iphone_app_name': 'string',
        'ipad_url': 'string',
        'ipad_app_store_id': 'unsigned int',
        'ipad_app_name': 'string',
        'android_url': 'string',
        'android_package': 'string',
        'android_class': 'string',
        'android_app_name': 'string',
        'windows_phone_url': 'string',
        'windows_phone_app_id': 'string',
        'windows_phone_app_name': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AgeGroup'] = ProductItem.AgeGroup.__dict__.values()
        field_enum_info['Availability'] = ProductItem.Availability.__dict__.values()
        field_enum_info['Condition'] = ProductItem.Condition.__dict__.values()
        field_enum_info['Gender'] = ProductItem.Gender.__dict__.values()
        field_enum_info['ReviewStatus'] = ProductItem.ReviewStatus.__dict__.values()
        field_enum_info['ShippingWeightUnit'] = ProductItem.ShippingWeightUnit.__dict__.values()
        field_enum_info['Visibility'] = ProductItem.Visibility.__dict__.values()
        return field_enum_info


