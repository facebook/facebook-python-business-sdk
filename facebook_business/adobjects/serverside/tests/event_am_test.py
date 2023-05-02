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

from facebook_business import FacebookAdsApi
from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.user_data import UserData


class EventAmTest(TestCase):
    def test_constructor(self):
        event_name = 'custom'
        event_time = 123
        user_data = UserData(email='eg@test.com')
        custom_data = CustomData(custom_properties={'col_1': 'foo'})
        data_processing_options = ['AMO']
        advanced_measurement_table = 'test_am_table'
        event = Event(
            event_name=event_name,
            event_time=event_time,
            user_data=user_data,
            custom_data=custom_data,
            data_processing_options=data_processing_options,
            action_source=None,
            advanced_measurement_table=advanced_measurement_table
        )
        expected_params = {
            'event_name': event_name,
            'event_time': event_time,
            'user_data': user_data.normalize(),
            'custom_data': custom_data.normalize(),
            'data_processing_options': data_processing_options,
            'advanced_measurement_table': advanced_measurement_table
        }

        self.assertEqual(event.normalize(), expected_params)
