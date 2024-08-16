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

from facebook_business.adobjects.serverside.attribution_model import AttributionModel

class AttributionData(object):
    param_types = {
        'scope': 'str',
        'visit_time': 'int',
        'ad_id': 'str',
        'adset_id': 'str',
        'campaign_id': 'str',
        'attribution_share': 'float',
        'attribution_model': 'AttributionModel',
        'attr_window': 'int',
    }

    def __init__(self, scope = None, visit_time = None, ad_id = None, adset_id = None, campaign_id = None, attribution_share = None, attribution_model = None, attr_window = None):
        # type: (str, int) -> None

        """Conversions API Attribution Data"""
        self._scope = None
        self._visit_time = None
        self._ad_id = None
        self._adset_id = None
        self._campaign_id = None
        self._attribution_share = None
        self._attribution_model = None
        self._attr_window = None

        if scope is not None:
            self.scope = scope
        if visit_time is not None:
            self.visit_time = visit_time
        if ad_id is not None:
            self.ad_id = ad_id
        if adset_id is not None:
            self.adset_id = adset_id
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if attribution_share is not None:
            self.attribution_share = attribution_share
        if attribution_model is not None:
            self.attribution_model = attribution_model
        if attr_window is not None:
            self.attr_window = attr_window

    @property
    def scope(self):
        """Gets the scope of Attribution Data.

        Touchpoint type.

        :return: The scope of Attribution Data.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of Attribution Data.

        Touchpoint type.

        :param scope: The scope of Attribution Data.
        :type: str
        """
        self._scope = scope

    @property
    def visit_time(self):
        """Gets the visit_time of Attribution Data.

        A Unix timestamp in seconds indicating time that the campaign_id or fbc was first received.

        :return: The visit_time of Attribution Data.
        :rtype: int
        """
        return self._visit_time

    @visit_time.setter
    def visit_time(self, visit_time):
        """Sets the visit_time of Attribution Data.

        A Unix timestamp in seconds indicating time that the campaign_id or fbc was first received.

        :param visit_time: The visit_time of Attribution Data.
        :type: int
        """
        if not isinstance(visit_time, int):
            raise TypeError('AttributionData.visit_time must be an int')

        self._visit_time = visit_time
        
    @property
    def ad_id(self):
        """Gets the ad_id of Attribution Data.

        Meta-provided ad id from URL/deeplink.

        :return: The ad_id of Attribution Data.
        :rtype: str
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of Attribution Data.

        Meta-provided ad id from URL/deeplink.

        :param ad_id: The ad_id of Attribution Data.
        :type: str
        """
        self._ad_id = ad_id
    
    @property
    def adset_id(self):
        """Gets the adset_id of Attribution Data.

        Meta-provided adset id from URL/deeplink.

        :return: The adset_id of Attribution Data.
        :rtype: str
        """
        return self._adset_id

    @adset_id.setter
    def adset_id(self, adset_id):
        """Sets the adset_id of Attribution Data.

        Meta-provided adset id from URL/deeplink.

        :param adset_id: The adset_id of Attribution Data.
        :type: str
        """
        self._adset_id = adset_id
    
    @property
    def campaign_id(self):
        """Gets the campaign_id of Attribution Data.

        Meta-provided campaign id from URL/deeplink.

        :return: The campaign_id of Attribution Data.
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of Attribution Data.

        Meta-provided campaign id from URL/deeplink.

        :param campaign_id: The campaign_id of Attribution Data.
        :type: str
        """
        self._campaign_id = campaign_id
    
    @property
    def attribution_share(self):
        """Gets the attribution_share of Attribution Data.

        [0-1] weight of credit assigned to the visit.

        :return: The attribution_share of Attribution Data.
        :rtype: float
        """
        return self._attribution_share

    @attribution_share.setter
    def attribution_share(self, attribution_share):
        """Sets the attribution_share of Attribution Data.

        [0-1] weight of credit assigned to the visit.

        :param attribution_share: The attribution_share of Attribution Data.
        :type: float
        """
        self._attribution_share = attribution_share

    @property
    def attribution_model(self):
        """Gets the attribution_model of Attribution Data.

        Attribution model used to attribute the event.

        :return: The attribution_model of Attribution Data.
        :rtype: AttributionModel
        """
        return self._attribution_model

    @attribution_model.setter
    def attribution_model(self, attribution_model):
        """Sets the attribution_model of Attribution Data.

        Attribution model used to attribute the event.

        :param attribution_model: The attribution_model of Attribution Data.
        :type: AttributionModel
        """
        self._attribution_model = attribution_model
    
    @property
    def attr_window(self):
        """Gets the attr_window of Attribution Data.

        Attribution window in days.

        :return: The attr_window of Attribution Data.
        :rtype: int
        """
        return self._attr_window

    @attr_window.setter
    def attr_window(self, attr_window):
        """Sets the attr_window of Attribution Data.

        Attribution window in days.

        :param attr_window: The attr_window of Attribution Data.
        :type: int
        """
        self._attr_window = attr_window


    def normalize(self):
        normalized_payload = {
            'scope': self.scope,
            'visit_time': self.visit_time,
            'ad_id': self.ad_id,
            'adset_id': self.adset_id,
            'campaign_id': self.campaign_id,
            'attribution_share': self.attribution_share,
            'attribution_model': self.attribution_model,
            'attr_window': self.attr_window,
        }
        normalized_payload = {k: v for k, v in normalized_payload.items() if v is not None}
        return normalized_payload

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
        if issubclass(AttributionData, dict):
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
        if not isinstance(other, AttributionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
