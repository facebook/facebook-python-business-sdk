# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.exceptions import (
    FacebookBadObjectError,
)
from facebook_business.adobjects.abstractobject import AbstractObject

class ObjectParser:
    """
    Parser for API response
    """

    def __init__(
        self,
        api=None,
        target_class=None,
        reuse_object=None,
        custom_parse_method=None,
    ):
        """ Initialize an ObjectParser.
        To Initialize, you need to provide either a reuse_object, target_class,
        or an custom_parse_method.
        Args:
            api: FacebookAdsApi object.
            target_class (optional): The expected return object type.
            reuse_object (optional): Reuse existing object to populate response.
            custom_parse_method (optional): Custom parsing method.
        """
        if not any([target_class, reuse_object is not None, custom_parse_method]):
            raise FacebookBadObjectError(
                'Must specify either target class calling object' +
                'or custom parse method for parser')
        self._reuse_object = reuse_object
        self._target_class = target_class
        self._custom_parse_method = custom_parse_method
        self._api = api

    def parse_single(self, response):
        if self._custom_parse_method is not None:
            return self._custom_parse_method(response, self._api)

        data = response
        if 'data' in response and isinstance(response['data'], dict):
            data = response['data']
        elif 'images' in response and not isinstance(data['images'], list):
            _, data = data['images'].popitem()
        if 'campaigns' in data:
            _, data = data['campaigns'].popitem()
        elif 'adsets' in data:
            _, data = data['adsets'].popitem()
        elif 'ads' in data:
            _, data = data['ads'].popitem()
        if 'success' in data:
            del data['success']

        if self._reuse_object is not None:
            self._reuse_object._set_data(data)
            return self._reuse_object
        elif self._target_class is not None:
            return AbstractObject.create_object(self._api, data,
                                                self._target_class)
        else:
            raise FacebookBadObjectError(
                'Must specify either target class calling object' +
                'or custom parse method for parser')

    def parse_multiple(self, response):
        if 'data' in response and isinstance(response['data'], list):
            ret = []
            if isinstance(response['data'], list):
                for json_obj in response['data']:
                    ret.append(self.parse_single(json_obj))
            else:
                ret.append(self.parse_single(response['data']))
        else:
            data = response['data'] if 'data' in response else response
            ret = [AbstractObject.create_object(self._api, data,
                                                self._target_class)]

        return ret
