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
        data_source_types = 'data_source_types'
        delivery_status = 'delivery_status'
        description = 'description'
        excluded_custom_audiences = 'excluded_custom_audiences'
        expiry_time = 'expiry_time'
        external_event_source = 'external_event_source'
        household_audience = 'household_audience'
        id = 'id'
        included_custom_audiences = 'included_custom_audiences'
        is_household = 'is_household'
        is_snapshot = 'is_snapshot'
        is_value_based = 'is_value_based'
        list_of_accounts = 'list_of_accounts'
        lookalike_audience_ids = 'lookalike_audience_ids'
        lookalike_spec = 'lookalike_spec'
        name = 'name'
        operation_status = 'operation_status'
        opt_out_link = 'opt_out_link'
        permission_for_actions = 'permission_for_actions'
        pixel_id = 'pixel_id'
        retention_days = 'retention_days'
        rev_share_policy_id = 'rev_share_policy_id'
        rule = 'rule'
        rule_aggregation = 'rule_aggregation'
        rule_v2 = 'rule_v2'
        seed_audience = 'seed_audience'
        sharing_status = 'sharing_status'
        study_spec = 'study_spec'
        subtype = 'subtype'
        time_content_updated = 'time_content_updated'
        time_created = 'time_created'
        time_updated = 'time_updated'
        creation_params = 'creation_params'
        parent_audience_id = 'parent_audience_id'
        tags = 'tags'
        associated_audience_id = 'associated_audience_id'
        is_household_exclusion = 'is_household_exclusion'
        allowed_domains = 'allowed_domains'
        partner_reference_key = 'partner_reference_key'
        prefill = 'prefill'
        inclusions = 'inclusions'
        exclusions = 'exclusions'
        countries = 'countries'
        origin_audience_id = 'origin_audience_id'
        details = 'details'
        source = 'source'
        isprivate = 'isPrivate'
        additionalmetadata = 'additionalMetadata'
        minage = 'minAge'
        maxage = 'maxAge'
        expectedsize = 'expectedSize'
        gender = 'gender'
        partnerid = 'partnerID'
        accountid = 'accountID'
        claim_objective = 'claim_objective'
        content_type = 'content_type'
        event_source_group = 'event_source_group'
        product_set_id = 'product_set_id'
        event_sources = 'event_sources'
        video_group_ids = 'video_group_ids'
        dataset_id = 'dataset_id'

    class ClaimObjective:
        automotive_model = 'AUTOMOTIVE_MODEL'
        home_listing = 'HOME_LISTING'
        product = 'PRODUCT'
        travel = 'TRAVEL'
        vehicle = 'VEHICLE'
        vehicle_offer = 'VEHICLE_OFFER'

    class ContentType:
        automotive_model = 'AUTOMOTIVE_MODEL'
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
        bag_of_accounts = 'BAG_OF_ACCOUNTS'
        study_rule_audience = 'STUDY_RULE_AUDIENCE'
        fox = 'FOX'

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
            'ad_account_id': 'string',
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
            'description': 'string',
            'name': 'string',
            'opt_out_link': 'string',
            'parent_audience_id': 'unsigned int',
            'seed_audience': 'unsigned int',
            'tags': 'list<string>',
            'is_household': 'bool',
            'is_household_exclusion': 'bool',
            'allowed_domains': 'list<string>',
            'lookalike_spec': 'string',
            'retention_days': 'unsigned int',
            'customer_file_source': 'customer_file_source_enum',
            'rule': 'string',
            'rule_aggregation': 'string',
            'inclusions': 'list<Object>',
            'exclusions': 'list<Object>',
            'countries': 'string',
            'details': 'string',
            'source': 'string',
            'isPrivate': 'bool',
            'additionalMetadata': 'string',
            'minAge': 'unsigned int',
            'maxAge': 'unsigned int',
            'expectedSize': 'unsigned int',
            'gender': 'string',
            'partnerID': 'string',
            'accountID': 'string',
            'rev_share_policy_id': 'unsigned int',
            'partner_reference_key': 'string',
            'claim_objective': 'claim_objective_enum',
            'content_type': 'content_type_enum',
            'event_source_group': 'string',
            'product_set_id': 'string',
            'event_sources': 'list<map>',
            'study_spec': 'Object',
        }
        enums = {
            'customer_file_source_enum': CustomAudience.CustomerFileSource.__dict__.values(),
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

    def create_ad_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adaccounts': 'list<string>',
            'permissions': 'string',
            'replace': 'bool',
            'relationship_type': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adaccounts',
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

    def delete_capabilities(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adaccounts': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/capabilities',
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

    def create_capability(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'accounts_capabilities': 'string',
            'relationship_type': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/capabilities',
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

    def create_datum(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'action_type': 'action_type_enum',
            'encoding': 'encoding_enum',
            'entry_type': 'entry_type_enum',
            'entries': 'list<string>',
            'session_id': 'unsigned int',
            'batch_seq': 'unsigned int',
            'last_batch_flag': 'bool',
        }
        enums = {
            'action_type_enum': [
                'add',
                'remove',
                'match',
                'optout',
            ],
            'encoding_enum': [
                'md5',
                'sha256',
                'plain',
            ],
            'entry_type_enum': [
                '0',
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/data',
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

    def get_share_d_account_info(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudiencesharedaccountinfo import CustomAudiencesharedAccountInfo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shared_account_info',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudiencesharedAccountInfo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudiencesharedAccountInfo, api=self._api),
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

    def delete_upload(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'session': 'Object',
            'payload': 'Object',
            'namespace': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/upload',
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
            'session': 'Object',
            'payload': 'Object',
            'namespace': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/upload',
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

    def delete_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'session': 'Object',
            'payload': 'Object',
            'namespace': 'string',
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
        param_types = {
            'session': 'Object',
            'payload': 'Object',
            'namespace': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/users',
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

    _field_types = {
        'account_id': 'string',
        'approximate_count': 'int',
        'customer_file_source': 'string',
        'data_source': 'CustomAudienceDataSource',
        'data_source_types': 'string',
        'delivery_status': 'CustomAudienceStatus',
        'description': 'string',
        'excluded_custom_audiences': 'list<CustomAudience>',
        'expiry_time': 'unsigned int',
        'external_event_source': 'AdsPixel',
        'household_audience': 'int',
        'id': 'string',
        'included_custom_audiences': 'list<CustomAudience>',
        'is_household': 'bool',
        'is_snapshot': 'bool',
        'is_value_based': 'bool',
        'list_of_accounts': 'list<string>',
        'lookalike_audience_ids': 'list<string>',
        'lookalike_spec': 'LookalikeSpec',
        'name': 'string',
        'operation_status': 'CustomAudienceStatus',
        'opt_out_link': 'string',
        'permission_for_actions': 'AudiencePermissionForActions',
        'pixel_id': 'string',
        'retention_days': 'int',
        'rev_share_policy_id': 'unsigned int',
        'rule': 'string',
        'rule_aggregation': 'string',
        'rule_v2': 'string',
        'seed_audience': 'int',
        'sharing_status': 'CustomAudienceSharingStatus',
        'study_spec': 'AudienceInsightsStudySpec',
        'subtype': 'string',
        'time_content_updated': 'unsigned int',
        'time_created': 'unsigned int',
        'time_updated': 'unsigned int',
        'creation_params': 'map',
        'parent_audience_id': 'unsigned int',
        'tags': 'list<string>',
        'associated_audience_id': 'unsigned int',
        'is_household_exclusion': 'bool',
        'allowed_domains': 'list<string>',
        'partner_reference_key': 'string',
        'prefill': 'bool',
        'inclusions': 'list<Object>',
        'exclusions': 'list<Object>',
        'countries': 'string',
        'origin_audience_id': 'string',
        'details': 'string',
        'source': 'string',
        'isPrivate': 'bool',
        'additionalMetadata': 'string',
        'minAge': 'unsigned int',
        'maxAge': 'unsigned int',
        'expectedSize': 'unsigned int',
        'gender': 'string',
        'partnerID': 'string',
        'accountID': 'string',
        'claim_objective': 'ClaimObjective',
        'content_type': 'ContentType',
        'event_source_group': 'string',
        'product_set_id': 'string',
        'event_sources': 'list<map>',
        'video_group_ids': 'list<string>',
        'dataset_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ClaimObjective'] = CustomAudience.ClaimObjective.__dict__.values()
        field_enum_info['ContentType'] = CustomAudience.ContentType.__dict__.values()
        field_enum_info['CustomerFileSource'] = CustomAudience.CustomerFileSource.__dict__.values()
        field_enum_info['Subtype'] = CustomAudience.Subtype.__dict__.values()
        return field_enum_info


