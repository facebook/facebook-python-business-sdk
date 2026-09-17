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

class ProductSetProductsGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductSetProductsGet, self).__init__()
        self._isProductSetProductsGet = True
        self._api = api

    class Field(AbstractObject.Field):
        data = 'data'
        paging = 'paging'
        summary = 'summary'

    class DisplayFormat:
        carousel_ad = 'CAROUSEL_AD'
        shops_pdp = 'SHOPS_PDP'
        single_ad = 'SINGLE_AD'

    class ErrorPriority:
        high = 'HIGH'
        low = 'LOW'
        medium = 'MEDIUM'

    class ErrorType:
        address_blocklisted_in_market = 'ADDRESS_BLOCKLISTED_IN_MARKET'
        aggregated_localization_issues = 'AGGREGATED_LOCALIZATION_ISSUES'
        app_has_no_aem_setup = 'APP_HAS_NO_AEM_SETUP'
        ar_deleted_due_to_update = 'AR_DELETED_DUE_TO_UPDATE'
        ar_policy_violated = 'AR_POLICY_VIOLATED'
        available = 'AVAILABLE'
        bad_quality_image = 'BAD_QUALITY_IMAGE'
        big_catalog_with_all_items_in_stock = 'BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK'
        biz_msg_ai_agent_disabled_by_user = 'BIZ_MSG_AI_AGENT_DISABLED_BY_USER'
        biz_msg_gen_ai_policy_violated = 'BIZ_MSG_GEN_AI_POLICY_VIOLATED'
        cannot_edit_subscription_products = 'CANNOT_EDIT_SUBSCRIPTION_PRODUCTS'
        catalog_not_connected_to_event_source = 'CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE'
        checkout_disabled_by_user = 'CHECKOUT_DISABLED_BY_USER'
        commerce_account_legal_address_invalid = 'COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID'
        commerce_account_not_legally_compliant = 'COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT'
        crawled_availability_mismatch = 'CRAWLED_AVAILABILITY_MISMATCH'
        da_disabled_by_user = 'DA_DISABLED_BY_USER'
        da_policy_violation = 'DA_POLICY_VIOLATION'
        deleted_item = 'DELETED_ITEM'
        digital_goods_not_available_for_checkout = 'DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT'
        duplicate_images = 'DUPLICATE_IMAGES'
        duplicate_title_and_description = 'DUPLICATE_TITLE_AND_DESCRIPTION'
        empty_availability = 'EMPTY_AVAILABILITY'
        empty_brand = 'EMPTY_BRAND'
        empty_condition = 'EMPTY_CONDITION'
        empty_description = 'EMPTY_DESCRIPTION'
        empty_image_url = 'EMPTY_IMAGE_URL'
        empty_price = 'EMPTY_PRICE'
        empty_product_url = 'EMPTY_PRODUCT_URL'
        empty_seller_description = 'EMPTY_SELLER_DESCRIPTION'
        empty_title = 'EMPTY_TITLE'
        external_merchant_id_mismatch = 'EXTERNAL_MERCHANT_ID_MISMATCH'
        generic_invalid_field = 'GENERIC_INVALID_FIELD'
        groups_disabled_by_user = 'GROUPS_DISABLED_BY_USER'
        hidden_until_product_launch = 'HIDDEN_UNTIL_PRODUCT_LAUNCH'
        illegal_product_category = 'ILLEGAL_PRODUCT_CATEGORY'
        image_fetch_failed = 'IMAGE_FETCH_FAILED'
        image_fetch_failed_bad_gateway = 'IMAGE_FETCH_FAILED_BAD_GATEWAY'
        image_fetch_failed_file_size_exceeded = 'IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED'
        image_fetch_failed_forbidden = 'IMAGE_FETCH_FAILED_FORBIDDEN'
        image_fetch_failed_link_broken = 'IMAGE_FETCH_FAILED_LINK_BROKEN'
        image_fetch_failed_timed_out = 'IMAGE_FETCH_FAILED_TIMED_OUT'
        image_resolution_low = 'IMAGE_RESOLUTION_LOW'
        inactive_magento_product = 'INACTIVE_MAGENTO_PRODUCT'
        inactive_salesforce_commerce_cloud_product = 'INACTIVE_SALESFORCE_COMMERCE_CLOUD_PRODUCT'
        inactive_shopify_product = 'INACTIVE_SHOPIFY_PRODUCT'
        inactive_woocommerce_product = 'INACTIVE_WOOCOMMERCE_PRODUCT'
        invalid_commerce_tax_category = 'INVALID_COMMERCE_TAX_CATEGORY'
        invalid_comscore_market_codes = 'INVALID_COMSCORE_MARKET_CODES'
        invalid_consolidated_locality_information = 'INVALID_CONSOLIDATED_LOCALITY_INFORMATION'
        invalid_content_id = 'INVALID_CONTENT_ID'
        invalid_dealer_communication_parameters = 'INVALID_DEALER_COMMUNICATION_PARAMETERS'
        invalid_dma_codes = 'INVALID_DMA_CODES'
        invalid_fb_page_id = 'INVALID_FB_PAGE_ID'
        invalid_images = 'INVALID_IMAGES'
        invalid_monetizer_return_policy = 'INVALID_MONETIZER_RETURN_POLICY'
        invalid_offer_disclaimer_url = 'INVALID_OFFER_DISCLAIMER_URL'
        invalid_offer_end_date = 'INVALID_OFFER_END_DATE'
        invalid_pre_order_params = 'INVALID_PRE_ORDER_PARAMS'
        invalid_range_for_area_size = 'INVALID_RANGE_FOR_AREA_SIZE'
        invalid_range_for_built_up_area_size = 'INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE'
        invalid_range_for_num_of_baths = 'INVALID_RANGE_FOR_NUM_OF_BATHS'
        invalid_range_for_num_of_beds = 'INVALID_RANGE_FOR_NUM_OF_BEDS'
        invalid_range_for_num_of_rooms = 'INVALID_RANGE_FOR_NUM_OF_ROOMS'
        invalid_range_for_parking_spaces = 'INVALID_RANGE_FOR_PARKING_SPACES'
        invalid_sale_price = 'INVALID_SALE_PRICE'
        invalid_shelter_page_id = 'INVALID_SHELTER_PAGE_ID'
        invalid_shipping_profile_params = 'INVALID_SHIPPING_PROFILE_PARAMS'
        invalid_subscription_disable_params = 'INVALID_SUBSCRIPTION_DISABLE_PARAMS'
        invalid_subscription_enable_params = 'INVALID_SUBSCRIPTION_ENABLE_PARAMS'
        invalid_subscription_params = 'INVALID_SUBSCRIPTION_PARAMS'
        invalid_tax_extension_state = 'INVALID_TAX_EXTENSION_STATE'
        invalid_vehicle_state = 'INVALID_VEHICLE_STATE'
        invalid_virtual_tour_url_domain = 'INVALID_VIRTUAL_TOUR_URL_DOMAIN'
        inventory_zero_availability_in_stock = 'INVENTORY_ZERO_AVAILABILITY_IN_STOCK'
        in_another_product_launch = 'IN_ANOTHER_PRODUCT_LAUNCH'
        item_group_not_specified = 'ITEM_GROUP_NOT_SPECIFIED'
        item_not_shippable_for_sca_shop = 'ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP'
        item_override_empty_availability = 'ITEM_OVERRIDE_EMPTY_AVAILABILITY'
        item_override_empty_price = 'ITEM_OVERRIDE_EMPTY_PRICE'
        item_override_not_visible = 'ITEM_OVERRIDE_NOT_VISIBLE'
        item_price_not_positive = 'ITEM_PRICE_NOT_POSITIVE'
        item_stale_out_of_stock = 'ITEM_STALE_OUT_OF_STOCK'
        item_without_video = 'ITEM_WITHOUT_VIDEO'
        marketplace_disabled_by_user = 'MARKETPLACE_DISABLED_BY_USER'
        marketplace_not_shipped_item = 'MARKETPLACE_NOT_SHIPPED_ITEM'
        marketplace_partner_auction_no_bid_close_time = 'MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME'
        marketplace_partner_currency_not_valid = 'MARKETPLACE_PARTNER_CURRENCY_NOT_VALID'
        marketplace_partner_distribution_disabled = 'MARKETPLACE_PARTNER_DISTRIBUTION_DISABLED'
        marketplace_partner_listing_country_not_match_catalog = 'MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG'
        marketplace_partner_listing_limit_exceeded = 'MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED'
        marketplace_partner_missing_latlong = 'MARKETPLACE_PARTNER_MISSING_LATLONG'
        marketplace_partner_missing_shipping_cost = 'MARKETPLACE_PARTNER_MISSING_SHIPPING_COST'
        marketplace_partner_not_local_item = 'MARKETPLACE_PARTNER_NOT_LOCAL_ITEM'
        marketplace_partner_not_shipped_item = 'MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM'
        marketplace_partner_policy_violation = 'MARKETPLACE_PARTNER_POLICY_VIOLATION'
        marketplace_partner_rule_listing_limit_exceeded = 'MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED'
        marketplace_partner_seller_banned = 'MARKETPLACE_PARTNER_SELLER_BANNED'
        marketplace_partner_seller_not_valid = 'MARKETPLACE_PARTNER_SELLER_NOT_VALID'
        marketplace_shipped_item_expired = 'MARKETPLACE_SHIPPED_ITEM_EXPIRED'
        marketplace_shipped_item_not_available = 'MARKETPLACE_SHIPPED_ITEM_NOT_AVAILABLE'
        marketplace_shipped_seller_feature_banned = 'MARKETPLACE_SHIPPED_SELLER_FEATURE_BANNED'
        marketplace_shipped_seller_not_fully_onboarded = 'MARKETPLACE_SHIPPED_SELLER_NOT_FULLY_ONBOARDED'
        mini_shops_disabled_by_user = 'MINI_SHOPS_DISABLED_BY_USER'
        missing_checkout = 'MISSING_CHECKOUT'
        missing_checkout_currency = 'MISSING_CHECKOUT_CURRENCY'
        missing_color = 'MISSING_COLOR'
        missing_country_override_in_shipping_profile = 'MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE'
        missing_event = 'MISSING_EVENT'
        missing_india_compliance_fields = 'MISSING_INDIA_COMPLIANCE_FIELDS'
        missing_shipping_profile = 'MISSING_SHIPPING_PROFILE'
        missing_size = 'MISSING_SIZE'
        missing_tax_category = 'MISSING_TAX_CATEGORY'
        negative_community_feedback = 'NEGATIVE_COMMUNITY_FEEDBACK'
        negative_price = 'NEGATIVE_PRICE'
        not_enough_images = 'NOT_ENOUGH_IMAGES'
        not_enough_unique_products = 'NOT_ENOUGH_UNIQUE_PRODUCTS'
        no_content_id = 'NO_CONTENT_ID'
        overlay_disclaimer_exceeded_max_length = 'OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH'
        part_of_product_launch = 'PART_OF_PRODUCT_LAUNCH'
        passing_multiple_content_ids = 'PASSING_MULTIPLE_CONTENT_IDS'
        product_dominant_currency_mismatch = 'PRODUCT_DOMINANT_CURRENCY_MISMATCH'
        product_expired = 'PRODUCT_EXPIRED'
        product_item_hidden_from_all_shops = 'PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS'
        product_item_invalid_partner_tokens = 'PRODUCT_ITEM_INVALID_PARTNER_TOKENS'
        product_item_not_included_in_any_shop = 'PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP'
        product_item_not_visible = 'PRODUCT_ITEM_NOT_VISIBLE'
        product_not_approved = 'PRODUCT_NOT_APPROVED'
        product_not_dominant_currency = 'PRODUCT_NOT_DOMINANT_CURRENCY'
        product_out_of_stock = 'PRODUCT_OUT_OF_STOCK'
        product_url_equals_domain = 'PRODUCT_URL_EQUALS_DOMAIN'
        property_price_currency_not_supported = 'PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED'
        property_price_too_high = 'PROPERTY_PRICE_TOO_HIGH'
        property_price_too_low = 'PROPERTY_PRICE_TOO_LOW'
        property_unit_price_currency_mismatch_item_price_currency = 'PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY'
        property_value_contains_html_tags = 'PROPERTY_VALUE_CONTAINS_HTML_TAGS'
        property_value_description_contains_off_platform_link = 'PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK'
        property_value_format = 'PROPERTY_VALUE_FORMAT'
        property_value_missing = 'PROPERTY_VALUE_MISSING'
        property_value_missing_warning = 'PROPERTY_VALUE_MISSING_WARNING'
        property_value_non_positive = 'PROPERTY_VALUE_NON_POSITIVE'
        property_value_string_exceeds_length = 'PROPERTY_VALUE_STRING_EXCEEDS_LENGTH'
        property_value_string_too_short = 'PROPERTY_VALUE_STRING_TOO_SHORT'
        property_value_uppercase = 'PROPERTY_VALUE_UPPERCASE'
        property_value_uppercase_warning = 'PROPERTY_VALUE_UPPERCASE_WARNING'
        purchase_rate_below_addtocart = 'PURCHASE_RATE_BELOW_ADDTOCART'
        purchase_rate_below_viewcontent = 'PURCHASE_RATE_BELOW_VIEWCONTENT'
        quality_duplicated_description = 'QUALITY_DUPLICATED_DESCRIPTION'
        quality_item_link_broken = 'QUALITY_ITEM_LINK_BROKEN'
        quality_item_link_redirecting = 'QUALITY_ITEM_LINK_REDIRECTING'
        retailer_id_not_provided = 'RETAILER_ID_NOT_PROVIDED'
        retailer_id_used_by_group = 'RETAILER_ID_USED_BY_GROUP'
        shopify_invalid_retailer_id = 'SHOPIFY_INVALID_RETAILER_ID'
        shopify_item_missing_delivery_profile_zero_inventory = 'SHOPIFY_ITEM_MISSING_DELIVERY_PROFILE_ZERO_INVENTORY'
        shopify_item_missing_shipping_profile = 'SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE'
        shops_policy_violation = 'SHOPS_POLICY_VIOLATION'
        subscription_info_not_enabled_for_feed = 'SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED'
        tax_category_not_supported_in_uk = 'TAX_CATEGORY_NOT_SUPPORTED_IN_UK'
        top_product_without_videos = 'TOP_PRODUCT_WITHOUT_VIDEOS'
        unique_product_identifier_missing = 'UNIQUE_PRODUCT_IDENTIFIER_MISSING'
        unmatched_events = 'UNMATCHED_EVENTS'
        unsupported_product_category = 'UNSUPPORTED_PRODUCT_CATEGORY'
        variant_attribute_issue = 'VARIANT_ATTRIBUTE_ISSUE'
        video_fetch_failed = 'VIDEO_FETCH_FAILED'
        video_fetch_failed_bad_gateway = 'VIDEO_FETCH_FAILED_BAD_GATEWAY'
        video_fetch_failed_file_size_exceeded = 'VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED'
        video_fetch_failed_forbidden = 'VIDEO_FETCH_FAILED_FORBIDDEN'
        video_fetch_failed_link_broken = 'VIDEO_FETCH_FAILED_LINK_BROKEN'
        video_fetch_failed_rate_limited = 'VIDEO_FETCH_FAILED_RATE_LIMITED'
        video_fetch_failed_server_error = 'VIDEO_FETCH_FAILED_SERVER_ERROR'
        video_fetch_failed_timed_out = 'VIDEO_FETCH_FAILED_TIMED_OUT'
        video_issue_generic = 'VIDEO_ISSUE_GENERIC'
        video_not_downloadable = 'VIDEO_NOT_DOWNLOADABLE'
        whatsapp_disabled_by_user = 'WHATSAPP_DISABLED_BY_USER'
        whatsapp_marketing_message_disabled_by_user = 'WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER'
        whatsapp_marketing_message_policy_violation = 'WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION'
        whatsapp_policy_violation = 'WHATSAPP_POLICY_VIOLATION'

    _field_types = {
        'data': 'list<object>',
        'paging': 'object',
        'summary': 'object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DisplayFormat'] = ProductSetProductsGet.DisplayFormat.__dict__.values()
        field_enum_info['ErrorPriority'] = ProductSetProductsGet.ErrorPriority.__dict__.values()
        field_enum_info['ErrorType'] = ProductSetProductsGet.ErrorType.__dict__.values()
        return field_enum_info


