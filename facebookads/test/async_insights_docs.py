'''
Unit tests for the Python Facebook Ads API SDK.

How to run:
    python -m facebookads.test.async_adaccount_docs
'''

import sys

try:
    import mock
except ImportError:
    from unittest import mock

from facebookads.utils.httpretries import retry_policy
from facebookads.test.async_docs_utils import *


class AdAccountAsyncDocsTestCase(AsyncDocsTestCase):
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
