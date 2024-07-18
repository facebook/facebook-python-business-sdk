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

from facebook_business.adobjects.serverside.original_event_data import OriginalEventData


class OriginalEventDataTest(TestCase):
    def test_normalize(self):
        expected = {
            'event_name': 'event-name-1',
            'event_time': 123456,
        }
        original_event_data = OriginalEventData(
            event_name=expected['event_name'],
            event_time=expected['event_time'],
        )

        self.assertEqual(original_event_data.normalize(), expected)

    # original event data doesn't have mandatory fields, hence normalizing empty custom_data should return empty {}.
    def test_emptyobject_normalize(self):
        original_event_data = OriginalEventData()

        self.assertEqual(original_event_data.normalize(), {})
