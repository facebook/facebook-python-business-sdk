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

class LocalServiceBusiness(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isLocalServiceBusiness = True
        super(LocalServiceBusiness, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        applinks = 'applinks'
        availability = 'availability'
        brand = 'brand'
        category = 'category'
        category_specific_fields = 'category_specific_fields'
        condition = 'condition'
        cuisine_type = 'cuisine_type'
        currency = 'currency'
        custom_label_0 = 'custom_label_0'
        custom_label_1 = 'custom_label_1'
        custom_label_2 = 'custom_label_2'
        custom_label_3 = 'custom_label_3'
        custom_label_4 = 'custom_label_4'
        description = 'description'
        expiration_date = 'expiration_date'
        gtin = 'gtin'
        id = 'id'
        image_fetch_status = 'image_fetch_status'
        images = 'images'
        local_service_business_id = 'local_service_business_id'
        phone = 'phone'
        price = 'price'
        price_range = 'price_range'
        retailer_category = 'retailer_category'
        sanitized_images = 'sanitized_images'
        size = 'size'
        title = 'title'
        unit_price = 'unit_price'
        url = 'url'
        vendor_id = 'vendor_id'

    class Availability:
        available_for_order = 'AVAILABLE_FOR_ORDER'
        discontinued = 'DISCONTINUED'
        in_stock = 'IN_STOCK'
        out_of_stock = 'OUT_OF_STOCK'
        pending = 'PENDING'
        preorder = 'PREORDER'

    class Condition:
        pc_cpo = 'PC_CPO'
        pc_new = 'PC_NEW'
        pc_open_box_new = 'PC_OPEN_BOX_NEW'
        pc_refurbished = 'PC_REFURBISHED'
        pc_used = 'PC_USED'
        pc_used_fair = 'PC_USED_FAIR'
        pc_used_good = 'PC_USED_GOOD'
        pc_used_like_new = 'PC_USED_LIKE_NEW'

    class ImageFetchStatus:
        direct_upload = 'DIRECT_UPLOAD'
        fetched = 'FETCHED'
        fetch_failed = 'FETCH_FAILED'
        no_status = 'NO_STATUS'
        outdated = 'OUTDATED'
        partial_fetch = 'PARTIAL_FETCH'

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
            target_class=LocalServiceBusiness,
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

    def get_channels_to_integrity_status(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.catalogitemchannelstointegritystatus import CatalogItemChannelsToIntegrityStatus
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/channels_to_integrity_status',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CatalogItemChannelsToIntegrityStatus,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CatalogItemChannelsToIntegrityStatus, api=self._api),
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
        'address': 'Object',
        'applinks': 'CatalogItemAppLinks',
        'availability': 'Availability',
        'brand': 'string',
        'category': 'string',
        'category_specific_fields': 'CatalogSubVerticalList',
        'condition': 'Condition',
        'cuisine_type': 'string',
        'currency': 'string',
        'custom_label_0': 'string',
        'custom_label_1': 'string',
        'custom_label_2': 'string',
        'custom_label_3': 'string',
        'custom_label_4': 'string',
        'description': 'string',
        'expiration_date': 'string',
        'gtin': 'string',
        'id': 'string',
        'image_fetch_status': 'ImageFetchStatus',
        'images': 'list<string>',
        'local_service_business_id': 'string',
        'phone': 'string',
        'price': 'string',
        'price_range': 'string',
        'retailer_category': 'string',
        'sanitized_images': 'list<string>',
        'size': 'string',
        'title': 'string',
        'unit_price': 'Object',
        'url': 'string',
        'vendor_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Availability'] = LocalServiceBusiness.Availability.__dict__.values()
        field_enum_info['Condition'] = LocalServiceBusiness.Condition.__dict__.values()
        field_enum_info['ImageFetchStatus'] = LocalServiceBusiness.ImageFetchStatus.__dict__.values()
        return field_enum_info


