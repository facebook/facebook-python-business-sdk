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
    python -m facebookads.test.async_ad_docs
'''

import sys

from facebookads.utils.httpretries import retry_policy
from facebookads.test.async_docs_utils import *


class AdDocsTestCase(AsyncDocsTestCase):
    def setUp(self):
        campaign = self.create_campaign(1)
        adset = self.create_adset(1, campaign)
        creative = self.create_creative_leads(1)
        ad = self.create_ad(1, adset, creative)
        AsyncDocsDataStore.set('ad_id', ad.get_id())

    def test_get_insights(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        insights = ad.get_insights(fields=[
            Insights.Field.ad_id,
            Insights.Field.unique_clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.ad,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)

    def test_get_ad_creatives(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        creatives = ad.get_ad_creatives_aio(fields=[AdCreative.Field.name])
        self.store_response(creatives)

    def test_get_targeting_description(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        targeting_desc = ad.get_targeting_description_aio(fields=[
            'targetingsentencelines',
        ])
        self.store_response(targeting_desc)

    def test_get_keyword_stats(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        keywords = ad.get_keyword_stats_aio()
        self.store_response(keywords)

    def test_get_ad_preview(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        ad_preview = ad.get_ad_preview_aio(params={
            'ad_format': 'RIGHT_COLUMN_STANDARD',
        })
        self.store_response(ad_preview)

    def test_get_reach_estimate(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        reach_estimate = ad.get_reach_estimate_aio()
        self.store_response(reach_estimate)

    def test_get_click_tracking_tag(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        tag = ad.get_click_tracking_tag_aio()
        self.store_response(tag)

    def test_get_leads(self):
        ad = Ad(AsyncDocsDataStore.get('ad_id'))
        leads = ad.get_leads_aio()
        self.store_response(leads)


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
