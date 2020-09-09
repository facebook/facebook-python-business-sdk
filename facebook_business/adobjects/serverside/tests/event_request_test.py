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

import json
import time
from unittest import TestCase
from unittest.mock import patch

from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.event_response import EventResponse


class EventRequestTest(TestCase):
    @patch('facebook_business.adobjects.serverside.event_request.AdsPixel')
    def test_constructor(self, pixel_mock):
        event = Event(event_name='Purchase', event_time=int(time.time()))
        expected_event = json.dumps(
            {'event_name': event.event_name, 'event_time': event.event_time}
        )
        pixel_id = 'pixel123'
        expected_data = {
            'data': [expected_event],
            'test_event_code': 'test-code-1',
            'namespace_id': '222',
            'upload_id': '333',
            'upload_tag': 'upload-tag4',
            'upload_source': 'upload-source5',
        }
        event_request = EventRequest(
            pixel_id=pixel_id,
            events=[event],
            test_event_code=expected_data['test_event_code'],
            namespace_id=expected_data['namespace_id'],
            upload_id=expected_data['upload_id'],
            upload_tag=expected_data['upload_tag'],
            upload_source=expected_data['upload_source'],
        )
        ads_pixel = {
            'events_received': 2,
            'fbtrace_id': 'traceid1',
            'messages': ['1', '2'],
        }
        expected_event_response = EventResponse(
            events_received=2, fbtrace_id='traceid1', messages=['1', '2']
        )
        pixel_instance_mock = pixel_mock.return_value
        pixel_instance_mock.create_event.return_value = ads_pixel
        actual_event_response = event_request.execute()

        pixel_mock.assert_called_with(pixel_id)
        pixel_instance_mock.create_event.assert_called_with(
            fields=[], params=expected_data
        )
        self.assertEqual(actual_event_response, expected_event_response)
