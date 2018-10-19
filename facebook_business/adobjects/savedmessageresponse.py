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

class SavedMessageResponse(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isSavedMessageResponse = True
        super(SavedMessageResponse, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        category = 'category'
        id = 'id'
        image = 'image'
        is_enabled = 'is_enabled'
        message = 'message'
        title = 'title'

    class Category:
        standard = 'STANDARD'
        instant_reply = 'INSTANT_REPLY'
        away_message = 'AWAY_MESSAGE'
        welcome_message = 'WELCOME_MESSAGE'
        follow_up = 'FOLLOW_UP'
        messenger_code = 'MESSENGER_CODE'
        referral = 'REFERRAL'
        appointment_reminder = 'APPOINTMENT_REMINDER'
        smart_reply_contact = 'SMART_REPLY_CONTACT'
        smart_reply_hours = 'SMART_REPLY_HOURS'
        smart_reply_location = 'SMART_REPLY_LOCATION'
        smart_reply_negative_feedback = 'SMART_REPLY_NEGATIVE_FEEDBACK'
        smart_reply_positive_feedback = 'SMART_REPLY_POSITIVE_FEEDBACK'
        job_application = 'JOB_APPLICATION'

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
            target_class=SavedMessageResponse,
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
            'message': 'string',
            'title': 'string',
            'image': 'string',
            'remove_image': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SavedMessageResponse,
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

    def get_macros(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.savedmessageresponsemacro import SavedMessageResponseMacro
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/macros',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SavedMessageResponseMacro,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SavedMessageResponseMacro, api=self._api),
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
        'category': 'string',
        'id': 'string',
        'image': 'string',
        'is_enabled': 'bool',
        'message': 'string',
        'title': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Category'] = SavedMessageResponse.Category.__dict__.values()
        return field_enum_info


