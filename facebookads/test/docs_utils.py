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

import unittest
import inspect
import re
from ..objects import *
from ..specs import *
from ..exceptions import *


class DocsDataStore(object):
    _data = {}

    @classmethod
    def set(self, key, value):
        self._data[key] = value
        handle = open(DocsDataStore.get('filename'), 'a')
        handle.write('docs_data#' + key + "\n" + value + "\n\n")
        handle.close()

    @classmethod
    def get(self, key):
        return self._data[key]


class DocsTestCase(unittest.TestCase):
    def tearDown(self):
        account = AdAccount(DocsDataStore.get('adaccount_id'))
        campaigns = account.get_ad_campaigns()
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
        campaign = AdCampaign(parent_id=DocsDataStore.get('adaccount_id'))
        campaign['name'] = "Ad Campaign " + str(counter)
        campaign['campaign_group_status'] = "PAUSED"
        campaign.remote_create()
        return campaign

    def create_adset(self, counter, campaign):
        adset = AdSet(parent_id=DocsDataStore.get('adaccount_id'))
        adset['name'] = "Ad Set " + str(counter)
        adset['campaign_group_id'] = campaign['id']
        adset['bid_type'] = 'CPC'
        adset['bid_info'] = {
            'CLICKS': 500,
        }
        adset['campaign_status'] = 'PAUSED'
        adset['daily_budget'] = 1000
        adset['targeting'] = {
            'geo_locations': {
                'countries': ['US']
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

    def create_adgroup(self, counter, adset, creative):
        adgroup = AdGroup(parent_id=DocsDataStore.get('adaccount_id'))
        adgroup['name'] = "Ad Group " + str(counter)
        adgroup['campaign_id'] = adset['id']
        adgroup['creative'] = {'creative_id': creative.get_id()}
        adgroup['adgroup_status'] = 'PAUSED'
        adgroup.remote_create()
        return adgroup

    def create_creative(self, counter):
        creative = AdCreative(parent_id=DocsDataStore.get('adaccount_id'))
        creative['title'] = "My Creative " + str(counter)
        creative['body'] = "This is my creative's body"
        creative['object_url'] = "https://internet.org"
        creative['image_hash'] = self.create_image()['hash']
        creative.remote_create()
        return creative

    def create_image(self):
        image = AdImage(parent_id=DocsDataStore.get('adaccount_id'))
        image['filename'] = './facebookads/test/test.png'
        image.remote_create()
        return image

    def store_response(self, obj):
        class_name = re.sub(r'DocsTestCase$', '', self.__class__.__name__)
        method = inspect.stack()[1][3]
        handle = open(DocsDataStore.get('filename'), 'a')
        obj_str = str(obj)
        obj_str = re.sub('<', '&lt;', obj_str)
        obj_str = re.sub('>', '&gt;', obj_str)
        handle.write(class_name + '#' + method + "\n" + obj_str + "\n\n")
        handle.close()


DocsDataStore.set('filename', '/tmp/python_sdk_docs.nlsv')
