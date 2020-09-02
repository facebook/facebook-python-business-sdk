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

class OracleTransaction(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isOracleTransaction = True
        super(OracleTransaction, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_account_ids = 'ad_account_ids'
        amount = 'amount'
        amount_due = 'amount_due'
        billed_amount_details = 'billed_amount_details'
        billing_period = 'billing_period'
        cdn_download_uri = 'cdn_download_uri'
        currency = 'currency'
        download_uri = 'download_uri'
        due_date = 'due_date'
        entity = 'entity'
        id = 'id'
        invoice_date = 'invoice_date'
        invoice_id = 'invoice_id'
        invoice_type = 'invoice_type'
        liability_type = 'liability_type'
        payment_status = 'payment_status'
        payment_term = 'payment_term'
        type = 'type'

    class Type:
        cm = 'CM'
        inv = 'INV'

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
            target_class=OracleTransaction,
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

    def get_campaigns(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.invoicecampaign import InvoiceCampaign
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/campaigns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InvoiceCampaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InvoiceCampaign, api=self._api),
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
        'ad_account_ids': 'list<string>',
        'amount': 'string',
        'amount_due': 'CurrencyAmount',
        'billed_amount_details': 'BilledAmountDetails',
        'billing_period': 'string',
        'cdn_download_uri': 'string',
        'currency': 'string',
        'download_uri': 'string',
        'due_date': 'datetime',
        'entity': 'string',
        'id': 'string',
        'invoice_date': 'datetime',
        'invoice_id': 'string',
        'invoice_type': 'string',
        'liability_type': 'string',
        'payment_status': 'string',
        'payment_term': 'string',
        'type': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Type'] = OracleTransaction.Type.__dict__.values()
        return field_enum_info


