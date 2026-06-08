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

class HomeListingGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isHomeListingGet = True
        super(HomeListingGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ac_type = 'ac_type'
        additional_fees_description = 'additional_fees_description'
        address = 'address'
        agent_company = 'agent_company'
        agent_email = 'agent_email'
        agent_fb_page_id = 'agent_fb_page_id'
        agent_name = 'agent_name'
        agent_phone = 'agent_phone'
        applinks = 'applinks'
        area_size = 'area_size'
        area_unit = 'area_unit'
        availability = 'availability'
        capabilities = 'capabilities'
        capabilities_disabled_by_user = 'capabilities_disabled_by_user'
        capabilities_rendering_catalog_manager = 'capabilities_rendering_catalog_manager'
        capability_to_rejection_reason = 'capability_to_rejection_reason'
        catalog_item_overrides = 'catalog_item_overrides'
        channels_to_integrity_status = 'channels_to_integrity_status'
        co_2_emission_rating_eu = 'co_2_emission_rating_eu'
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
        days_on_market = 'days_on_market'
        description = 'description'
        enabled_capability_to_review_status = 'enabled_capability_to_review_status'
        energy_rating_eu = 'energy_rating_eu'
        furnish_type = 'furnish_type'
        group_id = 'group_id'
        heating_type = 'heating_type'
        home_listing_id = 'home_listing_id'
        id = 'id'
        image_fetch_status = 'image_fetch_status'
        images = 'images'
        is_blackholed = 'is_blackholed'
        laundry_type = 'laundry_type'
        listing_type = 'listing_type'
        max_currency = 'max_currency'
        max_price = 'max_price'
        min_currency = 'min_currency'
        min_price = 'min_price'
        name = 'name'
        num_baths = 'num_baths'
        num_beds = 'num_beds'
        num_rooms = 'num_rooms'
        num_units = 'num_units'
        override_details = 'override_details'
        parking_type = 'parking_type'
        partner_verification = 'partner_verification'
        pet_policy = 'pet_policy'
        price = 'price'
        product_feed = 'product_feed'
        property_type = 'property_type'
        sanitized_images = 'sanitized_images'
        sanitized_previews = 'sanitized_previews'
        securitydeposit_currency = 'securitydeposit_currency'
        securitydeposit_price = 'securitydeposit_price'
        tags = 'tags'
        unit_price = 'unit_price'
        url = 'url'
        url_shimmed = 'url_shimmed'
        validation_errors = 'validation_errors'
        videos_metadata = 'videos_metadata'
        visibility = 'visibility'
        year_built = 'year_built'

    class AcType:
        central = 'CENTRAL'
        empty_value = 'EMPTY_VALUE'
        none = 'NONE'
        other = 'OTHER'

    class AreaUnit:
        empty_value = 'EMPTY_VALUE'
        sqft = 'SQFT'
        sqm = 'SQM'

    class Availability:
        available_soon = 'AVAILABLE_SOON'
        for_rent = 'FOR_RENT'
        for_sale = 'FOR_SALE'
        off_market = 'OFF_MARKET'
        recently_sold = 'RECENTLY_SOLD'
        sale_pending = 'SALE_PENDING'

    class Capabilities:
        b2c_marketplace = 'B2C_MARKETPLACE'
        biz_msg_ai_agent = 'BIZ_MSG_AI_AGENT'
        business_inbox_in_messenger = 'BUSINESS_INBOX_IN_MESSENGER'
        buy_on_facebook = 'BUY_ON_FACEBOOK'
        c2c_marketplace = 'C2C_MARKETPLACE'
        cpas_parent_catalog = 'CPAS_PARENT_CATALOG'
        da = 'DA'
        daily_deals = 'DAILY_DEALS'
        daily_deals_legacy = 'DAILY_DEALS_LEGACY'
        event = 'EVENT'
        event_deprecated = 'EVENT_DEPRECATED'
        groups = 'GROUPS'
        ig_onsite_shopping = 'IG_ONSITE_SHOPPING'
        ig_product_tagging = 'IG_PRODUCT_TAGGING'
        ldp = 'LDP'
        marketplace = 'MARKETPLACE'
        marketplace_ads_deprecated = 'MARKETPLACE_ADS_DEPRECATED'
        marketplace_home_rentals = 'MARKETPLACE_HOME_RENTALS'
        marketplace_home_sales = 'MARKETPLACE_HOME_SALES'
        marketplace_motors = 'MARKETPLACE_MOTORS'
        marketplace_shops = 'MARKETPLACE_SHOPS'
        mini_shops = 'MINI_SHOPS'
        neighborhoods = 'NEIGHBORHOODS'
        offline_conversions = 'OFFLINE_CONVERSIONS'
        profile = 'PROFILE'
        service = 'SERVICE'
        shops = 'SHOPS'
        test_capability = 'TEST_CAPABILITY'
        universal_checkout = 'UNIVERSAL_CHECKOUT'
        us_marketplace = 'US_MARKETPLACE'
        whatsapp = 'WHATSAPP'
        whatsapp_marketing_message = 'WHATSAPP_MARKETING_MESSAGE'

    class CapabilitiesRenderingCatalogManager:
        b2c_marketplace = 'B2C_MARKETPLACE'
        biz_msg_ai_agent = 'BIZ_MSG_AI_AGENT'
        business_inbox_in_messenger = 'BUSINESS_INBOX_IN_MESSENGER'
        buy_on_facebook = 'BUY_ON_FACEBOOK'
        c2c_marketplace = 'C2C_MARKETPLACE'
        cpas_parent_catalog = 'CPAS_PARENT_CATALOG'
        da = 'DA'
        daily_deals = 'DAILY_DEALS'
        daily_deals_legacy = 'DAILY_DEALS_LEGACY'
        event = 'EVENT'
        event_deprecated = 'EVENT_DEPRECATED'
        groups = 'GROUPS'
        ig_onsite_shopping = 'IG_ONSITE_SHOPPING'
        ig_product_tagging = 'IG_PRODUCT_TAGGING'
        ldp = 'LDP'
        marketplace = 'MARKETPLACE'
        marketplace_ads_deprecated = 'MARKETPLACE_ADS_DEPRECATED'
        marketplace_home_rentals = 'MARKETPLACE_HOME_RENTALS'
        marketplace_home_sales = 'MARKETPLACE_HOME_SALES'
        marketplace_motors = 'MARKETPLACE_MOTORS'
        marketplace_shops = 'MARKETPLACE_SHOPS'
        mini_shops = 'MINI_SHOPS'
        neighborhoods = 'NEIGHBORHOODS'
        offline_conversions = 'OFFLINE_CONVERSIONS'
        profile = 'PROFILE'
        service = 'SERVICE'
        shops = 'SHOPS'
        test_capability = 'TEST_CAPABILITY'
        universal_checkout = 'UNIVERSAL_CHECKOUT'
        us_marketplace = 'US_MARKETPLACE'
        whatsapp = 'WHATSAPP'
        whatsapp_marketing_message = 'WHATSAPP_MARKETING_MESSAGE'

    class FurnishType:
        empty_value = 'EMPTY_VALUE'
        furnished = 'FURNISHED'
        semifurnished = 'SEMIFURNISHED'
        unfurnished = 'UNFURNISHED'

    class HeatingType:
        central = 'CENTRAL'
        electric = 'ELECTRIC'
        empty_value = 'EMPTY_VALUE'
        gas = 'GAS'
        none = 'NONE'
        other = 'OTHER'
        radiator = 'RADIATOR'

    class ImageFetchStatus:
        direct_upload = 'DIRECT_UPLOAD'
        fetched = 'FETCHED'
        fetch_failed = 'FETCH_FAILED'
        no_status = 'NO_STATUS'
        outdated = 'OUTDATED'
        partial_fetch = 'PARTIAL_FETCH'

    class LaundryType:
        empty_value = 'EMPTY_VALUE'
        in_building = 'IN_BUILDING'
        in_unit = 'IN_UNIT'
        none = 'NONE'
        other = 'OTHER'

    class ListingType:
        empty_value = 'EMPTY_VALUE'
        foreclosed = 'FORECLOSED'
        for_rent_by_agent = 'FOR_RENT_BY_AGENT'
        for_rent_by_owner = 'FOR_RENT_BY_OWNER'
        for_sale_by_agent = 'FOR_SALE_BY_AGENT'
        for_sale_by_owner = 'FOR_SALE_BY_OWNER'
        new_construction = 'NEW_CONSTRUCTION'
        new_listing = 'NEW_LISTING'
        other = 'OTHER'

    class ParkingType:
        empty_value = 'EMPTY_VALUE'
        garage = 'GARAGE'
        none = 'NONE'
        off_street = 'OFF_STREET'
        other = 'OTHER'
        street = 'STREET'

    class PartnerVerification:
        empty_value = 'EMPTY_VALUE'
        none = 'NONE'
        verified = 'VERIFIED'

    class PropertyType:
        apartment = 'APARTMENT'
        apartment_room = 'APARTMENT_ROOM'
        builder_floor = 'BUILDER_FLOOR'
        bungalow = 'BUNGALOW'
        condo = 'CONDO'
        condo_room = 'CONDO_ROOM'
        empty_value = 'EMPTY_VALUE'
        house = 'HOUSE'
        house_in_condominium = 'HOUSE_IN_CONDOMINIUM'
        house_in_villa = 'HOUSE_IN_VILLA'
        house_room = 'HOUSE_ROOM'
        land = 'LAND'
        loft = 'LOFT'
        manufactured = 'MANUFACTURED'
        other = 'OTHER'
        other_room = 'OTHER_ROOM'
        penthouse = 'PENTHOUSE'
        single_family_home = 'SINGLE_FAMILY_HOME'
        studio = 'STUDIO'
        townhouse = 'TOWNHOUSE'
        townhouse_room = 'TOWNHOUSE_ROOM'

    class Visibility:
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        hidden = 'HIDDEN'
        legacy_public = 'LEGACY_PUBLIC'
        published = 'PUBLISHED'
        staging = 'STAGING'
        visible_only_with_overrides = 'VISIBLE_ONLY_WITH_OVERRIDES'
        whitelist_only = 'WHITELIST_ONLY'

    _field_types = {
        'ac_type': 'AcType',
        'additional_fees_description': 'string',
        'address': 'object',
        'agent_company': 'string',
        'agent_email': 'string',
        'agent_fb_page_id': 'object',
        'agent_name': 'string',
        'agent_phone': 'string',
        'applinks': 'object',
        'area_size': 'int',
        'area_unit': 'AreaUnit',
        'availability': 'Availability',
        'capabilities': 'list<Capabilities>',
        'capabilities_disabled_by_user': 'list<string>',
        'capabilities_rendering_catalog_manager': 'list<CapabilitiesRenderingCatalogManager>',
        'capability_to_rejection_reason': 'list<object>',
        'catalog_item_overrides': 'object',
        'channels_to_integrity_status': 'object',
        'co_2_emission_rating_eu': 'object',
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
        'days_on_market': 'int',
        'description': 'string',
        'enabled_capability_to_review_status': 'list<object>',
        'energy_rating_eu': 'object',
        'furnish_type': 'FurnishType',
        'group_id': 'string',
        'heating_type': 'HeatingType',
        'home_listing_id': 'string',
        'id': 'int',
        'image_fetch_status': 'ImageFetchStatus',
        'images': 'list<string>',
        'is_blackholed': 'bool',
        'laundry_type': 'LaundryType',
        'listing_type': 'ListingType',
        'max_currency': 'string',
        'max_price': 'string',
        'min_currency': 'string',
        'min_price': 'string',
        'name': 'string',
        'num_baths': 'float',
        'num_beds': 'float',
        'num_rooms': 'float',
        'num_units': 'int',
        'override_details': 'object',
        'parking_type': 'ParkingType',
        'partner_verification': 'PartnerVerification',
        'pet_policy': 'string',
        'price': 'string',
        'product_feed': 'object',
        'property_type': 'PropertyType',
        'sanitized_images': 'list<string>',
        'sanitized_previews': 'list<string>',
        'securitydeposit_currency': 'string',
        'securitydeposit_price': 'string',
        'tags': 'list<string>',
        'unit_price': 'object',
        'url': 'string',
        'url_shimmed': 'string',
        'validation_errors': 'object',
        'videos_metadata': 'object',
        'visibility': 'Visibility',
        'year_built': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AcType'] = HomeListingGet.AcType.__dict__.values()
        field_enum_info['AreaUnit'] = HomeListingGet.AreaUnit.__dict__.values()
        field_enum_info['Availability'] = HomeListingGet.Availability.__dict__.values()
        field_enum_info['Capabilities'] = HomeListingGet.Capabilities.__dict__.values()
        field_enum_info['CapabilitiesRenderingCatalogManager'] = HomeListingGet.CapabilitiesRenderingCatalogManager.__dict__.values()
        field_enum_info['FurnishType'] = HomeListingGet.FurnishType.__dict__.values()
        field_enum_info['HeatingType'] = HomeListingGet.HeatingType.__dict__.values()
        field_enum_info['ImageFetchStatus'] = HomeListingGet.ImageFetchStatus.__dict__.values()
        field_enum_info['LaundryType'] = HomeListingGet.LaundryType.__dict__.values()
        field_enum_info['ListingType'] = HomeListingGet.ListingType.__dict__.values()
        field_enum_info['ParkingType'] = HomeListingGet.ParkingType.__dict__.values()
        field_enum_info['PartnerVerification'] = HomeListingGet.PartnerVerification.__dict__.values()
        field_enum_info['PropertyType'] = HomeListingGet.PropertyType.__dict__.values()
        field_enum_info['Visibility'] = HomeListingGet.Visibility.__dict__.values()
        return field_enum_info


