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

from facebook_business.adobjects.serverside.util import Util

if Util.async_requests_available():

    from facebook_business.adobjects.serverside.batch_processor import BatchProcessor
    from facebook_business.adobjects.serverside.event import Event
    from facebook_business.adobjects.serverside.event_request_async import EventRequestAsync
    from facebook_business.adobjects.serverside.event_response import EventResponse

    from unittest import TestCase
    from unittest.mock import patch, AsyncMock, Mock

    import asyncio

    class BatchProcessorTests(TestCase):
        @patch('facebook_business.adobjects.serverside.batch_processor.BatchProcessor.process_event_requests_generator')
        def test_process_event_requests(self, mock_process_event_requests_generator):
            event_requests_async = self.get_event_requests_async(8)
            batch_processor = BatchProcessor(2, 3)
            batch_processor.process_event_requests(event_requests_async)

            mock_process_event_requests_generator.assert_called_with(event_requests_async)

        def test_process_event_requests_generator(self):
            async def async_test():
                event_requests_async = self.get_event_requests_async(8)
                batch_processor = BatchProcessor(2, 3)
                requests_generator = batch_processor.process_event_requests_generator(event_requests_async)
                expected_responses = [
                    [0, 1, 2],
                    [3, 4, 5],
                    [6, 7],
                ]
                actual_responses = []
                async for responses in requests_generator:
                    actual_responses.append(list(map(lambda response: response.fbtrace_id, responses)))

                self.assertEqual(actual_responses, expected_responses)
                for event_request_async in event_requests_async:
                    event_request_async.execute.assert_called()

            asyncio.run(async_test())

        @patch('facebook_business.adobjects.serverside.batch_processor.BatchProcessor.process_events_generator')
        def test_process_events(self, mock_process_events_generator):
            event_request_to_clone = EventRequestAsync('pixel123', events=[Mock(Event)])
            events = [Mock(Event)] * 7
            batch_processor = BatchProcessor(2, 3)
            requests_generator = batch_processor.process_events(event_request_to_clone, events)

            mock_process_events_generator.assert_called_with(event_request_to_clone, events)

        @patch('facebook_business.adobjects.serverside.event_request_async.EventRequestAsync.execute')
        def test_process_events_generator(self, execute_async_mock):
            async def async_test():
                self.num = 0
                self.events_set = []
                def request_counter():
                    num = self.num
                    self.num += 1
                    return num
                event_request_to_clone = EventRequestAsync('pixel123', events=[Mock(Event)])
                execute_async_mock.side_effect = request_counter
                events = [Mock(Event)] * 7
                batch_processor = BatchProcessor(2, 3)
                requests_generator = batch_processor.process_events_generator(event_request_to_clone, events)
                expected_responses = [
                    [0, 1, 2],
                    [3]
                ]
                actual_responses = []
                async for responses in requests_generator:
                    actual_responses.append(responses)

                self.assertEqual(actual_responses, expected_responses)

            asyncio.run(async_test())


        # Test helpers
        def get_event_requests_async(self, num):
            event_requests_async = []
            for i in range(num):
                response_mock = EventResponse(fbtrace_id=i)
                request_mock = AsyncMock(EventRequestAsync)
                request_mock.execute.return_value = response_mock
                event_requests_async.append(request_mock)

            return event_requests_async
