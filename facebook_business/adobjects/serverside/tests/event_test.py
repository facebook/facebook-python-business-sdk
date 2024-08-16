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
from facebook_business.adobjects.serverside.app_data import AppData
from facebook_business.adobjects.serverside.attribution_data import AttributionData
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.extended_device_info import ExtendedDeviceInfo
from facebook_business.adobjects.serverside.original_event_data import OriginalEventData
from facebook_business.adobjects.serverside.user_data import UserData


class EventTest(TestCase):
    def test_constructor(self):
        event_name = 'event_name-0'
        event_time = 123
        event_source_url = 'event_source_url-2'
        opt_out = False
        event_id = 'event_id-3'
        user_data = UserData(email='eg@test.com')
        custom_data = CustomData(order_id=123)
        attribution_data = AttributionData(scope='click', attribution_share=0.5)
        original_event_data = OriginalEventData(event_name='event-name-1', event_time=123456)
        ext_device_info = ExtendedDeviceInfo(
            ext_info_version = '1.2',
            app_package_name = 'bizSDK',
            short_version = '1.0',
            long_version = '1.0.1.2',
            os_version = '13.4.1',
            device_model_name = 'iPhone5,1',
            locale = 'En_US',
            timezone_abbreviation = 'SGT',
            carrier = 'Starhub',
            screen_width = 320,
            screen_height = 568,
            screen_density = '2',
            cpu_core_count = 2,
            total_disk_space_gb = 13,
            free_disk_space_gb = 8,
            device_time_zone = 'Singapore',
        )
        app_data = AppData(
            application_tracking_enabled = True,
            advertiser_tracking_enabled = True,
            campaign_ids = "100001,100002",
            consider_views = True,
            extinfo = ext_device_info,
            include_dwell_data = True,
            include_video_data = True,
            install_referrer = 'xyz',
            installer_package = 'abc',
            receipt_data = 'abc',
            url_schemes = 'myapp://',
            windows_attribution_id = 'aabbcc',
        )
        data_processing_options = ['4' '5']
        data_processing_options_country = 6
        data_processing_options_state = 7
        action_source = ActionSource.APP
        event = Event(
            event_name=event_name,
            event_time=event_time,
            event_source_url=event_source_url,
            opt_out=opt_out,
            event_id=event_id,
            user_data=user_data,
            custom_data=custom_data,
            data_processing_options=data_processing_options,
            data_processing_options_country=data_processing_options_country,
            data_processing_options_state=data_processing_options_state,
            action_source=action_source,
            app_data=app_data,
            original_event_data=original_event_data,
            attribution_data=attribution_data,
        )
        expected_params = {
            'event_name': event_name,
            'event_time': event_time,
            'event_source_url': event_source_url,
            'opt_out': opt_out,
            'event_id': event_id,
            'user_data': user_data.normalize(),
            'custom_data': custom_data.normalize(),
            'data_processing_options': data_processing_options,
            'data_processing_options_country': data_processing_options_country,
            'data_processing_options_state': data_processing_options_state,
            'action_source': action_source.value,
            'app_data': app_data.normalize(),
            'original_event_data': original_event_data.normalize(),
            'attribution_data': attribution_data.normalize(),
        }
        self.assertEqual(event.normalize(), expected_params)

    def test_action_source_validation(self):
        action_source = 'wrong type'
        expected_exception_message = 'action_source must be an ActionSource. TypeError on value: ' + action_source

        with self.assertRaises(TypeError) as context:
            Event(
                event_name='event-name',
                event_time=1,
                action_source=action_source,
            ).normalize()

        self.assertTrue(expected_exception_message in str(context.exception))
