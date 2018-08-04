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

class AdAccountCreationRequest(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountCreationRequest = True
        super(AdAccountCreationRequest, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_accounts_info = 'ad_accounts_info'
        additional_comment = 'additional_comment'
        address_in_chinese = 'address_in_chinese'
        address_in_english = 'address_in_english'
        advertiser_business = 'advertiser_business'
        appeal_reason = 'appeal_reason'
        business = 'business'
        business_registration_id = 'business_registration_id'
        chinese_legal_entity_name = 'chinese_legal_entity_name'
        contact = 'contact'
        creator = 'creator'
        disapproval_reasons = 'disapproval_reasons'
        english_legal_entity_name = 'english_legal_entity_name'
        extended_credit_id = 'extended_credit_id'
        id = 'id'
        is_smb = 'is_smb'
        is_test = 'is_test'
        is_under_authorization = 'is_under_authorization'
        official_website_url = 'official_website_url'
        planning_agency_business = 'planning_agency_business'
        planning_agency_business_id = 'planning_agency_business_id'
        promotable_app_ids = 'promotable_app_ids'
        promotable_page_ids = 'promotable_page_ids'
        promotable_urls = 'promotable_urls'
        request_change_reasons = 'request_change_reasons'
        status = 'status'
        subvertical = 'subvertical'
        time_created = 'time_created'
        vertical = 'vertical'
        advertiser_business_id = 'advertiser_business_id'
        business_registration = 'business_registration'
        promotable_page_urls = 'promotable_page_urls'

    class Subvertical:
        accounting_and_taxes_and_legal = 'ACCOUNTING_AND_TAXES_AND_LEGAL'
        agriculture_and_farming = 'AGRICULTURE_AND_FARMING'
        ecommerce_agriculture_and_farming = 'ECOMMERCE_AGRICULTURE_AND_FARMING'
        air = 'AIR'
        air_freight_or_package = 'AIR_FREIGHT_OR_PACKAGE'
        apparel_and_accessories = 'APPAREL_AND_ACCESSORIES'
        arts = 'ARTS'
        auctions = 'AUCTIONS'
        auto_agency = 'AUTO_AGENCY'
        auto_rental = 'AUTO_RENTAL'
        automotive_manufacturer = 'AUTOMOTIVE_MANUFACTURER'
        b2b = 'B2B'
        b2b_manufacturing = 'B2B_MANUFACTURING'
        beauty_and_personal_care = 'BEAUTY_AND_PERSONAL_CARE'
        beer_and_wine_and_liquor = 'BEER_AND_WINE_AND_LIQUOR'
        bookstores = 'BOOKSTORES'
        bus_and_taxi_and_auto_retal = 'BUS_AND_TAXI_AND_AUTO_RETAL'
        business_support_services = 'BUSINESS_SUPPORT_SERVICES'
        cable_and_satellite = 'CABLE_AND_SATELLITE'
        career = 'CAREER'
        computing_and_peripherals = 'COMPUTING_AND_PERIPHERALS'
        console_developer = 'CONSOLE_DEVELOPER'
        console_device = 'CONSOLE_DEVICE'
        construction_and_mining = 'CONSTRUCTION_AND_MINING'
        consulting = 'CONSULTING'
        consumer_electronics = 'CONSUMER_ELECTRONICS'
        consumer_tech = 'CONSUMER_TECH'
        credit_and_financing_and_mortages = 'CREDIT_AND_FINANCING_AND_MORTAGES'
        cruises_and_marine = 'CRUISES_AND_MARINE'
        cvb_convention_and_visitors_bureau = 'CVB_CONVENTION_AND_VISITORS_BUREAU'
        dailydeals = 'DAILYDEALS'
        dating = 'DATING'
        dealership = 'DEALERSHIP'
        department_store = 'DEPARTMENT_STORE'
        desktop_software = 'DESKTOP_SOFTWARE'
        digital_advertising_and_marketing_or_untagged_agencies = 'DIGITAL_ADVERTISING_AND_MARKETING_OR_UNTAGGED_AGENCIES'
        ecatalog = 'ECATALOG'
        ed_tech = 'ED_TECH'
        education_resources = 'EDUCATION_RESOURCES'
        elearning_and_massive_online_open_courses = 'ELEARNING_AND_MASSIVE_ONLINE_OPEN_COURSES'
        engineering_and_design = 'ENGINEERING_AND_DESIGN'
        events = 'EVENTS'
        family_and_health = 'FAMILY_AND_HEALTH'
        fitness = 'FITNESS'
        food = 'FOOD'
        footwear = 'FOOTWEAR'
        for_profit_colleges_and_universities = 'FOR_PROFIT_COLLEGES_AND_UNIVERSITIES'
        gambling = 'GAMBLING'
        government = 'GOVERNMENT'
        grocery_and_drug_and_convenience = 'GROCERY_AND_DRUG_AND_CONVENIENCE'
        highways = 'HIGHWAYS'
        home_and_office = 'HOME_AND_OFFICE'
        home_improvement = 'HOME_IMPROVEMENT'
        home_service = 'HOME_SERVICE'
        hotel_and_accomodation = 'HOTEL_AND_ACCOMODATION'
        household_goods = 'HOUSEHOLD_GOODS'
        industrial_and_farm_vehicle = 'INDUSTRIAL_AND_FARM_VEHICLE'
        insurance = 'INSURANCE'
        investment_bank_and_brokerage = 'INVESTMENT_BANK_AND_BROKERAGE'
        media = 'MEDIA'
        mobile_and_social = 'MOBILE_AND_SOCIAL'
        mobile_apps = 'MOBILE_APPS'
        motorcycles = 'MOTORCYCLES'
        movies = 'MOVIES'
        museums_and_parks_and_libraries = 'MUSEUMS_AND_PARKS_AND_LIBRARIES'
        music_and_radio = 'MUSIC_AND_RADIO'
        non_profit = 'NON_PROFIT'
        not_for_profit_colleges_and_universities = 'NOT_FOR_PROFIT_COLLEGES_AND_UNIVERSITIES'
        office = 'OFFICE'
        oil_and_gas_and_consumable_fuel = 'OIL_AND_GAS_AND_CONSUMABLE_FUEL'
        online_or_software = 'ONLINE_OR_SOFTWARE'
        parts_and_service = 'PARTS_AND_SERVICE'
        pet = 'PET'
        pet_retail = 'PET_RETAIL'
        pharmaceutical_or_health = 'PHARMACEUTICAL_OR_HEALTH'
        photography_and_filming_services = 'PHOTOGRAPHY_AND_FILMING_SERVICES'
        political = 'POLITICAL'
        pr = 'PR'
        publishing_internet = 'PUBLISHING_INTERNET'
        railroads = 'RAILROADS'
        recreational = 'RECREATIONAL'
        real_estate = 'REAL_ESTATE'
        real_money_or_skilled_gaming = 'REAL_MONEY_OR_SKILLED_GAMING'
        religious = 'RELIGIOUS'
        restaurant = 'RESTAURANT'
        retail_and_credit_union_and_commercial_bank = 'RETAIL_AND_CREDIT_UNION_AND_COMMERCIAL_BANK'
        school_and_early_children_edcation = 'SCHOOL_AND_EARLY_CHILDREN_EDCATION'
        seasonal_political_spenders = 'SEASONAL_POLITICAL_SPENDERS'
        smb_agents_and_promoters = 'SMB_AGENTS_AND_PROMOTERS'
        smb_artists_and_performers = 'SMB_ARTISTS_AND_PERFORMERS'
        smb_canvas = 'SMB_CANVAS'
        smb_catalog = 'SMB_CATALOG'
        smb_consumer_mobile_device = 'SMB_CONSUMER_MOBILE_DEVICE'
        smb_cross_platform = 'SMB_CROSS_PLATFORM'
        smb_electronics_and_appliances = 'SMB_ELECTRONICS_AND_APPLIANCES'
        smb_energy = 'SMB_ENERGY'
        smb_game_and_toy = 'SMB_GAME_AND_TOY'
        smb_information = 'SMB_INFORMATION'
        smb_navigation_and_measurement = 'SMB_NAVIGATION_AND_MEASUREMENT'
        smb_operations_and_other = 'SMB_OPERATIONS_AND_OTHER'
        smb_other = 'SMB_OTHER'
        smb_personal_care = 'SMB_PERSONAL_CARE'
        smb_religious = 'SMB_RELIGIOUS'
        smb_rentals = 'SMB_RENTALS'
        smb_repair_and_maintenance = 'SMB_REPAIR_AND_MAINTENANCE'
        other_wireline_services = 'OTHER_WIRELINE_SERVICES'
        software = 'SOFTWARE'
        sporting = 'SPORTING'
        sports = 'SPORTS'
        streaming = 'STREAMING'
        television = 'TELEVISION'
        tobacco = 'TOBACCO'
        toy_and_hobby = 'TOY_AND_HOBBY'
        trade_school = 'TRADE_SCHOOL'
        transportation_equipment = 'TRANSPORTATION_EQUIPMENT'
        traval_agency = 'TRAVAL_AGENCY'
        truck_and_moving = 'TRUCK_AND_MOVING'
        utilities_and_energy_equipment_and_services = 'UTILITIES_AND_ENERGY_EQUIPMENT_AND_SERVICES'
        water_and_soft_drink_and_baverage = 'WATER_AND_SOFT_DRINK_AND_BAVERAGE'
        wireless_services = 'WIRELESS_SERVICES'

    class Vertical:
        advertising_and_marketing = 'ADVERTISING_AND_MARKETING'
        auto_agency = 'AUTO_AGENCY'
        automotive = 'AUTOMOTIVE'
        consumer_packaged_goods = 'CONSUMER_PACKAGED_GOODS'
        cpg_and_beverage = 'CPG_AND_BEVERAGE'
        ecommerce = 'ECOMMERCE'
        education = 'EDUCATION'
        energy_and_utilities = 'ENERGY_AND_UTILITIES'
        entertainment_and_media = 'ENTERTAINMENT_AND_MEDIA'
        financial_services = 'FINANCIAL_SERVICES'
        gaming = 'GAMING'
        goverment_and_politics = 'GOVERMENT_AND_POLITICS'
        motorcycles = 'MOTORCYCLES'
        organizations_and_associations = 'ORGANIZATIONS_AND_ASSOCIATIONS'
        other = 'OTHER'
        professional_services = 'PROFESSIONAL_SERVICES'
        retail = 'RETAIL'
        technology = 'TECHNOLOGY'
        telecom = 'TELECOM'
        travel = 'TRAVEL'

    class Status:
        pending = 'PENDING'
        under_review = 'UNDER_REVIEW'
        approved = 'APPROVED'
        disapproved = 'DISAPPROVED'
        requested_change = 'REQUESTED_CHANGE'
        cancelled = 'CANCELLED'
        auto_approved = 'AUTO_APPROVED'
        auto_disapproved = 'AUTO_DISAPPROVED'
        appeal_pending = 'APPEAL_PENDING'
        appeal_under_review = 'APPEAL_UNDER_REVIEW'
        appeal_approved = 'APPEAL_APPROVED'
        appeal_disapproved = 'APPEAL_DISAPPROVED'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adaccountcreationrequests'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        return Business(api=self._api, fbid=parent_id).create_ad_account_creation_request(fields, params, batch, pending)

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
            target_class=AdAccountCreationRequest,
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
            'ad_accounts_info': 'list<Object>',
            'additional_comment': 'string',
            'address_in_chinese': 'string',
            'address_in_english': 'Object',
            'advertiser_business_id': 'string',
            'business_registration': 'file',
            'business_registration_id': 'string',
            'chinese_legal_entity_name': 'string',
            'contact': 'Object',
            'disapprove_appeal_comment': 'string',
            'english_legal_entity_name': 'string',
            'extended_credit_id': 'string',
            'is_smb': 'bool',
            'official_website_url': 'Object',
            'planning_agency_business_id': 'string',
            'promotable_app_ids': 'list<string>',
            'promotable_page_ids': 'list<string>',
            'promotable_page_urls': 'list<Object>',
            'promotable_urls': 'list<Object>',
            'subvertical': 'subvertical_enum',
            'vertical': 'vertical_enum',
        }
        enums = {
            'subvertical_enum': AdAccountCreationRequest.Subvertical.__dict__.values(),
            'vertical_enum': AdAccountCreationRequest.Vertical.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountCreationRequest,
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

    _field_types = {
        'ad_accounts_info': 'list<Object>',
        'additional_comment': 'string',
        'address_in_chinese': 'string',
        'address_in_english': 'Object',
        'advertiser_business': 'Business',
        'appeal_reason': 'Object',
        'business': 'Business',
        'business_registration_id': 'string',
        'chinese_legal_entity_name': 'string',
        'contact': 'Object',
        'creator': 'User',
        'disapproval_reasons': 'list<Object>',
        'english_legal_entity_name': 'string',
        'extended_credit_id': 'string',
        'id': 'string',
        'is_smb': 'bool',
        'is_test': 'bool',
        'is_under_authorization': 'bool',
        'official_website_url': 'string',
        'planning_agency_business': 'Business',
        'planning_agency_business_id': 'string',
        'promotable_app_ids': 'list<string>',
        'promotable_page_ids': 'list<string>',
        'promotable_urls': 'list<string>',
        'request_change_reasons': 'list<Object>',
        'status': 'string',
        'subvertical': 'string',
        'time_created': 'datetime',
        'vertical': 'string',
        'advertiser_business_id': 'string',
        'business_registration': 'file',
        'promotable_page_urls': 'list<Object>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Subvertical'] = AdAccountCreationRequest.Subvertical.__dict__.values()
        field_enum_info['Vertical'] = AdAccountCreationRequest.Vertical.__dict__.values()
        field_enum_info['Status'] = AdAccountCreationRequest.Status.__dict__.values()
        return field_enum_info
