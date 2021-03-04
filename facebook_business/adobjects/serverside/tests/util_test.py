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

from unittest import TestCase
from unittest.mock import PropertyMock, patch

from facebook_business.adobjects.serverside.util import Util, sys

import hashlib
import hmac
import os

class UtilTest(TestCase):
    @patch('facebook_business.adobjects.serverside.util.sys')
    def test_async_requests_available(self, mock_sys):
        type(mock_sys).version_info = PropertyMock(return_value=(3, 7))
        self.assertTrue(Util.async_requests_available())
        type(mock_sys).version_info = PropertyMock(return_value=(3, 5, 3))
        self.assertTrue(Util.async_requests_available())

        type(mock_sys).version_info = PropertyMock(return_value=(3, 4, 10))
        self.assertFalse(Util.async_requests_available())
        type(mock_sys).version_info = PropertyMock(return_value=(3, 2, 1))
        self.assertFalse(Util.async_requests_available())
        type(mock_sys).version_info = PropertyMock(return_value=(2, 7))
        self.assertFalse(Util.async_requests_available())

    def test_ca_bundle_path(self):
        self.assertTrue(os.path.exists(Util.ca_bundle_path()))

    def test_appsecret_proof(self):
        appsecret = 'appsecret-123'
        access_token = 'access-token-234'
        expected = hmac.new(
            appsecret.encode('utf-8'),
            msg=access_token.encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()
        actual = Util.appsecret_proof(appsecret, access_token)

        self.assertEqual(actual, expected)
