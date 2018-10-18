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

class DeliveryInfo(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isDeliveryInfo = True
        super(DeliveryInfo, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        active_accelerated_campaign_count = 'active_accelerated_campaign_count'
        active_day_parted_campaign_count = 'active_day_parted_campaign_count'
        active_rotated_campaign_count = 'active_rotated_campaign_count'
        are_all_daily_budgets_spent = 'are_all_daily_budgets_spent'
        completed_campaign_count = 'completed_campaign_count'
        credit_needed_ads_count = 'credit_needed_ads_count'
        delivery_insight = 'delivery_insight'
        delivery_insights = 'delivery_insights'
        eligible_for_delivery_insights = 'eligible_for_delivery_insights'
        end_time = 'end_time'
        has_account_hit_spend_limit = 'has_account_hit_spend_limit'
        has_campaign_group_hit_spend_limit = 'has_campaign_group_hit_spend_limit'
        has_no_active_ads = 'has_no_active_ads'
        has_no_ads = 'has_no_ads'
        inactive_ads_count = 'inactive_ads_count'
        inactive_campaign_count = 'inactive_campaign_count'
        is_account_closed = 'is_account_closed'
        is_account_disabled = 'is_account_disabled'
        is_ad_uneconomical = 'is_ad_uneconomical'
        is_adfarm_penalized = 'is_adfarm_penalized'
        is_adgroup_partially_rejected = 'is_adgroup_partially_rejected'
        is_campaign_accelerated = 'is_campaign_accelerated'
        is_campaign_completed = 'is_campaign_completed'
        is_campaign_day_parted = 'is_campaign_day_parted'
        is_campaign_disabled = 'is_campaign_disabled'
        is_campaign_group_disabled = 'is_campaign_group_disabled'
        is_campaign_rotated = 'is_campaign_rotated'
        is_campaign_scheduled = 'is_campaign_scheduled'
        is_clickbait_penalized = 'is_clickbait_penalized'
        is_daily_budget_spent = 'is_daily_budget_spent'
        is_reach_and_frequency_misconfigured = 'is_reach_and_frequency_misconfigured'
        is_split_test_active = 'is_split_test_active'
        is_split_test_valid = 'is_split_test_valid'
        lift_study_time_period = 'lift_study_time_period'
        limited_campaign_count = 'limited_campaign_count'
        limited_campaign_ids = 'limited_campaign_ids'
        needs_credit = 'needs_credit'
        needs_tax_number = 'needs_tax_number'
        non_deleted_ads_count = 'non_deleted_ads_count'
        not_delivering_campaign_count = 'not_delivering_campaign_count'
        pending_ads_count = 'pending_ads_count'
        reach_frequency_campaign_underdelivery_reason = 'reach_frequency_campaign_underdelivery_reason'
        rejected_ads_count = 'rejected_ads_count'
        scheduled_campaign_count = 'scheduled_campaign_count'
        start_time = 'start_time'
        status = 'status'
        text_penalty_level = 'text_penalty_level'
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
            target_class=DeliveryInfo,
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
        'active_accelerated_campaign_count': 'int',
        'active_day_parted_campaign_count': 'int',
        'active_rotated_campaign_count': 'int',
        'are_all_daily_budgets_spent': 'bool',
        'completed_campaign_count': 'int',
        'credit_needed_ads_count': 'int',
        'delivery_insight': 'Object',
        'delivery_insights': 'list<Object>',
        'eligible_for_delivery_insights': 'bool',
        'end_time': 'datetime',
        'has_account_hit_spend_limit': 'bool',
        'has_campaign_group_hit_spend_limit': 'bool',
        'has_no_active_ads': 'bool',
        'has_no_ads': 'bool',
        'inactive_ads_count': 'int',
        'inactive_campaign_count': 'int',
        'is_account_closed': 'bool',
        'is_account_disabled': 'bool',
        'is_ad_uneconomical': 'bool',
        'is_adfarm_penalized': 'bool',
        'is_adgroup_partially_rejected': 'bool',
        'is_campaign_accelerated': 'bool',
        'is_campaign_completed': 'bool',
        'is_campaign_day_parted': 'bool',
        'is_campaign_disabled': 'bool',
        'is_campaign_group_disabled': 'bool',
        'is_campaign_rotated': 'bool',
        'is_campaign_scheduled': 'bool',
        'is_clickbait_penalized': 'bool',
        'is_daily_budget_spent': 'bool',
        'is_reach_and_frequency_misconfigured': 'bool',
        'is_split_test_active': 'bool',
        'is_split_test_valid': 'bool',
        'lift_study_time_period': 'string',
        'limited_campaign_count': 'int',
        'limited_campaign_ids': 'list<string>',
        'needs_credit': 'bool',
        'needs_tax_number': 'bool',
        'non_deleted_ads_count': 'int',
        'not_delivering_campaign_count': 'int',
        'pending_ads_count': 'int',
        'reach_frequency_campaign_underdelivery_reason': 'string',
        'rejected_ads_count': 'int',
        'scheduled_campaign_count': 'int',
        'start_time': 'datetime',
        'status': 'string',
        'text_penalty_level': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


