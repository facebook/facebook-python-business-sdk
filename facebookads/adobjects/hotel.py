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

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class Hotel(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isHotel = True
        super(Hotel, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        applinks = 'applinks'
        brand = 'brand'
        description = 'description'
        guest_ratings = 'guest_ratings'
        hotel_id = 'hotel_id'
        id = 'id'
        images = 'images'
        lowest_base_price = 'lowest_base_price'
        name = 'name'
        phone = 'phone'
        star_rating = 'star_rating'
        url = 'url'

    @classmethod
    def get_endpoint(cls):
        return 'hotels'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_hotel(fields, params, batch, pending)

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Hotel,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_hotel_room(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.hotelroom import HotelRoom
        param_types = {
            'applinks': 'Object',
            'base_price': 'float',
            'currency': 'string',
            'description': 'string',
            'images': 'list<Object>',
            'margin_level': 'unsigned int',
            'name': 'string',
            'pricing_variables': 'list<Object>',
            'room_id': 'string',
            'url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/hotel_rooms',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=HotelRoom,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=HotelRoom),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'address': 'string',
        'applinks': 'AppLinks',
        'brand': 'string',
        'description': 'string',
        'guest_ratings': 'string',
        'hotel_id': 'string',
        'id': 'string',
        'images': 'list<string>',
        'lowest_base_price': 'string',
        'name': 'string',
        'phone': 'string',
        'star_rating': 'string',
        'url': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
