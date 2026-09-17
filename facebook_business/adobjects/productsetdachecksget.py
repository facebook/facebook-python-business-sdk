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

class ProductSetDAChecksGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductSetDAChecksGet, self).__init__()
        self._isProductSetDAChecksGet = True
        self._api = api

    class Field(AbstractObject.Field):
        data = 'data'

    class Capabilities:
        b2c_marketplace = 'B2C_MARKETPLACE'
        c2c_marketplace = 'C2C_MARKETPLACE'
        da = 'DA'
        daily_deals = 'DAILY_DEALS'
        daily_deals_legacy = 'DAILY_DEALS_LEGACY'
        ig_product_tagging = 'IG_PRODUCT_TAGGING'
        marketplace = 'MARKETPLACE'
        marketplace_ads_deprecated = 'MARKETPLACE_ADS_DEPRECATED'
        marketplace_shops = 'MARKETPLACE_SHOPS'
        mini_shops = 'MINI_SHOPS'
        offline_conversions = 'OFFLINE_CONVERSIONS'
        shops = 'SHOPS'
        universal_checkout = 'UNIVERSAL_CHECKOUT'
        whatsapp = 'WHATSAPP'

    class Categories:
        appliances = 'APPLIANCES'
        baby_feeding = 'BABY_FEEDING'
        baby_transport = 'BABY_TRANSPORT'
        beauty = 'BEAUTY'
        bedding = 'BEDDING'
        cameras = 'CAMERAS'
        cameras_and_photos = 'CAMERAS_AND_PHOTOS'
        cell_phones_and_smart_watches = 'CELL_PHONES_AND_SMART_WATCHES'
        cleaning_supplies = 'CLEANING_SUPPLIES'
        clothing = 'CLOTHING'
        clothing_accessories = 'CLOTHING_ACCESSORIES'
        clo_offer = 'CLO_OFFER'
        computers_and_tablets = 'COMPUTERS_AND_TABLETS'
        computers_laptops_and_tablets = 'COMPUTERS_LAPTOPS_AND_TABLETS'
        computer_components = 'COMPUTER_COMPONENTS'
        diapering_and_potty_training = 'DIAPERING_AND_POTTY_TRAINING'
        electronics_accessories = 'ELECTRONICS_ACCESSORIES'
        electronic_accessories_and_cables = 'ELECTRONIC_ACCESSORIES_AND_CABLES'
        empty = 'EMPTY'
        furniture = 'FURNITURE'
        health = 'HEALTH'
        home = 'HOME'
        home_goods = 'HOME_GOODS'
        household_and_cleaning_supplies = 'HOUSEHOLD_AND_CLEANING_SUPPLIES'
        jewelry = 'JEWELRY'
        large_appliances = 'LARGE_APPLIANCES'
        local_service_business_item = 'LOCAL_SERVICE_BUSINESS_ITEM'
        local_service_business_restaurant = 'LOCAL_SERVICE_BUSINESS_RESTAURANT'
        nursery = 'NURSERY'
        printers_and_scanners = 'PRINTERS_AND_SCANNERS'
        printers_scanners_and_fax_machines = 'PRINTERS_SCANNERS_AND_FAX_MACHINES'
        product_discount = 'PRODUCT_DISCOUNT'
        projectors = 'PROJECTORS'
        shoes = 'SHOES'
        shoes_and_footwear = 'SHOES_AND_FOOTWEAR'
        software = 'SOFTWARE'
        televisions_and_monitors = 'TELEVISIONS_AND_MONITORS'
        test_child_sub_vertical = 'TEST_CHILD_SUB_VERTICAL'
        test_grand_child_sub_vertical = 'TEST_GRAND_CHILD_SUB_VERTICAL'
        test_sub_vertical = 'TEST_SUB_VERTICAL'
        test_sub_vertical_alias = 'TEST_SUB_VERTICAL_ALIAS'
        test_sub_vertical_data_object = 'TEST_SUB_VERTICAL_DATA_OBJECT'
        third_party_electronics = 'THIRD_PARTY_ELECTRONICS'
        third_party_toys_and_games = 'THIRD_PARTY_TOYS_AND_GAMES'
        toys = 'TOYS'
        toys_and_games = 'TOYS_AND_GAMES'
        tvs_and_monitors = 'TVS_AND_MONITORS'
        vehicle_manufacturer = 'VEHICLE_MANUFACTURER'
        video_games_and_consoles = 'VIDEO_GAMES_AND_CONSOLES'
        video_game_consoles_and_video_games = 'VIDEO_GAME_CONSOLES_AND_VIDEO_GAMES'
        video_projectors = 'VIDEO_PROJECTORS'
        watches = 'WATCHES'

    class ConnectionMethod:
        all = 'ALL'
        app = 'APP'
        browser = 'BROWSER'
        server = 'SERVER'

    class Features:
        agentic_checkout = 'AGENTIC_CHECKOUT'
        amazon_buy_with_prime = 'AMAZON_BUY_WITH_PRIME'
        augmented_reality = 'AUGMENTED_REALITY'
        checkout = 'CHECKOUT'
        integrated_checkout_lowes = 'INTEGRATED_CHECKOUT_LOWES'
        integrated_checkout_meli = 'INTEGRATED_CHECKOUT_MELI'
        integrated_checkout_shein = 'INTEGRATED_CHECKOUT_SHEIN'
        integrated_checkout_shopee = 'INTEGRATED_CHECKOUT_SHOPEE'
        integrated_checkout_walmart = 'INTEGRATED_CHECKOUT_WALMART'
        integrated_checkout_zalando = 'INTEGRATED_CHECKOUT_ZALANDO'
        live_shopping = 'LIVE_SHOPPING'

    _field_types = {
        'data': 'list<object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Capabilities'] = ProductSetDAChecksGet.Capabilities.__dict__.values()
        field_enum_info['Categories'] = ProductSetDAChecksGet.Categories.__dict__.values()
        field_enum_info['ConnectionMethod'] = ProductSetDAChecksGet.ConnectionMethod.__dict__.values()
        field_enum_info['Features'] = ProductSetDAChecksGet.Features.__dict__.values()
        return field_enum_info


