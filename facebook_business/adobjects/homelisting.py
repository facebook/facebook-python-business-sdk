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

class HomeListing(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isHomeListing = True
        super(HomeListing, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ac_type = 'ac_type'
        additional_fees_description = 'additional_fees_description'
        address = 'address'
        agent_company = 'agent_company'
        agent_email = 'agent_email'
        agent_fb_page_id = 'agent_fb_page_id'
        agent_name = 'agent_name'
        agent_phone = 'agent_phone'
        applinks = 'applinks'
        area_size = 'area_size'
        area_unit = 'area_unit'
        availability = 'availability'
        co_2_emission_rating_eu = 'co_2_emission_rating_eu'
        currency = 'currency'
        days_on_market = 'days_on_market'
        description = 'description'
        energy_rating_eu = 'energy_rating_eu'
        furnish_type = 'furnish_type'
        group_id = 'group_id'
        heating_type = 'heating_type'
        home_listing_id = 'home_listing_id'
        id = 'id'
        images = 'images'
        laundry_type = 'laundry_type'
        listing_type = 'listing_type'
        max_currency = 'max_currency'
        max_price = 'max_price'
        min_currency = 'min_currency'
        min_price = 'min_price'
        name = 'name'
        num_baths = 'num_baths'
        num_beds = 'num_beds'
        num_rooms = 'num_rooms'
        num_units = 'num_units'
        parking_type = 'parking_type'
        partner_verification = 'partner_verification'
        pet_policy = 'pet_policy'
        price = 'price'
        property_type = 'property_type'
        sanitized_images = 'sanitized_images'
        url = 'url'
        year_built = 'year_built'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'home_listings'

    # @deprecated api_create is being deprecated
    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_home_listing(fields, params, batch, success, failure, pending)

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            target_class=HomeListing,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'address': 'Object',
            'availability': 'string',
            'currency': 'string',
            'description': 'string',
            'images': 'list<Object>',
            'listing_type': 'string',
            'name': 'string',
            'num_baths': 'float',
            'num_beds': 'float',
            'num_units': 'float',
            'price': 'float',
            'property_type': 'string',
            'url': 'string',
            'year_built': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=HomeListing,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'ac_type': 'string',
        'additional_fees_description': 'string',
        'address': 'Object',
        'agent_company': 'string',
        'agent_email': 'string',
        'agent_fb_page_id': 'Page',
        'agent_name': 'string',
        'agent_phone': 'string',
        'applinks': 'CatalogItemAppLinks',
        'area_size': 'unsigned int',
        'area_unit': 'string',
        'availability': 'string',
        'co_2_emission_rating_eu': 'Object',
        'currency': 'string',
        'days_on_market': 'unsigned int',
        'description': 'string',
        'energy_rating_eu': 'Object',
        'furnish_type': 'string',
        'group_id': 'string',
        'heating_type': 'string',
        'home_listing_id': 'string',
        'id': 'string',
        'images': 'list<string>',
        'laundry_type': 'string',
        'listing_type': 'string',
        'max_currency': 'string',
        'max_price': 'string',
        'min_currency': 'string',
        'min_price': 'string',
        'name': 'string',
        'num_baths': 'float',
        'num_beds': 'float',
        'num_rooms': 'float',
        'num_units': 'unsigned int',
        'parking_type': 'string',
        'partner_verification': 'string',
        'pet_policy': 'string',
        'price': 'string',
        'property_type': 'string',
        'sanitized_images': 'list<string>',
        'url': 'string',
        'year_built': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


