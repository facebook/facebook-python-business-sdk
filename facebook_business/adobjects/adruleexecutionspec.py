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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdRuleExecutionSpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdRuleExecutionSpec, self).__init__()
        self._isAdRuleExecutionSpec = True
        self._api = api

    class Field(AbstractObject.Field):
        execution_options = 'execution_options'
        execution_type = 'execution_type'

    class ExecutionType:
        add_interest_relaxation = 'ADD_INTEREST_RELAXATION'
        add_questionnaire_interests = 'ADD_QUESTIONNAIRE_INTERESTS'
        change_bid = 'CHANGE_BID'
        change_budget = 'CHANGE_BUDGET'
        change_campaign_budget = 'CHANGE_CAMPAIGN_BUDGET'
        increase_radius = 'INCREASE_RADIUS'
        notification = 'NOTIFICATION'
        pause = 'PAUSE'
        ping_endpoint = 'PING_ENDPOINT'
        rebalance_budget = 'REBALANCE_BUDGET'
        rotate = 'ROTATE'
        unpause = 'UNPAUSE'
        update_creative = 'UPDATE_CREATIVE'

    _field_types = {
        'execution_options': 'list<AdRuleExecutionOptions>',
        'execution_type': 'ExecutionType',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ExecutionType'] = AdRuleExecutionSpec.ExecutionType.__dict__.values()
        return field_enum_info


