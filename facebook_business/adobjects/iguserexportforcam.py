# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

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

class IGUserExportForCAM(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isIGUserExportForCAM = True
        super(IGUserExportForCAM, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        age_bucket = 'age_bucket'
        biography = 'biography'
        country = 'country'
        email = 'email'
        gender = 'gender'
        id = 'id'
        is_account_verified = 'is_account_verified'
        is_paid_partnership_messages_enabled = 'is_paid_partnership_messages_enabled'
        messaging_id = 'messaging_id'
        onboarded_status = 'onboarded_status'
        portfolio_url = 'portfolio_url'
        username = 'username'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            target_class=IGUserExportForCAM,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_branded_content_media(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/branded_content_media',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        if is_async:
          return self.get_insights_async(fields, params, batch, success, failure, pending)
        param_types = {
            'breakdown': 'breakdown_enum',
            'metrics': 'list<metrics_enum>',
            'period': 'period_enum',
            'time_range': 'time_range_enum',
        }
        enums = {
            'breakdown_enum': [
                'AGE',
                'FOLLOW_TYPE',
                'GENDER',
                'MEDIA_TYPE',
                'TOP_CITIES',
                'TOP_COUNTRIES',
            ],
            'metrics_enum': [
                'CREATOR_ENGAGED_ACCOUNTS',
                'CREATOR_REACH',
                'REELS_HOOK_RATE',
                'REELS_INTERACTION_RATE',
                'TOTAL_FOLLOWERS',
            ],
            'period_enum': [
                'DAY',
                'OVERALL',
            ],
            'time_range_enum': [
                'LAST_14_DAYS',
                'LAST_90_DAYS',
                'LIFETIME',
                'THIS_MONTH',
                'THIS_WEEK',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_recent_media(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/recent_media',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'age_bucket': 'string',
        'biography': 'string',
        'country': 'string',
        'email': 'string',
        'gender': 'string',
        'id': 'string',
        'is_account_verified': 'bool',
        'is_paid_partnership_messages_enabled': 'bool',
        'messaging_id': 'string',
        'onboarded_status': 'bool',
        'portfolio_url': 'string',
        'username': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


