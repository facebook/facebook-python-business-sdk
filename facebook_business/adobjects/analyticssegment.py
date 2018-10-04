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

class AnalyticsSegment(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAnalyticsSegment = True
        super(AnalyticsSegment, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        custom_audience_ineligiblity_reasons = 'custom_audience_ineligiblity_reasons'
        description = 'description'
        estimated_custom_audience_size = 'estimated_custom_audience_size'
        event_info_rules = 'event_info_rules'
        event_rules = 'event_rules'
        event_source = 'event_source'
        filter_set = 'filter_set'
        has_demographic_rules = 'has_demographic_rules'
        id = 'id'
        is_all_user = 'is_all_user'
        is_eligible_for_push_campaign = 'is_eligible_for_push_campaign'
        is_internal = 'is_internal'
        name = 'name'
        percentile_rules = 'percentile_rules'
        push_backfill_status = 'push_backfill_status'
        time_last_seen = 'time_last_seen'
        time_last_updated = 'time_last_updated'
        user_property_rules = 'user_property_rules'
        web_param_rules = 'web_param_rules'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'async_task_id': 'string',
            'end_date': 'int',
            'start_date': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AnalyticsSegment,
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
        'custom_audience_ineligiblity_reasons': 'list<string>',
        'description': 'string',
        'estimated_custom_audience_size': 'unsigned int',
        'event_info_rules': 'list<Object>',
        'event_rules': 'list<Object>',
        'event_source': 'ExternalEventSource',
        'filter_set': 'string',
        'has_demographic_rules': 'bool',
        'id': 'string',
        'is_all_user': 'bool',
        'is_eligible_for_push_campaign': 'bool',
        'is_internal': 'bool',
        'name': 'string',
        'percentile_rules': 'list<Object>',
        'push_backfill_status': 'Object',
        'time_last_seen': 'unsigned int',
        'time_last_updated': 'unsigned int',
        'user_property_rules': 'list<Object>',
        'web_param_rules': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


