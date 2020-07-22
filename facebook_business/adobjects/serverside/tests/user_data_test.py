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
from unittest.mock import MagicMock, patch

from facebook_business.adobjects.serverside.user_data import UserData


class UserDataTest(TestCase):
    @patch('facebook_business.adobjects.serverside.user_data.UserData.hash_sha_256')
    @patch('facebook_business.adobjects.serverside.user_data.Normalize.normalize_field')
    def test_normalize(self, normalize_mock, hash_sha_256_mock):
        initial_state = {
            'f5first': 'FirstName',
            'f5last': 'LastName',
            'fi': 'FI',
            'dobd': '01',
            'dobm': '02',
            'doby': '2000',
        }
        user_data = UserData(
            f5first=initial_state['f5first'],
            f5last=initial_state['f5last'],
            fi=initial_state['fi'],
            dobd=initial_state['dobd'],
            dobm=initial_state['dobm'],
            doby=initial_state['doby'],
        )
        hash_sha_256_mock.side_effect = (
            lambda field: field + '-sha256' if field else None
        )
        normalize_mock.side_effect = (
            lambda _, field: field + '-normal' if field else None
        )
        actual = user_data.normalize()
        expected = {}
        for key, value in initial_state.items():
            expected[key] = '%s-normal-sha256' % value

        self.assertEqual(actual, expected)
