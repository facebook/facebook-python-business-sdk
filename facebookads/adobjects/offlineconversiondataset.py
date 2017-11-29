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

class OfflineConversionDataSet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isOfflineConversionDataSet = True
        super(OfflineConversionDataSet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        attribute_stats = 'attribute_stats'
        business = 'business'
        config = 'config'
        creation_time = 'creation_time'
        description = 'description'
        duplicate_entries = 'duplicate_entries'
        enable_auto_assign_to_accounts = 'enable_auto_assign_to_accounts'
        event_stats = 'event_stats'
        event_time_max = 'event_time_max'
        event_time_min = 'event_time_min'
        id = 'id'
        is_restricted_use = 'is_restricted_use'
        last_upload_app = 'last_upload_app'
        matched_entries = 'matched_entries'
        matched_unique_users = 'matched_unique_users'
        name = 'name'
        usage = 'usage'
        valid_entries = 'valid_entries'
        auto_assign_to_new_accounts_only = 'auto_assign_to_new_accounts_only'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'offline_conversion_data_sets'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.business import Business
        return Business(api=self._api, fbid=parent_id).create_offline_conversion_data_set(fields, params, batch, pending)

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
            target_class=OfflineConversionDataSet,
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

    def get_activities(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business_id': 'string',
            'end_time': 'datetime',
            'event_type': 'event_type_enum',
            'start_time': 'datetime',
        }
        enums = {
            'event_type_enum': [
                'dataset_assign_to_adacct',
                'dataset_autotrack_on_adacct',
                'dataset_disable_autotrack_on_adacct',
                'dataset_unassign_from_adacct',
                'add_dataset_to_business',
                'add_user_to_dataset',
                'remove_user_from_dataset',
                'update_user_role_on_dataset',
                'create_custom_conversion',
                'update_custom_conversion',
                'create_custom_audience',
                'share_custom_audience',
                'unshare_custom_audience',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/activities',
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

    def get_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adaccounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccount,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccount, api=self._api),
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

    def create_ad_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'auto_track_for_ads': 'bool',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adaccounts',
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

    def create_event(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'data': 'list<Object>',
            'namespace_id': 'string',
            'progress': 'Object',
            'upload_id': 'string',
            'upload_tag': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/events',
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

    def get_stats(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'aggr_time': 'aggr_time_enum',
            'end': 'int',
            'skip_empty_values': 'bool',
            'start': 'int',
            'user_timezone_id': 'unsigned int',
        }
        enums = {
            'aggr_time_enum': [
                'upload_time',
                'event_time',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/stats',
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
        param_types = {
            'upload_tag': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/uploads',
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
        'attribute_stats': 'string',
        'business': 'Business',
        'config': 'string',
        'creation_time': 'datetime',
        'description': 'string',
        'duplicate_entries': 'int',
        'enable_auto_assign_to_accounts': 'bool',
        'event_stats': 'string',
        'event_time_max': 'int',
        'event_time_min': 'int',
        'id': 'string',
        'is_restricted_use': 'bool',
        'last_upload_app': 'string',
        'matched_entries': 'int',
        'matched_unique_users': 'int',
        'name': 'string',
        'usage': 'Object',
        'valid_entries': 'int',
        'auto_assign_to_new_accounts_only': 'bool',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
