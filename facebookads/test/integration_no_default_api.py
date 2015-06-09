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
Integration tests for the Python Facebook Ads API SDK without a default API.

How to run:
    python -m facebookads.test.integration_no_default_api access_token
'''

import unittest
import time
import sys
import os
import json

from .. import objects
from .. import specs
from .. import api
from .. import session
from .. import exceptions as fbexceptions


class FacebookAdsNoDefaultApiTestCase(unittest.TestCase):

    TEST_SESSION = None
    TEST_API = None
    TEST_ACCOUNT = None
    TEST_ID = str(int(time.time()) % 1000)

    def runTest(self):
        assert api.FacebookAdsApi.get_default_api() == None # Ensure the default api is not set
        me = objects.AdUser(fbid='me', api=FacebookAdsNoDefaultApiTestCase.TEST_API)
        ad_account = me.get_ad_account()
        assert ad_account.get_api() == FacebookAdsNoDefaultApiTestCase.TEST_API

if __name__ == '__main__':
    try:
        config_file = open('./config.json')
    except IOError:
        print("No config file found, skipping integration tests")
        sys.exit()

    config = json.load(config_file)
    config_file.close()

    test_account_id = config['act_id']
    page_id = config['page_id']
    app_id = config['app_id']
    app_secret = config['app_secret']

    if 'access_token' in config:
        access_token = config['access_token']
    else:
        if len(sys.argv) < 2:
            raise TypeError("Please provide the access token as an argument")

        access_token = sys.argv.pop()

    FacebookAdsNoDefaultApiTestCase.TEST_SESSION = session.FacebookSession(
        app_id,
        app_secret,
        access_token
    )
    FacebookAdsNoDefaultApiTestCase.TEST_API = api.FacebookAdsApi(
        FacebookAdsNoDefaultApiTestCase.TEST_SESSION
    )

    if 'act_' not in test_account_id:
        test_account_id = 'act_' + test_account_id
    FacebookAdsNoDefaultApiTestCase.TEST_ACCOUNT = objects.AdAccount(test_account_id)
    FacebookAdsNoDefaultApiTestCase.PAGE_ID = page_id

    unittest.main()
