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

class AdRuleTrigger(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdRuleTrigger, self).__init__()
        self._isAdRuleTrigger = True
        self._api = api

    class Field(AbstractObject.Field):
        field = 'field'
        operator = 'operator'
        type = 'type'
        value = 'value'

    class Operator:
        all = 'ALL'
        any = 'ANY'
        contain = 'CONTAIN'
        equal = 'EQUAL'
        greater_than = 'GREATER_THAN'
        value_in = 'IN'
        in_range = 'IN_RANGE'
        less_than = 'LESS_THAN'
        none = 'NONE'
        not_contain = 'NOT_CONTAIN'
        not_equal = 'NOT_EQUAL'
        not_in = 'NOT_IN'
        not_in_range = 'NOT_IN_RANGE'

    class Type:
        delivery_insights_change = 'DELIVERY_INSIGHTS_CHANGE'
        metadata_creation = 'METADATA_CREATION'
        metadata_update = 'METADATA_UPDATE'
        stats_change = 'STATS_CHANGE'
        stats_milestone = 'STATS_MILESTONE'

    _field_types = {
        'field': 'string',
        'operator': 'Operator',
        'type': 'Type',
        'value': 'Object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Operator'] = AdRuleTrigger.Operator.__dict__.values()
        field_enum_info['Type'] = AdRuleTrigger.Type.__dict__.values()
        return field_enum_info


