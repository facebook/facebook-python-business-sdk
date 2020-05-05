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

class VehicleOffer(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isVehicleOffer = True
        super(VehicleOffer, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        amount_currency = 'amount_currency'
        amount_percentage = 'amount_percentage'
        amount_price = 'amount_price'
        amount_qualifier = 'amount_qualifier'
        applinks = 'applinks'
        body_style = 'body_style'
        cashback_currency = 'cashback_currency'
        cashback_price = 'cashback_price'
        currency = 'currency'
        dma_codes = 'dma_codes'
        downpayment_currency = 'downpayment_currency'
        downpayment_price = 'downpayment_price'
        downpayment_qualifier = 'downpayment_qualifier'
        end_date = 'end_date'
        end_time = 'end_time'
        id = 'id'
        images = 'images'
        make = 'make'
        model = 'model'
        offer_description = 'offer_description'
        offer_disclaimer = 'offer_disclaimer'
        offer_type = 'offer_type'
        price = 'price'
        sanitized_images = 'sanitized_images'
        start_date = 'start_date'
        start_time = 'start_time'
        term_length = 'term_length'
        term_qualifier = 'term_qualifier'
        title = 'title'
        trim = 'trim'
        url = 'url'
        vehicle_offer_id = 'vehicle_offer_id'
        year = 'year'

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
            target_class=VehicleOffer,
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

    _field_types = {
        'amount_currency': 'string',
        'amount_percentage': 'float',
        'amount_price': 'string',
        'amount_qualifier': 'string',
        'applinks': 'CatalogItemAppLinks',
        'body_style': 'string',
        'cashback_currency': 'string',
        'cashback_price': 'string',
        'currency': 'string',
        'dma_codes': 'list<string>',
        'downpayment_currency': 'string',
        'downpayment_price': 'string',
        'downpayment_qualifier': 'string',
        'end_date': 'string',
        'end_time': 'int',
        'id': 'string',
        'images': 'list<string>',
        'make': 'string',
        'model': 'string',
        'offer_description': 'string',
        'offer_disclaimer': 'string',
        'offer_type': 'string',
        'price': 'string',
        'sanitized_images': 'list<string>',
        'start_date': 'string',
        'start_time': 'int',
        'term_length': 'unsigned int',
        'term_qualifier': 'string',
        'title': 'string',
        'trim': 'string',
        'url': 'string',
        'vehicle_offer_id': 'string',
        'year': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


