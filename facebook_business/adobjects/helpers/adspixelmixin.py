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

from facebook_business.adobjects.business import Business
from facebook_business.adobjects.adaccount import AdAccount

class AdsPixelMixin:

    def share_pixel_with_ad_account(self, business_id, account_id):
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'shared_accounts'),
            params={
                'business': business_id,
                'account_id': account_id,
            },
        )

    def share_pixel_with_agency(self, business_id, agency_id):
        """Associate ads pixel with another business"""
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'shared_agencies'),
            params={
                'business': business_id,
                'agency_id': agency_id,
            },
        )

    def unshare_pixel_from_ad_account(self, business_id, account_id):
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'shared_accounts'),
            params={
                'business': business_id,
                'account_id': account_id,
            },
        )

    def unshare_pixel_from_agency(self, business_id, agency_id):
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'shared_agencies'),
            params={
                'business': business_id,
                'agency_id': agency_id,
            },
        )

    def get_agencies(self):
        """Returns a list of businesses associated with the ads pixel"""
        response = self.get_api_assured().call(
            'GET',
            (self.get_id_assured(), 'shared_agencies'),
        ).json()

        ret_val = []
        if response:
            keys = response['data']
            for item in keys:
                search_obj = Business()
                search_obj.update(item)
                ret_val.append(search_obj)
        return ret_val

    def get_ad_accounts(self, business_id):
        """Returns list of adaccounts associated with the ads pixel"""
        response = self.get_api_assured().call(
            'GET',
            (self.get_id_assured(), 'shared_accounts'),
            params={'business': business_id},
        ).json()

        ret_val = []
        if response:
            keys = response['data']
            for item in keys:
                search_obj = AdAccount()
                search_obj.update(item)
                ret_val.append(search_obj)
        return ret_val
