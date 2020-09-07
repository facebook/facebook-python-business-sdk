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
        additional_image_files = 'additional_image_files'
        android_app_name = 'android_app_name'
        android_class = 'android_class'
        android_package = 'android_package'
        android_url = 'android_url'
        checkout_url = 'checkout_url'
        commerce_tax_category = 'commerce_tax_category'
        ios_app_name = 'ios_app_name'
        ios_app_store_id = 'ios_app_store_id'
        ios_url = 'ios_url'
        ipad_app_name = 'ipad_app_name'
        ipad_app_store_id = 'ipad_app_store_id'
        ipad_url = 'ipad_url'
        iphone_app_name = 'iphone_app_name'
        iphone_app_store_id = 'iphone_app_store_id'
        iphone_url = 'iphone_url'
        launch_date = 'launch_date'
        offer_price_amount = 'offer_price_amount'
        offer_price_end_date = 'offer_price_end_date'
        offer_price_start_date = 'offer_price_start_date'
        return_policy_days = 'return_policy_days'
        windows_phone_app_id = 'windows_phone_app_id'
        windows_phone_app_name = 'windows_phone_app_name'
        windows_phone_url = 'windows_phone_url'

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
        used_fair = 'used_fair'
        used_good = 'used_good'
        used_like_new = 'used_like_new'

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

    class CommerceTaxCategory:
        fb_animal = 'FB_ANIMAL'
        fb_animal_supp = 'FB_ANIMAL_SUPP'
        fb_aprl = 'FB_APRL'
        fb_aprl_accessories = 'FB_APRL_ACCESSORIES'
        fb_aprl_athl_unif = 'FB_APRL_ATHL_UNIF'
        fb_aprl_cases = 'FB_APRL_CASES'
        fb_aprl_clothing = 'FB_APRL_CLOTHING'
        fb_aprl_costume = 'FB_APRL_COSTUME'
        fb_aprl_cstm = 'FB_APRL_CSTM'
        fb_aprl_handbag = 'FB_APRL_HANDBAG'
        fb_aprl_jewelry = 'FB_APRL_JEWELRY'
        fb_aprl_shoe = 'FB_APRL_SHOE'
        fb_aprl_shoe_acc = 'FB_APRL_SHOE_ACC'
        fb_aprl_swim = 'FB_APRL_SWIM'
        fb_aprl_swim_chil = 'FB_APRL_SWIM_CHIL'
        fb_aprl_swim_cvr = 'FB_APRL_SWIM_CVR'
        fb_arts = 'FB_ARTS'
        fb_arts_hobby = 'FB_ARTS_HOBBY'
        fb_arts_party = 'FB_ARTS_PARTY'
        fb_arts_party_gift_card = 'FB_ARTS_PARTY_GIFT_CARD'
        fb_arts_ticket = 'FB_ARTS_TICKET'
        fb_baby = 'FB_BABY'
        fb_baby_bath = 'FB_BABY_BATH'
        fb_baby_blanket = 'FB_BABY_BLANKET'
        fb_baby_diaper = 'FB_BABY_DIAPER'
        fb_baby_gift_set = 'FB_BABY_GIFT_SET'
        fb_baby_health = 'FB_BABY_HEALTH'
        fb_baby_nursing = 'FB_BABY_NURSING'
        fb_baby_potty_trn = 'FB_BABY_POTTY_TRN'
        fb_baby_safe = 'FB_BABY_SAFE'
        fb_baby_toys = 'FB_BABY_TOYS'
        fb_baby_transport = 'FB_BABY_TRANSPORT'
        fb_baby_transport_acc = 'FB_BABY_TRANSPORT_ACC'
        fb_bags = 'FB_BAGS'
        fb_bags_bkpk = 'FB_BAGS_BKPK'
        fb_bags_boxes = 'FB_BAGS_BOXES'
        fb_bags_brfcs = 'FB_BAGS_BRFCS'
        fb_bags_csmt_bag = 'FB_BAGS_CSMT_BAG'
        fb_bags_dffl = 'FB_BAGS_DFFL'
        fb_bags_dipr = 'FB_BAGS_DIPR'
        fb_bags_fnny = 'FB_BAGS_FNNY'
        fb_bags_grmt = 'FB_BAGS_GRMT'
        fb_bags_lugg = 'FB_BAGS_LUGG'
        fb_bags_lug_acc = 'FB_BAGS_LUG_ACC'
        fb_bags_msgr = 'FB_BAGS_MSGR'
        fb_bags_tote = 'FB_BAGS_TOTE'
        fb_bags_trn_cas = 'FB_BAGS_TRN_CAS'
        fb_bldg = 'FB_BLDG'
        fb_bldg_acc = 'FB_BLDG_ACC'
        fb_bldg_cnsmb = 'FB_BLDG_CNSMB'
        fb_bldg_fence = 'FB_BLDG_FENCE'
        fb_bldg_fuel_tnk = 'FB_BLDG_FUEL_TNK'
        fb_bldg_ht_vnt = 'FB_BLDG_HT_VNT'
        fb_bldg_lock = 'FB_BLDG_LOCK'
        fb_bldg_matrl = 'FB_BLDG_MATRL'
        fb_bldg_plmb = 'FB_BLDG_PLMB'
        fb_bldg_pump = 'FB_BLDG_PUMP'
        fb_bldg_pwrs = 'FB_BLDG_PWRS'
        fb_bldg_str_tank = 'FB_BLDG_STR_TANK'
        fb_bldg_s_eng = 'FB_BLDG_S_ENG'
        fb_bldg_tl_acc = 'FB_BLDG_TL_ACC'
        fb_bldg_tool = 'FB_BLDG_TOOL'
        fb_busind = 'FB_BUSIND'
        fb_busind_advertising = 'FB_BUSIND_ADVERTISING'
        fb_busind_agriculture = 'FB_BUSIND_AGRICULTURE'
        fb_busind_automation = 'FB_BUSIND_AUTOMATION'
        fb_busind_heavy_mach = 'FB_BUSIND_HEAVY_MACH'
        fb_busind_lab = 'FB_BUSIND_LAB'
        fb_busind_medical = 'FB_BUSIND_MEDICAL'
        fb_busind_retail = 'FB_BUSIND_RETAIL'
        fb_busind_sanitary_ct = 'FB_BUSIND_SANITARY_CT'
        fb_busind_sign = 'FB_BUSIND_SIGN'
        fb_busind_storage = 'FB_BUSIND_STORAGE'
        fb_busind_storage_acc = 'FB_BUSIND_STORAGE_ACC'
        fb_busind_work_gear = 'FB_BUSIND_WORK_GEAR'
        fb_camera_acc = 'FB_CAMERA_ACC'
        fb_camera_camera = 'FB_CAMERA_CAMERA'
        fb_camera_optic = 'FB_CAMERA_OPTIC'
        fb_camera_optics = 'FB_CAMERA_OPTICS'
        fb_camera_photo = 'FB_CAMERA_PHOTO'
        fb_elec = 'FB_ELEC'
        fb_elec_acc = 'FB_ELEC_ACC'
        fb_elec_arcdade = 'FB_ELEC_ARCDADE'
        fb_elec_audio = 'FB_ELEC_AUDIO'
        fb_elec_circuit = 'FB_ELEC_CIRCUIT'
        fb_elec_comm = 'FB_ELEC_COMM'
        fb_elec_computer = 'FB_ELEC_COMPUTER'
        fb_elec_gps_acc = 'FB_ELEC_GPS_ACC'
        fb_elec_gps_nav = 'FB_ELEC_GPS_NAV'
        fb_elec_gps_trk = 'FB_ELEC_GPS_TRK'
        fb_elec_marine = 'FB_ELEC_MARINE'
        fb_elec_network = 'FB_ELEC_NETWORK'
        fb_elec_part = 'FB_ELEC_PART'
        fb_elec_print = 'FB_ELEC_PRINT'
        fb_elec_radar = 'FB_ELEC_RADAR'
        fb_elec_speed_rdr = 'FB_ELEC_SPEED_RDR'
        fb_elec_toll = 'FB_ELEC_TOLL'
        fb_elec_video = 'FB_ELEC_VIDEO'
        fb_elec_vid_gm_acc = 'FB_ELEC_VID_GM_ACC'
        fb_elec_vid_gm_cnsl = 'FB_ELEC_VID_GM_CNSL'
        fb_food = 'FB_FOOD'
        fb_furn = 'FB_FURN'
        fb_furn_baby = 'FB_FURN_BABY'
        fb_furn_bench = 'FB_FURN_BENCH'
        fb_furn_cart = 'FB_FURN_CART'
        fb_furn_chair = 'FB_FURN_CHAIR'
        fb_furn_chair_acc = 'FB_FURN_CHAIR_ACC'
        fb_furn_divide = 'FB_FURN_DIVIDE'
        fb_furn_divide_acc = 'FB_FURN_DIVIDE_ACC'
        fb_furn_ent_ctr = 'FB_FURN_ENT_CTR'
        fb_furn_futn = 'FB_FURN_FUTN'
        fb_furn_futn_pad = 'FB_FURN_FUTN_PAD'
        fb_furn_office = 'FB_FURN_OFFICE'
        fb_furn_office_acc = 'FB_FURN_OFFICE_ACC'
        fb_furn_otto = 'FB_FURN_OTTO'
        fb_furn_outdoor = 'FB_FURN_OUTDOOR'
        fb_furn_outdoor_acc = 'FB_FURN_OUTDOOR_ACC'
        fb_furn_sets = 'FB_FURN_SETS'
        fb_furn_shelve_acc = 'FB_FURN_SHELVE_ACC'
        fb_furn_shlf = 'FB_FURN_SHLF'
        fb_furn_sofa = 'FB_FURN_SOFA'
        fb_furn_sofa_acc = 'FB_FURN_SOFA_ACC'
        fb_furn_storage = 'FB_FURN_STORAGE'
        fb_furn_tabl = 'FB_FURN_TABL'
        fb_furn_tabl_acc = 'FB_FURN_TABL_ACC'
        fb_generic_taxable = 'FB_GENERIC_TAXABLE'
        fb_hlth = 'FB_HLTH'
        fb_hlth_hlth = 'FB_HLTH_HLTH'
        fb_hlth_jwl_cr = 'FB_HLTH_JWL_CR'
        fb_hlth_lilp_blm = 'FB_HLTH_LILP_BLM'
        fb_hlth_ltn_spf = 'FB_HLTH_LTN_SPF'
        fb_hlth_prsl_cr = 'FB_HLTH_PRSL_CR'
        fb_hlth_skn_cr = 'FB_HLTH_SKN_CR'
        fb_hmgn = 'FB_HMGN'
        fb_hmgn_bath = 'FB_HMGN_BATH'
        fb_hmgn_dcor = 'FB_HMGN_DCOR'
        fb_hmgn_emgy = 'FB_HMGN_EMGY'
        fb_hmgn_fplc = 'FB_HMGN_FPLC'
        fb_hmgn_fplc_acc = 'FB_HMGN_FPLC_ACC'
        fb_hmgn_gs_sft = 'FB_HMGN_GS_SFT'
        fb_hmgn_hs_acc = 'FB_HMGN_HS_ACC'
        fb_hmgn_hs_app = 'FB_HMGN_HS_APP'
        fb_hmgn_hs_spl = 'FB_HMGN_HS_SPL'
        fb_hmgn_ktcn = 'FB_HMGN_KTCN'
        fb_hmgn_lawn = 'FB_HMGN_LAWN'
        fb_hmgn_lght = 'FB_HMGN_LGHT'
        fb_hmgn_linn = 'FB_HMGN_LINN'
        fb_hmgn_lt_acc = 'FB_HMGN_LT_ACC'
        fb_hmgn_otdr = 'FB_HMGN_OTDR'
        fb_hmgn_pool = 'FB_HMGN_POOL'
        fb_hmgn_scty = 'FB_HMGN_SCTY'
        fb_hmgn_smk_acc = 'FB_HMGN_SMK_ACC'
        fb_hmgn_umbr = 'FB_HMGN_UMBR'
        fb_hmgn_umbr_acc = 'FB_HMGN_UMBR_ACC'
        fb_mdia = 'FB_MDIA'
        fb_mdia_book = 'FB_MDIA_BOOK'
        fb_mdia_dvds = 'FB_MDIA_DVDS'
        fb_mdia_mag = 'FB_MDIA_MAG'
        fb_mdia_manl = 'FB_MDIA_MANL'
        fb_mdia_musc = 'FB_MDIA_MUSC'
        fb_mdia_prj_pln = 'FB_MDIA_PRJ_PLN'
        fb_mdia_sht_mus = 'FB_MDIA_SHT_MUS'
        fb_offc = 'FB_OFFC'
        fb_offc_bkac = 'FB_OFFC_BKAC'
        fb_offc_crts = 'FB_OFFC_CRTS'
        fb_offc_dskp = 'FB_OFFC_DSKP'
        fb_offc_eqip = 'FB_OFFC_EQIP'
        fb_offc_flng = 'FB_OFFC_FLNG'
        fb_offc_gnrl = 'FB_OFFC_GNRL'
        fb_offc_instm = 'FB_OFFC_INSTM'
        fb_offc_lp_dsk = 'FB_OFFC_LP_DSK'
        fb_offc_mats = 'FB_OFFC_MATS'
        fb_offc_nm_plt = 'FB_OFFC_NM_PLT'
        fb_offc_ppr_hndl = 'FB_OFFC_PPR_HNDL'
        fb_offc_prsnt_spl = 'FB_OFFC_PRSNT_SPL'
        fb_offc_sealr = 'FB_OFFC_SEALR'
        fb_offc_ship_spl = 'FB_OFFC_SHIP_SPL'
        fb_rlgn = 'FB_RLGN'
        fb_rlgn_cmny = 'FB_RLGN_CMNY'
        fb_rlgn_item = 'FB_RLGN_ITEM'
        fb_rlgn_wedd = 'FB_RLGN_WEDD'
        fb_sftwr = 'FB_SFTWR'
        fb_sfwr_cmptr = 'FB_SFWR_CMPTR'
        fb_sfwr_dgtl_gd = 'FB_SFWR_DGTL_GD'
        fb_sfwr_game = 'FB_SFWR_GAME'
        fb_shipping = 'FB_SHIPPING'
        fb_spor = 'FB_SPOR'
        fb_sport_athl = 'FB_SPORT_ATHL'
        fb_sport_athl_clth = 'FB_SPORT_ATHL_CLTH'
        fb_sport_athl_shoe = 'FB_SPORT_ATHL_SHOE'
        fb_sport_athl_sprt = 'FB_SPORT_ATHL_SPRT'
        fb_sport_exrcs = 'FB_SPORT_EXRCS'
        fb_sport_indr_gm = 'FB_SPORT_INDR_GM'
        fb_sport_otdr_gm = 'FB_SPORT_OTDR_GM'
        fb_toys = 'FB_TOYS'
        fb_toys_eqip = 'FB_TOYS_EQIP'
        fb_toys_game = 'FB_TOYS_GAME'
        fb_toys_pzzl = 'FB_TOYS_PZZL'
        fb_toys_tmrs = 'FB_TOYS_TMRS'
        fb_toys_toys = 'FB_TOYS_TOYS'
        fb_vehi = 'FB_VEHI'
        fb_vehi_part = 'FB_VEHI_PART'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'products'

    # @deprecated api_create is being deprecated
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
            'additional_image_files': 'list<file>',
            'additional_image_urls': 'list<string>',
            'additional_variant_attributes': 'map',
            'android_app_name': 'string',
            'android_class': 'string',
            'android_package': 'string',
            'android_url': 'string',
            'availability': 'availability_enum',
            'brand': 'string',
            'category': 'string',
            'checkout_url': 'string',
            'color': 'string',
            'commerce_tax_category': 'commerce_tax_category_enum',
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
            'launch_date': 'string',
            'manufacturer_part_number': 'string',
            'material': 'string',
            'mobile_link': 'string',
            'name': 'string',
            'offer_price_amount': 'unsigned int',
            'offer_price_end_date': 'datetime',
            'offer_price_start_date': 'datetime',
            'ordering_index': 'unsigned int',
            'pattern': 'string',
            'price': 'unsigned int',
            'product_type': 'string',
            'retailer_id': 'string',
            'return_policy_days': 'unsigned int',
            'sale_price': 'unsigned int',
            'sale_price_end_date': 'datetime',
            'sale_price_start_date': 'datetime',
            'short_description': 'string',
            'size': 'string',
            'start_date': 'string',
            'url': 'string',
            'visibility': 'visibility_enum',
            'windows_phone_app_id': 'string',
            'windows_phone_app_name': 'string',
            'windows_phone_url': 'string',
        }
        enums = {
            'availability_enum': ProductItem.Availability.__dict__.values(),
            'commerce_tax_category_enum': ProductItem.CommerceTaxCategory.__dict__.values(),
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
        'applinks': 'CatalogItemAppLinks',
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
        'additional_image_files': 'list<file>',
        'android_app_name': 'string',
        'android_class': 'string',
        'android_package': 'string',
        'android_url': 'string',
        'checkout_url': 'string',
        'commerce_tax_category': 'CommerceTaxCategory',
        'ios_app_name': 'string',
        'ios_app_store_id': 'unsigned int',
        'ios_url': 'string',
        'ipad_app_name': 'string',
        'ipad_app_store_id': 'unsigned int',
        'ipad_url': 'string',
        'iphone_app_name': 'string',
        'iphone_app_store_id': 'unsigned int',
        'iphone_url': 'string',
        'launch_date': 'string',
        'offer_price_amount': 'unsigned int',
        'offer_price_end_date': 'datetime',
        'offer_price_start_date': 'datetime',
        'return_policy_days': 'unsigned int',
        'windows_phone_app_id': 'string',
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
        field_enum_info['CommerceTaxCategory'] = ProductItem.CommerceTaxCategory.__dict__.values()
        return field_enum_info


