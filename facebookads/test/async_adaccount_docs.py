'''
Unit tests for the Python Facebook Ads API SDK.

How to run:
    python -m facebookads.test.async_adaccount_docs
'''

import sys

from facebookads.utils.httpretries import retry_policy
from facebookads.test.async_docs_utils import *


class AdAccountAsyncDocsTestCase(AsyncDocsTestCase):
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
        AsyncDocsDataStore.set('ad_id', ad.get_id())
        # Create Ad Labels
        adlabel = self.create_adlabel()
        AsyncDocsDataStore.set('adlabel_id', adlabel['id'])
        # Create AdImage
        image = self.create_image()
        AsyncDocsDataStore.set('ad_account_image_hash', image['hash'])

    def test_get_insights_async(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        job = account.get_insights_aio(fields=[
            Insights.Field.campaign_id,
            Insights.Field.unique_clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.campaign,
            'date_preset': Insights.Preset.last_week,
        }, async=True)
        while not job:
            time.sleep(0.3)
            job.remote_read()
        insights = job.get_result()
        results = [x for x in insights]
        self.store_response(results)

    def test_get_insights_aio(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        insights = account.get_insights_aio(fields=[
            Insights.Field.campaign_id,
            Insights.Field.unique_clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.campaign,
            'date_preset': Insights.Preset.last_week,
        })
        results = [x for x in insights]
        self.store_response(results)

    def test_get_insights_old(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        insights = account.get_insights(fields=[
            Insights.Field.campaign_id,
            Insights.Field.unique_clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.campaign,
            'date_preset': Insights.Preset.last_week,
        })
        results = [x for x in insights]
        self.store_response(results)

    def test_get_activities(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        activities = account.get_activities_aio(fields=[
            baseobjects.Activity.Field.event_type,
            baseobjects.Activity.Field.event_time,
        ], limit=1000)
        self.store_response(activities[0])
        self.assertEqual(len(activities), 10)
        activities.load_next_page()
        self.assertEqual(len(activities), 20)

    def test_get_my_account(self):
        account = AdAccount.get_my_account()
        self.store_response(account)

    def test_opt_out_user_from_targeting(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        response = account.opt_out_user_from_targeting(
            schema=CustomAudience.Schema.email_hash,
            users=['joe@example.com'],
        )
        self.store_response(response)

    def test_get_campaigns(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        campaigns = account.get_campaigns_aio(fields=[
            Campaign.Field.name,
            Campaign.Field.configured_status,
        ])
        self.store_response(campaigns)

    def test_get_ad_sets(self):
        for acc_id in [AsyncDocsDataStore.get('adaccount_id')]:
            account = AdAccount(acc_id)
            account.get_ad_sets_aio(fields=[
                AdSet.Field.name,
                AdSet.Field.bid_info,
                AdSet.Field.configured_status,
                AdSet.Field.daily_budget,
                AdSet.Field.targeting,
            ])
        adsets = []
        for res in FacebookAdsAsyncApi.get_default_api().get_all_async_results():
            adsets += res.get_all_results()
        self.store_response(adsets)

    def test_get_ads(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        ads = account.get_ads_aio(fields=[
            Ad.Field.name,
            Ad.Field.configured_status,
            Ad.Field.creative,
        ])
        self.store_response(ads)

    def test_get_ad_users(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        users = account.get_ad_users_aio()
        self.store_response(users)

    def test_get_ad_creatives(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        creatives = account.get_ad_creatives_aio(fields=[
            AdCreative.Field.name,
            AdCreative.Field.image_hash,
        ])
        self.store_response(creatives[0:2])

    def test_get_ad_images(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        images = account.get_ad_images_aio(fields=[
            AdImage.Field.hash,
        ])
        self.store_response(images)

    def test_get_ad_conversion_pixels(self):
        for acc_id in [AsyncDocsDataStore.get('adaccount_id')]:
            account = AdAccount(acc_id)
            account.get_ad_conversion_pixels_aio(fields=[
                AdImage.Field.hash,
            ])
        all_pixels = {}
        for res in FacebookAdsAsyncApi.get_default_api().get_all_async_results():
            account_pixels = res.get_all_results()
            all_pixels[res._source_object[AdAccount.Field.id]] = account_pixels
        self.store_response(all_pixels)

    def test_get_broad_category_targeting(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        bct = account.get_broad_category_targeting_aio()
        self.store_response(bct[0:2])

    def test_get_connection_objects(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        connection_objects = account.get_connection_objects_aio()
        connection_objects = [
            co for co in connection_objects if co['id'] == '606699326111137']
        self.store_response(connection_objects)

    def test_get_custom_audiences(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        custom_audiences = account.get_custom_audiences_aio()
        self.store_response(custom_audiences)

    def test_get_partner_categories(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        partner_categories = account.get_partner_categories_aio(limit=10)
        self.store_response(partner_categories[0])

    def test_get_rate_cards(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        rate_cards = account.get_rate_cards_aio()
        self.store_response(rate_cards[0:2])

    def test_get_reach_estimate(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        reach_estimate = account.get_reach_estimate_aio(params={
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
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        transactions = account.get_transactions_aio()
        self.store_response(transactions)

    def test_get_ad_preview(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        ad_preview = account.get_ad_preview_aio(params={
            'creative': {
                'title': 'This is the title',
                'body': 'This is the body',
                'object_url': 'https://facebookmarketingpartners.com',
                'image_hash': AsyncDocsDataStore.get('ad_account_image_hash'),
            },
            'ad_format': 'RIGHT_COLUMN_STANDARD',
        })
        self.store_response(ad_preview)

    def test_get_ads_pixel(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        pixels = account.get_ads_pixels(fields=[
            AdsPixel.Field.name,
            AdsPixel.Field.id,
        ])
        self.store_response(pixels)

    def test_get_targeting_description(self):
        adgroup = Ad(AsyncDocsDataStore.get('ad_id'))
        targeting = {
            baseobjects.TargetingSpecsField.geo_locations: {
                baseobjects.TargetingSpecsField.countries: ['US'],
            },
        }
        targeting_desc = adgroup.get_targeting_description_aio(fields=[
            'targetingsentencelines'
        ], params={
            'targeting_spec': targeting
        })
        self.store_response(targeting_desc)

    def test_get_ad_labels(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        adlabels = account.get_ad_labels_aio(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ])
        self.store_response(adlabels)

    def test_get_ad_creatives_by_labels(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        adlabel_id = AsyncDocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        adcreatives = account.get_ad_creatives_by_labels_aio(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(adcreatives)

    def test_get_ads_by_labels(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        adlabel_id = AsyncDocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        ads = account.get_ads_by_labels_aio(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(ads)

    def test_get_adsets_by_labels(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        adlabel_id = AsyncDocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        adsets = account.get_adsets_by_labels_aio(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(adsets)

    def test_get_campaigns_by_labels(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        adlabel_id = AsyncDocsDataStore.get('adlabel_id')
        params = {'ad_label_ids': [adlabel_id], 'operator': 'ALL'}
        campaigns = account.get_campaigns_by_labels_aio(fields=[
            AdLabel.Field.name,
            AdLabel.Field.id,
        ], params=params)
        self.store_response(campaigns)

    def test_get_minimum_budgets(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        min_budgets = account.get_minimum_budgets_aio(limit=10)
        min_budgets = [x for x in min_budgets]
        self.assertGreaterEqual(len(min_budgets), 49)
        self.store_response(min_budgets)


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
