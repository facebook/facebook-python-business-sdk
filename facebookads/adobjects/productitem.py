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

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker

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
        additional_image_urls = 'additional_image_urls'
        age_group = 'age_group'
        applinks = 'applinks'
        availability = 'availability'
        brand = 'brand'
        category = 'category'
        color = 'color'
        commerce_insights = 'commerce_insights'
        condition = 'condition'
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
        image_url = 'image_url'
        manufacturer_part_number = 'manufacturer_part_number'
        material = 'material'
        name = 'name'
        ordering_index = 'ordering_index'
        pattern = 'pattern'
        price = 'price'
        product_feed = 'product_feed'
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
        size = 'size'
        start_date = 'start_date'
        url = 'url'
        visibility = 'visibility'
        android_app_name = 'android_app_name'
        android_class = 'android_class'
        android_package = 'android_package'
        android_url = 'android_url'
        checkout_url = 'checkout_url'
        currency = 'currency'
        inventory = 'inventory'
        ios_app_name = 'ios_app_name'
        ios_app_store_id = 'ios_app_store_id'
        ios_url = 'ios_url'
        ipad_app_name = 'ipad_app_name'
        ipad_app_store_id = 'ipad_app_store_id'
        ipad_url = 'ipad_url'
        iphone_app_name = 'iphone_app_name'
        iphone_app_store_id = 'iphone_app_store_id'
        iphone_url = 'iphone_url'
        windows_phone_app_id = 'windows_phone_app_id'
        windows_phone_app_name = 'windows_phone_app_name'
        windows_phone_url = 'windows_phone_url'

    class AgeGroup:
        kids = 'kids'
        adult = 'adult'
        infant = 'infant'
        toddler = 'toddler'
        newborn = 'newborn'

    class Availability:
        in_stock = 'in stock'
        out_of_stock = 'out of stock'
        preorder = 'preorder'
        available_for_order = 'available for order'
        discontinued = 'discontinued'

    class Condition:
        new = 'new'
        refurbished = 'refurbished'
        used = 'used'

    class Gender:
        female = 'female'
        male = 'male'
        unisex = 'unisex'

    class ReviewStatus:
        pending = 'pending'
        rejected = 'rejected'
        approved = 'approved'

    class ShippingWeightUnit:
        lb = 'lb'
        oz = 'oz'
        value_g = 'g'
        kg = 'kg'

    class Visibility:
        staging = 'staging'
        published = 'published'

    class ReviewRejectionReasons:
        unknown = 'UNKNOWN'
        irregular_app_install = 'IRREGULAR_APP_INSTALL'
        text_overlay = 'TEXT_OVERLAY'
        adult_content = 'ADULT_CONTENT'
        adult_health = 'ADULT_HEALTH'
        alcohol = 'ALCOHOL'
        animated_image = 'ANIMATED_IMAGE'
        before_and_after = 'BEFORE_AND_AFTER'
        casual_dating = 'CASUAL_DATING'
        dating = 'DATING'
        facebook_reference = 'FACEBOOK_REFERENCE'
        financial = 'FINANCIAL'
        gambling = 'GAMBLING'
        idealized_body = 'IDEALIZED_BODY'
        language = 'LANGUAGE'
        landing_page_fail = 'LANDING_PAGE_FAIL'
        sexual = 'SEXUAL'
        test = 'TEST'
        tobacco_sale = 'TOBACCO_SALE'
        trapping = 'TRAPPING'
        unsubstantiated_claim = 'UNSUBSTANTIATED_CLAIM'
        other = 'OTHER'
        weapon_sale = 'WEAPON_SALE'
        work_from_home = 'WORK_FROM_HOME'
        cash_advance = 'CASH_ADVANCE'
        shock_and_scare = 'SHOCK_AND_SCARE'
        spy_camera = 'SPY_CAMERA'
        bad_health_product = 'BAD_HEALTH_PRODUCT'
        grammar = 'GRAMMAR'
        illegal = 'ILLEGAL'
        misuse_of_like = 'MISUSE_OF_LIKE'
        non_existent_functionality = 'NON_EXISTENT_FUNCTIONALITY'
        online_pharmacy = 'ONLINE_PHARMACY'
        penny_auction = 'PENNY_AUCTION'
        porn = 'PORN'
        copyright = 'COPYRIGHT'
        trademark = 'TRADEMARK'
        counterfeit = 'COUNTERFEIT'
        system_issue = 'SYSTEM_ISSUE'
        q_blurry_pixelated = 'Q_BLURRY_PIXELATED'
        q_borderline_sexual = 'Q_BORDERLINE_SEXUAL'
        q_border_background = 'Q_BORDER_BACKGROUND'
        q_grammar_capitalization = 'Q_GRAMMAR_CAPITALIZATION'
        q_irrelevant_image_copy = 'Q_IRRELEVANT_IMAGE_COPY'
        q_misleading = 'Q_MISLEADING'
        q_multiple_images = 'Q_MULTIPLE_IMAGES'
        q_hot_button = 'Q_HOT_BUTTON'
        q_zoom_in_body_parts = 'Q_ZOOM_IN_BODY_PARTS'
        q_zoom_in_food = 'Q_ZOOM_IN_FOOD'
        quality_low = 'QUALITY_LOW'
        lead_ad_from_aggregator = 'LEAD_AD_FROM_AGGREGATOR'
        unsuitable_question = 'UNSUITABLE_QUESTION'
        fraud_associated = 'FRAUD_ASSOCIATED'
        mystery_image = 'MYSTERY_IMAGE'
        app_scam = 'APP_SCAM'
        text_penalty_high = 'TEXT_PENALTY_HIGH'
        text_penalty_medium = 'TEXT_PENALTY_MEDIUM'
        text_penalty_low = 'TEXT_PENALTY_LOW'
        bad_subscription = 'BAD_SUBSCRIPTION'
        facebook_word_manipulated = 'FACEBOOK_WORD_MANIPULATED'
        facebook_icons = 'FACEBOOK_ICONS'
        facebook_page_lookalike = 'FACEBOOK_PAGE_LOOKALIKE'
        facebook_logo_focus = 'FACEBOOK_LOGO_FOCUS'
        facebook_logo_overlap = 'FACEBOOK_LOGO_OVERLAP'
        facebook_logo = 'FACEBOOK_LOGO'
        facebook_logo_thumbs_up = 'FACEBOOK_LOGO_THUMBS_UP'
        facebook_screenshot_prod = 'FACEBOOK_SCREENSHOT_PROD'
        facebook_wordmark = 'FACEBOOK_WORDMARK'
        facebook_zuckpic = 'FACEBOOK_ZUCKPIC'
        highlighted_pain_points = 'HIGHLIGHTED_PAIN_POINTS'
        perfect_body = 'PERFECT_BODY'
        scales = 'SCALES'
        tape_measure = 'TAPE_MEASURE'
        undesirable_body = 'UNDESIRABLE_BODY'
        zoom_body_part = 'ZOOM_BODY_PART'
        harrassment = 'HARRASSMENT'
        user_attributes_callout = 'USER_ATTRIBUTES_CALLOUT'
        user_finanical_callout = 'USER_FINANICAL_CALLOUT'
        user_health_attributes = 'USER_HEALTH_ATTRIBUTES'
        user_weight_attributes = 'USER_WEIGHT_ATTRIBUTES'
        profanity = 'PROFANITY'
        fake_form_elements = 'FAKE_FORM_ELEMENTS'
        fake_notifications = 'FAKE_NOTIFICATIONS'
        mouse_cursor = 'MOUSE_CURSOR'
        play_button = 'PLAY_BUTTON'
        qr_codes = 'QR_CODES'
        excessive_skin = 'EXCESSIVE_SKIN'
        indirect_nudity = 'INDIRECT_NUDITY'
        indirect_sexual_act = 'INDIRECT_SEXUAL_ACT'
        sexual_other = 'SEXUAL_OTHER'
        zoom_sexual_image = 'ZOOM_SEXUAL_IMAGE'
        breastenlargement = 'BREASTENLARGEMENT'
        genitalsurgery = 'GENITALSURGERY'
        libido = 'LIBIDO'
        nudity_notporn = 'NUDITY_NOTPORN'
        pheromone = 'PHEROMONE'
        scheme_hotgirlpage = 'SCHEME_HOTGIRLPAGE'
        services_seduction = 'SERVICES_SEDUCTION'
        sexpublications = 'SEXPUBLICATIONS'
        sextoys = 'SEXTOYS'
        sexualpleasure = 'SEXUALPLEASURE'
        stripclubs = 'STRIPCLUBS'
        mention_botox = 'MENTION_BOTOX'
        mention_dietproduct = 'MENTION_DIETPRODUCT'
        mention_lasers = 'MENTION_LASERS'
        mention_sexualhealth = 'MENTION_SEXUALHEALTH'
        mention_supplement = 'MENTION_SUPPLEMENT'
        mention_surgery = 'MENTION_SURGERY'
        mention_brand_alcohol = 'MENTION_BRAND_ALCOHOL'
        mention_consumption_alcohol = 'MENTION_CONSUMPTION_ALCOHOL'
        mention_sales_alcohol = 'MENTION_SALES_ALCOHOL'
        sponsorship = 'SPONSORSHIP'
        mention_sales_badhealthproduct = 'MENTION_SALES_BADHEALTHPRODUCT'
        unclear_cancellation_subscription = 'UNCLEAR_CANCELLATION_SUBSCRIPTION'
        unclear_pricing_subscription = 'UNCLEAR_PRICING_SUBSCRIPTION'
        ba_hairloss = 'BA_HAIRLOSS'
        ba_medical = 'BA_MEDICAL'
        ba_skin = 'BA_SKIN'
        ba_teeth = 'BA_TEETH'
        ba_weightloss = 'BA_WEIGHTLOSS'
        gibberish = 'GIBBERISH'
        randomcharacters = 'RANDOMCHARACTERS'
        drugs_illegal = 'DRUGS_ILLEGAL'
        human_trafficking = 'HUMAN_TRAFFICKING'
        services_escort = 'SERVICES_ESCORT'
        image_animalcruelty = 'IMAGE_ANIMALCRUELTY'
        image_medical = 'IMAGE_MEDICAL'
        image_offensivegesture = 'IMAGE_OFFENSIVEGESTURE'
        image_vehiclecollision = 'IMAGE_VEHICLECOLLISION'
        image_weaponatuser = 'IMAGE_WEAPONATUSER'
        mention_image_violence_gore = 'MENTION_IMAGE_VIOLENCE_GORE'
        mention_accessory_consumption_tobacco = 'MENTION_ACCESSORY_CONSUMPTION_TOBACCO'
        mention_brand_tobacco = 'MENTION_BRAND_TOBACCO'
        falsenotification = 'FALSENOTIFICATION'
        impossiblecures = 'IMPOSSIBLECURES'
        mention_numeric_claim = 'MENTION_NUMERIC_CLAIM'
        mention_trickstips = 'MENTION_TRICKSTIPS'
        specificindividualclaim = 'SPECIFICINDIVIDUALCLAIM'
        unrealistic_ebookpromise = 'UNREALISTIC_EBOOKPROMISE'
        videosexual = 'VIDEOSEXUAL'
        videoschockandscare = 'VIDEOSCHOCKANDSCARE'
        videolanguage = 'VIDEOLANGUAGE'
        not_dating_partner = 'NOT_DATING_PARTNER'

    @classmethod
    def get_endpoint(cls):
        return 'products'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_product(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'id': 'string',
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

        return request if pending else request.execute()

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
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
            target_class=ProductItem,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'additional_image_urls': 'list<string>',
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
            'id': 'string',
            'image_url': 'string',
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
            'name': 'string',
            'ordering_index': 'unsigned int',
            'pattern': 'string',
            'price': 'unsigned int',
            'product_type': 'string',
            'sale_price': 'unsigned int',
            'sale_price_end_date': 'datetime',
            'sale_price_start_date': 'datetime',
            'size': 'string',
            'start_date': 'string',
            'url': 'string',
            'visibility': 'visibility_enum',
            'windows_phone_app_id': 'unsigned int',
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

        return request if pending else request.execute()

    def get_product_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.productset import ProductSet
        self.assure_call()
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
            response_parser=ObjectParser(target_class=ProductSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    _field_types = {
        'additional_image_urls': 'list<string>',
        'age_group': 'AgeGroup',
        'applinks': 'AppLinks',
        'availability': 'Availability',
        'brand': 'string',
        'category': 'string',
        'color': 'string',
        'commerce_insights': 'ProductItemCommerceInsights',
        'condition': 'Condition',
        'custom_data': 'list<Object>',
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
        'image_url': 'string',
        'manufacturer_part_number': 'string',
        'material': 'string',
        'name': 'string',
        'ordering_index': 'int',
        'pattern': 'string',
        'price': 'string',
        'product_feed': 'ProductFeed',
        'product_type': 'string',
        'retailer_id': 'string',
        'retailer_product_group_id': 'string',
        'review_rejection_reasons': 'ReviewRejectionReasons',
        'review_status': 'ReviewStatus',
        'sale_price': 'string',
        'sale_price_end_date': 'string',
        'sale_price_start_date': 'string',
        'shipping_weight_unit': 'ShippingWeightUnit',
        'shipping_weight_value': 'float',
        'size': 'string',
        'start_date': 'string',
        'url': 'string',
        'visibility': 'Visibility',
        'android_app_name': 'string',
        'android_class': 'string',
        'android_package': 'string',
        'android_url': 'string',
        'checkout_url': 'string',
        'currency': 'string',
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
        'windows_phone_app_id': 'unsigned int',
        'windows_phone_app_name': 'string',
        'windows_phone_url': 'string',
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
        field_enum_info['ReviewRejectionReasons'] = ProductItem.ReviewRejectionReasons.__dict__.values()
        return field_enum_info
