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

class Transaction(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isTransaction = True
        super(Transaction, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        app_amount = 'app_amount'
        billing_end_time = 'billing_end_time'
        billing_reason = 'billing_reason'
        billing_start_time = 'billing_start_time'
        charge_type = 'charge_type'
        checkout_campaign_group_id = 'checkout_campaign_group_id'
        credential_id = 'credential_id'
        fatura_id = 'fatura_id'
        id = 'id'
        is_business_ec_charge = 'is_business_ec_charge'
        is_funding_event = 'is_funding_event'
        payment_option = 'payment_option'
        product_type = 'product_type'
        provider_amount = 'provider_amount'
        status = 'status'
        time = 'time'
        tracking_id = 'tracking_id'
        transaction_type = 'transaction_type'
        tx_type = 'tx_type'

    class ProductType:
        facebook_ad = 'facebook_ad'
        ig_ad = 'ig_ad'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'transactions'

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
            target_class=Transaction,
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
        'account_id': 'string',
        'app_amount': 'Object',
        'billing_end_time': 'unsigned int',
        'billing_reason': 'string',
        'billing_start_time': 'unsigned int',
        'charge_type': 'string',
        'checkout_campaign_group_id': 'string',
        'credential_id': 'string',
        'fatura_id': 'unsigned int',
        'id': 'string',
        'is_business_ec_charge': 'bool',
        'is_funding_event': 'bool',
        'payment_option': 'string',
        'product_type': 'ProductType',
        'provider_amount': 'Object',
        'status': 'string',
        'time': 'unsigned int',
        'tracking_id': 'string',
        'transaction_type': 'string',
        'tx_type': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ProductType'] = Transaction.ProductType.__dict__.values()
        return field_enum_info


