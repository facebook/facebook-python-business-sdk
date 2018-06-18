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

class AdStudy(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdStudy = True
        super(AdStudy, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        business = 'business'
        canceled_time = 'canceled_time'
        cooldown_start_time = 'cooldown_start_time'
        created_by = 'created_by'
        created_time = 'created_time'
        description = 'description'
        end_time = 'end_time'
        id = 'id'
        name = 'name'
        observation_end_time = 'observation_end_time'
        results_first_available_date = 'results_first_available_date'
        start_time = 'start_time'
        type = 'type'
        updated_by = 'updated_by'
        updated_time = 'updated_time'
        cells = 'cells'
        client_business = 'client_business'
        confidence_level = 'confidence_level'
        objectives = 'objectives'
        viewers = 'viewers'

    class AudienceType:
        most_responsive = 'MOST_RESPONSIVE'
        not_most_responsive = 'NOT_MOST_RESPONSIVE'

    class Role:
        admin = 'ADMIN'
        analyst = 'ANALYST'

    class Type:
        lift = 'LIFT'
        split_test = 'SPLIT_TEST'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'ad_studies'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        return Business(api=self._api, fbid=parent_id).create_ad_study(fields, params, batch, pending)

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
            target_class=AdStudy,
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
            'cells': 'list<Object>',
            'client_business': 'string',
            'confidence_level': 'float',
            'cooldown_start_time': 'int',
            'description': 'string',
            'end_time': 'int',
            'name': 'string',
            'objectives': 'list<Object>',
            'observation_end_time': 'int',
            'start_time': 'int',
            'viewers': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudy,
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

    def create_custom_audience(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'audience_name': 'string',
            'audience_type': 'audience_type_enum',
            'cell_id': 'string',
            'objective_id': 'string',
        }
        enums = {
            'audience_type_enum': AdStudy.AudienceType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/customaudiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudy,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdStudy, api=self._api),
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

    def create_objective(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adstudyobjective import AdStudyObjective
        param_types = {
            'adspixels': 'list<Object>',
            'applications': 'list<Object>',
            'customconversions': 'list<Object>',
            'is_primary': 'bool',
            'name': 'string',
            'offline_conversion_data_sets': 'list<Object>',
            'offsitepixels': 'list<Object>',
            'type': 'type_enum',
        }
        enums = {
            'type_enum': AdStudyObjective.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/objectives',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudyObjective,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdStudyObjective, api=self._api),
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
            'business': 'string',
            'email': 'string',
            'user': 'int',
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

    def create_user_permission(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
            'email': 'string',
            'role': 'role_enum',
            'user': 'int',
        }
        enums = {
            'role_enum': AdStudy.Role.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/userpermissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudy,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdStudy, api=self._api),
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
        'business': 'Business',
        'canceled_time': 'datetime',
        'cooldown_start_time': 'datetime',
        'created_by': 'User',
        'created_time': 'datetime',
        'description': 'string',
        'end_time': 'datetime',
        'id': 'string',
        'name': 'string',
        'observation_end_time': 'datetime',
        'results_first_available_date': 'string',
        'start_time': 'datetime',
        'type': 'string',
        'updated_by': 'User',
        'updated_time': 'datetime',
        'cells': 'list<Object>',
        'client_business': 'string',
        'confidence_level': 'float',
        'objectives': 'list<Object>',
        'viewers': 'list<int>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AudienceType'] = AdStudy.AudienceType.__dict__.values()
        field_enum_info['Role'] = AdStudy.Role.__dict__.values()
        field_enum_info['Type'] = AdStudy.Type.__dict__.values()
        return field_enum_info
