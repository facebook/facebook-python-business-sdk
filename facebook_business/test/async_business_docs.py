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
    python -m facebookads.test.async_business_docs
'''

import sys

from facebookads.utils.httpretries import retry_policy
from facebookads.test.async_docs_utils import *


class BusinessDocsTestCase(AsyncDocsTestCase):
    def test_get_product_catalogs(self):
        business = Business(AsyncDocsDataStore.get('business_id'))
        catalogs = [x for x in business.get_product_catalogs_aio()]
        self.assertGreater(len(catalogs), 1)
        if catalogs:
            self.store_response(catalogs[0])

    def test_get_ad_accounts(self):
        business = Business(AsyncDocsDataStore.get('business_id'))
        accounts = business.get_ad_accounts_aio()
        accounts = [x for x in accounts]
        self.assertGreaterEqual(len(accounts), 1)
        self.store_response(accounts)

    def test_get_insights(self):
        business = Business(AsyncDocsDataStore.get('business_id'))
        insights = business.get_insights_aio(fields=[
            Insights.Field.campaign_id,
            Insights.Field.unique_clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.campaign,
            'date_preset': Insights.Preset.last_week,
        })
        results = [x for x in insights]
        self.store_response(results)


if __name__ == '__main__':
    handle = open(AsyncDocsDataStore.get('filename'), 'w')
    handle.write('')
    handle.close()

    try:
        config_file = open('./autogen_docs_config.json')
    except IOError:
        print("No config file found, skipping docs tests")
        sys.exit()
    config = json.load(config_file)
    config_file.close()

    FacebookAdsAsyncApi.init(
        config['app_id'],
        config['app_secret'],
        config['access_token'],
        config['adaccount_id'],
        pool_maxsize=10,
        max_retries=retry_policy()
    )

    AsyncDocsDataStore.set('adaccount_id', config['adaccount_id'])
    AsyncDocsDataStore.set('adaccount_id_int', config['adaccount_id_int'])
    AsyncDocsDataStore.set('business_id', config['business_id'])
    AsyncDocsDataStore.set('ca_id', config['ca_id'])
    AsyncDocsDataStore.set('dpa_catalog_id', config['dpa_catalog_id'])
    AsyncDocsDataStore.set('dpa_set_id', config['dpa_set_id'])
    AsyncDocsDataStore.set('dpa_feed_id', config['dpa_feed_id'])
    AsyncDocsDataStore.set('dpa_upload_id', config['dpa_upload_id'])
    AsyncDocsDataStore.set('as_user_id', config['as_user_id'])
    AsyncDocsDataStore.set('page_id', config['page_id'])
    AsyncDocsDataStore.set('pixel_id', config['pixel_id'])

    unittest.main()
