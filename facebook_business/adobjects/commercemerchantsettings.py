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

class CommerceMerchantSettings(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCommerceMerchantSettings = True
        super(CommerceMerchantSettings, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        braintree_merchant_id = 'braintree_merchant_id'
        checkout_message = 'checkout_message'
        contact_email = 'contact_email'
        disable_checkout_urls = 'disable_checkout_urls'
        has_discount_code = 'has_discount_code'
        id = 'id'
        merchant_alert_email = 'merchant_alert_email'
        merchant_page = 'merchant_page'
        merchant_status = 'merchant_status'
        payment_provider = 'payment_provider'
        privacy_url_by_locale = 'privacy_url_by_locale'
        review_rejection_messages = 'review_rejection_messages'
        review_rejection_reasons = 'review_rejection_reasons'
        review_status = 'review_status'
        supported_card_types = 'supported_card_types'
        terms = 'terms'
        terms_url_by_locale = 'terms_url_by_locale'

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
            target_class=CommerceMerchantSettings,
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

    def get_product_catalogs(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_catalogs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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
        'braintree_merchant_id': 'string',
        'checkout_message': 'string',
        'contact_email': 'string',
        'disable_checkout_urls': 'bool',
        'has_discount_code': 'bool',
        'id': 'string',
        'merchant_alert_email': 'string',
        'merchant_page': 'Profile',
        'merchant_status': 'string',
        'payment_provider': 'string',
        'privacy_url_by_locale': 'list<Object>',
        'review_rejection_messages': 'list<string>',
        'review_rejection_reasons': 'list<string>',
        'review_status': 'string',
        'supported_card_types': 'list<string>',
        'terms': 'string',
        'terms_url_by_locale': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


