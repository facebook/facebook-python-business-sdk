# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from unittest import TestCase

from facebook_business.adobjects.serverside.preference import Preference


class PreferenceTest(TestCase):

    def test_default_constructor_allows_everything(self):
        p = Preference()
        self.assertTrue(p.is_fbc_allowed)
        self.assertTrue(p.is_fbp_allowed)
        self.assertTrue(p.is_client_ip_address_allowed)
        self.assertTrue(p.is_referrer_url_allowed)
        self.assertTrue(p.is_event_source_url_allowed)

    def test_all_disallowed_denies_every_field(self):
        p = Preference(False, False, False, False, False)
        self.assertFalse(p.is_fbc_allowed)
        self.assertFalse(p.is_fbp_allowed)
        self.assertFalse(p.is_client_ip_address_allowed)
        self.assertFalse(p.is_referrer_url_allowed)
        self.assertFalse(p.is_event_source_url_allowed)

    def test_partial_allowlist_keeps_requested_flags_true(self):
        # Only fbc and client_ip_address allowed.
        p = Preference(True, False, True, False, False)
        self.assertTrue(p.is_fbc_allowed)
        self.assertFalse(p.is_fbp_allowed)
        self.assertTrue(p.is_client_ip_address_allowed)
        self.assertFalse(p.is_referrer_url_allowed)
        self.assertFalse(p.is_event_source_url_allowed)

    def test_each_flag_is_independently_controllable(self):
        cases = [
            (True, False, False, False, False, 'fbc'),
            (False, True, False, False, False, 'fbp'),
            (False, False, True, False, False, 'client_ip_address'),
            (False, False, False, True, False, 'referrer_url'),
            (False, False, False, False, True, 'event_source_url'),
        ]
        for fbc, fbp, ip, ref, esu, _label in cases:
            p = Preference(fbc, fbp, ip, ref, esu)
            self.assertEqual(p.is_fbc_allowed, fbc)
            self.assertEqual(p.is_fbp_allowed, fbp)
            self.assertEqual(p.is_client_ip_address_allowed, ip)
            self.assertEqual(p.is_referrer_url_allowed, ref)
            self.assertEqual(p.is_event_source_url_allowed, esu)

    def test_non_bool_raises_type_error(self):
        with self.assertRaises(TypeError):
            Preference(is_fbc_allowed='yes')
        with self.assertRaises(TypeError):
            Preference(is_fbp_allowed=1)
        with self.assertRaises(TypeError):
            Preference(is_client_ip_address_allowed=None)
        with self.assertRaises(TypeError):
            Preference(is_referrer_url_allowed=0)
        with self.assertRaises(TypeError):
            Preference(is_event_source_url_allowed='no')

    def test_equality(self):
        self.assertEqual(Preference(), Preference())
        self.assertEqual(
            Preference(True, False, True, False, True),
            Preference(True, False, True, False, True),
        )
        self.assertNotEqual(
            Preference(True, True, True, True, True),
            Preference(False, True, True, True, True),
        )
        self.assertNotEqual(
            Preference(True, True, True, True, True),
            Preference(True, True, True, True, False),
        )

    def test_to_dict_round_trip(self):
        p = Preference(True, False, True, False, True)
        self.assertEqual(p.to_dict(), {
            'is_fbc_allowed': True,
            'is_fbp_allowed': False,
            'is_client_ip_address_allowed': True,
            'is_referrer_url_allowed': False,
            'is_event_source_url_allowed': True,
        })
