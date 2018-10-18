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

class AtlasCampaign(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAtlasCampaign = True
        super(AtlasCampaign, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        alias = 'alias'
        created_by = 'created_by'
        created_date = 'created_date'
        created_time = 'created_time'
        creator_name = 'creator_name'
        cumulative_edited_date = 'cumulative_edited_date'
        custom_fields = 'custom_fields'
        description = 'description'
        flight_dates = 'flight_dates'
        id = 'id'
        is_archived = 'is_archived'
        is_auto_tracked = 'is_auto_tracked'
        is_favorite = 'is_favorite'
        is_mta = 'is_mta'
        last_modified_by = 'last_modified_by'
        last_modified_date = 'last_modified_date'
        last_modified_time = 'last_modified_time'
        name = 'name'
        purchase_order_alias = 'purchase_order_alias'
        target_audience = 'target_audience'
        type = 'type'
        version = 'version'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'metric_scope': 'map',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AtlasCampaign,
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

    def create_import_template(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'filename': 'string',
            'template': 'string',
            'export': 'string',
            'format': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/importtemplate',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AtlasCampaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AtlasCampaign, api=self._api),
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

    def get_invoices(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.oracletransaction import OracleTransaction
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/invoices',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OracleTransaction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OracleTransaction, api=self._api),
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

    def get_trafficking_data(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.atlasurl import AtlasURL
        param_types = {
            'redirect': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/trafficking_data',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AtlasURL,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AtlasURL, api=self._api),
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
        'alias': 'string',
        'created_by': 'Object',
        'created_date': 'datetime',
        'created_time': 'datetime',
        'creator_name': 'string',
        'cumulative_edited_date': 'datetime',
        'custom_fields': 'list<Object>',
        'description': 'string',
        'flight_dates': 'Object',
        'id': 'string',
        'is_archived': 'bool',
        'is_auto_tracked': 'bool',
        'is_favorite': 'bool',
        'is_mta': 'bool',
        'last_modified_by': 'Object',
        'last_modified_date': 'datetime',
        'last_modified_time': 'datetime',
        'name': 'string',
        'purchase_order_alias': 'string',
        'target_audience': 'Object',
        'type': 'string',
        'version': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


