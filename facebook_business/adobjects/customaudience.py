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
from facebook_business.adobjects.helpers.customaudiencemixin import CustomAudienceMixin

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
        customer_file_source = 'customer_file_source'
        data_source = 'data_source'
        delivery_status = 'delivery_status'
        description = 'description'
        external_event_source = 'external_event_source'
        id = 'id'
        is_value_based = 'is_value_based'
        lookalike_audience_ids = 'lookalike_audience_ids'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        operation_status = 'operation_status'
        opt_out_link = 'opt_out_link'
        permission_for_actions = 'permission_for_actions'
        pixel_id = 'pixel_id'
        retention_days = 'retention_days'
        rule = 'rule'
        rule_aggregation = 'rule_aggregation'
        subtype = 'subtype'
        time_content_updated = 'time_content_updated'
        time_created = 'time_created'
        time_updated = 'time_updated'
        allowed_domains = 'allowed_domains'
        claim_objective = 'claim_objective'
        content_type = 'content_type'
        dataset_id = 'dataset_id'
        event_source_group = 'event_source_group'
        event_sources = 'event_sources'
        list_of_accounts = 'list_of_accounts'
        origin_audience_id = 'origin_audience_id'
        prefill = 'prefill'
        product_set_id = 'product_set_id'
        associated_audience_id = 'associated_audience_id'
        creation_params = 'creation_params'
        exclusions = 'exclusions'
        inclusions = 'inclusions'
        parent_audience_id = 'parent_audience_id'
        tags = 'tags'

    class ClaimObjective:
        auto_offer = 'AUTO_OFFER'
        home_listing = 'HOME_LISTING'
        product = 'PRODUCT'
        travel = 'TRAVEL'
        vehicle = 'VEHICLE'

    class ContentType:
        destination = 'DESTINATION'
        flight = 'FLIGHT'
        home_listing = 'HOME_LISTING'
        hotel = 'HOTEL'
        media_title = 'MEDIA_TITLE'
        product = 'PRODUCT'
        vehicle = 'VEHICLE'
        vehicle_offer = 'VEHICLE_OFFER'

    class CustomerFileSource:
        user_provided_only = 'USER_PROVIDED_ONLY'
        partner_provided_only = 'PARTNER_PROVIDED_ONLY'
        both_user_and_partner_provided = 'BOTH_USER_AND_PARTNER_PROVIDED'

    class Subtype:
        custom = 'CUSTOM'
        website = 'WEBSITE'
        app = 'APP'
        offline_conversion = 'OFFLINE_CONVERSION'
        claim = 'CLAIM'
        partner = 'PARTNER'
        managed = 'MANAGED'
        video = 'VIDEO'
        lookalike = 'LOOKALIKE'
        engagement = 'ENGAGEMENT'
        data_set = 'DATA_SET'
        bag_of_accounts = 'BAG_OF_ACCOUNTS'
        study_rule_audience = 'STUDY_RULE_AUDIENCE'
        fox = 'FOX'

    class Fields:
        account_id = 'account_id'
        approximate_count = 'approximate_count'
        customer_file_source = 'customer_file_source'
        data_source = 'data_source'
        delivery_status = 'delivery_status'
        description = 'description'
        external_event_source = 'external_event_source'
        id = 'id'
        is_value_based = 'is_value_based'
        lookalike_audience_ids = 'lookalike_audience_ids'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        operation_status = 'operation_status'
        opt_out_link = 'opt_out_link'
        permission_for_actions = 'permission_for_actions'
        pixel_id = 'pixel_id'
        retention_days = 'retention_days'
        rule = 'rule'
        rule_aggregation = 'rule_aggregation'
        subtype = 'subtype'
        time_content_updated = 'time_content_updated'
        time_created = 'time_created'
        time_updated = 'time_updated'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'customaudiences'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
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
            'allowed_domains': 'list<string>',
            'claim_objective': 'claim_objective_enum',
            'content_type': 'content_type_enum',
            'customer_file_source': 'customer_file_source_enum',
            'description': 'string',
            'event_source_group': 'string',
            'event_sources': 'list<map>',
            'lookalike_spec': 'string',
            'name': 'string',
            'opt_out_link': 'string',
            'product_set_id': 'string',
            'retention_days': 'unsigned int',
            'rule': 'string',
            'rule_aggregation': 'string',
        }
        enums = {
            'claim_objective_enum': CustomAudience.ClaimObjective.__dict__.values(),
            'content_type_enum': CustomAudience.ContentType.__dict__.values(),
            'customer_file_source_enum': CustomAudience.CustomerFileSource.__dict__.values(),
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

    def create_ad_account(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
            'adaccounts': 'list<string>',
            'permissions': 'string',
            'relationship_type': 'list<string>',
            'replace': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/ad_accounts',
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

    def get_ads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.ad import Ad
        param_types = {
            'effective_status': 'list<string>',
            'status': 'list<string>',
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
            response_parser=ObjectParser(target_class=Ad, api=self._api),
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
        from facebook_business.adobjects.customaudienceprefillstate import CustomAudiencePrefillState
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
            response_parser=ObjectParser(target_class=CustomAudiencePrefillState, api=self._api),
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
        from facebook_business.adobjects.customaudiencesession import CustomAudienceSession
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
            response_parser=ObjectParser(target_class=CustomAudienceSession, api=self._api),
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
            'namespace': 'string',
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

    def create_user(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
            'namespace': 'string',
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
            response_parser=ObjectParser(target_class=User, api=self._api),
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
        'customer_file_source': 'string',
        'data_source': 'CustomAudienceDataSource',
        'delivery_status': 'CustomAudienceStatus',
        'description': 'string',
        'external_event_source': 'AdsPixel',
        'id': 'string',
        'is_value_based': 'bool',
        'lookalike_audience_ids': 'list<string>',
        'lookalike_spec': 'LookalikeSpec',
        'name': 'string',
        'operation_status': 'CustomAudienceStatus',
        'opt_out_link': 'string',
        'permission_for_actions': 'CustomAudiencePermission',
        'pixel_id': 'string',
        'retention_days': 'int',
        'rule': 'string',
        'rule_aggregation': 'string',
        'subtype': 'string',
        'time_content_updated': 'unsigned int',
        'time_created': 'unsigned int',
        'time_updated': 'unsigned int',
        'allowed_domains': 'list<string>',
        'claim_objective': 'ClaimObjective',
        'content_type': 'ContentType',
        'dataset_id': 'string',
        'event_source_group': 'string',
        'event_sources': 'list<map>',
        'list_of_accounts': 'list<unsigned int>',
        'origin_audience_id': 'string',
        'prefill': 'bool',
        'product_set_id': 'string',
        'associated_audience_id': 'unsigned int',
        'creation_params': 'map',
        'exclusions': 'list<Object>',
        'inclusions': 'list<Object>',
        'parent_audience_id': 'unsigned int',
        'tags': 'list<string>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ClaimObjective'] = CustomAudience.ClaimObjective.__dict__.values()
        field_enum_info['ContentType'] = CustomAudience.ContentType.__dict__.values()
        field_enum_info['CustomerFileSource'] = CustomAudience.CustomerFileSource.__dict__.values()
        field_enum_info['Subtype'] = CustomAudience.Subtype.__dict__.values()
        field_enum_info['Fields'] = CustomAudience.Fields.__dict__.values()
        return field_enum_info
