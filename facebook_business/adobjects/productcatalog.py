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
            'da_display_settings': 'Object',
            'default_image_url': 'string',
            'destination_catalog_settings': 'map',
            'fallback_image_url': 'string',
            'flight_catalog_settings': 'map',
            'name': 'string',
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

    def create_batch(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productitem import ProductItem
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
            'aggregation_type': 'aggregation_type_enum',
            'event': 'event_enum',
            'source_id': 'string',
        }
        enums = {
            'aggregation_type_enum': ProductDaEventSamplesBatch.AggregationType.__dict__.values(),
            'event_enum': ProductDaEventSamplesBatch.Event.__dict__.values(),
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
        from facebook_business.adobjects.externaleventsource import ExternalEventSource
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

    def get_flights(self, fields=None, params=None, batch=None, pending=False):
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

    def get_home_listings(self, fields=None, params=None, batch=None, pending=False):
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

    def create_home_listing(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'address': 'Object',
            'availability': 'string',
            'currency': 'string',
            'description': 'string',
            'home_listing_id': 'string',
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
            endpoint='/home_listings',
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
        from facebook_business.adobjects.productcataloghotelroomsbatch import ProductCatalogHotelRoomsBatch
        param_types = {
            'file': 'file',
            'password': 'string',
            'standard': 'standard_enum',
            'update_only': 'bool',
            'url': 'string',
            'username': 'string',
        }
        enums = {
            'standard_enum': ProductCatalogHotelRoomsBatch.Standard.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def get_hotels(self, fields=None, params=None, batch=None, pending=False):
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

    def create_hotel(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'address': 'Object',
            'applinks': 'Object',
            'brand': 'string',
            'description': 'string',
            'guest_ratings': 'list<Object>',
            'hotel_id': 'string',
            'images': 'list<Object>',
            'name': 'string',
            'phone': 'string',
            'star_rating': 'float',
            'url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/hotels',
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
        from facebook_business.adobjects.productcatalogpricingvariablesbatch import ProductCatalogPricingVariablesBatch
        param_types = {
            'file': 'file',
            'password': 'string',
            'standard': 'standard_enum',
            'update_only': 'bool',
            'url': 'string',
            'username': 'string',
        }
        enums = {
            'standard_enum': ProductCatalogPricingVariablesBatch.Standard.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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
            'country': 'string',
            'default_currency': 'string',
            'deletion_enabled': 'bool',
            'delimiter': 'delimiter_enum',
            'encoding': 'encoding_enum',
            'feed_type': 'feed_type_enum',
            'file_name': 'string',
            'name': 'string',
            'quoted_fields_mode': 'quoted_fields_mode_enum',
            'rules': 'list<string>',
            'schedule': 'string',
            'update_schedule': 'string',
        }
        enums = {
            'delimiter_enum': ProductFeed.Delimiter.__dict__.values(),
            'encoding_enum': ProductFeed.Encoding.__dict__.values(),
            'feed_type_enum': ProductFeed.FeedType.__dict__.values(),
            'quoted_fields_mode_enum': ProductFeed.QuotedFieldsMode.__dict__.values(),
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
            'ancestor_id': 'string',
            'has_children': 'bool',
            'parent_id': 'string',
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

    def get_products(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productitem import ProductItem
        param_types = {
            'bulk_pagination': 'bool',
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
            'additional_image_urls': 'list<string>',
            'additional_variant_attributes': 'Object',
            'android_app_name': 'string',
            'android_class': 'string',
            'android_package': 'string',
            'android_url': 'string',
            'availability': 'availability_enum',
            'brand': 'string',
            'category': 'string',
            'checkout_url': 'string',
            'color': 'string',
            'condition': 'condition_enum',
            'currency': 'string',
            'custom_data': 'map',
            'custom_label_0': 'string',
            'custom_label_1': 'string',
            'custom_label_2': 'string',
            'custom_label_3': 'string',
            'custom_label_4': 'string',
            'description': 'string',
            'expiration_date': 'string',
            'gender': 'gender_enum',
            'gtin': 'string',
            'image_url': 'Object',
            'inventory': 'unsigned int',
            'ios_app_name': 'string',
            'ios_app_store_id': 'unsigned int',
            'ios_url': 'string',
            'ipad_app_name': 'string',
            'ipad_app_store_id': 'unsigned int',
            'ipad_url': 'string',
            'iphone_app_name': 'string',
            'iphone_app_store_id': 'unsigned int',
            'iphone_url': 'string',
            'manufacturer_part_number': 'string',
            'material': 'string',
            'mobile_link': 'Object',
            'name': 'string',
            'offer_price_amount': 'unsigned int',
            'offer_price_end_date': 'Object',
            'offer_price_start_date': 'Object',
            'ordering_index': 'unsigned int',
            'pattern': 'string',
            'price': 'unsigned int',
            'product_type': 'string',
            'retailer_id': 'string',
            'retailer_product_group_id': 'string',
            'sale_price': 'unsigned int',
            'sale_price_end_date': 'datetime',
            'sale_price_start_date': 'datetime',
            'short_description': 'string',
            'size': 'string',
            'start_date': 'string',
            'url': 'Object',
            'visibility': 'visibility_enum',
            'windows_phone_app_id': 'string',
            'windows_phone_app_name': 'string',
            'windows_phone_url': 'string',
        }
        enums = {
            'availability_enum': ProductItem.Availability.__dict__.values(),
            'condition_enum': ProductItem.Condition.__dict__.values(),
            'gender_enum': ProductItem.Gender.__dict__.values(),
            'visibility_enum': ProductItem.Visibility.__dict__.values(),
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

    def get_quality_issues(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productsqualityissue import ProductsQualityIssue
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/quality_issues',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductsQualityIssue,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductsQualityIssue, api=self._api),
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

    def create_video(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'audio_story_wave_animation_handle': 'string',
            'content_category': 'content_category_enum',
            'description': 'string',
            'embeddable': 'bool',
            'end_offset': 'unsigned int',
            'file_size': 'unsigned int',
            'file_url': 'string',
            'fisheye_video_cropped': 'bool',
            'fov': 'unsigned int',
            'front_z_rotation': 'float',
            'guide': 'list<list<unsigned int>>',
            'guide_enabled': 'bool',
            'initial_heading': 'unsigned int',
            'initial_pitch': 'unsigned int',
            'original_fov': 'unsigned int',
            'original_projection_type': 'original_projection_type_enum',
            'react_mode_metadata': 'string',
            'referenced_sticker_id': 'string',
            'replace_video_id': 'string',
            'slideshow_spec': 'map',
            'source': 'string',
            'spherical': 'bool',
            'start_offset': 'unsigned int',
            'swap_mode': 'swap_mode_enum',
            'thumb': 'file',
            'title': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'upload_phase': 'upload_phase_enum',
            'upload_session_id': 'string',
            'video_file_chunk': 'string',
        }
        enums = {
            'content_category_enum': [
                'BEAUTY_FASHION',
                'BUSINESS',
                'CARS_TRUCKS',
                'COMEDY',
                'CUTE_ANIMALS',
                'ENTERTAINMENT',
                'FAMILY',
                'FOOD_HEALTH',
                'HOME',
                'LIFESTYLE',
                'MUSIC',
                'NEWS',
                'POLITICS',
                'SCIENCE',
                'SPORTS',
                'TECHNOLOGY',
                'VIDEO_GAMING',
                'OTHER',
            ],
            'original_projection_type_enum': [
                'equirectangular',
                'cubemap',
                'equiangular_cubemap',
                'half_equirectangular',
            ],
            'swap_mode_enum': [
                'replace',
            ],
            'unpublished_content_type_enum': [
                'SCHEDULED',
                'DRAFT',
                'ADS_POST',
                'INLINE_CREATED',
                'PUBLISHED',
            ],
            'upload_phase_enum': [
                'start',
                'transfer',
                'finish',
                'cancel',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/videos',
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

    _field_types = {
        'business': 'Business',
        'da_display_settings': 'ProductCatalogImageSettings',
        'default_image_url': 'string',
        'fallback_image_url': 'list<string>',
        'feed_count': 'int',
        'flight_catalog_settings': 'Object',
        'id': 'string',
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
        return field_enum_info
