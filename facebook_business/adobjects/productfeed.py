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

class ProductFeed(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductFeed = True
        super(ProductFeed, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        country = 'country'
        created_time = 'created_time'
        default_currency = 'default_currency'
        deletion_enabled = 'deletion_enabled'
        delimiter = 'delimiter'
        encoding = 'encoding'
        file_name = 'file_name'
        id = 'id'
        latest_upload = 'latest_upload'
        name = 'name'
        override_type = 'override_type'
        product_count = 'product_count'
        qualified_product_count = 'qualified_product_count'
        quoted_fields = 'quoted_fields'
        quoted_fields_mode = 'quoted_fields_mode'
        schedule = 'schedule'
        update_schedule = 'update_schedule'
        feed_type = 'feed_type'
        rules = 'rules'

    class Delimiter:
        autodetect = 'AUTODETECT'
        bar = 'BAR'
        comma = 'COMMA'
        tab = 'TAB'
        tilde = 'TILDE'
        semicolon = 'SEMICOLON'

    class QuotedFieldsMode:
        autodetect = 'AUTODETECT'
        on = 'ON'
        off = 'OFF'

    class Encoding:
        autodetect = 'AUTODETECT'
        latin1 = 'LATIN1'
        utf8 = 'UTF8'
        utf16le = 'UTF16LE'
        utf16be = 'UTF16BE'
        utf32le = 'UTF32LE'
        utf32be = 'UTF32BE'

    class FeedType:
        auto = 'AUTO'
        destination = 'DESTINATION'
        flight = 'FLIGHT'
        home_listing = 'HOME_LISTING'
        hotel = 'HOTEL'
        hotel_room = 'HOTEL_ROOM'
        local_inventory = 'LOCAL_INVENTORY'
        market = 'MARKET'
        media_title = 'MEDIA_TITLE'
        products = 'PRODUCTS'
        vehicle_offer = 'VEHICLE_OFFER'
        vehicles = 'VEHICLES'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'product_feeds'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_product_feed(fields, params, batch, pending)

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
            target_class=ProductFeed,
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
            'default_currency': 'string',
            'delimiter': 'delimiter_enum',
            'encoding': 'encoding_enum',
            'name': 'string',
            'quoted_fields_mode': 'quoted_fields_mode_enum',
            'schedule': 'string',
            'update_schedule': 'string',
            'quoted_fields': 'bool',
            'deletion_enabled': 'bool',
        }
        enums = {
            'delimiter_enum': ProductFeed.Delimiter.__dict__.values(),
            'encoding_enum': ProductFeed.Encoding.__dict__.values(),
            'quoted_fields_mode_enum': ProductFeed.QuotedFieldsMode.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeed,
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

    def get_rules(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/rules',
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

    def create_rule(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'attribute': 'string',
            'params': 'map',
            'rule_type': 'rule_type_enum',
        }
        enums = {
            'rule_type_enum': [
                'mapping_rule',
                'value_mapping_rule',
                'letter_case_rule',
                'fallback_rule',
                'regex_replace_rule',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/rules',
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

    def get_uploads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productfeedupload import ProductFeedUpload
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/uploads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeedUpload,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductFeedUpload, api=self._api),
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

    def create_upload(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productfeedupload import ProductFeedUpload
        param_types = {
            'file': 'file',
            'password': 'string',
            'update_only': 'bool',
            'url': 'string',
            'username': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/uploads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeedUpload,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductFeedUpload, api=self._api),
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

    _field_types = {
        'country': 'string',
        'created_time': 'datetime',
        'default_currency': 'string',
        'deletion_enabled': 'bool',
        'delimiter': 'Delimiter',
        'encoding': 'string',
        'file_name': 'string',
        'id': 'string',
        'latest_upload': 'ProductFeedUpload',
        'name': 'string',
        'override_type': 'string',
        'product_count': 'int',
        'qualified_product_count': 'unsigned int',
        'quoted_fields': 'bool',
        'quoted_fields_mode': 'QuotedFieldsMode',
        'schedule': 'ProductFeedSchedule',
        'update_schedule': 'ProductFeedSchedule',
        'feed_type': 'FeedType',
        'rules': 'list<string>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Delimiter'] = ProductFeed.Delimiter.__dict__.values()
        field_enum_info['QuotedFieldsMode'] = ProductFeed.QuotedFieldsMode.__dict__.values()
        field_enum_info['Encoding'] = ProductFeed.Encoding.__dict__.values()
        field_enum_info['FeedType'] = ProductFeed.FeedType.__dict__.values()
        return field_enum_info


