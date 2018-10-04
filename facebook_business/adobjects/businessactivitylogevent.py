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

class BusinessActivityLogEvent(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusinessActivityLogEvent = True
        super(BusinessActivityLogEvent, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        acted_upon_business_id = 'acted_upon_business_id'
        acted_upon_business_name = 'acted_upon_business_name'
        acted_upon_business_object_id = 'acted_upon_business_object_id'
        acted_upon_business_object_name = 'acted_upon_business_object_name'
        acted_upon_business_object_type = 'acted_upon_business_object_type'
        acted_upon_user_id = 'acted_upon_user_id'
        acted_upon_user_name = 'acted_upon_user_name'
        acting_business_id = 'acting_business_id'
        acting_business_name = 'acting_business_name'
        acting_user_id = 'acting_user_id'
        acting_user_name = 'acting_user_name'
        event_time = 'event_time'
        event_type = 'event_type'
        extra_data = 'extra_data'
        target_business_id = 'target_business_id'
        target_business_name = 'target_business_name'
        target_business_object_id = 'target_business_object_id'
        target_business_object_name = 'target_business_object_name'
        target_business_object_type = 'target_business_object_type'
        id = 'id'

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
            target_class=BusinessActivityLogEvent,
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

    _field_types = {
        'acted_upon_business_id': 'string',
        'acted_upon_business_name': 'string',
        'acted_upon_business_object_id': 'string',
        'acted_upon_business_object_name': 'string',
        'acted_upon_business_object_type': 'string',
        'acted_upon_user_id': 'string',
        'acted_upon_user_name': 'string',
        'acting_business_id': 'string',
        'acting_business_name': 'string',
        'acting_user_id': 'string',
        'acting_user_name': 'string',
        'event_time': 'unsigned int',
        'event_type': 'string',
        'extra_data': 'list<Object>',
        'target_business_id': 'string',
        'target_business_name': 'string',
        'target_business_object_id': 'string',
        'target_business_object_name': 'string',
        'target_business_object_type': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


