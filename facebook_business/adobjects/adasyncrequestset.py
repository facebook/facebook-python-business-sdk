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

class AdAsyncRequestSet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAsyncRequestSet = True
        super(AdAsyncRequestSet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        canceled_count = 'canceled_count'
        created_time = 'created_time'
        error_count = 'error_count'
        id = 'id'
        in_progress_count = 'in_progress_count'
        initial_count = 'initial_count'
        is_completed = 'is_completed'
        name = 'name'
        notification_mode = 'notification_mode'
        notification_result = 'notification_result'
        notification_status = 'notification_status'
        notification_uri = 'notification_uri'
        owner_id = 'owner_id'
        success_count = 'success_count'
        total_count = 'total_count'
        updated_time = 'updated_time'
        ad_specs = 'ad_specs'

    class NotificationMode:
        off = 'OFF'
        on_complete = 'ON_COMPLETE'

    class NotificationStatus:
        not_sent = 'NOT_SENT'
        sending = 'SENDING'
        sent = 'SENT'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'asyncadrequestsets'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_async_ad_request_set(fields, params, batch, pending)

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
            target_class=AdAsyncRequestSet,
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

    def get_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adasyncrequest import AdAsyncRequest
        param_types = {
            'statuses': 'list<statuses_enum>',
        }
        enums = {
            'statuses_enum': AdAsyncRequest.Statuses.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAsyncRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAsyncRequest, api=self._api),
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
        'canceled_count': 'int',
        'created_time': 'datetime',
        'error_count': 'int',
        'id': 'string',
        'in_progress_count': 'int',
        'initial_count': 'unsigned int',
        'is_completed': 'bool',
        'name': 'string',
        'notification_mode': 'NotificationMode',
        'notification_result': 'AdAsyncRequestSetNotificationResult',
        'notification_status': 'NotificationStatus',
        'notification_uri': 'string',
        'owner_id': 'string',
        'success_count': 'int',
        'total_count': 'unsigned int',
        'updated_time': 'datetime',
        'ad_specs': 'list<map>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['NotificationMode'] = AdAsyncRequestSet.NotificationMode.__dict__.values()
        field_enum_info['NotificationStatus'] = AdAsyncRequestSet.NotificationStatus.__dict__.values()
        return field_enum_info
