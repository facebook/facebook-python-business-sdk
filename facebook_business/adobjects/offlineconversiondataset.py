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
        data_origin = 'data_origin'
        description = 'description'
        duplicate_entries = 'duplicate_entries'
        enable_auto_assign_to_accounts = 'enable_auto_assign_to_accounts'
        event_stats = 'event_stats'
        event_time_max = 'event_time_max'
        event_time_min = 'event_time_min'
        id = 'id'
        is_restricted_use = 'is_restricted_use'
        last_upload_app = 'last_upload_app'
        last_upload_app_changed_time = 'last_upload_app_changed_time'
        match_rate_approx = 'match_rate_approx'
        matched_entries = 'matched_entries'
        matched_unique_users = 'matched_unique_users'
        name = 'name'
        usage = 'usage'
        valid_entries = 'valid_entries'
        auto_assign_to_new_accounts_only = 'auto_assign_to_new_accounts_only'

    class DataOrigin:
        directly_from_people = 'DIRECTLY_FROM_PEOPLE'
        people_and_partners = 'PEOPLE_AND_PARTNERS'
        directly_from_partners = 'DIRECTLY_FROM_PARTNERS'
        none = 'NONE'

    class PermittedRoles:
        admin = 'ADMIN'
        uploader = 'UPLOADER'
        advertiser = 'ADVERTISER'

    class RelationshipType:
        ad_manager = 'AD_MANAGER'
        audience_manager = 'AUDIENCE_MANAGER'
        agency = 'AGENCY'
        other = 'OTHER'

    class Role:
        admin = 'ADMIN'
        uploader = 'UPLOADER'
        advertiser = 'ADVERTISER'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'offline_conversion_data_sets'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        return Business(api=self._api, fbid=parent_id).create_offline_conversion_data_set(fields, params, batch, pending)

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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'description': 'string',
            'data_origin': 'data_origin_enum',
            'enable_auto_assign_to_accounts': 'bool',
            'auto_assign_to_new_accounts_only': 'bool',
        }
        enums = {
            'data_origin_enum': OfflineConversionDataSet.DataOrigin.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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
            'start_time': 'datetime',
            'end_time': 'datetime',
            'event_type': 'event_type_enum',
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

    def delete_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
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

    def get_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
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
            'business': 'string',
            'auto_track_for_ads': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adaccounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OfflineConversionDataSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineConversionDataSet, api=self._api),
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
            'relationship_type': 'list<relationship_type_enum>',
            'other_relationship': 'string',
        }
        enums = {
            'permitted_roles_enum': OfflineConversionDataSet.PermittedRoles.__dict__.values(),
            'relationship_type_enum': OfflineConversionDataSet.RelationshipType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OfflineConversionDataSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineConversionDataSet, api=self._api),
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

    def get_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudience import CustomAudience
        param_types = {
            'ad_account': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/audiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudience, api=self._api),
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

    def get_custom_conversions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
            'ad_account': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/customconversions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomConversion,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomConversion, api=self._api),
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

    def get_da_checks(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.dacheck import DACheck
        param_types = {
            'checks': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/da_checks',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DACheck,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DACheck, api=self._api),
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
            'upload_tag': 'string',
            'upload_id': 'string',
            'upload_source': 'string',
            'data': 'list<string>',
            'namespace_id': 'string',
            'progress': 'Object',
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
            'start': 'int',
            'end': 'int',
            'skip_empty_values': 'bool',
            'aggr_time': 'aggr_time_enum',
            'user_timezone_id': 'unsigned int',
            'granularity': 'granularity_enum',
        }
        enums = {
            'aggr_time_enum': [
                'upload_time',
                'event_time',
            ],
            'granularity_enum': [
                'daily',
                'hourly',
                'six_hourly',
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
            'start_time': 'Object',
            'end_time': 'Object',
            'sort_by': 'sort_by_enum',
            'order': 'order_enum',
        }
        enums = {
            'sort_by_enum': [
                'CREATION_TIME',
                'FIRST_UPLOAD_TIME',
                'LAST_UPLOAD_TIME',
                'API_CALLS',
                'EVENT_TIME_MIN',
                'EVENT_TIME_MAX',
                'IS_EXCLUDED_FOR_LIFT',
            ],
            'order_enum': [
                'ASCENDING',
                'DESCENDING',
            ],
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

    def create_upload(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'upload_tag': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def delete_user_permissions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'email': 'string',
            'business': 'Object',
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
        param_types = {
            'business': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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

    def create_user_permission(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'role': 'role_enum',
            'business': 'Object',
        }
        enums = {
            'role_enum': OfflineConversionDataSet.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/userpermissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OfflineConversionDataSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineConversionDataSet, api=self._api),
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

    def create_validate(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'data': 'list<string>',
            'namespace_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/validate',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OfflineConversionDataSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineConversionDataSet, api=self._api),
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
        'data_origin': 'string',
        'description': 'string',
        'duplicate_entries': 'int',
        'enable_auto_assign_to_accounts': 'bool',
        'event_stats': 'string',
        'event_time_max': 'int',
        'event_time_min': 'int',
        'id': 'string',
        'is_restricted_use': 'bool',
        'last_upload_app': 'string',
        'last_upload_app_changed_time': 'int',
        'match_rate_approx': 'int',
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
        field_enum_info['DataOrigin'] = OfflineConversionDataSet.DataOrigin.__dict__.values()
        field_enum_info['PermittedRoles'] = OfflineConversionDataSet.PermittedRoles.__dict__.values()
        field_enum_info['RelationshipType'] = OfflineConversionDataSet.RelationshipType.__dict__.values()
        field_enum_info['Role'] = OfflineConversionDataSet.Role.__dict__.values()
        return field_enum_info


