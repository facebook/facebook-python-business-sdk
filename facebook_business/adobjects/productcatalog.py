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
from facebook_business.adobjects.helpers.productcatalogmixin import ProductCatalogMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ProductCatalog(
    ProductCatalogMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductCatalog = True
        super(ProductCatalog, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        business = 'business'
        da_display_settings = 'da_display_settings'
        default_image_url = 'default_image_url'
        fallback_image_url = 'fallback_image_url'
        feed_count = 'feed_count'
        flight_catalog_settings = 'flight_catalog_settings'
        id = 'id'
        image_padding_landscape = 'image_padding_landscape'
        image_padding_square = 'image_padding_square'
        name = 'name'
        product_count = 'product_count'
        qualified_product_count = 'qualified_product_count'
        vertical = 'vertical'
        destination_catalog_settings = 'destination_catalog_settings'

    class Vertical:
        commerce = 'commerce'
        destinations = 'destinations'
        flights = 'flights'
        home_listings = 'home_listings'
        hotels = 'hotels'
        vehicles = 'vehicles'

    class PermittedRoles:
        admin = 'ADMIN'
        advertiser = 'ADVERTISER'

    class PermittedTasks:
        admin = 'ADMIN'
        advertiser = 'ADVERTISER'

    class Standard:
        google = 'google'

    class Role:
        admin = 'ADMIN'
        advertiser = 'ADVERTISER'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'owned_product_catalogs'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        return Business(api=self._api, fbid=parent_id).create_owned_product_catalog(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
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
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

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
            target_class=ProductCatalog,
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'default_image_url': 'string',
            'fallback_image_url': 'string',
            'flight_catalog_settings': 'map',
            'destination_catalog_settings': 'map',
            'da_display_settings': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
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

    def delete_agencies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_agencies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Business,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Business, api=self._api),
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

    def create_agency(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
            'permitted_roles': 'list<permitted_roles_enum>',
            'permitted_tasks': 'list<permitted_tasks_enum>',
        }
        enums = {
            'permitted_roles_enum': ProductCatalog.PermittedRoles.__dict__.values(),
            'permitted_tasks_enum': ProductCatalog.PermittedTasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_automotive_models(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.automotivemodel import AutomotiveModel
        param_types = {
            'bulk_pagination': 'bool',
            'filter': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/automotive_models',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AutomotiveModel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AutomotiveModel, api=self._api),
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

    def create_batch(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'requests': 'list<map>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/batch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_check_batch_request_status(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.checkbatchrequeststatus import CheckBatchRequestStatus
        param_types = {
            'handle': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/check_batch_request_status',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CheckBatchRequestStatus,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CheckBatchRequestStatus, api=self._api),
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

    def get_da_event_samples(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productdaeventsamplesbatch import ProductDaEventSamplesBatch
        param_types = {
            'source_id': 'string',
            'event': 'event_enum',
            'aggregation_type': 'aggregation_type_enum',
        }
        enums = {
            'event_enum': ProductDaEventSamplesBatch.Event.__dict__.values(),
            'aggregation_type_enum': ProductDaEventSamplesBatch.AggregationType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/da_event_samples',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductDaEventSamplesBatch,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductDaEventSamplesBatch, api=self._api),
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

    def get_destinations(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.destination import Destination
        param_types = {
            'bulk_pagination': 'bool',
            'filter': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/destinations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Destination,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Destination, api=self._api),
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

    def get_event_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.producteventstat import ProductEventStat
        param_types = {
            'breakdowns': 'list<breakdowns_enum>',
        }
        enums = {
            'breakdowns_enum': ProductEventStat.Breakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/event_stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductEventStat,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductEventStat, api=self._api),
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

    def delete_external_event_sources(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'external_event_sources': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/external_event_sources',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_external_event_sources(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.externaleventsource import ExternalEventSource
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/external_event_sources',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExternalEventSource,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExternalEventSource, api=self._api),
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

    def create_external_event_source(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'external_event_sources': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/external_event_sources',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_flights(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.flight import Flight
        param_types = {
            'bulk_pagination': 'bool',
            'filter': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/flights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Flight,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Flight, api=self._api),
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

    def create_flight(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.flight import Flight
        param_types = {
            'images': 'list<Object>',
            'origin_airport': 'string',
            'destination_airport': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/flights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Flight,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Flight, api=self._api),
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

    def get_home_listings(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.homelisting import HomeListing
        param_types = {
            'bulk_pagination': 'bool',
            'filter': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/home_listings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=HomeListing,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=HomeListing, api=self._api),
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

    def create_home_listing(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.homelisting import HomeListing
        param_types = {
            'home_listing_id': 'string',
            'address': 'Object',
            'availability': 'string',
            'images': 'list<Object>',
            'name': 'string',
            'currency': 'string',
            'price': 'float',
            'url': 'string',
            'year_built': 'unsigned int',
            'description': 'string',
            'listing_type': 'string',
            'num_baths': 'float',
            'num_beds': 'float',
            'num_units': 'float',
            'property_type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/home_listings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=HomeListing,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=HomeListing, api=self._api),
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

    def get_hotel_rooms_batch(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcataloghotelroomsbatch import ProductCatalogHotelRoomsBatch
        param_types = {
            'handle': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/hotel_rooms_batch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalogHotelRoomsBatch,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalogHotelRoomsBatch, api=self._api),
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

    def create_hotel_rooms_batch(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'file': 'file',
            'password': 'string',
            'standard': 'standard_enum',
            'url': 'string',
            'username': 'string',
            'update_only': 'bool',
        }
        enums = {
            'standard_enum': ProductCatalog.Standard.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/hotel_rooms_batch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_hotels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.hotel import Hotel
        param_types = {
            'bulk_pagination': 'bool',
            'filter': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/hotels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Hotel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Hotel, api=self._api),
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

    def create_hotel(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.hotel import Hotel
        param_types = {
            'hotel_id': 'string',
            'address': 'Object',
            'brand': 'string',
            'description': 'string',
            'name': 'string',
            'url': 'string',
            'images': 'list<Object>',
            'currency': 'string',
            'base_price': 'unsigned int',
            'applinks': 'Object',
            'phone': 'string',
            'star_rating': 'float',
            'guest_ratings': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/hotels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Hotel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Hotel, api=self._api),
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

    def get_pricing_variables_batch(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalogpricingvariablesbatch import ProductCatalogPricingVariablesBatch
        param_types = {
            'handle': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pricing_variables_batch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalogPricingVariablesBatch,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalogPricingVariablesBatch, api=self._api),
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

    def create_pricing_variables_batch(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'file': 'file',
            'password': 'string',
            'standard': 'standard_enum',
            'url': 'string',
            'username': 'string',
            'update_only': 'bool',
        }
        enums = {
            'standard_enum': ProductCatalog.Standard.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/pricing_variables_batch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_product_feeds(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productfeed import ProductFeed
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_feeds',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeed,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductFeed, api=self._api),
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

    def create_product_feed(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productfeed import ProductFeed
        param_types = {
            'default_currency': 'string',
            'delimiter': 'delimiter_enum',
            'encoding': 'encoding_enum',
            'name': 'string',
            'quoted_fields_mode': 'quoted_fields_mode_enum',
            'schedule': 'string',
            'update_schedule': 'string',
            'country': 'string',
            'deletion_enabled': 'bool',
            'feed_type': 'feed_type_enum',
            'file_name': 'string',
            'quoted_fields': 'bool',
            'rules': 'list<string>',
        }
        enums = {
            'delimiter_enum': ProductFeed.Delimiter.__dict__.values(),
            'encoding_enum': ProductFeed.Encoding.__dict__.values(),
            'quoted_fields_mode_enum': ProductFeed.QuotedFieldsMode.__dict__.values(),
            'feed_type_enum': ProductFeed.FeedType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/product_feeds',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeed,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductFeed, api=self._api),
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

    def get_product_groups(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productgroup import ProductGroup
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductGroup, api=self._api),
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

    def create_product_group(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productgroup import ProductGroup
        param_types = {
            'retailer_id': 'string',
            'variants': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/product_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductGroup, api=self._api),
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

    def get_product_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productset import ProductSet
        param_types = {
            'parent_id': 'string',
            'ancestor_id': 'string',
            'has_children': 'bool',
            'retailer_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductSet, api=self._api),
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

    def create_product_set(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productset import ProductSet
        param_types = {
            'filter': 'Object',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/product_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductSet, api=self._api),
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

    def get_product_sets_batch(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalogproductsetsbatch import ProductCatalogProductSetsBatch
        param_types = {
            'handle': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_sets_batch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalogProductSetsBatch,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalogProductSetsBatch, api=self._api),
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

    def create_product_sets_batch(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'file': 'file',
            'password': 'string',
            'standard': 'standard_enum',
            'url': 'string',
            'username': 'string',
            'update_only': 'bool',
        }
        enums = {
            'standard_enum': ProductCatalog.Standard.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/product_sets_batch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_products(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productitem import ProductItem
        param_types = {
            'bulk_pagination': 'bool',
            'return_only_approved_products': 'bool',
            'filter': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/products',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductItem, api=self._api),
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

    def create_product(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productitem import ProductItem
        param_types = {
            'retailer_id': 'string',
            'retailer_product_group_id': 'string',
            'availability': 'availability_enum',
            'currency': 'string',
            'condition': 'condition_enum',
            'description': 'string',
            'image_url': 'Object',
            'name': 'string',
            'price': 'unsigned int',
            'product_type': 'string',
            'visibility': 'visibility_enum',
            'additional_image_urls': 'list<string>',
            'additional_variant_attributes': 'Object',
            'brand': 'string',
            'category': 'string',
            'checkout_url': 'string',
            'color': 'string',
            'custom_data': 'map',
            'custom_label_0': 'string',
            'custom_label_1': 'string',
            'custom_label_2': 'string',
            'custom_label_3': 'string',
            'custom_label_4': 'string',
            'expiration_date': 'string',
            'gender': 'gender_enum',
            'gtin': 'string',
            'inventory': 'unsigned int',
            'manufacturer_part_number': 'string',
            'mobile_link': 'Object',
            'material': 'string',
            'offer_price_amount': 'unsigned int',
            'offer_price_end_date': 'Object',
            'offer_price_start_date': 'Object',
            'ordering_index': 'unsigned int',
            'pattern': 'string',
            'sale_price': 'unsigned int',
            'sale_price_end_date': 'datetime',
            'sale_price_start_date': 'datetime',
            'short_description': 'string',
            'size': 'string',
            'start_date': 'string',
            'url': 'Object',
            'ios_url': 'string',
            'ios_app_store_id': 'unsigned int',
            'ios_app_name': 'string',
            'iphone_url': 'string',
            'iphone_app_store_id': 'unsigned int',
            'iphone_app_name': 'string',
            'ipad_url': 'string',
            'ipad_app_store_id': 'unsigned int',
            'ipad_app_name': 'string',
            'android_url': 'string',
            'android_package': 'string',
            'android_class': 'string',
            'android_app_name': 'string',
            'windows_phone_url': 'string',
            'windows_phone_app_id': 'string',
            'windows_phone_app_name': 'string',
        }
        enums = {
            'availability_enum': ProductItem.Availability.__dict__.values(),
            'condition_enum': ProductItem.Condition.__dict__.values(),
            'visibility_enum': ProductItem.Visibility.__dict__.values(),
            'gender_enum': ProductItem.Gender.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/products',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductItem,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductItem, api=self._api),
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

    def delete_user_permissions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'email': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/userpermissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_user_permissions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcataloguserpermissions import ProductCatalogUserPermissions
        param_types = {
            'business': 'Object',
            'user': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/userpermissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalogUserPermissions,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalogUserPermissions, api=self._api),
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

    def create_user_permission(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'email': 'string',
            'role': 'role_enum',
            'business': 'string',
        }
        enums = {
            'role_enum': ProductCatalog.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/userpermissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_vehicles(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.vehicle import Vehicle
        param_types = {
            'bulk_pagination': 'bool',
            'filter': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/vehicles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Vehicle,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Vehicle, api=self._api),
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

    def create_video(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'title': 'string',
            'source': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'time_since_original_post': 'unsigned int',
            'file_url': 'string',
            'composer_session_id': 'string',
            'waterfall_id': 'string',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_suggestion_mechanism': 'string',
            'manual_privacy': 'bool',
            'is_explicit_share': 'bool',
            'thumb': 'file',
            'spherical': 'bool',
            'original_projection_type': 'original_projection_type_enum',
            'initial_heading': 'unsigned int',
            'initial_pitch': 'unsigned int',
            'fov': 'unsigned int',
            'original_fov': 'unsigned int',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'guide_enabled': 'bool',
            'guide': 'list<list<unsigned int>>',
            'audio_story_wave_animation_handle': 'string',
            'adaptive_type': 'string',
            'animated_effect_id': 'unsigned int',
            'asked_fun_fact_prompt_id': 'unsigned int',
            'composer_entry_picker': 'string',
            'composer_entry_point': 'string',
            'composer_entry_time': 'unsigned int',
            'composer_session_events_log': 'string',
            'composer_source_surface': 'string',
            'composer_type': 'string',
            'formatting': 'formatting_enum',
            'fun_fact_prompt_id': 'string',
            'fun_fact_toastee_id': 'unsigned int',
            'is_group_linking_post': 'bool',
            'has_nickname': 'bool',
            'holiday_card': 'string',
            'instant_game_entry_point_data': 'string',
            'is_boost_intended': 'bool',
            'location_source_id': 'string',
            'description': 'string',
            'offer_like_post_id': 'string',
            'publish_event_id': 'unsigned int',
            'react_mode_metadata': 'string',
            'sales_promo_id': 'unsigned int',
            'text_format_metadata': 'string',
            'throwback_camera_roll_media': 'string',
            'video_start_time_ms': 'unsigned int',
            'application_id': 'string',
            'upload_phase': 'upload_phase_enum',
            'file_size': 'unsigned int',
            'start_offset': 'unsigned int',
            'end_offset': 'unsigned int',
            'video_file_chunk': 'string',
            'fbuploader_video_file_chunk': 'string',
            'upload_session_id': 'string',
            'is_voice_clip': 'bool',
            'attribution_app_id': 'string',
            'content_category': 'content_category_enum',
            'embeddable': 'bool',
            'slideshow_spec': 'map',
            'upload_setting_properties': 'string',
            'transcode_setting_properties': 'string',
            'container_type': 'container_type_enum',
            'referenced_sticker_id': 'string',
            'replace_video_id': 'string',
            'swap_mode': 'swap_mode_enum',
        }
        enums = {
            'unpublished_content_type_enum': AdVideo.UnpublishedContentType.__dict__.values(),
            'original_projection_type_enum': AdVideo.OriginalProjectionType.__dict__.values(),
            'formatting_enum': AdVideo.Formatting.__dict__.values(),
            'upload_phase_enum': AdVideo.UploadPhase.__dict__.values(),
            'content_category_enum': AdVideo.ContentCategory.__dict__.values(),
            'container_type_enum': AdVideo.ContainerType.__dict__.values(),
            'swap_mode_enum': AdVideo.SwapMode.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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
        'business': 'Business',
        'da_display_settings': 'ProductCatalogImageSettings',
        'default_image_url': 'string',
        'fallback_image_url': 'list<string>',
        'feed_count': 'int',
        'flight_catalog_settings': 'FlightCatalogSettings',
        'id': 'string',
        'image_padding_landscape': 'bool',
        'image_padding_square': 'bool',
        'name': 'string',
        'product_count': 'int',
        'qualified_product_count': 'unsigned int',
        'vertical': 'string',
        'destination_catalog_settings': 'map',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Vertical'] = ProductCatalog.Vertical.__dict__.values()
        field_enum_info['PermittedRoles'] = ProductCatalog.PermittedRoles.__dict__.values()
        field_enum_info['PermittedTasks'] = ProductCatalog.PermittedTasks.__dict__.values()
        field_enum_info['Standard'] = ProductCatalog.Standard.__dict__.values()
        field_enum_info['Role'] = ProductCatalog.Role.__dict__.values()
        return field_enum_info


