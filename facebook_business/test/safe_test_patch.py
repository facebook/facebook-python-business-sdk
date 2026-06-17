import asyncio
import unittest
from unittest.mock import patch, AsyncMock, MagicMock

from facebook_business.utils.safe_serverside import SafeEventRequestAsync
from facebook_business.adobjects.serverside.event_response import EventResponse


class TestSafeEventRequestAsync(unittest.TestCase):
    """Tests for SafeEventRequestAsync's KeyError handling on fbtrace_id."""

    def _run(self, coro):
        """Helper to run async code in tests."""
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coro)
        finally:
            loop.close()

    @patch('facebook_business.adobjects.serverside.event_request_async.aiohttp.ClientSession')
    @patch.object(SafeEventRequestAsync, 'create_event', new_callable=AsyncMock)
    def test_normal_response_with_fbtrace_id(self, mock_create_event, mock_client_session):
        """When the API response includes fbtrace_id, it should work normally."""
        # create_event returns a raw dict (the JSON from Facebook's API)
        mock_create_event.return_value = {
            'events_received': 2,
            'messages': [],
            'fbtrace_id': 'AbCdEf123456',
        }

        # Mock ClientSession as an async context manager
        mock_session = AsyncMock()
        mock_client_session.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client_session.return_value.__aexit__ = AsyncMock(return_value=False)

        request = SafeEventRequestAsync(pixel_id='123456', events=[])
        result = self._run(request.execute())

        self.assertIsInstance(result, EventResponse)
        self.assertEqual(result.events_received, 2)
        self.assertEqual(result.fbtrace_id, 'AbCdEf123456')
        self.assertEqual(result.messages, [])
        print("PASS: Normal response with fbtrace_id works correctly.")

    @patch('facebook_business.adobjects.serverside.event_request_async.aiohttp.ClientSession')
    @patch.object(SafeEventRequestAsync, 'create_event', new_callable=AsyncMock)
    def test_response_missing_fbtrace_id(self, mock_create_event, mock_client_session):
        """When the API response is MISSING fbtrace_id, the original code throws
        KeyError. SafeEventRequestAsync should catch it and return a fallback."""
        # fbtrace_id is intentionally MISSING — this is the bug we're fixing
        mock_create_event.return_value = {
            'events_received': 1,
            'messages': ['some message'],
        }

        mock_session = AsyncMock()
        mock_client_session.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client_session.return_value.__aexit__ = AsyncMock(return_value=False)

        request = SafeEventRequestAsync(pixel_id='123456', events=[])
        result = self._run(request.execute())

        # Should NOT crash — SafeEventRequestAsync handles the KeyError
        self.assertIsInstance(result, EventResponse)
        self.assertEqual(result.events_received, 1)
        self.assertEqual(result.fbtrace_id, 'SAFE-FALLBACK')
        self.assertIn('fbtrace_id missing', result.messages[0])
        print("PASS: Missing fbtrace_id handled gracefully (no KeyError).")

    @patch('facebook_business.adobjects.serverside.event_request_async.aiohttp.ClientSession')
    @patch.object(SafeEventRequestAsync, 'create_event', new_callable=AsyncMock)
    def test_other_key_error_still_raises(self, mock_create_event, mock_client_session):
        """A KeyError for something OTHER than fbtrace_id should still propagate."""
        # Response missing 'messages' — will cause a KeyError('messages'), not fbtrace_id
        mock_create_event.return_value = {
            'events_received': 1,
            'fbtrace_id': 'trace123',
            # 'messages' is missing
        }

        mock_session = AsyncMock()
        mock_client_session.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client_session.return_value.__aexit__ = AsyncMock(return_value=False)

        request = SafeEventRequestAsync(pixel_id='123456', events=[])

        with self.assertRaises(KeyError):
            self._run(request.execute())
        print("PASS: Non-fbtrace_id KeyError still raises as expected.")

    @patch('facebook_business.adobjects.serverside.event_request_async.aiohttp.ClientSession')
    @patch.object(SafeEventRequestAsync, 'create_event', new_callable=AsyncMock)
    def test_zero_events_missing_fbtrace_id(self, mock_create_event, mock_client_session):
        """Even the else-branch (events_received=0) hits fbtrace_id. Verify fix."""
        mock_create_event.return_value = {
            'events_received': 0,
            'messages': ['error'],
            # fbtrace_id missing
        }

        mock_session = AsyncMock()
        mock_client_session.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client_session.return_value.__aexit__ = AsyncMock(return_value=False)

        request = SafeEventRequestAsync(pixel_id='123456', events=[])
        result = self._run(request.execute())

        self.assertIsInstance(result, EventResponse)
        self.assertEqual(result.fbtrace_id, 'SAFE-FALLBACK')
        print("PASS: Zero events + missing fbtrace_id handled gracefully.")


if __name__ == '__main__':
    unittest.main()
