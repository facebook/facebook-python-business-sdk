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

class UserPaymentMethodsInfo(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isUserPaymentMethodsInfo = True
        super(UserPaymentMethodsInfo, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        available_card_types = 'available_card_types'
        available_payment_methods = 'available_payment_methods'
        available_payment_methods_details = 'available_payment_methods_details'
        country = 'country'
        currency = 'currency'
        existing_payment_methods = 'existing_payment_methods'
        id = 'id'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'unsigned int',
            'country_code': 'string',
            'extra_data': 'string',
            'nmor_order_type': 'nmor_order_type_enum',
            'payment_type': 'payment_type_enum',
        }
        enums = {
            'nmor_order_type_enum': [
                'unknown',
                'none',
                'pages_commerce',
                'nmor_pages_commerce',
                'component_flow',
                'business_platform_commerce',
                'synchronous_component_flow',
                'event_ticketing',
                'platform_self_serve',
                'messenger_platform',
                'messenger_omnim',
                'billing_engine',
                'tip_jar',
                'instant_experiences',
                'checkout_experiences',
                'buy_on_facebook',
                'payment_app',
                'donation_p4p',
                'whatsapp_p2p',
                'p2p',
                'mobile_top_up',
                'shipping_label',
                'marketplace_dropoff',
                'pages_solution',
                'blackbaud_rwr_donation',
                'instagram_p2b',
                'marketplace_shipping',
                'facebook_incentive_seller',
                'facebook_incentive_buyer',
                'dummy',
                'ppgf_donation',
                'advertiser_subscription',
                'whatsapp_p2m',
                'movie_ticketing',
            ],
            'payment_type_enum': [
                'none',
                'ads_invoice',
                'donations',
                'donations_matching_confirmation',
                'donations_matching_pledge',
                'facebook_shop',
                'fan_funding',
                'group_subscription',
                'game_tipping_token',
                'instant_games',
                'oculus_cv1',
                'oculus_launch_v1',
                'oculus_launch_v2',
                'ozone',
                'open_graph_product',
                'messenger_commerce',
                'p2p_transfer',
                'dummy_first_party',
                'dummy_third_party',
                'gifts',
                'bill',
                'airmail',
                'event_ticketing',
                'payment_lite',
                'messenger_api_fee',
                'workplace',
                'nmor_pages_commerce',
                'stored_balance',
                'third_party_bundle',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UserPaymentMethodsInfo,
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
        'available_card_types': 'list<string>',
        'available_payment_methods': 'list<string>',
        'available_payment_methods_details': 'list<Object>',
        'country': 'string',
        'currency': 'string',
        'existing_payment_methods': 'list<Object>',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


