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

class CustomConversion(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCustomConversion = True
        super(CustomConversion, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        aggregation_rule = 'aggregation_rule'
        creation_time = 'creation_time'
        custom_event_type = 'custom_event_type'
        data_sources = 'data_sources'
        default_conversion_value = 'default_conversion_value'
        description = 'description'
        event_source_type = 'event_source_type'
        first_fired_time = 'first_fired_time'
        id = 'id'
        is_archived = 'is_archived'
        last_fired_time = 'last_fired_time'
        name = 'name'
        offline_conversion_data_set = 'offline_conversion_data_set'
        pixel = 'pixel'
        retention_days = 'retention_days'
        rule = 'rule'
        advanced_rule = 'advanced_rule'
        event_source_id = 'event_source_id'

    class CustomEventType:
        add_payment_info = 'ADD_PAYMENT_INFO'
        add_to_cart = 'ADD_TO_CART'
        add_to_wishlist = 'ADD_TO_WISHLIST'
        complete_registration = 'COMPLETE_REGISTRATION'
        content_view = 'CONTENT_VIEW'
        initiated_checkout = 'INITIATED_CHECKOUT'
        lead = 'LEAD'
        purchase = 'PURCHASE'
        search = 'SEARCH'
        contact = 'CONTACT'
        customize_product = 'CUSTOMIZE_PRODUCT'
        donate = 'DONATE'
        find_location = 'FIND_LOCATION'
        schedule = 'SCHEDULE'
        start_trial = 'START_TRIAL'
        submit_application = 'SUBMIT_APPLICATION'
        subscribe = 'SUBSCRIBE'
        take_survey = 'TAKE_SURVEY'
        other = 'OTHER'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'customconversions'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_custom_conversion(fields, params, batch, pending)

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
            target_class=CustomConversion,
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
            'default_conversion_value': 'float',
            'description': 'string',
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
            target_class=CustomConversion,
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
            'end_time': 'Object',
            'event_type': 'event_type_enum',
            'start_time': 'Object',
        }
        enums = {
            'event_type_enum': [
                'conversion_create',
                'conversion_delete',
                'conversion_update',
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

    def create_ad_account(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
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

    def delete_shared_agencies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
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

    def create_shared_agency(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/shared_agencies',
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

    def get_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversionstatsresult import CustomConversionStatsResult
        param_types = {
            'aggregation': 'aggregation_enum',
            'end_time': 'datetime',
            'start_time': 'datetime',
        }
        enums = {
            'aggregation_enum': CustomConversionStatsResult.Aggregation.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomConversionStatsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomConversionStatsResult, api=self._api),
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
        'aggregation_rule': 'string',
        'creation_time': 'datetime',
        'custom_event_type': 'CustomEventType',
        'data_sources': 'list<ExternalEventSource>',
        'default_conversion_value': 'int',
        'description': 'string',
        'event_source_type': 'string',
        'first_fired_time': 'datetime',
        'id': 'string',
        'is_archived': 'bool',
        'last_fired_time': 'datetime',
        'name': 'string',
        'offline_conversion_data_set': 'OfflineConversionDataSet',
        'pixel': 'AdsPixel',
        'retention_days': 'unsigned int',
        'rule': 'string',
        'advanced_rule': 'string',
        'event_source_id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CustomEventType'] = CustomConversion.CustomEventType.__dict__.values()
        return field_enum_info
