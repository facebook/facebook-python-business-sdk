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

class FAMEAdCampaign(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isFAMEAdCampaign = True
        super(FAMEAdCampaign, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        adaccount_id = 'adaccount_id'
        adaccount_name = 'adaccount_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        adset_status = 'adset_status'
        bid_amount = 'bid_amount'
        campaign_id = 'campaign_id'
        daily_budget = 'daily_budget'
        end_time = 'end_time'
        lifetime_budget = 'lifetime_budget'
        start_time = 'start_time'
        id = 'id'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'date_preset': 'date_preset_enum',
            'time_range': 'Object',
        }
        enums = {
            'date_preset_enum': [
                'today',
                'yesterday',
                'this_month',
                'last_month',
                'this_quarter',
                'lifetime',
                'last_3d',
                'last_7d',
                'last_14d',
                'last_28d',
                'last_30d',
                'last_90d',
                'last_week_mon_sun',
                'last_week_sun_sat',
                'last_quarter',
                'last_year',
                'this_week_mon_today',
                'this_week_sun_today',
                'this_year',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FAMEAdCampaign,
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
        'adaccount_id': 'string',
        'adaccount_name': 'string',
        'adset_id': 'string',
        'adset_name': 'string',
        'adset_status': 'string',
        'bid_amount': 'string',
        'campaign_id': 'string',
        'daily_budget': 'string',
        'end_time': 'datetime',
        'lifetime_budget': 'string',
        'start_time': 'datetime',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


