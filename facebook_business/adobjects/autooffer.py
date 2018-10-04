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

class AutoOffer(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAutoOffer = True
        super(AutoOffer, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        amount_currency = 'amount_currency'
        amount_percentage = 'amount_percentage'
        amount_price = 'amount_price'
        amount_qualifier = 'amount_qualifier'
        applinks = 'applinks'
        auto_offer_id = 'auto_offer_id'
        downpayment_currency = 'downpayment_currency'
        downpayment_price = 'downpayment_price'
        downpayment_qualifier = 'downpayment_qualifier'
        id = 'id'
        images = 'images'
        offer_description = 'offer_description'
        offer_disclaimer = 'offer_disclaimer'
        offer_type = 'offer_type'
        sanitized_images = 'sanitized_images'
        term_length = 'term_length'
        term_qualifier = 'term_qualifier'
        url = 'url'

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
            target_class=AutoOffer,
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
        'amount_currency': 'string',
        'amount_percentage': 'float',
        'amount_price': 'string',
        'amount_qualifier': 'string',
        'applinks': 'AppLinks',
        'auto_offer_id': 'string',
        'downpayment_currency': 'string',
        'downpayment_price': 'string',
        'downpayment_qualifier': 'string',
        'id': 'string',
        'images': 'list<string>',
        'offer_description': 'string',
        'offer_disclaimer': 'string',
        'offer_type': 'string',
        'sanitized_images': 'list<string>',
        'term_length': 'Object',
        'term_qualifier': 'string',
        'url': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


