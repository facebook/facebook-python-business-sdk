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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class LeadgenForm(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isLeadgenForm = True
        super(LeadgenForm, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        allow_organic_lead = 'allow_organic_lead'
        context_card = 'context_card'
        continued_flow_request_method = 'continued_flow_request_method'
        created_time = 'created_time'
        creator = 'creator'
        creator_id = 'creator_id'
        cusomized_tcpa_content = 'cusomized_tcpa_content'
        expired_leads_count = 'expired_leads_count'
        follow_up_action_text = 'follow_up_action_text'
        follow_up_action_url = 'follow_up_action_url'
        id = 'id'
        is_continued_flow = 'is_continued_flow'
        leadgen_export_csv_url = 'leadgen_export_csv_url'
        leads_count = 'leads_count'
        legal_content = 'legal_content'
        locale = 'locale'
        messenger_welcome_message = 'messenger_welcome_message'
        name = 'name'
        page = 'page'
        page_id = 'page_id'
        privacy_policy_url = 'privacy_policy_url'
        qualifiers = 'qualifiers'
        questions = 'questions'
        status = 'status'
        tcpa_compliance = 'tcpa_compliance'

    @classmethod
    def get_endpoint(cls):
        return 'leadgen_forms'

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
            target_class=LeadgenForm,
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

    def get_leads(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.lead import Lead
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Lead,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Lead),
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

    def create_test_lead(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'custom_disclaimer_responses': 'list<Object>',
            'field_data': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/test_leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadgenForm,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadgenForm),
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
        'allow_organic_lead': 'bool',
        'context_card': 'Object',
        'continued_flow_request_method': 'string',
        'created_time': 'datetime',
        'creator': 'User',
        'creator_id': 'int',
        'cusomized_tcpa_content': 'string',
        'expired_leads_count': 'unsigned int',
        'follow_up_action_text': 'string',
        'follow_up_action_url': 'string',
        'id': 'string',
        'is_continued_flow': 'bool',
        'leadgen_export_csv_url': 'string',
        'leads_count': 'unsigned int',
        'legal_content': 'Object',
        'locale': 'string',
        'messenger_welcome_message': 'string',
        'name': 'string',
        'page': 'Object',
        'page_id': 'string',
        'privacy_policy_url': 'string',
        'qualifiers': 'list<LeadGenQualifier>',
        'questions': 'list<LeadGenQuestion>',
        'status': 'string',
        'tcpa_compliance': 'bool',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
