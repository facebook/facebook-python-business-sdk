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

class ProductCatalogVersionItemsBatchPost(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductCatalogVersionItemsBatchPost, self).__init__()
        self._isProductCatalogVersionItemsBatchPost = True
        self._api = api

    class Field(AbstractObject.Field):
        handles = 'handles'
        validation_status = 'validation_status'

    class ItemSubType:
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

    _field_types = {
        'handles': 'list<string>',
        'validation_status': 'list<object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ItemSubType'] = ProductCatalogVersionItemsBatchPost.ItemSubType.__dict__.values()
        return field_enum_info


