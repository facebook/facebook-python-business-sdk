# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from unittest import TestCase
from unittest.mock import MagicMock, patch

from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.preference import Preference
from facebook_business.adobjects.serverside.user_data import UserData


def _mock_param_builder(fbc=None, fbp=None, event_source_url=None, referrer_url=None):
    """Builds a MagicMock that quacks like a ParamBuilder with the given
    extracted values. process_request_from_context is a no-op. Defaults
    every getter to None so unrelated tests do not see MagicMock-fabricated
    truthy values leak into the Event payload."""
    pb = MagicMock()
    pb.process_request_from_context.return_value = None
    pb.get_fbc.return_value = fbc
    pb.get_fbp.return_value = fbp
    pb.get_event_source_url.return_value = event_source_url
    pb.get_referrer_url.return_value = referrer_url
    return pb


PB_PATH = 'facebook_business.adobjects.serverside.event.ParamBuilder'


class EventRequestContextTest(TestCase):

    # ---------------------------------------------------------------------
    # set_request_context contract
    # ---------------------------------------------------------------------

    def test_set_request_context_stores_context_and_preference(self):
        context = {'req': 'opaque'}
        pref = Preference(False, True, True, False)

        with patch(PB_PATH, return_value=_mock_param_builder()):
            event = Event(event_name='Lead', event_time=1700000001)
            returned = event.set_request_context(context, pref)

        self.assertIs(event.get_request_context(), context)
        self.assertIs(event.get_preference(), pref)
        self.assertIs(returned, event, 'set_request_context must return self')

    def test_set_request_context_defaults_to_allow_all_preference(self):
        with patch(PB_PATH, return_value=_mock_param_builder()):
            event = Event(event_name='PageView', event_time=1700000002)
            event.set_request_context({})

        pref = event.get_preference()
        self.assertIsInstance(pref, Preference)
        self.assertTrue(pref.is_fbc_allowed)
        self.assertTrue(pref.is_fbp_allowed)
        self.assertTrue(pref.is_client_ip_address_allowed)
        self.assertTrue(pref.is_referrer_url_allowed)
        self.assertTrue(pref.is_event_source_url_allowed)

    def test_set_request_context_rejects_non_preference(self):
        event = Event(event_name='PageView', event_time=1700000003)
        with self.assertRaises(TypeError):
            event.set_request_context({}, preference='not-a-preference')

    # ---------------------------------------------------------------------
    # normalize() without set_request_context
    # ---------------------------------------------------------------------

    def test_normalize_without_set_request_context_leaves_user_data_untouched(self):
        ud = UserData(email='a@example.com')
        event = Event(
            event_name='Purchase',
            event_time=1700000000,
            user_data=ud,
        )
        payload = event.normalize()
        # user_data normalize() returns no fbc/fbp/client_ip when none were set.
        self.assertNotIn('fbc', payload['user_data'])
        self.assertNotIn('fbp', payload['user_data'])
        self.assertNotIn('client_ip_address', payload['user_data'])

    def test_normalize_with_no_user_data_and_no_request_context_is_safe(self):
        # No user_data, no request context — normalize() should not crash.
        event = Event(event_name='PageView', event_time=1700000004)
        payload = event.normalize()
        self.assertEqual(payload['event_name'], 'PageView')

    # ---------------------------------------------------------------------
    # normalize() auto-populates fbc/fbp from the ParamBuilder, gated by
    # Preference and never overwriting caller-supplied values.
    # ---------------------------------------------------------------------

    def test_normalize_auto_populates_fbc(self):
        pb = _mock_param_builder(fbc='fb.1.1700000000000.AbCdEf12345')
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000010)
            event.set_request_context({})

        payload = event.normalize()
        self.assertEqual(
            payload['user_data']['fbc'], 'fb.1.1700000000000.AbCdEf12345')

    def test_normalize_auto_populates_fbp(self):
        pb = _mock_param_builder(fbp='fb.1.1700000000000.987654321')
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000011)
            event.set_request_context({})

        payload = event.normalize()
        self.assertEqual(
            payload['user_data']['fbp'], 'fb.1.1700000000000.987654321')

    def test_caller_supplied_fbc_takes_precedence_over_builder(self):
        pb = _mock_param_builder(fbc='BUILDER_FBC')
        with patch(PB_PATH, return_value=pb):
            event = Event(
                event_name='Lead',
                event_time=1700000020,
                user_data=UserData(fbc='CALLER_FBC'),
            )
            event.set_request_context({})

        self.assertEqual(event.normalize()['user_data']['fbc'], 'CALLER_FBC')

    def test_caller_supplied_fbp_takes_precedence_over_builder(self):
        pb = _mock_param_builder(fbp='BUILDER_FBP')
        with patch(PB_PATH, return_value=pb):
            event = Event(
                event_name='Lead',
                event_time=1700000021,
                user_data=UserData(fbp='CALLER_FBP'),
            )
            event.set_request_context({})

        self.assertEqual(event.normalize()['user_data']['fbp'], 'CALLER_FBP')

    def test_preference_fbp_false_gates_fbp_but_keeps_fbc(self):
        pb = _mock_param_builder(fbc='WITHFBC', fbp='WITHFBP')
        pref = Preference(True, False, True, True)
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000030)
            event.set_request_context({}, pref)

        payload = event.normalize()
        self.assertEqual(payload['user_data']['fbc'], 'WITHFBC')
        self.assertNotIn('fbp', payload['user_data'])

    def test_preference_all_false_suppresses_every_auto_field(self):
        pb = _mock_param_builder(
            fbc='XX', fbp='YY',
            event_source_url='https://shop.example.com/cart',
            referrer_url='https://referrer.example.com/')
        pref = Preference(False, False, False, False, False)
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000031)
            event.set_request_context({}, pref)

        payload = event.normalize()
        ud = payload.get('user_data', {})
        self.assertNotIn('fbc', ud)
        self.assertNotIn('fbp', ud)
        self.assertIsNone(payload.get('event_source_url'))
        self.assertIsNone(payload.get('referrer_url'))

    # ---------------------------------------------------------------------
    # Deferring extraction to normalize() makes call order between
    # user_data assignment and set_request_context() irrelevant.
    # ---------------------------------------------------------------------

    def test_order_independent_user_data_before_request_context(self):
        pb = _mock_param_builder(fbc='FROM_BUILDER')
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='AddToCart', event_time=1700000040)
            event.user_data = UserData(email='a@b.com')
            event.set_request_context({})

        ud = event.normalize()['user_data']
        self.assertEqual(ud['fbc'], 'FROM_BUILDER')
        self.assertEqual(len(ud['em']), 1)

    def test_order_independent_request_context_before_user_data(self):
        pb = _mock_param_builder(fbc='FROM_BUILDER')
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='AddToCart', event_time=1700000041)
            event.set_request_context({})
            event.user_data = UserData(email='a@b.com')

        ud = event.normalize()['user_data']
        self.assertEqual(ud['fbc'], 'FROM_BUILDER')
        self.assertEqual(len(ud['em']), 1)

    # ---------------------------------------------------------------------
    # event_source_url auto-population from ParamBuilder.get_event_source_url
    # ---------------------------------------------------------------------

    def test_normalize_auto_populates_event_source_url(self):
        pb = _mock_param_builder(
            event_source_url='https://shop.example.com/cart')
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000060)
            event.set_request_context({})

        payload = event.normalize()
        self.assertEqual(
            payload['event_source_url'], 'https://shop.example.com/cart')

    def test_caller_supplied_event_source_url_takes_precedence_over_builder(self):
        pb = _mock_param_builder(event_source_url='https://from-builder/')
        with patch(PB_PATH, return_value=pb):
            event = Event(
                event_name='Lead',
                event_time=1700000061,
                event_source_url='https://from-caller/',
            )
            event.set_request_context({})

        self.assertEqual(
            event.normalize()['event_source_url'], 'https://from-caller/')

    # ---------------------------------------------------------------------
    # referrer_url auto-population from ParamBuilder.get_referrer_url
    # ---------------------------------------------------------------------

    def test_normalize_auto_populates_referrer_url(self):
        pb = _mock_param_builder(referrer_url='https://google.com/search?q=foo')
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000070)
            event.set_request_context({})

        payload = event.normalize()
        self.assertEqual(payload['referrer_url'], 'https://google.com/search?q=foo')

    def test_caller_supplied_referrer_url_takes_precedence_over_builder(self):
        pb = _mock_param_builder(referrer_url='https://builder.example.com/')
        with patch(PB_PATH, return_value=pb):
            event = Event(
                event_name='Lead',
                event_time=1700000071,
                referrer_url='https://caller.example.com/',
            )
            event.set_request_context({})

        self.assertEqual(
            event.normalize()['referrer_url'], 'https://caller.example.com/')

    def test_preference_referrer_url_false_gates_referrer_url(self):
        pb = _mock_param_builder(
            fbc='WITHFBC', referrer_url='https://builder.example.com/')
        pref = Preference(True, True, True, False, True)
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000072)
            event.set_request_context({}, pref)

        payload = event.normalize()
        self.assertEqual(payload['user_data']['fbc'], 'WITHFBC')
        self.assertIsNone(payload.get('referrer_url'))

    def test_preference_event_source_url_false_gates_event_source_url(self):
        pb = _mock_param_builder(
            fbc='WITHFBC', event_source_url='https://from-builder/')
        pref = Preference(True, True, True, True, False)
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='PageView', event_time=1700000062)
            event.set_request_context({}, pref)

        payload = event.normalize()
        self.assertEqual(payload['user_data']['fbc'], 'WITHFBC')
        self.assertIsNone(payload.get('event_source_url'))

    def test_normalize_output_is_stable_across_repeated_calls(self):
        pb = _mock_param_builder(fbc='IDEMPOTENT')
        with patch(PB_PATH, return_value=pb):
            event = Event(event_name='Lead', event_time=1700000050)
            event.set_request_context({})

            first = event.normalize()
            second = event.normalize()

        self.assertEqual(first, second)


class RealParamBuilderIntegrationTest(TestCase):
    """Guardrails against drift between the SDK and the upstream
    `capi-param-builder-python` package. These tests do NOT mock
    ParamBuilder — they import and call it for real, so they fail loudly
    if upstream renames or removes methods the SDK depends on.
    """

    def test_param_builder_exposes_methods_the_sdk_calls(self):
        from capi_param_builder import ParamBuilder
        pb = ParamBuilder()
        self.assertTrue(
            callable(getattr(pb, 'process_request_from_context', None)),
            'capi-param-builder-python must expose process_request_from_context; '
            'Event.set_request_context() calls it. Bump the pinned version '
            'in requirements.txt if the upstream API has shifted.',
        )
        self.assertTrue(callable(getattr(pb, 'get_fbc', None)))
        self.assertTrue(callable(getattr(pb, 'get_fbp', None)))
        self.assertTrue(callable(getattr(pb, 'get_event_source_url', None)))
        self.assertTrue(callable(getattr(pb, 'get_referrer_url', None)))

    def test_set_request_context_then_normalize_populates_fbp(self):
        # Real ParamBuilder, real request-shaped dict, no mocking.
        # The builder regenerates `fbp` from the cookie, so we assert the
        # output is a non-empty `fb.*` value rather than echoing the input.
        event = (
            Event(event_name='PageView', event_time=1700000000)
            .set_request_context({
                'headers': {
                    'host': 'shop.example.com',
                    'cookie': '_fbp=fb.1.1700000000000.987654321',
                },
                'url': '/',
            })
        )
        payload = event.normalize()
        fbp = payload.get('user_data', {}).get('fbp')
        self.assertIsNotNone(fbp, 'fbp should be auto-populated by ParamBuilder')
        self.assertTrue(fbp.startswith('fb.'),
                        'fbp should follow the fb.* shape, got: ' + repr(fbp))
