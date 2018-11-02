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

class MerchantReport(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isMerchantReport = True
        super(MerchantReport, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        add_to_cart = 'add_to_cart'
        brand = 'brand'
        catalog_segment = 'catalog_segment'
        catalog_segment_id = 'catalog_segment_id'
        catalog_segment_purchase_value = 'catalog_segment_purchase_value'
        category = 'category'
        date = 'date'
        link_clicks = 'link_clicks'
        merchant_currency = 'merchant_currency'
        page = 'page'
        page_id = 'page_id'
        product_id = 'product_id'
        product_quantity = 'product_quantity'
        product_total_value = 'product_total_value'
        purchase = 'purchase'
        purchase_value = 'purchase_value'
        id = 'id'

    _field_types = {
        'add_to_cart': 'int',
        'brand': 'string',
        'catalog_segment': 'ProductCatalog',
        'catalog_segment_id': 'string',
        'catalog_segment_purchase_value': 'float',
        'category': 'string',
        'date': 'string',
        'link_clicks': 'int',
        'merchant_currency': 'string',
        'page': 'Page',
        'page_id': 'string',
        'product_id': 'string',
        'product_quantity': 'int',
        'product_total_value': 'float',
        'purchase': 'int',
        'purchase_value': 'float',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


