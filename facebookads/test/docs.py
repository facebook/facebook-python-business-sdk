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

import os
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

    def test_get_insights(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        insights = adgroup.get_insights(fields=[
            Insights.Field.adgroup_id,
            Insights.Field.clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.adgroup,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)

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
        adgroup_preview = adgroup.get_ad_preview(params={
            'ad_format': 'RIGHT_COLUMN_STANDARD',
        })
        self.store_response(adgroup_preview)

    def test_get_reach_estimate(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        reach_estimate = adgroup.get_reach_estimate()
        self.store_response(reach_estimate)

    def test_get_stats(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        stats = adgroup.get_stats()
        self.store_response(stats)

    def test_get_click_tracking_tag(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        tag = adgroup.get_click_tracking_tag()
        self.store_response(tag)

    def test_get_conversion_stats(self):
        adgroup = AdGroup(DocsDataStore.get('adgroup_id'))
        stats = adgroup.get_conversion_stats()
        self.store_response(stats)


class AdCreativeDocsTestCase(DocsTestCase):
    def setUp(self):
        creative = self.create_creative(1)
        DocsDataStore.set('creative_id', creative.get_id())

    def test_get_ad_preview(self):
        creative = AdCreative(DocsDataStore.get('creative_id'))
        preview = creative.get_ad_preview(params={
            'ad_format': 'RIGHT_COLUMN_STANDARD',
        })
        self.store_response(preview)


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

    def test_get_insights(self):
        adset = AdSet(DocsDataStore.get('adset_id'))
        insights = adset.get_insights(fields=[
            Insights.Field.adgroup_id,
            Insights.Field.clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.adgroup,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)

    def test_get_ad_groups(self):
        adset = AdSet(DocsDataStore.get('adset_id'))
        adgroups = adset.get_ad_groups(fields=[
            AdGroup.Field.name,
            AdGroup.Field.campaign_id,
            AdGroup.Field.creative,
            AdGroup.Field.status,
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

    def test_get_stats(self):
        adset = AdSet(DocsDataStore.get('adset_id'))
        adsetstats = adset.get_stats(fields=[
            'spent',
            'impressions',
        ])
        self.store_response(adsetstats)


class AdCampaignDocsTestCase(DocsTestCase):
    def setUp(self):
        campaign = self.create_campaign(1)
        adset = self.create_adset(1, campaign)
        self.create_adset(2, campaign)
        creative = self.create_creative(1)
        self.create_adgroup(1, adset, creative)
        self.create_adgroup(2, adset, creative)
        DocsDataStore.set('adcampaign_id', campaign.get_id())

    def test_get_insights(self):
        adcampaign = AdCampaign(DocsDataStore.get('adcampaign_id'))
        insights = adcampaign.get_insights(fields=[
            Insights.Field.adgroup_id,
            Insights.Field.clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.adgroup,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)

    def test_get_ad_sets(self):
        adcampaign = AdCampaign(DocsDataStore.get('adcampaign_id'))
        adsets = adcampaign.get_ad_sets(fields=[
            AdSet.Field.name,
            AdSet.Field.id,
            AdSet.Field.daily_budget,
        ])
        self.store_response(adsets[0])

    def test_get_ad_groups(self):
        adcampaign = AdCampaign(DocsDataStore.get('adcampaign_id'))
        adgroups = adcampaign.get_ad_groups(fields=[
            AdGroup.Field.name,
            AdGroup.Field.status,
            AdGroup.Field.creative,
        ])
        self.store_response(adgroups)

    def test_get_stats(self):
        adcampaign = AdCampaign(DocsDataStore.get('adcampaign_id'))
        adcampaignstats = adcampaign.get_stats(fields=[
            'impressions',
            'actions',
            'clicks',
        ])
        self.store_response(adcampaignstats)


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
        self.create_adgroup(1, adset, creative1)
        self.create_adgroup(2, adset, creative2)
        # Create AdImage
        image = self.create_image()
        DocsDataStore.set('ad_account_image_hash', image['hash'])

    def test_get_insights(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        insights = account.get_insights(fields=[
            Insights.Field.campaign_id,
            Insights.Field.clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.campaign,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)

    def test_get_activities(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        activities = account.get_activities(fields=[
            Activity.Field.actor_id,
            Activity.Field.actor_name,
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

    def test_get_ad_groups(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        adgroups = account.get_ad_groups(fields=[
            AdGroup.Field.name,
            AdGroup.Field.status,
            AdGroup.Field.creative,
        ])
        self.store_response(adgroups)

    def test_get_ad_users(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        users = account.get_ad_users()
        self.store_response(users)

    def test_get_ad_campaign_stats(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        campaign_stats = account.get_ad_campaign_stats()
        self.store_response(campaign_stats[0])

    def test_get_ad_group_stats(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        ad_stats = account.get_ad_group_stats()
        self.store_response(ad_stats[0])

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
            'targeting_spec': {
                'geo_locations': {
                    'countries': ['US']
                }
            }
        })
        self.store_response(reach_estimate)

    def test_get_report_stats(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        report_stats = account.get_report_stats(params={
            'date_preset': 'last_28_days',
            'data_columns': ['adgroup_id', 'actions', 'spend'],
        })
        self.store_response(report_stats)

    def test_get_stats(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        stats = account.get_stats()
        self.store_response(stats)

    def test_get_transactions(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        transactions = account.get_transactions()
        self.store_response(transactions)

    def test_get_conversion_stats(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        conversion_stats = account.get_conversion_stats()
        self.store_response(conversion_stats)

    def test_get_ad_campaign_conversion_stats(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        stats = account.get_ad_campaign_conversion_stats()
        self.store_response(stats)

    def test_get_ad_group_conversion_stats(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        stats = account.get_ad_group_conversion_stats()
        self.store_response(stats)

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


class AdAccountGroupDocsTestCase(DocsTestCase):
    def setUp(self):
        account_group = self.create_adaccount_group(
            DocsDataStore.get('adaccount_id')
        )
        DocsDataStore.set('adaccount_group_id', account_group.get_id())

    def test_get_users(self):
        account_group = AdAccountGroup(DocsDataStore.get('adaccount_group_id'))
        users = account_group.get_users()
        self.store_response(users)

    def test_get_accounts(self):
        account_group = AdAccountGroup(DocsDataStore.get('adaccount_group_id'))
        accounts = account_group.get_accounts()
        self.store_response(accounts)


class AdConversionPixelDocsTestCase(DocsTestCase):
    pass


class AdImageDocsTestCase(DocsTestCase):
    def setUp(self):
        DocsDataStore.set(
            'image_zip', os.path.join(os.path.dirname(__file__), 'test.zip'))
        DocsDataStore.set(
            'image_path', os.path.join(os.path.dirname(__file__), 'test.png'))
        image = AdImage(parent_id=DocsDataStore.get('adaccount_id'))
        image[AdImage.Field.filename] = DocsDataStore.get('image_path')
        image.remote_create()
        DocsDataStore.set('image_id', image['id'])

    def test_remote_create(self):
        image = AdImage(parent_id=DocsDataStore.get('adaccount_id'))
        image[AdImage.Field.filename] = DocsDataStore.get('image_path')
        image.remote_create()
        self.store_response(image)

    def test_remote_create_from_zip(self):
        images = AdImage.remote_create_from_zip(
            filename=DocsDataStore.get('image_zip'),
            parent_id=DocsDataStore.get('adaccount_id'),
        )
        self.store_response(images)

    def test_remote_read(self):
        image = AdImage(DocsDataStore.get('image_id'))
        image.remote_read()
        self.store_response(image)

    def test_get_hash(self):
        image = AdImage(DocsDataStore.get('image_id'))
        image.remote_read()
        image_hash = image.get_hash()
        self.store_response(image_hash)


class CustomAudienceDocsTestCase(DocsTestCase):
    def test_add_users(self):
        custom_audience = CustomAudience(DocsDataStore.get('ca_id'))
        response = custom_audience.add_users(
            schema=CustomAudience.Schema.email_hash,
            users=[
                'joe@example.com',
            ]
        )
        self.store_response(response)

    def test_remove_users(self):
        custom_audience = CustomAudience(DocsDataStore.get('ca_id'))
        response = custom_audience.remove_users(
            schema=CustomAudience.Schema.email_hash,
            users=[
                'joe@example.com',
            ]
        )
        self.store_response(response)

    def test_format_params(self):
        formatted_params = CustomAudience.format_params(
            schema=CustomAudience.Schema.email_hash,
            users=['joe@example.com'],
        )
        self.store_response(formatted_params)

    def test_share_audience(self):
        custom_audience = CustomAudience(DocsDataStore.get('ca_id'))
        response = custom_audience.share_audience(account_ids=[
            DocsDataStore.get('adaccount_id_int'),
        ])
        self.store_response(response)

    def test_unshare_audience(self):
        custom_audience = CustomAudience(DocsDataStore.get('ca_id'))
        response = custom_audience.unshare_audience(account_ids=[
            DocsDataStore.get('adaccount_id_int'),
        ])
        self.store_response(response)


class LookalikeAudienceDocsTestCase(DocsTestCase):
    pass


class ReachFrequencyPredictionDocsTestCase(DocsTestCase):
    def setUp(self):
        rfp = self.create_reach_frequency_prediction()
        DocsDataStore.set('rfp_id', rfp.get_id())

    def test_reserve(self):
        pass

    def test_cancel(self):
        pass


class AdUserDocsTestCase(DocsTestCase):
    def test_get_ad_accounts(self):
        user = AdUser('me')
        accounts = user.get_ad_accounts(fields=[
            AdAccount.Field.name,
        ])
        self.store_response(accounts[0:3])

    def test_get_ad_account(self):
        user = AdUser('me')
        account = user.get_ad_account(fields=[
            AdAccount.Field.name,
        ])
        self.store_response(account)


class TargetingSearchDocsTestCase(DocsTestCase):
    def test_search(self):
        results = TargetingSearch.search(params={
            'q': 'United States',
            'type': TargetingSearch.TargetingSearchTypes.country,
            'limit': 2
        })
        self.store_response(results)


class BusinessDocsTestCase(DocsTestCase):
    def test_get_product_catalogs(self):
        business = Business(DocsDataStore.get('business_id'))
        catalogs = business.get_product_catalogs()
        self.store_response(catalogs[0])

    def test_get_insights(self):
        business = Business(DocsDataStore.get('business_id'))
        insights = business.get_insights(fields=[
            Insights.Field.campaign_id,
            Insights.Field.clicks,
            Insights.Field.impressions,
        ], params={
            'level': Insights.Level.campaign,
            'date_preset': Insights.Preset.last_week,
        })
        self.store_response(insights)


class ProductGroupDocsTestCase(DocsTestCase):
    pass


class ProductFeedDocsTestCase(DocsTestCase):
    def test_get_products(self):
        feed = ProductFeed(DocsDataStore.get('dpa_feed_id'))
        products = feed.get_products(fields=[
            Product.Field.title,
            Product.Field.price,
        ])
        self.store_response(products)

    def test_get_uploads(self):
        feed = ProductFeed(DocsDataStore.get('dpa_feed_id'))
        uploads = feed.get_uploads()
        self.store_response(uploads)


class ProductAudienceDocsTestCase(DocsTestCase):
    pass


class ProductDocsTestCase(DocsTestCase):
    pass


class ProductCatalogDocsTestCase(DocsTestCase):
    def test_get_product_feeds(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        feeds = catalog.get_product_feeds()
        self.store_response(feeds[0])

    def test_add_user(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        response = catalog.add_user(
            user=DocsDataStore.get('as_user_id'),
            role=ProductCatalog.Role.admin,
        )
        self.store_response(response)

    def test_remove_user(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        response = catalog.remove_user(
            user=DocsDataStore.get('as_user_id'),
        )
        self.store_response(response)

    def test_add_external_event_sources(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        response = catalog.add_external_event_sources(pixel_ids=[
            DocsDataStore.get('pixel_id'),
        ])
        self.store_response(response)

    def test_remove_external_event_sources(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        response = catalog.remove_external_event_sources(pixel_ids=[
            DocsDataStore.get('pixel_id'),
        ])
        self.store_response(response)

    def test_get_external_event_sources(self):
        catalog = ProductCatalog(DocsDataStore.get('dpa_catalog_id'))
        sources = catalog.get_external_event_sources()
        self.store_response(sources)


class ProductFeedUploadDocsTestCase(DocsTestCase):
    def test_get_errors(self):
        upload = ProductFeedUpload(DocsDataStore.get('dpa_upload_id'))
        errors = upload.get_errors()
        self.store_response(errors)


class ProductSetDocsTestCase(DocsTestCase):
    def test_get_product_groups(self):
        product_set = ProductSet(DocsDataStore.get('dpa_set_id'))
        product_groups = product_set.get_product_groups(fields=[
            Product.Field.title,
            Product.Field.price,
        ])
        self.store_response(product_groups)

    def test_get_products(self):
        product_set = ProductSet(DocsDataStore.get('dpa_set_id'))
        products = product_set.get_products(fields=[
            Product.Field.title,
            Product.Field.price,
        ])
        self.store_response(products)


class ProductFeedUploadErrorDocsTestCase(DocsTestCase):
    pass


class ClickTrackingTagDocsTestCase(DocsTestCase):
    pass


class InsightsDocsTestCase(DocsTestCase):
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

    act_id = "1505766289694659"
    FacebookAdsApi.init(
        config['app_id'],
        config['app_secret'],
        config['access_token'],
        'act_' + str(act_id)
    )
    DocsDataStore.set('adaccount_id', 'act_' + str(act_id))
    DocsDataStore.set('adaccount_id_int', act_id)
    DocsDataStore.set('business_id', '1454288444842444')
    DocsDataStore.set('ca_id', '6026172406640')
    DocsDataStore.set('dpa_catalog_id', '447683242047472')
    DocsDataStore.set('dpa_set_id', '808641022536664')
    DocsDataStore.set('dpa_feed_id', '1577689442497017')
    DocsDataStore.set('dpa_upload_id', '1577690399163588')
    DocsDataStore.set('as_user_id', '358829457619128')
    DocsDataStore.set('pixel_id', '417531085081002')

    unittest.main()
