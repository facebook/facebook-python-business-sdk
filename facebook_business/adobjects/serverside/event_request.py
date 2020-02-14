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
import pprint
from typing import List

import six
from facebook_business.adobjects.adspixel import AdsPixel
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_response import EventResponse


class EventRequest(object):
    """
    Server-Side Event Request.
    """
    param_types = {
        'events': 'list[Event]',
        'test_event_code': 'str'
    }

    def __init__(self, pixel_id: str = None, events: List[Event] = None, test_event_code: str = None):
        self._events = None
        self._test_event_code = None
        self.__pixel_id = None
        if pixel_id is None:
            raise ValueError("Invalid value for `pixel_id`, must not be `None`")
        self.__pixel_id = pixel_id
        self.events = events
        if test_event_code is not None:
            self.test_event_code = test_event_code

    @property
    def events(self):
        """Gets the events.

        An array of Server Event objects

        :return: The events.
        :rtype: list[Event]
        """
        return self._events

    @events.setter
    def events(self, events: List[Event]):
        """Sets the events.

        An array of Server Event objects

        :param events: The events.
        :type: list[Event]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")

        self._events = events

    @property
    def test_event_code(self):
        """Gets the test_event_code.

        Code used to verify that your server events are received correctly by Facebook.
        Use this code to test your server events in the Test Events feature in Events Manager.
        See Test Events Tool (https://developers.facebook.com/docs/marketing-api/facebook-pixel/server-side-api/using-the-api#testEvents) for an example.

        :return: The test_event_code.
        :rtype: str
        """
        return self._test_event_code

    @test_event_code.setter
    def test_event_code(self, test_event_code: str):
        """Sets the test_event_code.

        Code used to verify that your server events are received correctly by Facebook.
        Use this code to test your server events in the Test Events feature in Events Manager.
        See Test Events Tool (https://developers.facebook.com/docs/marketing-api/facebook-pixel/server-side-api/using-the-api#testEvents) for an example.

        :param test_event_code: The test_event_code.
        :type: str
        """

        self._test_event_code = test_event_code

    def execute(self):

        params = {"data": self.normalize()}

        if self.test_event_code is not None:
            params['test_event_code'] = self.test_event_code

        response = AdsPixel(self.__pixel_id).create_event(
            fields=[],
            params=params,
        )
        event_response = EventResponse(events_received=response['events_received'],
                                       fbtrace_id=response['fbtrace_id'],
                                       messages=response['messages'])
        return event_response

    def normalize(self):
        normalized_events = []
        for event in self.events:
            normalized_event = event.normalize()
            normalized_events.append(json.dumps(normalized_event))

        return normalized_events

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.param_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EventRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
