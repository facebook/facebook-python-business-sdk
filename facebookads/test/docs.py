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
    python -m facebookads.test.docs
'''

import sys
import json
from .docs_utils import *


class AdGroupDocsTestCase(DocsTestCase):
    def setUp(self):
        campaign = self.create_campaign(1)
        adset = self.create_adset(1, campaign)
        creative = self.create_creative(1)
        adgroup = self.create_adgroup(1, adset, creative)
        DocsDataStore.set('adgroup_id', adgroup.get_id())

    def test_get_ad_creatives(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        creatives = adgroup.get_ad_creatives(fields=[AdCreative.Field.name])
        self.store_response(creatives)

    def test_get_targeting_description(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        targeting_desc = adgroup.get_targeting_description(fields=[
            'targetingsentencelines',
        ])
        self.store_response(targeting_desc)

    def test_get_keyword_stats(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        keywords = adgroup.get_keyword_stats()
        self.store_response(keywords)

    def test_get_ad_preview(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        fields = ['body']
        params = {'ad_format': 'DESKTOP_FEED_STANDARD'}
        adgroup_preview = adgroup.get_ad_preview(fields=fields, params=params)
        self.store_response(adgroup_preview)


class AdSetDocsTestCase(DocsTestCase):
    def setUp(self):
        campaign = self.create_campaign(1)
        adset = self.create_adset(1, campaign)
        creative1 = self.create_creative(1)
        creative2 = self.create_creative(2)
        self.create_adgroup(1, adset, creative1)
        self.create_adgroup(2, adset, creative2)
        DocsDataStore.set('adcampaign_id', campaign.get_id())
        DocsDataStore.set('adset_id', adset.get_id())

    def test_get_ad_groups(self):
        adset = AdSet(DocsDataStore.get('adset_id'))
        adgroups = adset.get_ad_groups(fields=[
            AdGroup.Field.name,
            AdGroup.Field.campaign_id,
            AdGroup.Field.creative,
            AdGroup.Field.status,
        ])
        self.store_response(adgroups)


class AdAccountDocsTestCase(DocsTestCase):
    def setUp(self):
        campaign = self.create_campaign(1)
        self.create_adset(1, campaign)
        self.create_adset(2, campaign)

    def test_get_ad_campaigns(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        campaigns = account.get_ad_campaigns(fields=[
            AdCampaign.Field.name,
            AdCampaign.Field.status,
        ])
        self.store_response(campaigns)

    def test_get_ad_sets(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adsets = account.get_ad_sets(fields=[
            AdSet.Field.name,
            AdSet.Field.bid_type,
            AdSet.Field.bid_info,
            AdSet.Field.status,
            AdSet.Field.daily_budget,
            AdSet.Field.targeting,
        ])
        self.store_response(adsets)


class AdCampaignDocsTestCase(DocsTestCase):
    pass


if __name__ == '__main__':
    handle = open(DocsDataStore.get('filename'), 'w')
    handle.write('')
    handle.close()

    try:
        config_file = open('./config.json')
    except IOError:
        print("No config file found, skipping docs tests")
        sys.exit()
    config = json.load(config_file)
    config_file.close()

    act_id = "act_1505766289694659"
    FacebookAdsApi.init(
        config['app_id'],
        config['app_secret'],
        config['access_token'],
        act_id
    )
    DocsDataStore.set('adaccount_id', act_id)

    unittest.main()
