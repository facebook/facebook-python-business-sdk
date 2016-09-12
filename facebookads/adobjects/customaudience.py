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
from facebookads.adobjects.helpers.customaudiencemixin import CustomAudienceMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class CustomAudience(
    CustomAudienceMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCustomAudience = True
        super(CustomAudience, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        approximate_count = 'approximate_count'
        data_source = 'data_source'
        delivery_status = 'delivery_status'
        description = 'description'
        external_event_source = 'external_event_source'
        id = 'id'
        last_used_time = 'last_used_time'
        lookalike_audience_ids = 'lookalike_audience_ids'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        operation_status = 'operation_status'
        opt_out_link = 'opt_out_link'
        owner_business = 'owner_business'
        permission_for_actions = 'permission_for_actions'
        pixel_id = 'pixel_id'
        retention_days = 'retention_days'
        rule = 'rule'
        subtype = 'subtype'
        time_content_updated = 'time_content_updated'
        time_created = 'time_created'
        time_updated = 'time_updated'
        claim_objective = 'claim_objective'
        content_type = 'content_type'
        dataset_id = 'dataset_id'
        event_source_group = 'event_source_group'
        list_of_accounts = 'list_of_accounts'
        origin_audience_id = 'origin_audience_id'
        prefill = 'prefill'
        product_set_id = 'product_set_id'

    class ClaimObjective:
        product = 'PRODUCT'
        travel = 'TRAVEL'

    class ContentType:
        hotel = 'HOTEL'
        flight = 'FLIGHT'

    class Subtype:
        custom = 'CUSTOM'
        website = 'WEBSITE'
        app = 'APP'
        offline = 'OFFLINE'
        claim = 'CLAIM'
        partner = 'PARTNER'
        managed = 'MANAGED'
        video = 'VIDEO'
        lookalike = 'LOOKALIKE'
        engagement = 'ENGAGEMENT'
        data_set = 'DATA_SET'
        bag_of_accounts = 'BAG_OF_ACCOUNTS'

    class Fields:
        id = 'id'
        account_id = 'account_id'
        approximate_count = 'approximate_count'
        data_source = 'data_source'
        delivery_status = 'delivery_status'
        description = 'description'
        external_event_source = 'external_event_source'
        last_used_time = 'last_used_time'
        lookalike_audience_ids = 'lookalike_audience_ids'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        operation_status = 'operation_status'
        opt_out_link = 'opt_out_link'
        owner_business = 'owner_business'
        permission_for_actions = 'permission_for_actions'
        pixel_id = 'pixel_id'
        retention_days = 'retention_days'
        rule = 'rule'
        subtype = 'subtype'
        time_content_updated = 'time_content_updated'
        time_created = 'time_created'
        time_updated = 'time_updated'

    @classmethod
    def get_endpoint(cls):
        return 'customaudiences'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_custom_audience(fields, params, batch, pending)

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
            target_class=CustomAudience,
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
            'claim_objective': 'claim_objective_enum',
            'content_type': 'content_type_enum',
            'description': 'string',
            'event_source_group': 'string',
            'lookalike_spec': 'string',
            'name': 'string',
            'opt_out_link': 'string',
            'product_set_id': 'string',
            'retention_days': 'unsigned int',
            'rule': 'string',
        }
        enums = {
            'claim_objective_enum': CustomAudience.ClaimObjective.__dict__.values(),
            'content_type_enum': CustomAudience.ContentType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudience,
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

    def delete_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adaccounts': 'list<string>',
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
            response_parser=ObjectParser(target_class=AbstractCrudObject),
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
            'permissions': 'string',
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
            response_parser=ObjectParser(target_class=AdAccount),
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
        from facebookads.adobjects.adaccount import AdAccount
        param_types = {
            'adaccounts': 'list<string>',
            'permissions': 'string',
            'replace': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adaccounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccount,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccount),
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

    def get_ads(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.ad import Ad
        param_types = {
            'effective_status': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Ad,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Ad),
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

    def get_prefills(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.customaudienceprefillstate import CustomAudiencePrefillState
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/prefills',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudiencePrefillState,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudiencePrefillState),
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

    def get_sessions(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.customaudiencesession import CustomAudienceSession
        param_types = {
            'session_id': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sessions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudienceSession,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudienceSession),
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

    def delete_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'payload': 'Object',
            'session': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
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

    def create_user(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.user import User
        param_types = {
            'payload': 'Object',
            'session': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=User,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=User),
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
        'account_id': 'string',
        'approximate_count': 'int',
        'data_source': 'CustomAudienceDataSource',
        'delivery_status': 'CustomAudienceStatus',
        'description': 'string',
        'external_event_source': 'AdsPixel',
        'id': 'string',
        'last_used_time': 'datetime',
        'lookalike_audience_ids': 'list<string>',
        'lookalike_spec': 'LookalikeSpec',
        'name': 'string',
        'operation_status': 'CustomAudienceStatus',
        'opt_out_link': 'string',
        'owner_business': 'Business',
        'permission_for_actions': 'CustomAudiencePermission',
        'pixel_id': 'string',
        'retention_days': 'int',
        'rule': 'string',
        'subtype': 'string',
        'time_content_updated': 'unsigned int',
        'time_created': 'unsigned int',
        'time_updated': 'unsigned int',
        'claim_objective': 'ClaimObjective',
        'content_type': 'ContentType',
        'dataset_id': 'string',
        'event_source_group': 'string',
        'list_of_accounts': 'list<unsigned int>',
        'origin_audience_id': 'string',
        'prefill': 'bool',
        'product_set_id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ClaimObjective'] = CustomAudience.ClaimObjective.__dict__.values()
        field_enum_info['ContentType'] = CustomAudience.ContentType.__dict__.values()
        field_enum_info['Subtype'] = CustomAudience.Subtype.__dict__.values()
        field_enum_info['Fields'] = CustomAudience.Fields.__dict__.values()
        return field_enum_info
