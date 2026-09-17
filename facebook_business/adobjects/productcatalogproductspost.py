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

class ProductCatalogProductsPost(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductCatalogProductsPost = True
        super(ProductCatalogProductsPost, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_image_cdn_urls = 'additional_image_cdn_urls'
        additional_image_urls = 'additional_image_urls'
        additional_variant_attributes = 'additional_variant_attributes'
        age_group = 'age_group'
        applinks = 'applinks'
        availability = 'availability'
        available_quantity_to_sell_on_facebook = 'available_quantity_to_sell_on_facebook'
        base_commission_rate = 'base_commission_rate'
        brand = 'brand'
        capabilities_disabled_by_user = 'capabilities_disabled_by_user'
        capability_features = 'capability_features'
        capability_to_review_status = 'capability_to_review_status'
        category = 'category'
        category_specific_fields = 'category_specific_fields'
        channels_to_integrity_status = 'channels_to_integrity_status'
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
        custom_number_0 = 'custom_number_0'
        custom_number_1 = 'custom_number_1'
        custom_number_2 = 'custom_number_2'
        custom_number_3 = 'custom_number_3'
        custom_number_4 = 'custom_number_4'
        da_display_preview_url = 'da_display_preview_url'
        description = 'description'
        enabled_capability_to_review_status = 'enabled_capability_to_review_status'
        errors = 'errors'
        expiration_date = 'expiration_date'
        fb_product_category = 'fb_product_category'
        gender = 'gender'
        gtin = 'gtin'
        id = 'id'
        image_cdn_urls = 'image_cdn_urls'
        image_fetch_status = 'image_fetch_status'
        image_url = 'image_url'
        images = 'images'
        importer_name = 'importer_name'
        invalidation_errors = 'invalidation_errors'
        inventory = 'inventory'
        is_bundle_hero = 'is_bundle_hero'
        manufacturer_info = 'manufacturer_info'
        manufacturer_part_number = 'manufacturer_part_number'
        material = 'material'
        mobile_link = 'mobile_link'
        name = 'name'
        ordering_index = 'ordering_index'
        origin_country = 'origin_country'
        override_details = 'override_details'
        pattern = 'pattern'
        post_conversion_signal_based_enforcement_appeal_eligibility = 'post_conversion_signal_based_enforcement_appeal_eligibility'
        price = 'price'
        product_catalog = 'product_catalog'
        product_feed = 'product_feed'
        product_group = 'product_group'
        product_priority_0 = 'product_priority_0'
        product_priority_1 = 'product_priority_1'
        product_priority_2 = 'product_priority_2'
        product_priority_3 = 'product_priority_3'
        product_priority_4 = 'product_priority_4'
        product_relationship = 'product_relationship'
        product_sets = 'product_sets'
        product_type = 'product_type'
        quantity_to_sell_on_facebook = 'quantity_to_sell_on_facebook'
        retailer_id = 'retailer_id'
        retailer_product_group_id = 'retailer_product_group_id'
        review_rejection_reasons = 'review_rejection_reasons'
        review_status = 'review_status'
        rich_text_description = 'rich_text_description'
        sale_price = 'sale_price'
        sale_price_end_date = 'sale_price_end_date'
        sale_price_start_date = 'sale_price_start_date'
        shipping_weight_unit = 'shipping_weight_unit'
        shipping_weight_value = 'shipping_weight_value'
        short_description = 'short_description'
        size = 'size'
        status = 'status'
        tags = 'tags'
        url = 'url'
        validation_errors = 'validation_errors'
        vendor_id = 'vendor_id'
        video_fetch_status = 'video_fetch_status'
        videos = 'videos'
        videos_metadata = 'videos_metadata'
        visibility = 'visibility'
        wa_compliance_category = 'wa_compliance_category'

    class AgeGroup:
        adult = 'ADULT'
        all_ages = 'ALL_AGES'
        infant = 'INFANT'
        kids = 'KIDS'
        newborn = 'NEWBORN'
        teen = 'TEEN'
        toddler = 'TODDLER'
        unknown = 'UNKNOWN'

    class Availability:
        available_for_order = 'AVAILABLE_FOR_ORDER'
        discontinued = 'DISCONTINUED'
        in_stock = 'IN_STOCK'
        mark_as_expired = 'MARK_AS_EXPIRED'
        mark_as_sold = 'MARK_AS_SOLD'
        out_of_stock = 'OUT_OF_STOCK'
        pending = 'PENDING'
        preorder = 'PREORDER'
        unknown = 'UNKNOWN'

    class Condition:
        pc_cpo = 'PC_CPO'
        pc_new = 'PC_NEW'
        pc_open_box_new = 'PC_OPEN_BOX_NEW'
        pc_refurbished = 'PC_REFURBISHED'
        pc_used = 'PC_USED'
        pc_used_fair = 'PC_USED_FAIR'
        pc_used_good = 'PC_USED_GOOD'
        pc_used_like_new = 'PC_USED_LIKE_NEW'
        unknown = 'UNKNOWN'

    class Gender:
        female = 'FEMALE'
        male = 'MALE'
        unisex = 'UNISEX'
        unknown = 'UNKNOWN'

    _field_types = {
        'additional_image_cdn_urls': 'list<list<object>>',
        'additional_image_urls': 'list<string>',
        'additional_variant_attributes': 'list<object>',
        'age_group': 'AgeGroup',
        'applinks': 'object',
        'availability': 'Availability',
        'available_quantity_to_sell_on_facebook': 'int',
        'base_commission_rate': 'int',
        'brand': 'string',
        'capabilities_disabled_by_user': 'list<string>',
        'capability_features': 'list<string>',
        'capability_to_review_status': 'list<object>',
        'category': 'string',
        'category_specific_fields': 'map<mixed, mixed>',
        'channels_to_integrity_status': 'object',
        'color': 'string',
        'commerce_insights': 'object',
        'condition': 'Condition',
        'currency': 'string',
        'custom_data': 'list<object>',
        'custom_label_0': 'string',
        'custom_label_1': 'string',
        'custom_label_2': 'string',
        'custom_label_3': 'string',
        'custom_label_4': 'string',
        'custom_number_0': 'string',
        'custom_number_1': 'string',
        'custom_number_2': 'string',
        'custom_number_3': 'string',
        'custom_number_4': 'string',
        'da_display_preview_url': 'string',
        'description': 'string',
        'enabled_capability_to_review_status': 'list<object>',
        'errors': 'list<object>',
        'expiration_date': 'string',
        'fb_product_category': 'string',
        'gender': 'Gender',
        'gtin': 'string',
        'id': 'int',
        'image_cdn_urls': 'list<object>',
        'image_fetch_status': 'string',
        'image_url': 'string',
        'images': 'list<string>',
        'importer_name': 'string',
        'invalidation_errors': 'list<object>',
        'inventory': 'int',
        'is_bundle_hero': 'bool',
        'manufacturer_info': 'string',
        'manufacturer_part_number': 'string',
        'material': 'string',
        'mobile_link': 'string',
        'name': 'string',
        'ordering_index': 'int',
        'origin_country': 'string',
        'override_details': 'object',
        'pattern': 'string',
        'post_conversion_signal_based_enforcement_appeal_eligibility': 'bool',
        'price': 'string',
        'product_catalog': 'object',
        'product_feed': 'object',
        'product_group': 'object',
        'product_priority_0': 'float',
        'product_priority_1': 'float',
        'product_priority_2': 'float',
        'product_priority_3': 'float',
        'product_priority_4': 'float',
        'product_relationship': 'string',
        'product_sets': 'object',
        'product_type': 'string',
        'quantity_to_sell_on_facebook': 'int',
        'retailer_id': 'string',
        'retailer_product_group_id': 'string',
        'review_rejection_reasons': 'list<string>',
        'review_status': 'string',
        'rich_text_description': 'string',
        'sale_price': 'string',
        'sale_price_end_date': 'string',
        'sale_price_start_date': 'string',
        'shipping_weight_unit': 'string',
        'shipping_weight_value': 'float',
        'short_description': 'string',
        'size': 'string',
        'status': 'string',
        'tags': 'list<string>',
        'url': 'string',
        'validation_errors': 'object',
        'vendor_id': 'string',
        'video_fetch_status': 'string',
        'videos': 'list<object>',
        'videos_metadata': 'object',
        'visibility': 'string',
        'wa_compliance_category': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AgeGroup'] = ProductCatalogProductsPost.AgeGroup.__dict__.values()
        field_enum_info['Availability'] = ProductCatalogProductsPost.Availability.__dict__.values()
        field_enum_info['Condition'] = ProductCatalogProductsPost.Condition.__dict__.values()
        field_enum_info['Gender'] = ProductCatalogProductsPost.Gender.__dict__.values()
        return field_enum_info


