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

class AdAccountAdRulesHistory(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountAdRulesHistory = True
        super(AdAccountAdRulesHistory, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        evaluation_spec = 'evaluation_spec'
        exception_code = 'exception_code'
        exception_message = 'exception_message'
        execution_spec = 'execution_spec'
        is_manual = 'is_manual'
        results = 'results'
        rule_id = 'rule_id'
        schedule_spec = 'schedule_spec'
        timestamp = 'timestamp'
        id = 'id'

    class Action:
        budget_not_redistributed = 'BUDGET_NOT_REDISTRIBUTED'
        changed_bid = 'CHANGED_BID'
        changed_budget = 'CHANGED_BUDGET'
        email = 'EMAIL'
        endpoint_pinged = 'ENDPOINT_PINGED'
        error = 'ERROR'
        facebook_notification_sent = 'FACEBOOK_NOTIFICATION_SENT'
        message_sent = 'MESSAGE_SENT'
        not_changed = 'NOT_CHANGED'
        paused = 'PAUSED'
        unpaused = 'UNPAUSED'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'action': 'action_enum',
            'hide_no_changes': 'bool',
            'object_id': 'string',
        }
        enums = {
            'action_enum': [
                'BUDGET_NOT_REDISTRIBUTED',
                'CHANGED_BID',
                'CHANGED_BUDGET',
                'EMAIL',
                'ENDPOINT_PINGED',
                'ERROR',
                'FACEBOOK_NOTIFICATION_SENT',
                'MESSAGE_SENT',
                'NOT_CHANGED',
                'PAUSED',
                'UNPAUSED',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountAdRulesHistory,
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
        'evaluation_spec': 'AdRuleEvaluationSpec',
        'exception_code': 'int',
        'exception_message': 'string',
        'execution_spec': 'AdRuleExecutionSpec',
        'is_manual': 'bool',
        'results': 'list<AdRuleHistoryResult>',
        'rule_id': 'int',
        'schedule_spec': 'AdRuleScheduleSpec',
        'timestamp': 'datetime',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Action'] = AdAccountAdRulesHistory.Action.__dict__.values()
        return field_enum_info


