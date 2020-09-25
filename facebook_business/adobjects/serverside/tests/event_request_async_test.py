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
    import json
    import time
    from unittest import TestCase

    from facebook_business.adobjects.serverside.event import Event
    from facebook_business.adobjects.serverside.event_request_async import EventRequestAsync


    class EventRequestAsyncTest(TestCase):
        def test_get_params(self):
            event = Event(event_name='Purchase', event_time=int(time.time()))
            pixel_id = 'pixel123'
            expected = {
                'test_event_code': 'test-code-1',
                'namespace_id': '222',
                'upload_id': '333',
                'upload_tag': 'upload-tag4',
                'upload_source': 'upload-source5',
                'partner_agent': 'partner-agent-6',
                'data': json.dumps([event.normalize()]),
            }
            event_request_async = EventRequestAsync(
                pixel_id=pixel_id,
                events=[event],
                test_event_code=expected['test_event_code'],
                namespace_id=expected['namespace_id'],
                upload_id=expected['upload_id'],
                upload_tag=expected['upload_tag'],
                upload_source=expected['upload_source'],
                partner_agent=expected['partner_agent'],
            )

            self.assertEqual(event_request_async.get_params(), expected)
            self.assertEqual(event_request_async.pixel_id, pixel_id)

        def test_clone_without_events(self):
            event_request_async = EventRequestAsync(
                pixel_id='pixel123',
                events=[Event(event_name='Purchase', event_time=int(time.time()))],
                test_event_code='test-code-1',
                namespace_id='222',
                upload_id='333',
                upload_tag='upload-tag4',
                upload_source='upload-source5',
            )
            expected_event_request_async = EventRequestAsync(
                pixel_id=event_request_async.pixel_id,
                events=[],
                test_event_code=event_request_async.test_event_code,
                namespace_id=event_request_async.namespace_id,
                upload_id=event_request_async.upload_id,
                upload_tag=event_request_async.upload_tag,
                upload_source=event_request_async.upload_source,
            )
            event_request_async_cloned = event_request_async.clone_without_events()

            self.assertEqual(event_request_async_cloned, expected_event_request_async)
