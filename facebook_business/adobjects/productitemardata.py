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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ProductItemARData(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductItemARData, self).__init__()
        self._isProductItemARData = True
        self._api = api

    class Field(AbstractObject.Field):
        container_effect = 'container_effect'
        effect_icon = 'effect_icon'
        effect_parameters = 'effect_parameters'
        picker_icon = 'picker_icon'
        product_ar_link = 'product_ar_link'
        state = 'state'
        surfaces = 'surfaces'

    class Surfaces:
        b2c_marketplace = 'B2C_MARKETPLACE'
        c2c_marketplace = 'C2C_MARKETPLACE'
        da = 'DA'
        daily_deals = 'DAILY_DEALS'
        daily_deals_legacy = 'DAILY_DEALS_LEGACY'
        ig_product_tagging = 'IG_PRODUCT_TAGGING'
        marketplace = 'MARKETPLACE'
        marketplace_ads_deprecated = 'MARKETPLACE_ADS_DEPRECATED'
        marketplace_shops = 'MARKETPLACE_SHOPS'
        offline_conversions = 'OFFLINE_CONVERSIONS'
        shops = 'SHOPS'
        universal_checkout = 'UNIVERSAL_CHECKOUT'
        whatsapp = 'WHATSAPP'

    _field_types = {
        'container_effect': 'string',
        'effect_icon': 'string',
        'effect_parameters': 'Object',
        'picker_icon': 'string',
        'product_ar_link': 'Object',
        'state': 'string',
        'surfaces': 'list<Surfaces>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Surfaces'] = ProductItemARData.Surfaces.__dict__.values()
        return field_enum_info


