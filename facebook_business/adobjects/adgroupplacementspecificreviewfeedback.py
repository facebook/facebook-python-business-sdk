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

class AdgroupPlacementSpecificReviewFeedback(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdgroupPlacementSpecificReviewFeedback, self).__init__()
        self._isAdgroupPlacementSpecificReviewFeedback = True
        self._api = api

    class Field(AbstractObject.Field):
        account_admin = 'account_admin'
        ad = 'ad'
        ads_conversion_experiences = 'ads_conversion_experiences'
        b2c = 'b2c'
        b2c_commerce_unified = 'b2c_commerce_unified'
        bsg = 'bsg'
        city_community = 'city_community'
        commerce = 'commerce'
        daily_deals = 'daily_deals'
        daily_deals_legacy = 'daily_deals_legacy'
        dpa = 'dpa'
        dri_copyright = 'dri_copyright'
        dri_counterfeit = 'dri_counterfeit'
        facebook = 'facebook'
        facebook_pages_live_shopping = 'facebook_pages_live_shopping'
        instagram = 'instagram'
        instagram_shop = 'instagram_shop'
        lead_gen_honeypot = 'lead_gen_honeypot'
        marketplace = 'marketplace'
        marketplace_home_rentals = 'marketplace_home_rentals'
        marketplace_home_sales = 'marketplace_home_sales'
        marketplace_motors = 'marketplace_motors'
        marketplace_shops = 'marketplace_shops'
        max_review_placements = 'max_review_placements'
        page_admin = 'page_admin'
        product = 'product'
        product_service = 'product_service'
        profile = 'profile'
        seller = 'seller'
        shops = 'shops'
        traffic_quality = 'traffic_quality'
        whatsapp = 'whatsapp'

    _field_types = {
        'account_admin': 'map<string, string>',
        'ad': 'map<string, string>',
        'ads_conversion_experiences': 'map<string, string>',
        'b2c': 'map<string, string>',
        'b2c_commerce_unified': 'map<string, string>',
        'bsg': 'map<string, string>',
        'city_community': 'map<string, string>',
        'commerce': 'map<string, string>',
        'daily_deals': 'map<string, string>',
        'daily_deals_legacy': 'map<string, string>',
        'dpa': 'map<string, string>',
        'dri_copyright': 'map<string, string>',
        'dri_counterfeit': 'map<string, string>',
        'facebook': 'map<string, string>',
        'facebook_pages_live_shopping': 'map<string, string>',
        'instagram': 'map<string, string>',
        'instagram_shop': 'map<string, string>',
        'lead_gen_honeypot': 'map<string, string>',
        'marketplace': 'map<string, string>',
        'marketplace_home_rentals': 'map<string, string>',
        'marketplace_home_sales': 'map<string, string>',
        'marketplace_motors': 'map<string, string>',
        'marketplace_shops': 'map<string, string>',
        'max_review_placements': 'map<string, string>',
        'page_admin': 'map<string, string>',
        'product': 'map<string, string>',
        'product_service': 'map<string, string>',
        'profile': 'map<string, string>',
        'seller': 'map<string, string>',
        'shops': 'map<string, string>',
        'traffic_quality': 'map<string, string>',
        'whatsapp': 'map<string, string>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


