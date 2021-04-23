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
            'emails': ['joe@eg.com', 'mary@test.com', 'mary@test.com'],
            'phones': ['12345678912', '12062072008', '12062072008'],
            'genders': [Gender.MALE, Gender.FEMALE, Gender.FEMALE],
            'dates_of_birth': ['19900101', '19660202', '19660202'],
            'last_names': ['smith', 'brown', 'brown'],
            'first_names': ['joe', 'mary', 'mary'],
            'cities': ['seattle', 'sanfrancisco', 'sanfrancisco'],
            'states': ['ca', 'wa', 'wa'],
            'country_codes': ['us', 'ca', 'ca'],
            'zip_codes': ['98001', '12345', '12345'],
            'external_ids': ['123', '456', '456'],
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

        actual = user_data.normalize()
        expected = {
            'em': self.__hash_list(initial_state['emails'][0:2]),
            'ph': self.__hash_list(initial_state['phones'][0:2]),
            'ge': self.__hash_list(list(map(lambda g: g.value, initial_state['genders'][0:2]))),
            'db': self.__hash_list(initial_state['dates_of_birth'][0:2]),
            'ln': self.__hash_list(initial_state['last_names'][0:2]),
            'fn': self.__hash_list(initial_state['first_names'][0:2]),
            'ct': self.__hash_list(initial_state['cities'][0:2]),
            'st': self.__hash_list(initial_state['states'][0:2]),
            'zp': self.__hash_list(initial_state['zip_codes'][0:2]),
            'country': self.__hash_list(initial_state['country_codes'][0:2]),
            'external_id': initial_state['external_ids'][0:2],
            'f5first': Normalize.hash_sha_256(initial_state['f5first'].lower()),
            'f5last': Normalize.hash_sha_256(initial_state['f5last'].lower()),
            'fi': Normalize.hash_sha_256(initial_state['fi'].lower()),
            'dobd': Normalize.hash_sha_256(initial_state['dobd']),
            'dobm': Normalize.hash_sha_256(initial_state['dobm']),
            'doby': Normalize.hash_sha_256(initial_state['doby']),
            'lead_id': initial_state['lead_id'],
        }

        not_equal_items = {k: actual[k] for k in actual if k not in expected or sorted(actual[k]) != sorted(expected[k])}
        self.assertEqual(len(not_equal_items), 0)
        self.assertEqual(len(actual), len(expected))

    def test_multiple_values_getters_and_setters(self):
        initial_state = {
            'emails': ['joe@eg.com', 'mary@test.com'],
            'phones': ['12345678912', '12062072008'],
            'genders': [Gender.MALE, Gender.FEMALE],
            'dates_of_birth': ['19900101', '19660202'],
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

        # Also check that single getters/setters when multiple values exist
        self.assertEqual(user_data.email, initial_state['emails'][0])
        self.assertEqual(user_data.phone, initial_state['phones'][0])
        self.assertEqual(user_data.gender, initial_state['genders'][0])
        self.assertEqual(user_data.date_of_birth, initial_state['dates_of_birth'][0])
        self.assertEqual(user_data.last_name, initial_state['last_names'][0])
        self.assertEqual(user_data.first_name, initial_state['first_names'][0])
        self.assertEqual(user_data.city, initial_state['cities'][0])
        self.assertEqual(user_data.state, initial_state['states'][0])
        self.assertEqual(user_data.country_code, initial_state['country_codes'][0])
        self.assertEqual(user_data.zip_code, initial_state['zip_codes'][0])
        self.assertEqual(user_data.external_id, initial_state['external_ids'][0])

    # Assign value via singular setter/constructor, retrieve via singular getters
    def test_single_getters_setters_constructor(self):
        initial_state = {
            'email': 'joe@eg.com',
            'phone': '12345678912',
            'gender': Gender.MALE,
            'date_of_birth': '19900101',
            'last_name': 'smith',
            'first_name': 'joe',
            'city': 'seattle',
            'state': 'ca',
            'country_code': 'us',
            'zip_code': '98001',
            'external_id': '123'
        }

        user_data_via_setter = UserData()
        user_data_via_setter.email = initial_state['email']
        user_data_via_setter.phone = initial_state['phone']
        user_data_via_setter.gender = initial_state['gender']
        user_data_via_setter.date_of_birth = initial_state['date_of_birth']
        user_data_via_setter.last_name = initial_state['last_name']
        user_data_via_setter.first_name = initial_state['first_name']
        user_data_via_setter.city = initial_state['city']
        user_data_via_setter.state = initial_state['state']
        user_data_via_setter.country_code = initial_state['country_code']
        user_data_via_setter.zip_code = initial_state['zip_code']
        user_data_via_setter.external_id = initial_state['external_id']

        user_data_via_constructor = UserData(
            email=initial_state['email'],
            phone=initial_state['phone'],
            gender=initial_state['gender'],
            date_of_birth=initial_state['date_of_birth'],
            last_name=initial_state['last_name'],
            first_name=initial_state['first_name'],
            city=initial_state['city'],
            state=initial_state['state'],
            country_code=initial_state['country_code'],
            zip_code=initial_state['zip_code'],
            external_id=initial_state['external_id']
        )

        self.__assert_equality_via_singular_getters(initial_state, user_data_via_setter)
        self.__assert_equality_via_singular_getters(initial_state, user_data_via_constructor)

    def __assert_equality_via_singular_getters(self, expected, actual):
        self.assertEqual(actual.email, expected['email'])
        self.assertEqual(actual.phone, expected['phone'])
        self.assertEqual(actual.gender, expected['gender'])
        self.assertEqual(actual.date_of_birth, expected['date_of_birth'])
        self.assertEqual(actual.last_name, expected['last_name'])
        self.assertEqual(actual.first_name, expected['first_name'])
        self.assertEqual(actual.city, expected['city'])
        self.assertEqual(actual.state, expected['state'])
        self.assertEqual(actual.country_code, expected['country_code'])
        self.assertEqual(actual.zip_code, expected['zip_code'])
        self.assertEqual(actual.external_id, expected['external_id'])

    def test_single_getters_and_setters_with_none(self):
        user_data = UserData()

        self.assertIsNone(user_data.email)
        self.assertIsNone(user_data.phone)
        self.assertIsNone(user_data.gender)
        self.assertIsNone(user_data.date_of_birth)
        self.assertIsNone(user_data.last_name)
        self.assertIsNone(user_data.first_name)
        self.assertIsNone(user_data.city)
        self.assertIsNone(user_data.state)
        self.assertIsNone(user_data.country_code)
        self.assertIsNone(user_data.zip_code)
        self.assertIsNone(user_data.external_id)

    def test_single_getters_and_setters_with_empty(self):
        user_data = UserData()
        user_data.emails = []
        user_data.phones = []
        user_data.genders = []
        user_data.dates_of_birth = []
        user_data.last_names = []
        user_data.first_names = []
        user_data.cities = []
        user_data.states = []
        user_data.country_codes = []
        user_data.zip_codes = []
        user_data.external_ids = []

        self.assertIsNone(user_data.email)
        self.assertIsNone(user_data.phone)
        self.assertIsNone(user_data.gender)
        self.assertIsNone(user_data.date_of_birth)
        self.assertIsNone(user_data.last_name)
        self.assertIsNone(user_data.first_name)
        self.assertIsNone(user_data.city)
        self.assertIsNone(user_data.state)
        self.assertIsNone(user_data.country_code)
        self.assertIsNone(user_data.zip_code)
        self.assertIsNone(user_data.external_id)

    def test_multiple_values_constructor_with_only_plural_values(self):
        initial_state = {
            'emails': ['joe@eg.com', 'mary@test.com'],
            'phones': ['12345678912', '12062072008'],
            'genders': [Gender.MALE, Gender.FEMALE],
            'dates_of_birth': ['19900101', '19660202'],
            'last_names': ['smith', 'brown'],
            'first_names': ['joe', 'mary'],
            'cities': ['seattle', 'san francisco'],
            'states': ['ca', 'wa'],
            'country_codes': ['us', 'ca'],
            'zip_codes': ['98001', '12345'],
            'external_ids': ['123', '456']
        }

        user_data = UserData(
            emails=initial_state['emails'],
            phones=initial_state['phones'],
            genders=initial_state['genders'],
            dates_of_birth=initial_state['dates_of_birth'],
            last_names=initial_state['last_names'],
            first_names=initial_state['first_names'],
            cities=initial_state['cities'],
            states=initial_state['states'],
            country_codes=initial_state['country_codes'],
            zip_codes=initial_state['zip_codes'],
            external_ids=initial_state['external_ids']
        )

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

    def test_multiple_values_constructor_with_singular_and_plural_values(self):
        params = [
            ['email', 'emails'],
            ['phone', 'phones'],
            ['gender', 'genders'],
            ['date_of_birth', 'dates_of_birth'],
            ['last_name', 'last_names'],
            ['first_name', 'first_names'],
            ['city', 'cities'],
            ['state', 'states'],
            ['country_code', 'country_codes'],
            ['zip_code', 'zip_codes'],
            ['external_id', 'external_ids'],
        ]

        for p in params:
            param_dict = {
                p[0]: 'test',
                p[1]: ['test', 'test']
            }
            with self.assertRaises(ValueError) as context:
                user_data = UserData(
                    **param_dict
                )
            self.assertEqual(UserData.multi_value_constructor_err.format(list(param_dict)[0], list(param_dict)[1]), str(context.exception))

    def test_multi_value_normalization_with_empty(self):
        user_data = UserData()
        user_data.emails = []
        user_data.phones = []
        user_data.genders = []
        user_data.dates_of_birth = []
        user_data.last_names = []
        user_data.first_names = []
        user_data.cities = []
        user_data.states = []
        user_data.country_codes = []
        user_data.zip_codes = []
        user_data.external_ids = []

        normalized_data = user_data.normalize()

        self.assertFalse(normalized_data)

    def __hash_list(self, value_list):
        return list(map(lambda val: Normalize.hash_sha_256(val), value_list))
