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
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class Vehicle(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isVehicle = True
        super(Vehicle, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        applinks = 'applinks'
        availability = 'availability'
        body_style = 'body_style'
        condition = 'condition'
        currency = 'currency'
        custom_label_0 = 'custom_label_0'
        date_first_on_lot = 'date_first_on_lot'
        dealer_communication_channel = 'dealer_communication_channel'
        dealer_id = 'dealer_id'
        dealer_name = 'dealer_name'
        dealer_phone = 'dealer_phone'
        dealer_privacy_policy_url = 'dealer_privacy_policy_url'
        description = 'description'
        drivetrain = 'drivetrain'
        exterior_color = 'exterior_color'
        fb_page_id = 'fb_page_id'
        features = 'features'
        fuel_type = 'fuel_type'
        id = 'id'
        images = 'images'
        interior_color = 'interior_color'
        legal_disclosure_impressum_url = 'legal_disclosure_impressum_url'
        make = 'make'
        mileage = 'mileage'
        model = 'model'
        previous_currency = 'previous_currency'
        previous_price = 'previous_price'
        price = 'price'
        sale_currency = 'sale_currency'
        sale_price = 'sale_price'
        sanitized_images = 'sanitized_images'
        state_of_vehicle = 'state_of_vehicle'
        title = 'title'
        transmission = 'transmission'
        trim = 'trim'
        url = 'url'
        vehicle_id = 'vehicle_id'
        vehicle_registration_plate = 'vehicle_registration_plate'
        vehicle_specifications = 'vehicle_specifications'
        vehicle_type = 'vehicle_type'
        vin = 'vin'
        year = 'year'

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
            target_class=Vehicle,
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

    _field_types = {
        'address': 'Object',
        'applinks': 'AppLinks',
        'availability': 'string',
        'body_style': 'string',
        'condition': 'string',
        'currency': 'string',
        'custom_label_0': 'string',
        'date_first_on_lot': 'string',
        'dealer_communication_channel': 'string',
        'dealer_id': 'string',
        'dealer_name': 'string',
        'dealer_phone': 'string',
        'dealer_privacy_policy_url': 'string',
        'description': 'string',
        'drivetrain': 'string',
        'exterior_color': 'string',
        'fb_page_id': 'Page',
        'features': 'list<Object>',
        'fuel_type': 'string',
        'id': 'string',
        'images': 'list<string>',
        'interior_color': 'string',
        'legal_disclosure_impressum_url': 'string',
        'make': 'string',
        'mileage': 'Object',
        'model': 'string',
        'previous_currency': 'string',
        'previous_price': 'string',
        'price': 'string',
        'sale_currency': 'string',
        'sale_price': 'string',
        'sanitized_images': 'list<string>',
        'state_of_vehicle': 'string',
        'title': 'string',
        'transmission': 'string',
        'trim': 'string',
        'url': 'string',
        'vehicle_id': 'string',
        'vehicle_registration_plate': 'string',
        'vehicle_specifications': 'list<Object>',
        'vehicle_type': 'string',
        'vin': 'string',
        'year': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


