# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import pprint
import six


class Preference(object):
    """Preference is an allowlist to specify what data are allowed to be
    automatically set on the CAPI event from the request context object.
    All fields default to true.
    """

    param_types = {
        'is_fbc_allowed': 'bool',
        'is_fbp_allowed': 'bool',
        'is_client_ip_address_allowed': 'bool',
        'is_referrer_url_allowed': 'bool',
        'is_event_source_url_allowed': 'bool',
    }

    def __init__(self, is_fbc_allowed=True, is_fbp_allowed=True,
                 is_client_ip_address_allowed=True, is_referrer_url_allowed=True,
                 is_event_source_url_allowed=True):
        # type: (bool, bool, bool, bool, bool) -> None

        self._is_fbc_allowed = True
        self._is_fbp_allowed = True
        self._is_client_ip_address_allowed = True
        self._is_referrer_url_allowed = True
        self._is_event_source_url_allowed = True
        self.is_fbc_allowed = is_fbc_allowed
        self.is_fbp_allowed = is_fbp_allowed
        self.is_client_ip_address_allowed = is_client_ip_address_allowed
        self.is_referrer_url_allowed = is_referrer_url_allowed
        self.is_event_source_url_allowed = is_event_source_url_allowed

    @property
    def is_fbc_allowed(self):
        """Gets whether fbc is allowed to be set from the request context.

        :return: Whether fbc is allowed.
        :rtype: bool
        """
        return self._is_fbc_allowed

    @is_fbc_allowed.setter
    def is_fbc_allowed(self, is_fbc_allowed):
        """Sets whether fbc is allowed to be set from the request context.

        :param is_fbc_allowed: Whether fbc is allowed.
        :type: bool
        """
        if not isinstance(is_fbc_allowed, bool):
            raise TypeError('Preference.is_fbc_allowed must be a bool')
        self._is_fbc_allowed = is_fbc_allowed

    @property
    def is_fbp_allowed(self):
        """Gets whether fbp is allowed to be set from the request context.

        :return: Whether fbp is allowed.
        :rtype: bool
        """
        return self._is_fbp_allowed

    @is_fbp_allowed.setter
    def is_fbp_allowed(self, is_fbp_allowed):
        """Sets whether fbp is allowed to be set from the request context.

        :param is_fbp_allowed: Whether fbp is allowed.
        :type: bool
        """
        if not isinstance(is_fbp_allowed, bool):
            raise TypeError('Preference.is_fbp_allowed must be a bool')
        self._is_fbp_allowed = is_fbp_allowed

    @property
    def is_client_ip_address_allowed(self):
        """Gets whether client_ip_address is allowed to be set from the request context.

        :return: Whether client_ip_address is allowed.
        :rtype: bool
        """
        return self._is_client_ip_address_allowed

    @is_client_ip_address_allowed.setter
    def is_client_ip_address_allowed(self, is_client_ip_address_allowed):
        """Sets whether client_ip_address is allowed to be set from the request context.

        :param is_client_ip_address_allowed: Whether client_ip_address is allowed.
        :type: bool
        """
        if not isinstance(is_client_ip_address_allowed, bool):
            raise TypeError('Preference.is_client_ip_address_allowed must be a bool')
        self._is_client_ip_address_allowed = is_client_ip_address_allowed

    @property
    def is_referrer_url_allowed(self):
        """Gets whether referrer_url is allowed to be set from the request context.

        :return: Whether referrer_url is allowed.
        :rtype: bool
        """
        return self._is_referrer_url_allowed

    @is_referrer_url_allowed.setter
    def is_referrer_url_allowed(self, is_referrer_url_allowed):
        """Sets whether referrer_url is allowed to be set from the request context.

        :param is_referrer_url_allowed: Whether referrer_url is allowed.
        :type: bool
        """
        if not isinstance(is_referrer_url_allowed, bool):
            raise TypeError('Preference.is_referrer_url_allowed must be a bool')
        self._is_referrer_url_allowed = is_referrer_url_allowed

    @property
    def is_event_source_url_allowed(self):
        """Gets whether event_source_url is allowed to be set from the request context.

        :return: Whether event_source_url is allowed.
        :rtype: bool
        """
        return self._is_event_source_url_allowed

    @is_event_source_url_allowed.setter
    def is_event_source_url_allowed(self, is_event_source_url_allowed):
        """Sets whether event_source_url is allowed to be set from the request context.

        :param is_event_source_url_allowed: Whether event_source_url is allowed.
        :type: bool
        """
        if not isinstance(is_event_source_url_allowed, bool):
            raise TypeError('Preference.is_event_source_url_allowed must be a bool')
        self._is_event_source_url_allowed = is_event_source_url_allowed

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
        if issubclass(Preference, dict):
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
        if not isinstance(other, Preference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
