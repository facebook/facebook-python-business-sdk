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

'''
Unit tests for the Python Facebook Ads API SDK.

How to run:
    python -m facebookads.test.adspixel_docs
'''

import os
import sys
import json
from .docs_utils import *


class AdCreativeDocsTestCase(DocsTestCase):

    def setUp(self):
        pixel = self.create_ads_pixel()
        DocsDataStore.set('pixel_id', pixel.get_id())

    def test_list_ad_accounts(self):
        business_id = DocsDataStore.get('business_id')
        pixel_id = DocsDataStore.get('pixel_id')
        pixel = AdsPixel(pixel_id)
        shared_accounts = pixel.list_ad_accounts(business_id)
        self.store_response(shared_accounts)

    def test_share_pixel(self):
        business_id = DocsDataStore.get('business_id')
        act_id = DocsDataStore.get('adaccount_id')
        destination_account_id = act_id.replace("act_", "")
        pixel_id = DocsDataStore.get('pixel_id')
        pixel = AdsPixel(pixel_id)
        pixel.share_pixel(business_id, destination_account_id)
        self.store_response(pixel)

    def test_share_pixel_agencies(self):
        business_id = DocsDataStore.get('business_id')
        agency_id = DocsDataStore.get('secondary_business_id')
        pixel_id = DocsDataStore.get('pixel_id')
        pixel = AdsPixel(pixel_id)
        pixel.share_pixel_agencies(business_id, agency_id)
        self.store_response(pixel)

    def test_list_shared_agencies(self):
        pixel_id = DocsDataStore.get('pixel_id')
        pixel = AdsPixel(pixel_id)
        shared_agencies = pixel.list_shared_agencies()
        self.store_response(shared_agencies)

    def test_unshare_pixel(self):
        business_id = DocsDataStore.get('business_id')
        account_id = DocsDataStore.get('adaccount_id').replace("act_", "")
        pixel_id = DocsDataStore.get('pixel_id')
        pixel = AdsPixel(pixel_id)
        pixel.unshare_pixel(business_id, account_id)
        self.store_response(pixel)

    def test_unshare_pixel_agencies(self):
        business_id = DocsDataStore.get('business_id')
        agency_id = DocsDataStore.get('secondary_business_id')
        pixel_id = DocsDataStore.get('pixel_id')
        pixel = AdsPixel(pixel_id)
        pixel.unshare_pixel_agencies(business_id, agency_id)
        self.store_response(pixel)


if __name__ == '__main__':
    handle = open(DocsDataStore.get('filename'), 'w')
    handle.write('')
    handle.close()
    try:
        config_file = open('./autogen_docs_config.json')
    except IOError:
        print("No config file found, skipping docs tests")
        sys.exit()
    config = json.load(config_file)
    config_file.close()

    FacebookAdsApi.init(
        config['app_id'],
        config['app_secret'],
        config['access_token'],
        config['adaccount_id'],
    )

    DocsDataStore.set('adaccount_id', config['adaccount_id'])
    DocsDataStore.set('adaccount_id_int', config['adaccount_id_int'])
    DocsDataStore.set('business_id', config['business_id'])
    DocsDataStore.set('ca_id', config['ca_id'])
    DocsDataStore.set('dpa_catalog_id', config['dpa_catalog_id'])
    DocsDataStore.set('dpa_set_id', config['dpa_set_id'])
    DocsDataStore.set('dpa_feed_id', config['dpa_feed_id'])
    DocsDataStore.set('dpa_upload_id', config['dpa_upload_id'])
    DocsDataStore.set('as_user_id', config['as_user_id'])
    DocsDataStore.set('page_id', config['page_id'])
    DocsDataStore.set('pixel_id', config['pixel_id'])
    DocsDataStore.set('secondary_business_id', config['sec_business'])

    unittest.main()
