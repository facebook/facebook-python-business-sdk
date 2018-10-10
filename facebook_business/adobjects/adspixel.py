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
from facebook_business.adobjects.helpers.adspixelmixin import AdsPixelMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdsPixel(
    AdsPixelMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsPixel = True
        super(AdsPixel, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        can_proxy = 'can_proxy'
        code = 'code'
        creation_time = 'creation_time'
        creator = 'creator'
        data_use_setting = 'data_use_setting'
        first_party_cookie_status = 'first_party_cookie_status'
        id = 'id'
        is_created_by_business = 'is_created_by_business'
        last_fired_time = 'last_fired_time'
        name = 'name'
        owner_ad_account = 'owner_ad_account'
        owner_business = 'owner_business'

    class SortBy:
        last_fired_time = 'LAST_FIRED_TIME'
        name = 'NAME'

    class DataUseSetting:
        empty = 'EMPTY'
        advertising_and_analytics = 'ADVERTISING_AND_ANALYTICS'
        analytics_only = 'ANALYTICS_ONLY'

    class FirstPartyCookieStatus:
        empty = 'EMPTY'
        first_party_cookie_enabled = 'FIRST_PARTY_COOKIE_ENABLED'
        first_party_cookie_disabled = 'FIRST_PARTY_COOKIE_DISABLED'

    class Tasks:
        edit = 'EDIT'
        analyze = 'ANALYZE'

    class Type:
        primary = 'PRIMARY'
        secondary = 'SECONDARY'

    class RelationshipType:
        ad_manager = 'AD_MANAGER'
        audience_manager = 'AUDIENCE_MANAGER'
        agency = 'AGENCY'
        other = 'OTHER'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adspixels'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ads_pixel(fields, params, batch, pending)

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
            target_class=AdsPixel,
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
            'first_party_cookie_status': 'first_party_cookie_status_enum',
            'data_use_setting': 'data_use_setting_enum',
        }
        enums = {
            'first_party_cookie_status_enum': AdsPixel.FirstPartyCookieStatus.__dict__.values(),
            'data_use_setting_enum': AdsPixel.DataUseSetting.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
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

    def delete_assigned_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/assigned_users',
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

    def get_assigned_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.assigneduser import AssignedUser
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AssignedUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AssignedUser, api=self._api),
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

    def create_assigned_user(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'tasks': 'list<tasks_enum>',
            'business': 'string',
        }
        enums = {
            'tasks_enum': AdsPixel.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/assigned_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
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

    def create_create_server_to_server_key(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/create_server_to_server_keys',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
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

    def get_extractors(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.signalsiwlextractor import SignalsIWLExtractor
        param_types = {
            'current_domain': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/extractors',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SignalsIWLExtractor,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SignalsIWLExtractor, api=self._api),
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

    def create_extractor(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.signalsiwlextractor import SignalsIWLExtractor
        param_types = {
            'domain_uri': 'Object',
            'event_type': 'event_type_enum',
            'extractor_config': 'map',
            'extractor_type': 'extractor_type_enum',
        }
        enums = {
            'event_type_enum': SignalsIWLExtractor.EventType.__dict__.values(),
            'extractor_type_enum': SignalsIWLExtractor.ExtractorType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/extractors',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SignalsIWLExtractor,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SignalsIWLExtractor, api=self._api),
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

    def get_pending_share_d_agencies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pending_shared_agencies',
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

    def create_reset_server_to_server_key(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': AdsPixel.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/reset_server_to_server_key',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
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

    def delete_share_d_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/shared_accounts',
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

    def get_share_d_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shared_accounts',
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

    def create_share_d_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/shared_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
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

    def delete_share_d_agencies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'agency_id': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/shared_agencies',
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

    def get_share_d_agencies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shared_agencies',
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

    def create_share_d_agency(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'agency_id': 'string',
            'business': 'string',
            'relationship_type': 'list<relationship_type_enum>',
            'other_relationship': 'string',
        }
        enums = {
            'relationship_type_enum': AdsPixel.RelationshipType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/shared_agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
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
        from facebook_business.adobjects.adspixelstatsresult import AdsPixelStatsResult
        param_types = {
            'start_time': 'Object',
            'end_time': 'Object',
            'aggregation': 'aggregation_enum',
            'event': 'string',
        }
        enums = {
            'aggregation_enum': AdsPixelStatsResult.Aggregation.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelStatsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelStatsResult, api=self._api),
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
        'can_proxy': 'bool',
        'code': 'string',
        'creation_time': 'datetime',
        'creator': 'User',
        'data_use_setting': 'string',
        'first_party_cookie_status': 'string',
        'id': 'string',
        'is_created_by_business': 'bool',
        'last_fired_time': 'datetime',
        'name': 'string',
        'owner_ad_account': 'AdAccount',
        'owner_business': 'Business',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['SortBy'] = AdsPixel.SortBy.__dict__.values()
        field_enum_info['DataUseSetting'] = AdsPixel.DataUseSetting.__dict__.values()
        field_enum_info['FirstPartyCookieStatus'] = AdsPixel.FirstPartyCookieStatus.__dict__.values()
        field_enum_info['Tasks'] = AdsPixel.Tasks.__dict__.values()
        field_enum_info['Type'] = AdsPixel.Type.__dict__.values()
        field_enum_info['RelationshipType'] = AdsPixel.RelationshipType.__dict__.values()
        return field_enum_info


