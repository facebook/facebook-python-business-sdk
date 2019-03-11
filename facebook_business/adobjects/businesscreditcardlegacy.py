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

class BusinessCreditCardLegacy(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusinessCreditCardLegacy = True
        super(BusinessCreditCardLegacy, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        business_id = 'business_id'
        credit_card_suffix = 'credit_card_suffix'
        credit_card_type = 'credit_card_type'
        expiration_month = 'expiration_month'
        expiration_year = 'expiration_year'
        first_name = 'first_name'
        fraud_status = 'fraud_status'
        id = 'id'
        last_name = 'last_name'
        middle_name = 'middle_name'

    _field_types = {
        'address': 'Object',
        'business_id': 'string',
        'credit_card_suffix': 'string',
        'credit_card_type': 'string',
        'expiration_month': 'int',
        'expiration_year': 'int',
        'first_name': 'string',
        'fraud_status': 'string',
        'id': 'string',
        'last_name': 'string',
        'middle_name': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


