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
    python -m facebookads.test.adaccount_docs
'''

import os
import sys
import json
from .docs_utils import *


class AdAccountDocsTestCase(DocsTestCase):
    def setUp(self):
        # Create Campaigns
        campaign = self.create_campaign(1)
        self.create_campaign(2)
        # Create AdSets
        adset = self.create_adset(1, campaign)
        self.create_adset(2, campaign)
        # Create Creatives
        creative1 = self.create_creative(1)
        creative2 = self.create_creative(2)
        # Create AdGroups
        ad = self.create_ad(1, adset, creative1)
        self.create_ad(2, adset, creative2)
        DocsDataStore.set('ad_id', ad.get_id())
        # Create Ad Labels
        adlabel = self.create_adlabel()
        DocsDataStore.set('adlabel_id', adlabel['id'])
        # Create AdImage
        image = self.create_image()
        DocsDataStore.set('ad_account_image_hash', image['hash'])


    def test_get_insights(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        insights = account.get_insights(fields=[
            Insights.Field.campaign_id,
            Insights.Field.unique_clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.campaign,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)

    def test_get_activities(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        activities = account.get_activities(fields=[
            Activity.Field.event_type,
            Activity.Field.event_time,
        ])
        self.store_response(activities[0])

    def test_get_my_account(self):
        account = AdAccount.get_my_account()
        self.store_response(account)

    def test_opt_out_user_from_targeting(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        response = account.opt_out_user_from_targeting(
            schema=CustomAudience.Schema.email_hash,
            users=['joe@example.com'],
        )
        self.store_response(response)

    def test_get_campaigns(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        campaigns = account.get_campaigns(fields=[
            Campaign.Field.name,
            Campaign.Field.configured_status,
        ])
        self.store_response(campaigns)

    def test_get_ad_sets(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adsets = account.get_ad_sets(fields=[
            AdSet.Field.name,
            AdSet.Field.bid_info,
            AdSet.Field.configured_status,
            AdSet.Field.daily_budget,
            AdSet.Field.targeting,
        ])
        self.store_response(adsets)

    def test_get_ads(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        ads = account.get_ads(fields=[
            Ad.Field.name,
            Ad.Field.configured_status,
            Ad.Field.creative,
        ])
        self.store_response(ads)

    def test_get_ad_users(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        users = account.get_ad_users()
        self.store_response(users)

    def test_get_ad_creatives(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        creatives = account.get_ad_creatives(fields=[
            AdCreative.Field.name,
            AdCreative.Field.image_hash,
        ])
        self.store_response(creatives[0:2])

    def test_get_ad_images(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        images = account.get_ad_images(fields=[
            AdImage.Field.hash,
        ])
        self.store_response(images)

    def test_get_ad_conversion_pixels(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        pixels = account.get_ad_conversion_pixels(fields=[
            AdImage.Field.hash,
        ])
        self.store_response(pixels)

    def test_get_broad_category_targeting(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        bct = account.get_broad_category_targeting()
        self.store_response(bct[0:2])

    def test_get_connection_objects(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        connection_objects = account.get_connection_objects()
        connection_objects = [
            co for co in connection_objects if co['id'] == '606699326111137']
        self.store_response(connection_objects)

    def test_get_custom_audiences(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        custom_audiences = account.get_custom_audiences()
        self.store_response(custom_audiences)

    def test_get_partner_categories(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        partner_categories = account.get_partner_categories()
        self.store_response(partner_categories[0])

    def test_get_rate_cards(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        rate_cards = account.get_rate_cards()
        self.store_response(rate_cards[0:2])

    def test_get_reach_estimate(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        reach_estimate = account.get_reach_estimate(params={
            'currency': 'USD',
            'optimize_for': 'OFFSITE_CONVERSIONS',
            'targeting_spec': {
                'geo_locations': {
                    'countries': ['US'],
                }
            }
        })
        self.store_response(reach_estimate)

    def test_get_transactions(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        transactions = account.get_transactions()
        self.store_response(transactions)

    def test_get_ad_preview(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        ad_preview = account.get_ad_preview(params={
            'creative': {
                'title': 'This is the title',
                'body': 'This is the body',
                'object_url': 'https://facebookmarketingpartners.com',
                'image_hash': DocsDataStore.get('ad_account_image_hash'),
            },
            'ad_format': 'RIGHT_COLUMN_STANDARD',
        })
        self.store_response(ad_preview)

    def test_get_ads_pixel(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        pixels = account.get_ads_pixels(fields=[
            AdsPixel.Field.name,
            AdsPixel.Field.id,
        ])
        self.store_response(pixels)

    def test_get_targeting_description(self):
        adgroup = Ad(DocsDataStore.get('ad_id'))
        targeting = {
            TargetingSpecsField.geo_locations: {
                TargetingSpecsField.countries: ['US'],
            },
        }
        targeting_desc = adgroup.get_targeting_description(fields=[
            'targetingsentencelines'
        ], params={
            'targeting_spec': targeting
        })
        self.store_response(targeting_desc)

    def test_get_ad_labels(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adlabels = account.get_ad_labels(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ])
        self.store_response(adlabels)

    def test_get_ad_creatives_by_labels(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adlabel_id = DocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        adcreatives = account.get_ad_creatives_by_labels(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(adcreatives)

    def test_get_ads_by_labels(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adlabel_id = DocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        ads = account.get_ads_by_labels(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(ads)

    def test_get_adsets_by_labels(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adlabel_id = DocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        adsets = account.get_adsets_by_labels(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(adsets)

    def test_get_campaigns_by_labels(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adlabel_id = DocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        campaigns = account.get_campaigns_by_labels(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(campaigns)

    def test_get_minimum_budgets(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        min_budgets = account.get_minimum_budgets()
        self.store_response(min_budgets)

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
