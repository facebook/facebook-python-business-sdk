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

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class Location(
    AbstractObject,
):

    def __init__(self, api=None):
        super(Location, self).__init__()
        self._isLocation = True
        self._api = api

    class Field(AbstractObject.Field):
        city = 'city'
        city_id = 'city_id'
        country = 'country'
        country_code = 'country_code'
        latitude = 'latitude'
        located_in = 'located_in'
        longitude = 'longitude'
        name = 'name'
        region = 'region'
        region_id = 'region_id'
        state = 'state'
        street = 'street'
        zip = 'zip'

    _field_types = {
        'city': 'string',
        'city_id': 'unsigned int',
        'country': 'string',
        'country_code': 'string',
        'latitude': 'float',
        'located_in': 'string',
        'longitude': 'float',
        'name': 'string',
        'region': 'string',
        'region_id': 'unsigned int',
        'state': 'string',
        'street': 'string',
        'zip': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


