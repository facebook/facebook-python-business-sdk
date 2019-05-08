import unittest
import inspect
from ..asyncobjects import *
from ..specs import *
from ..exceptions import *


class AsyncDocsDataStore(object):
    _data = {}

    @classmethod
    def set(self, key, value):
        self._data[key] = value
        handle = open(AsyncDocsDataStore.get('filename'), 'a')
        handle.write('docs_data#' + key + "\n" + value + "\n\n")
        handle.close()

    @classmethod
    def get(self, key):
        return self._data[key]


class AsyncDocsTestCase(unittest.TestCase):
    def tearDown(self):
        account = AdAccount(AsyncDocsDataStore.get('adaccount_id'))
        campaigns = account.get_campaigns()
        for campaign in campaigns:
            campaign.remote_delete()

    def verify(self, obj, output):
        def strip_spacing(content):
            content = str(content)
            content = re.sub(r'\s+', ' ', content)
            content = re.sub(r'\n|\r', '', content)
            return content

        return strip_spacing(obj) == strip_spacing(output)

    def create_campaign(self, counter):
        campaign = Campaign(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        campaign['name'] = "Campaign " + str(counter)
        campaign['status'] = "PAUSED"
        campaign.remote_create()
        return campaign

    def create_adset(self, counter, campaign):
        adset = AdSet(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        adset['name'] = "Ad Set " + str(counter)
        adset['campaign_id'] = campaign['id']
        adset['daily_budget'] = 1000
        adset['bid_amount'] = 2
        adset['billing_event'] = 'LINK_CLICKS'
        adset['optimization_goal'] = 'LINK_CLICKS'
        adset['status'] = 'PAUSED'
        adset['daily_budget'] = 1000
        adset['targeting'] = {
            'geo_locations': {
                'countries': ['US'],
            },
            'interests': [
                {
                    "id": "6003232518610",
                    "name": "Parenting",
                },
            ],
        }
        adset.remote_create()
        return adset

    def create_ad(self, counter, adset, creative):
        adgroup = Ad(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        adgroup['name'] = "Ad " + str(counter)
        adgroup['adset_id'] = adset['id']
        adgroup['creative'] = {'creative_id': creative.get_id()}
        adgroup['status'] = 'PAUSED'
        adgroup.remote_create()
        return adgroup

    def create_creative(self, counter):
        creative = AdCreative(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        creative['title'] = "My Creative " + str(counter)
        creative['body'] = "This is my creative's body"
        creative['object_url'] = "https://internet.org"
        creative['image_hash'] = self.create_image()['hash']
        creative.remote_create()
        return creative

    def create_creative_leads(self, counter):
        image_hash = self.create_image()['hash']
        link_data = LinkData()
        link_data[LinkData.Field.message] = 'try it out'
        link_data[LinkData.Field.link] = "www.wikipedia.com"
        link_data[LinkData.Field.caption] = 'Caption'
        link_data[LinkData.Field.image_hash] = image_hash

        object_story_spec = ObjectStorySpec()
        page_id = AsyncDocsDataStore.get('page_id')
        object_story_spec[ObjectStorySpec.Field.page_id] = page_id
        object_story_spec[ObjectStorySpec.Field.link_data] = link_data

        creative = AdCreative(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        creative[AdCreative.Field.name] = 'Test Creative'
        creative[AdCreative.Field.object_story_spec] = object_story_spec
        creative.remote_create()
        return creative

    def create_image(self):
        image = AdImage(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        image['filename'] = './facebookads/test/misc/image.png'
        image.remote_create()
        return image

    def create_adlabel(self):
        label = AdLabel(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        label[AdLabel.Field.name] = 'AdLabel name'
        label.remote_create()
        return label

    def create_custom_audience(self):
        audience = CustomAudience(parent_id=AsyncDocsDataStore.get('adaccount_id'))
        audience[CustomAudience.Field.subtype] = CustomAudience.Subtype.custom
        audience[CustomAudience.Field.name] = 'Test Audience'
        audience[CustomAudience.Field.description] = 'Autogen-docs example'
        audience.remote_create()
        return audience

    def create_reach_frequency_prediction(self):
        act_id = AsyncDocsDataStore.get('adaccount_id')
        rfp = ReachFrequencyPrediction(parent_id=act_id)
        rfp['frequency_cap'] = 2
        rfp['start_time'] = 1449080260
        rfp['stop_time'] = 1449083860
        rfp['reach'] = 20
        rfp['story_event_type'] = 0
        rfp['prediction_mode'] = 0
        rfp['target_spec'] = {
            'geo_locations': {
                'countries': ['US']
            },
        }
        rfp.remote_create()
        return rfp

    def create_product_catalog(self):
        params = {}
        params['name'] = 'Test Catalog'
        product_catalog = ProductCatalog(None, AsyncDocsDataStore.get('business_id'))
        product_catalog.update(params)
        product_catalog.remote_create()
        return product_catalog

    def create_product_set(self, product_catalog_id):
        params = {}
        params['name'] = 'Test Product Set'
        product_set = ProductSet(parent_id=product_catalog_id)
        product_set.update(params)
        product_set.remote_create()
        return product_set

    def create_product_feed(self, product_catalog_id):
        product_feed = ProductFeed(parent_id=product_catalog_id)
        product_feed[ProductFeed.Field.name] = 'Test Feed'
        product_feed[ProductFeed.Field.schedule] = {
            'interval': 'DAILY',
            'url': 'http://www.example.com/sample_feed.tsv',
            'hour': 22,
        }
        product_feed.remote_create()
        return product_feed

    def store_response(self, obj):
        class_name = re.sub(r'DocsTestCase$', '', self.__class__.__name__)
        method = inspect.stack()[1][3]
        handle = open(AsyncDocsDataStore.get('filename'), 'a')
        obj_str = str(obj)
        obj_str = re.sub('<', '&lt;', obj_str)
        obj_str = re.sub('>', '&gt;', obj_str)
        handle.write(class_name + '#' + method + "\n" + obj_str + "\n\n")
        handle.close()


AsyncDocsDataStore.set('filename', '/tmp/python_sdk_docs.nlsv')
