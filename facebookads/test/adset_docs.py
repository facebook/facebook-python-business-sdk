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
    python -m facebookads.test.adset_docs
'''

import os
import sys
import json
from .docs_utils import *


class AdSetDocsTestCase(DocsTestCase):
    def setUp(self):
        campaign = self.create_campaign(1)
        adset = self.create_adset(1, campaign)
        creative1 = self.create_creative(1)
        creative2 = self.create_creative(2)
        self.create_ad(1, adset, creative1)
        self.create_ad(2, adset, creative2)
        DocsDataStore.set('adcampaign_id', campaign.get_id())
        DocsDataStore.set('adset_id', adset.get_id())

    def test_get_insights(self):
        adset = AdSet(DocsDataStore.get('adset_id'))
        insights = adset.get_insights(fields=[
            Insights.Field.ad_id,
            Insights.Field.unique_clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.ad,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)

    def test_get_ads(self):
        adset = AdSet(DocsDataStore.get('adset_id'))
        adgroups = adset.get_ads(fields=[
            AdSet.Field.name,
            AdSet.Field.campaign_id,
            AdSet.Field.configured_status,
        ])
        self.store_response(adgroups)

    def test_get_ad_creatives(self):
        adset = AdSet(DocsDataStore.get('adset_id'))
        adcreatives = adset.get_ad_creatives(fields=[
            AdCreative.Field.name,
            AdCreative.Field.id,
            AdCreative.Field.preview_url,
            AdCreative.Field.call_to_action_type,
        ])
        self.store_response(adcreatives)


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

    unittest.main()
