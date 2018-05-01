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

class NativeOffer(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isNativeOffer = True
        super(NativeOffer, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        barcode_photo = 'barcode_photo'
        barcode_photo_uri = 'barcode_photo_uri'
        barcode_type = 'barcode_type'
        barcode_value = 'barcode_value'
        details = 'details'
        disable_location = 'disable_location'
        discounts = 'discounts'
        expiration_time = 'expiration_time'
        id = 'id'
        instore_code = 'instore_code'
        location_type = 'location_type'
        max_save_count = 'max_save_count'
        online_code = 'online_code'
        page = 'page'
        page_set_id = 'page_set_id'
        redemption_link = 'redemption_link'
        save_count = 'save_count'
        terms = 'terms'
        title = 'title'
        total_unique_codes = 'total_unique_codes'
        unique_codes = 'unique_codes'
        unique_codes_file_code_type = 'unique_codes_file_code_type'
        unique_codes_file_name = 'unique_codes_file_name'
        unique_codes_file_upload_status = 'unique_codes_file_upload_status'

    class UniqueCodesFileCodeType:
        discount_codes = 'discount_codes'
        barcodes = 'barcodes'
        online_discount_codes = 'online_discount_codes'
        instore_discount_codes = 'instore_discount_codes'
        instore_barcodes = 'instore_barcodes'
        discount_and_barcodes = 'discount_and_barcodes'
        discount_and_discount = 'discount_and_discount'

    class BarcodeType:
        code128 = 'CODE128'
        code128b = 'CODE128B'
        code93 = 'CODE93'
        databar = 'DATABAR'
        databar_expanded = 'DATABAR_EXPANDED'
        databar_expanded_stacked = 'DATABAR_EXPANDED_STACKED'
        databar_limited = 'DATABAR_LIMITED'
        datamatrix = 'DATAMATRIX'
        ean = 'EAN'
        pdf417 = 'PDF417'
        qr = 'QR'
        upc_a = 'UPC_A'
        upc_e = 'UPC_E'

    class LocationType:
        online = 'online'
        offline = 'offline'
        both = 'both'

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
            target_class=NativeOffer,
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

    def create_code(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'file': 'file',
            'unique_codes_file_code_type': 'unique_codes_file_code_type_enum',
        }
        enums = {
            'unique_codes_file_code_type_enum': NativeOffer.UniqueCodesFileCodeType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/codes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=NativeOffer,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=NativeOffer, api=self._api),
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

    def create_native_offer_view(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'ad_account': 'string',
            'ad_image_hashes': 'list<string>',
            'carousel_captions': 'list<string>',
            'carousel_links': 'list<string>',
            'image_crops': 'list<map>',
            'message': 'string',
            'photos': 'list<string>',
            'published': 'bool',
            'published_ads': 'bool',
            'urls': 'list<string>',
            'videos': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/nativeofferviews',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=NativeOffer,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=NativeOffer, api=self._api),
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
        'barcode_photo': 'string',
        'barcode_photo_uri': 'string',
        'barcode_type': 'string',
        'barcode_value': 'string',
        'details': 'string',
        'disable_location': 'bool',
        'discounts': 'list<Object>',
        'expiration_time': 'datetime',
        'id': 'string',
        'instore_code': 'string',
        'location_type': 'string',
        'max_save_count': 'int',
        'online_code': 'string',
        'page': 'Page',
        'page_set_id': 'string',
        'redemption_link': 'string',
        'save_count': 'int',
        'terms': 'string',
        'title': 'string',
        'total_unique_codes': 'string',
        'unique_codes': 'string',
        'unique_codes_file_code_type': 'string',
        'unique_codes_file_name': 'string',
        'unique_codes_file_upload_status': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['UniqueCodesFileCodeType'] = NativeOffer.UniqueCodesFileCodeType.__dict__.values()
        field_enum_info['BarcodeType'] = NativeOffer.BarcodeType.__dict__.values()
        field_enum_info['LocationType'] = NativeOffer.LocationType.__dict__.values()
        return field_enum_info
