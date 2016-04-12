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
    python -m facebookads.test.adimage_docs
'''

import os
import sys
import json
from .docs_utils import *


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
