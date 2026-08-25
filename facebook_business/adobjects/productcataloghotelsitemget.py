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

class ProductCatalogHotelsItemGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductCatalogHotelsItemGet = True
        super(ProductCatalogHotelsItemGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_image_urls = 'additional_image_urls'
        address = 'address'
        applink_android_app_name = 'applink_android_app_name'
        applink_android_class = 'applink_android_class'
        applink_android_package = 'applink_android_package'
        applink_android_url = 'applink_android_url'
        applink_ios_app_name = 'applink_ios_app_name'
        applink_ios_app_store_id = 'applink_ios_app_store_id'
        applink_ios_url = 'applink_ios_url'
        applinks = 'applinks'
        brand = 'brand'
        category = 'category'
        currency = 'currency'
        custom_label_0 = 'custom_label_0'
        custom_label_1 = 'custom_label_1'
        custom_label_2 = 'custom_label_2'
        custom_label_3 = 'custom_label_3'
        custom_label_4 = 'custom_label_4'
        custom_number_0 = 'custom_number_0'
        custom_number_1 = 'custom_number_1'
        custom_number_2 = 'custom_number_2'
        custom_number_3 = 'custom_number_3'
        custom_number_4 = 'custom_number_4'
        da_display_preview_url = 'da_display_preview_url'
        description = 'description'
        guest_ratings = 'guest_ratings'
        hotel_id = 'hotel_id'
        id = 'id'
        image_fetch_status = 'image_fetch_status'
        image_url = 'image_url'
        images = 'images'
        lowest_base_price = 'lowest_base_price'
        loyalty_program = 'loyalty_program'
        margin_level = 'margin_level'
        name = 'name'
        number_of_rooms = 'number_of_rooms'
        phone = 'phone'
        price = 'price'
        product_priority_0 = 'product_priority_0'
        product_priority_1 = 'product_priority_1'
        product_priority_2 = 'product_priority_2'
        product_priority_3 = 'product_priority_3'
        product_priority_4 = 'product_priority_4'
        retailer_id = 'retailer_id'
        sale_price = 'sale_price'
        sanitized_images = 'sanitized_images'
        star_rating = 'star_rating'
        tags = 'tags'
        url = 'url'
        video_urls = 'video_urls'
        videos_metadata = 'videos_metadata'
        visibility = 'visibility'

    class DisplayFormat:
        carousel_ad = 'CAROUSEL_AD'
        shops_pdp = 'SHOPS_PDP'
        single_ad = 'SINGLE_AD'

    _field_types = {
        'additional_image_urls': 'list<string>',
        'address': 'string',
        'applink_android_app_name': 'string',
        'applink_android_class': 'string',
        'applink_android_package': 'string',
        'applink_android_url': 'string',
        'applink_ios_app_name': 'string',
        'applink_ios_app_store_id': 'int',
        'applink_ios_url': 'string',
        'applinks': 'object',
        'brand': 'string',
        'category': 'string',
        'currency': 'string',
        'custom_label_0': 'string',
        'custom_label_1': 'string',
        'custom_label_2': 'string',
        'custom_label_3': 'string',
        'custom_label_4': 'string',
        'custom_number_0': 'int',
        'custom_number_1': 'int',
        'custom_number_2': 'int',
        'custom_number_3': 'int',
        'custom_number_4': 'int',
        'da_display_preview_url': 'string',
        'description': 'string',
        'guest_ratings': 'string',
        'hotel_id': 'string',
        'id': 'int',
        'image_fetch_status': 'string',
        'image_url': 'string',
        'images': 'list<string>',
        'lowest_base_price': 'string',
        'loyalty_program': 'string',
        'margin_level': 'int',
        'name': 'string',
        'number_of_rooms': 'int',
        'phone': 'string',
        'price': 'string',
        'product_priority_0': 'float',
        'product_priority_1': 'float',
        'product_priority_2': 'float',
        'product_priority_3': 'float',
        'product_priority_4': 'float',
        'retailer_id': 'string',
        'sale_price': 'string',
        'sanitized_images': 'list<string>',
        'star_rating': 'float',
        'tags': 'list<string>',
        'url': 'string',
        'video_urls': 'list<string>',
        'videos_metadata': 'object',
        'visibility': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DisplayFormat'] = ProductCatalogHotelsItemGet.DisplayFormat.__dict__.values()
        return field_enum_info


