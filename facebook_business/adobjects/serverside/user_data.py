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

import hashlib
import pprint

import six
from facebook_business.adobjects.serverside.gender import Gender
from facebook_business.adobjects.serverside.normalize import Normalize


class UserData(object):
    param_types = {
        'email': 'str',
        'phone': 'str',
        'gender': 'Gender',
        'date_of_birth': 'str',
        'last_name': 'str',
        'first_name': 'str',
        'city': 'str',
        'state': 'str',
        'country_code': 'str',
        'zip_code': 'str',
        'external_id': 'str',
        'client_ip_address': 'str',
        'client_user_agent': 'str',
        'fbc': 'str',
        'fbp': 'str',
        'subscription_id': 'str'
    }

    def __init__(self, email: str = None, phone: str = None, gender: Gender = None, date_of_birth: str = None,
                 last_name: str = None, first_name: str = None, city: str = None, state: str = None,
                 country_code: str = None, zip_code: str = None, external_id: str = None, client_ip_address: str = None,
                 client_user_agent: str = None, fbc: str = None, fbp: str = None, subscription_id: str = None):
        """UserData is a set of identifiers Facebook can use for targeted attribution"""
        self._email = None
        self._phone = None
        self._gender = None
        self._date_of_birth = None
        self._last_name = None
        self._first_name = None
        self._city = None
        self._state = None
        self._country_code = None
        self._zip_code = None
        self._external_id = None
        self._client_ip_address = None
        self._client_user_agent = None
        self._fbc = None
        self._fbp = None
        self._subscription_id = None
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if gender is not None:
            self.gender = gender
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if last_name is not None:
            self.last_name = last_name
        if first_name is not None:
            self.first_name = first_name
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country_code is not None:
            self.country_code = country_code
        if zip_code is not None:
            self.zip_code = zip_code
        if external_id is not None:
            self.external_id = external_id
        if client_ip_address is not None:
            self.client_ip_address = client_ip_address
        if client_user_agent is not None:
            self.client_user_agent = client_user_agent
        if fbc is not None:
            self.fbc = fbc
        if fbp is not None:
            self.fbp = fbp
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def email(self):
        """Gets the email.

        An email address, in lowercase.

        :return: The email.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email.

        An email address, in lowercase.

        :param email: The email.
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone.

        A phoneone number. Include only digits with country code, area code, and number.

        :return: The phone.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone.

        A phone number. Include only digits with country code, area code, and number.

        :param phone: The phone.
        :type: str
        """

        self._phone = phone

    @property
    def gender(self):
        """Gets the gender.

        Gender, in lowercase. Either f or m.

        :return: The gender.
        :rtype: Gender
        """
        return self._gender

    @gender.setter
    def gender(self, gender: Gender):
        """Sets the gender.

        Gender, in lowercase. Either f or m.

        :param gender: The gender.
        :type: Gender
        """
        if not isinstance(gender, Gender):
            raise TypeError('UserData.gender must be of type Gender')

        self._gender = gender

    @property
    def date_of_birth(self):
        """Gets the date of birth.

        A date of birth given as YYYYMMDD.


        :return: The date of birth.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str):
        """Sets the date of birth.

        A date of birth given as YYYYMMDD.

        :param date_of_birth: The date of birth.
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def last_name(self):
        """Gets the last_name.

        A last name in lowercase.

        :return: The last name.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last name.

        A last name in lowercase.

        :param last_name: The last name.
        :type: str
        """

        self._last_name = last_name

    @property
    def first_name(self):
        """Gets the first name.

        A first name in lowercase.

        :return: The first name.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first name.

        A first name in lowercase.

        :param first_name: The first name.
        :type: str
        """

        self._first_name = first_name

    @property
    def city(self):
        """Gets the city.

        A city in lower-case without spaces or punctuation.

        :return: The city.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city.

        A city in lower-case without spaces or punctuation.

        :param city: The city.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state.

        A two-letter state code in lowercase.

        :return: The state.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state.

        A two-letter state code in lowercase.

        :param state: The state.
        :type: str
        """

        self._state = state

    @property
    def country_code(self):
        """Gets the country code.

         A two-letter country code in lowercase

        :return: The country code.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """Sets a two-letter country code in lowercase.

        :param country_code: The country code
        :type: str
        """

        self._country_code = country_code

    @property
    def zip_code(self):
        """Gets the zipcode.

        TFor the United States, this is a five-digit zip code.
        For other locations, follow each country's standards.

        :return: The zipcode.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code: str):
        """Sets the zipcode.

        For the United States, this is a five-digit zip code.
        For other locations, follow each country's standards.

        :param zip_code: The zipcode.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def external_id(self):
        """Gets the external id.

        Any unique ID from the advertiser, such as loyalty membership IDs, user IDs, and external cookie IDs.
        In the Offline Conversions API (https://www.facebook.com/business/help/104039186799009),
        this is known as extern_id. For more information, see Offline Conversions, Providing External IDs. If
        External ID is being sent via other channels, then it should be sent in the same format via the server-side API.

        :return: The external id.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id: str):
        """Sets the external id.

        Any unique ID from the advertiser, such as loyalty membership IDs, user IDs, and external cookie IDs.
        In the Offline Conversions API (https://www.facebook.com/business/help/104039186799009),
        this is known as extern_id. For more information, see Offline Conversions, Providing External IDs. If
        External ID is being sent via other channels, then it should be sent in the same format via the server-side API.

        :param external_id: The external id.
        :type: str
        """

        self._external_id = external_id

    @property
    def client_ip_address(self):
        """Gets the client ip address.

        The IP address of the browser corresponding to the event.

        :return: The client ip address.
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address: str):
        """Sets the client ip address.

        The IP address of the browser corresponding to the event.

        :param client_ip_address: The client ip address.
        :type: str
        """

        self._client_ip_address = client_ip_address

    @property
    def client_user_agent(self):
        """Gets the client user agent.

        The user agent for the browser corresponding to the event.

        :return: The client user agent.
        :rtype: str
        """
        return self._client_user_agent

    @client_user_agent.setter
    def client_user_agent(self, client_user_agent: str):
        """Sets the client user agent.

        The user agent for the browser corresponding to the event.

        :param client_user_agent: The client user agent.
        :type: str
        """

        self._client_user_agent = client_user_agent

    @property
    def fbc(self):
        """Gets the fbc.

        The Facebook click ID value stored in the _fbc browser cookie under your domain.
        See Managing fbc and fbp Parameters for how to get this value
        (https://developers.facebook.com/docs/marketing-api/facebook-pixel/server-side-api/parameters#fbc),
        or generate this value from a fbclid query parameter.

        :return: The fbc.
        :rtype: str
        """
        return self._fbc

    @fbc.setter
    def fbc(self, fbc: str):
        """Sets the fbc.

        The Facebook click ID value stored in the _fbc browser cookie under your domain.
        See Managing fbc and fbp Parameters for how to get this value
        (https://developers.facebook.com/docs/marketing-api/facebook-pixel/server-side-api/parameters#fbc),
        or generate this value from a fbclid query parameter.

        :param fbc: The fbc.
        :type: str
        """

        self._fbc = fbc

    @property
    def fbp(self):
        """Gets the fbp.

        The Facebook browser ID value stored in the _fbp browser cookie under your domain.
        See Managing fbc and fbp Parameters for how to get this value
        (https://developers.facebook.com/docs/marketing-api/facebook-pixel/server-side-api/parameters#fbc),
        or generate this value from a fbclid query parameter.

        :return: The fbp.
        :rtype: str
        """
        return self._fbp

    @fbp.setter
    def fbp(self, fbp: str):
        """Sets the fbp.

        The Facebook browser ID value stored in the _fbp browser cookie under your domain.
        See Managing fbc and fbp Parameters for how to get this value
        (https://developers.facebook.com/docs/marketing-api/facebook-pixel/server-side-api/parameters#fbc),
        or generate this value from a fbclid query parameter.

        :param fbp: The fbp.
        :type: str
        """

        self._fbp = fbp

    @property
    def subscription_id(self):
        """Gets the subscription id.

        The subscription ID for the user in this transaction. This is similar to the order ID for an individual product.

        :return: The subscription id.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id: str):
        """Sets the subscription id.

        The subscription ID for the user in this transaction. This is similar to the order ID for an individual product.

        :param subscription_id: The subscription id.
        :type: str
        """

        self._subscription_id = subscription_id

    def normalize(self):
        normalized_payload = {'em': self.hash_sha_256(Normalize.normalize_field('em', self.email)),
                              'ph': self.hash_sha_256(Normalize.normalize_field('ph', self.phone)),
                              'db': self.hash_sha_256(Normalize.normalize_field('db', self.date_of_birth)),
                              'ln': self.hash_sha_256(Normalize.normalize_field('ln', self.last_name)),
                              'fn': self.hash_sha_256(Normalize.normalize_field('fn', self.first_name)),
                              'ct': self.hash_sha_256(Normalize.normalize_field('ct', self.city)),
                              'st': self.hash_sha_256(Normalize.normalize_field('st', self.state)),
                              'zp': self.hash_sha_256(Normalize.normalize_field('zp', self.zip_code)),
                              'country': self.hash_sha_256(Normalize.normalize_field('country', self.country_code)),
                              'external_id': self.external_id,
                              'client_ip_address': self.client_ip_address,
                              'client_user_agent': self.client_user_agent,
                              'fbc': self.fbc,
                              'fbp': self.fbp,
                              'subscription_id': self.subscription_id,
                              }
        if self.gender is not None:
            normalized_payload['ge'] = self.hash_sha_256(Normalize.normalize_field('ge', self.gender.value))

        normalized_payload: dict = {k: v for k, v in normalized_payload.items() if v is not None}
        return normalized_payload

    def hash_sha_256(self, input):
        if input is None:
            return None
        input = input.encode('utf-8')
        return hashlib.sha256(input).hexdigest()

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
        if issubclass(UserData, dict):
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
        if not isinstance(other, UserData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
