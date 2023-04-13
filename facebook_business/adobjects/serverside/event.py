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

import pprint
import six

from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.user_data import UserData


class Event(object):
    param_types = {
        'event_name': 'str',
        'event_time': 'int',
        'event_source_url': 'str',
        'opt_out': 'bool',
        'event_id': 'str',
        'user_data': 'UserData',
        'custom_data': 'CustomData',
        'data_processing_options': 'list[str]',
        'data_processing_options_country': 'int',
        'data_processing_options_state': 'int',
        'action_source': 'ActionSource',
    }

    def __init__(self, event_name = None, event_time = None, event_source_url = None,
                 opt_out = None, event_id = None, user_data = None, custom_data = None,
                 data_processing_options = None, data_processing_options_country = None,
                 data_processing_options_state = None, action_source = None):
        # type: (str, int, str, bool, str, UserData, CustomData, list[str], int, int, ActionSource) -> None

        """Conversions API Event"""
        self._event_name = None
        self._event_time = None
        self._event_source_url = None
        self._opt_out = None
        self._event_id = None
        self._user_data = None
        self._custom_data = None
        self._data_processing_options = None
        self._data_processing_options_country = None
        self._data_processing_options_state = None
        self._action_source = None
        self.event_name = event_name
        self.event_time = event_time
        if event_source_url is not None:
            self.event_source_url = event_source_url
        if opt_out is not None:
            self.opt_out = opt_out
        if event_id is not None:
            self.event_id = event_id
        if user_data is not None:
            self.user_data = user_data
        if custom_data is not None:
            self.custom_data = custom_data
        if data_processing_options is not None:
            self.data_processing_options = data_processing_options
        if data_processing_options_country is not None:
            self.data_processing_options_country = data_processing_options_country
        if data_processing_options_state is not None:
            self.data_processing_options_state = data_processing_options_state
        if action_source is not None:
            self.action_source = action_source

    @property
    def event_name(self):
        """Gets the event_name of this Event.

        A Facebook pixel Standard Event or Custom Event name.

        :return: The event_name of this Event.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this Event.

        A Facebook pixel Standard Event or Custom Event name.

        :param event_name: The event_name of this Event.
        :type: str
        :return self
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")

        self._event_name = event_name

    @property
    def event_time(self):
        """Gets the event_time of this Event.

        A Unix timestamp in seconds indicating when the actual event occurred.

        :return: The event_time of this Event.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this Event.

        A Unix timestamp in seconds indicating when the actual event occurred.

        :param event_time: The event_time of this Event.
        :type: int
        """
        if event_time is None:
            raise ValueError("Invalid value for `event_time`, must not be `None`")

        if not isinstance(event_time, int):
            raise TypeError('Event.event_time must be an int')

        self._event_time = event_time

    @property
    def event_source_url(self):
        """Gets the event_source_url of this Event.

        The browser URL where the event happened.

        :return: The event_source_url of this Event.
        :rtype: str
        """
        return self._event_source_url

    @event_source_url.setter
    def event_source_url(self, event_source_url):
        """Sets the event_source_url of this Event.

        The browser URL where the event happened.

        :param event_source_url: The event_source_url of this Event.
        :type: str
        """

        self._event_source_url = event_source_url

    @property
    def opt_out(self):
        """Gets the opt_out of this Event.

        A flag that indicates we should not use this event for ads delivery optimization.
        If set to true, we only use the event for attribution.

        :return: The opt_out of this Event.
        :rtype: bool
        """
        return self._opt_out

    @opt_out.setter
    def opt_out(self, opt_out):
        """Sets the opt_out of this Event.

        A flag that indicates we should not use this event for ads delivery optimization.
        If set to true, we only use the event for attribution.

        :param opt_out: The opt_out of this Event.
        :type: bool
        """

        if not isinstance(opt_out, bool):
            raise TypeError('Event.opt_out must be a bool')
        self._opt_out = opt_out

    @property
    def event_id(self):
        """Gets the event_id of this Event.

        This ID can be any string chosen by the advertiser.
        This is used with event_name to determine if events sent from
        both server and browser are identical.

        :return: The event_id of this Event.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Event.

        This ID can be any string chosen by the advertiser.
        This is used with event_name to determine if events sent from
        both server and browser are identical.

        :param event_id: The event_id of this Event.
        :type: str
        """

        self._event_id = event_id

    @property
    def user_data(self):
        """Gets the user_data of this Event.


        :return: The user_data of this Event.
        :rtype: UserData
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this Event.


        :param user_data: The user_data of this Event.
        :type: UserData
        """
        if user_data is None:
            raise ValueError("Invalid value for `user_data`, must not be `None`")

        if not isinstance(user_data, UserData):
            raise TypeError('Event.user_Data must be of type UserData')

        self._user_data = user_data

    @property
    def custom_data(self):
        """Gets the custom_data of this Event.


        :return: The custom_data of this Event.
        :rtype: CustomData
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data):
        """Sets the custom_data of this Event.


        :param custom_data: The custom_data of this Event.
        :type: CustomData
        """

        if not isinstance(custom_data, CustomData):
            raise TypeError('Event.custom_data must be of type CustomData')

        self._custom_data = custom_data

    @property
    def data_processing_options(self):
        """Gets the data_processing_options of this Event.

        :return: The data_processing_options of this Event.
        :rtype: list[str]
        """
        return self._data_processing_options

    @data_processing_options.setter
    def data_processing_options(self, data_processing_options):
        """Sets the data_processing_options of this Event.
        Processing options you would like to enable for a specific event.
        For more details see https://developers.facebook.com/docs/marketing-apis/data-processing-options

        :param data_processing_options: The data_processing_options of this Event.
        :type: list[str]
        """

        self._data_processing_options = data_processing_options

    @property
    def data_processing_options_country(self):
        """Gets the data_processing_options_country of this Event.

        :return: The data_processing_options_country of this Event.
        :rtype: int
        """
        return self._data_processing_options_country

    @data_processing_options_country.setter
    def data_processing_options_country(self, data_processing_options_country):
        """Sets the data_processing_options_country of this Event.
        A country that you want to associate to this data processing option.
        For more details: https://developers.intern.facebook.com/docs/marketing-apis/data-processing-options

        :param data_processing_options_country: The data_processing_options_country of this Event.
        :type: int
        """

        if not isinstance(data_processing_options_country, int):
            raise TypeError('Event.data_processing_options_country must be an int')

        self._data_processing_options_country = data_processing_options_country

    @property
    def data_processing_options_state(self):
        """Gets the data_processing_options_state of this Event.

        :return: The data_processing_options_state of this Event.
        :rtype: int
        """
        return self._data_processing_options_state

    @data_processing_options_state.setter
    def data_processing_options_state(self, data_processing_options_state):
        """Sets the data_processing_options_state of this Event.
        A state that you want to associate with this data processing option.
        For more details: https://developers.facebook.com/docs/marketing-apis/data-processing-options

        :param data_processing_options: The data_processing_options of this Event.
        :type: int
        """

        self._data_processing_options_state = data_processing_options_state

    @property
    def action_source(self):
        """Gets the action_source.

        Allows you to specify where the conversion occurred.

        :return: The action_source.
        :rtype: ActionSource
        """
        return self._action_source

    @action_source.setter
    def action_source(self, action_source):
        """Sets the action_source.

        Allows you to specify where the conversion occurred.

        :param action_source: The action_source.
        :type: ActionSource
        """

        self._action_source = action_source

    def normalize(self):
        normalized_payload = {'event_name': self.event_name, 'event_time': self.event_time,
                              'event_source_url': self.event_source_url, 'opt_out': self.opt_out,
                              'event_id': self.event_id, 'data_processing_options': self.data_processing_options,
                              'data_processing_options_country' : self.data_processing_options_country,
                              'data_processing_options_state': self.data_processing_options_state }

        if self.user_data is not None:
            normalized_payload['user_data'] = self.user_data.normalize()

        if self.custom_data is not None:
            normalized_payload['custom_data'] = self.custom_data.normalize()

        if self.action_source is not None:
            self.validate_action_source(self.action_source)
            normalized_payload['action_source'] = self.action_source.value

        normalized_payload = {k: v for k, v in normalized_payload.items() if v is not None}
        return normalized_payload

    def validate_action_source(self, action_source):
        if not type(action_source) == ActionSource:
            raise TypeError(
                'action_source must be an ActionSource. TypeError on value: %s' % action_source
            )

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
