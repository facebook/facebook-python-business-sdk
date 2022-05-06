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

class ProductGroup(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductGroup = True
        super(ProductGroup, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        id = 'id'
        product_catalog = 'product_catalog'
        retailer_id = 'retailer_id'
        variants = 'variants'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'product_groups'

    # @deprecated api_create is being deprecated
    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_product_group(fields, params, batch, success, failure, pending)

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'deletion_method': 'deletion_method_enum',
        }
        enums = {
            'deletion_method_enum': [
                'DELETE_ITEMS',
                'ONLY_IF_EMPTY',
            ],
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
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductGroup,
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
            'default_product_id': 'string',
            'variants': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductGroup,
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

    def get_products(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.productitem import ProductItem
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/products',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductItem, api=self._api),
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

    def create_product(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
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
            'custom_number_0': 'unsigned int',
            'custom_number_1': 'unsigned int',
            'custom_number_2': 'unsigned int',
            'custom_number_3': 'unsigned int',
            'custom_number_4': 'unsigned int',
            'description': 'string',
            'expiration_date': 'string',
            'fb_product_category': 'string',
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
            'marked_for_product_launch': 'marked_for_product_launch_enum',
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
            'quantity_to_sell_on_facebook': 'unsigned int',
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
            'availability_enum': [
                'available for order',
                'discontinued',
                'in stock',
                'out of stock',
                'pending',
                'preorder',
            ],
            'commerce_tax_category_enum': [
                'FB_ANIMAL',
                'FB_ANIMAL_SUPP',
                'FB_APRL',
                'FB_APRL_ACCESSORIES',
                'FB_APRL_ATHL_UNIF',
                'FB_APRL_CASES',
                'FB_APRL_CLOTHING',
                'FB_APRL_COSTUME',
                'FB_APRL_CSTM',
                'FB_APRL_FORMAL',
                'FB_APRL_HANDBAG',
                'FB_APRL_JEWELRY',
                'FB_APRL_SHOE',
                'FB_APRL_SHOE_ACC',
                'FB_APRL_SWIM',
                'FB_APRL_SWIM_CHIL',
                'FB_APRL_SWIM_CVR',
                'FB_ARTS',
                'FB_ARTS_HOBBY',
                'FB_ARTS_PARTY',
                'FB_ARTS_PARTY_GIFT_CARD',
                'FB_ARTS_TICKET',
                'FB_BABY',
                'FB_BABY_BATH',
                'FB_BABY_BLANKET',
                'FB_BABY_DIAPER',
                'FB_BABY_GIFT_SET',
                'FB_BABY_HEALTH',
                'FB_BABY_NURSING',
                'FB_BABY_POTTY_TRN',
                'FB_BABY_SAFE',
                'FB_BABY_TOYS',
                'FB_BABY_TRANSPORT',
                'FB_BABY_TRANSPORT_ACC',
                'FB_BAGS',
                'FB_BAGS_BKPK',
                'FB_BAGS_BOXES',
                'FB_BAGS_BRFCS',
                'FB_BAGS_CSMT_BAG',
                'FB_BAGS_DFFL',
                'FB_BAGS_DIPR',
                'FB_BAGS_FNNY',
                'FB_BAGS_GRMT',
                'FB_BAGS_LUGG',
                'FB_BAGS_LUG_ACC',
                'FB_BAGS_MSGR',
                'FB_BAGS_TOTE',
                'FB_BAGS_TRN_CAS',
                'FB_BLDG',
                'FB_BLDG_ACC',
                'FB_BLDG_CNSMB',
                'FB_BLDG_FENCE',
                'FB_BLDG_FUEL_TNK',
                'FB_BLDG_HT_VNT',
                'FB_BLDG_LOCK',
                'FB_BLDG_MATRL',
                'FB_BLDG_PLMB',
                'FB_BLDG_PUMP',
                'FB_BLDG_PWRS',
                'FB_BLDG_STR_TANK',
                'FB_BLDG_S_ENG',
                'FB_BLDG_TL_ACC',
                'FB_BLDG_TOOL',
                'FB_BUSIND',
                'FB_BUSIND_ADVERTISING',
                'FB_BUSIND_AGRICULTURE',
                'FB_BUSIND_AUTOMATION',
                'FB_BUSIND_HEAVY_MACH',
                'FB_BUSIND_LAB',
                'FB_BUSIND_MEDICAL',
                'FB_BUSIND_RETAIL',
                'FB_BUSIND_SANITARY_CT',
                'FB_BUSIND_SIGN',
                'FB_BUSIND_STORAGE',
                'FB_BUSIND_STORAGE_ACC',
                'FB_BUSIND_WORK_GEAR',
                'FB_CAMERA_ACC',
                'FB_CAMERA_CAMERA',
                'FB_CAMERA_OPTIC',
                'FB_CAMERA_OPTICS',
                'FB_CAMERA_PHOTO',
                'FB_ELEC',
                'FB_ELEC_ACC',
                'FB_ELEC_ARCDADE',
                'FB_ELEC_AUDIO',
                'FB_ELEC_CIRCUIT',
                'FB_ELEC_COMM',
                'FB_ELEC_COMPUTER',
                'FB_ELEC_GPS_ACC',
                'FB_ELEC_GPS_NAV',
                'FB_ELEC_GPS_TRK',
                'FB_ELEC_MARINE',
                'FB_ELEC_NETWORK',
                'FB_ELEC_PART',
                'FB_ELEC_PRINT',
                'FB_ELEC_RADAR',
                'FB_ELEC_SFTWR',
                'FB_ELEC_SPEED_RDR',
                'FB_ELEC_TELEVISION',
                'FB_ELEC_TOLL',
                'FB_ELEC_VIDEO',
                'FB_ELEC_VID_GM_ACC',
                'FB_ELEC_VID_GM_CNSL',
                'FB_FOOD',
                'FB_FURN',
                'FB_FURN_BABY',
                'FB_FURN_BENCH',
                'FB_FURN_CART',
                'FB_FURN_CHAIR',
                'FB_FURN_CHAIR_ACC',
                'FB_FURN_DIVIDE',
                'FB_FURN_DIVIDE_ACC',
                'FB_FURN_ENT_CTR',
                'FB_FURN_FUTN',
                'FB_FURN_FUTN_PAD',
                'FB_FURN_OFFICE',
                'FB_FURN_OFFICE_ACC',
                'FB_FURN_OTTO',
                'FB_FURN_OUTDOOR',
                'FB_FURN_OUTDOOR_ACC',
                'FB_FURN_SETS',
                'FB_FURN_SHELVE_ACC',
                'FB_FURN_SHLF',
                'FB_FURN_SOFA',
                'FB_FURN_SOFA_ACC',
                'FB_FURN_STORAGE',
                'FB_FURN_TABL',
                'FB_FURN_TABL_ACC',
                'FB_GENERIC_TAXABLE',
                'FB_HLTH',
                'FB_HLTH_HLTH',
                'FB_HLTH_JWL_CR',
                'FB_HLTH_LILP_BLM',
                'FB_HLTH_LTN_SPF',
                'FB_HLTH_PRSL_CR',
                'FB_HLTH_SKN_CR',
                'FB_HMGN',
                'FB_HMGN_BATH',
                'FB_HMGN_DCOR',
                'FB_HMGN_EMGY',
                'FB_HMGN_FPLC',
                'FB_HMGN_FPLC_ACC',
                'FB_HMGN_GS_SFT',
                'FB_HMGN_HS_ACC',
                'FB_HMGN_HS_APP',
                'FB_HMGN_HS_SPL',
                'FB_HMGN_KTCN',
                'FB_HMGN_LAWN',
                'FB_HMGN_LGHT',
                'FB_HMGN_LINN',
                'FB_HMGN_LT_ACC',
                'FB_HMGN_OTDR',
                'FB_HMGN_POOL',
                'FB_HMGN_SCTY',
                'FB_HMGN_SMK_ACC',
                'FB_HMGN_UMBR',
                'FB_HMGN_UMBR_ACC',
                'FB_MDIA',
                'FB_MDIA_BOOK',
                'FB_MDIA_DVDS',
                'FB_MDIA_MAG',
                'FB_MDIA_MANL',
                'FB_MDIA_MUSC',
                'FB_MDIA_PRJ_PLN',
                'FB_MDIA_SHT_MUS',
                'FB_OFFC',
                'FB_OFFC_BKAC',
                'FB_OFFC_CRTS',
                'FB_OFFC_DSKP',
                'FB_OFFC_EQIP',
                'FB_OFFC_FLNG',
                'FB_OFFC_GNRL',
                'FB_OFFC_INSTM',
                'FB_OFFC_LP_DSK',
                'FB_OFFC_MATS',
                'FB_OFFC_NM_PLT',
                'FB_OFFC_PPR_HNDL',
                'FB_OFFC_PRSNT_SPL',
                'FB_OFFC_SEALR',
                'FB_OFFC_SHIP_SPL',
                'FB_RLGN',
                'FB_RLGN_CMNY',
                'FB_RLGN_ITEM',
                'FB_RLGN_WEDD',
                'FB_SFTWR',
                'FB_SFWR_CMPTR',
                'FB_SFWR_DGTL_GD',
                'FB_SFWR_GAME',
                'FB_SHIPPING',
                'FB_SPOR',
                'FB_SPORT_ATHL',
                'FB_SPORT_ATHL_CLTH',
                'FB_SPORT_ATHL_SHOE',
                'FB_SPORT_ATHL_SPRT',
                'FB_SPORT_EXRCS',
                'FB_SPORT_INDR_GM',
                'FB_SPORT_OTDR_GM',
                'FB_TOYS',
                'FB_TOYS_EQIP',
                'FB_TOYS_GAME',
                'FB_TOYS_PZZL',
                'FB_TOYS_TMRS',
                'FB_TOYS_TOYS',
                'FB_VEHI',
                'FB_VEHI_PART',
            ],
            'condition_enum': [
                'cpo',
                'new',
                'open_box_new',
                'refurbished',
                'used',
                'used_fair',
                'used_good',
                'used_like_new',
            ],
            'gender_enum': [
                'female',
                'male',
                'unisex',
            ],
            'marked_for_product_launch_enum': [
                'default',
                'marked',
                'not_marked',
            ],
            'visibility_enum': [
                'published',
                'staging',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/products',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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
        'id': 'string',
        'product_catalog': 'ProductCatalog',
        'retailer_id': 'string',
        'variants': 'list<ProductVariant>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


