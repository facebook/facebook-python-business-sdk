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
        product_count = 'product_count'
        quoted_fields_mode = 'quoted_fields_mode'
        schedule = 'schedule'

    class Delimiter:
        autodetect = 'AUTODETECT'
        bar = 'BAR'
        comma = 'COMMA'
        tab = 'TAB'
        tilde = 'TILDE'
        semicolon = 'SEMICOLON'

    class Encoding:
        autodetect = 'AUTODETECT'
        latin1 = 'LATIN1'
        utf8 = 'UTF8'
        utf16le = 'UTF16LE'
        utf16be = 'UTF16BE'
        utf32le = 'UTF32LE'
        utf32be = 'UTF32BE'

    class QuotedFieldsMode:
        autodetect = 'AUTODETECT'
        on = 'ON'
        off = 'OFF'

    @classmethod
    def get_endpoint(cls):
        return 'product_feeds'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.productcatalog import ProductCatalog
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
            'deletion_enabled': 'bool',
            'delimiter': 'delimiter_enum',
            'encoding': 'encoding_enum',
            'name': 'string',
            'quoted_fields': 'bool',
            'schedule': 'string',
        }
        enums = {
            'delimiter_enum': ProductFeed.Delimiter.__dict__.values(),
            'encoding_enum': ProductFeed.Encoding.__dict__.values(),
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

    def get_products(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.productitem import ProductItem
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
            response_parser=ObjectParser(target_class=ProductItem),
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
        from facebookads.adobjects.productfeedupload import ProductFeedUpload
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
            response_parser=ObjectParser(target_class=ProductFeedUpload),
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
        from facebookads.adobjects.productfeedupload import ProductFeedUpload
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
            response_parser=ObjectParser(target_class=ProductFeedUpload),
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
        'encoding': 'Encoding',
        'file_name': 'string',
        'id': 'string',
        'latest_upload': 'ProductFeedUpload',
        'name': 'string',
        'product_count': 'int',
        'quoted_fields_mode': 'QuotedFieldsMode',
        'schedule': 'ProductFeedSchedule',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Delimiter'] = ProductFeed.Delimiter.__dict__.values()
        field_enum_info['Encoding'] = ProductFeed.Encoding.__dict__.values()
        field_enum_info['QuotedFieldsMode'] = ProductFeed.QuotedFieldsMode.__dict__.values()
        return field_enum_info
