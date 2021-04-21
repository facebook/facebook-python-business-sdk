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

from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.adobjects.serverside.normalize import Normalize
from facebook_business.adobjects.serverside.gender import Gender


class UserDataTest(TestCase):
    def test_normalize_it_normalizes_and_hashes(self):
        initial_state = {
            'f5first': 'First',
            'f5last': 'Last',
            'fi': 'A',
            'dobd': '01',
            'dobm': '02',
            'doby': '2000',
            'lead_id': 'lead-id-3',
        }
        user_data = UserData(
            f5first=initial_state['f5first'],
            f5last=initial_state['f5last'],
            fi=initial_state['fi'],
            dobd=initial_state['dobd'],
            dobm=initial_state['dobm'],
            doby=initial_state['doby'],
            lead_id=initial_state['lead_id'],
        )

        actual = user_data.normalize()
        expected = {
            'f5first': Normalize.hash_sha_256(initial_state['f5first'].lower()),
            'f5last': Normalize.hash_sha_256(initial_state['f5last'].lower()),
            'fi': Normalize.hash_sha_256(initial_state['fi'].lower()),
            'dobd': Normalize.hash_sha_256(initial_state['dobd']),
            'dobm': Normalize.hash_sha_256(initial_state['dobm']),
            'doby': Normalize.hash_sha_256(initial_state['doby']),
            'lead_id': initial_state['lead_id'],
        }

        self.assertEqual(actual, expected)

    def test_multiple_values_getters_and_setters(self):
        initial_state = {
            'emails': ['joe@eg.com', 'mary@test.com'],
            'phones': ['12345678912', '12062072008'],
            'genders': [Gender.MALE, Gender.FEMALE],
            'dates_of_birth':['19900101', '19660202'],
            'last_names': ['smith', 'brown'],
            'first_names': ['joe', 'mary'],
            'cities': ['seattle', 'san francisco'],
            'states': ['ca', 'wa'],
            'country_codes': ['us', 'ca'],
            'zip_codes': ['98001', '12345'],
            'external_ids': ['123', '456']
        }
        user_data = UserData()
        user_data.emails = initial_state['emails']
        user_data.phones = initial_state['phones']
        user_data.genders = initial_state['genders']
        user_data.dates_of_birth = initial_state['dates_of_birth']
        user_data.last_names = initial_state['last_names']
        user_data.first_names = initial_state['first_names']
        user_data.cities = initial_state['cities']
        user_data.states = initial_state['states']
        user_data.country_codes = initial_state['country_codes']
        user_data.zip_codes = initial_state['zip_codes']
        user_data.external_ids = initial_state['external_ids']

        self.assertListEqual(user_data.emails, initial_state['emails'])
        self.assertListEqual(user_data.phones, initial_state['phones'])
        self.assertListEqual(user_data.genders, initial_state['genders'])
        self.assertListEqual(user_data.dates_of_birth, initial_state['dates_of_birth'])
        self.assertListEqual(user_data.last_names, initial_state['last_names'])
        self.assertListEqual(user_data.first_names, initial_state['first_names'])
        self.assertListEqual(user_data.cities, initial_state['cities'])
        self.assertListEqual(user_data.states, initial_state['states'])
        self.assertListEqual(user_data.country_codes, initial_state['country_codes'])
        self.assertListEqual(user_data.zip_codes, initial_state['zip_codes'])
        self.assertListEqual(user_data.external_ids, initial_state['external_ids'])
