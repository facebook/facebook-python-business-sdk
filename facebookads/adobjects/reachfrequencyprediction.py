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
from facebookads.adobjects.helpers.reachfrequencypredictionmixin import ReachFrequencyPredictionMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ReachFrequencyPrediction(
    AbstractCrudObject,
    ReachFrequencyPredictionMixin,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isReachFrequencyPrediction = True
        super(ReachFrequencyPrediction, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        campaign_group_id = 'campaign_group_id'
        campaign_id = 'campaign_id'
        campaign_time_start = 'campaign_time_start'
        campaign_time_stop = 'campaign_time_stop'
        curve_budget_reach = 'curve_budget_reach'
        destination_id = 'destination_id'
        expiration_time = 'expiration_time'
        external_budget = 'external_budget'
        external_impression = 'external_impression'
        external_maximum_budget = 'external_maximum_budget'
        external_maximum_impression = 'external_maximum_impression'
        external_maximum_reach = 'external_maximum_reach'
        external_minimum_budget = 'external_minimum_budget'
        external_minimum_impression = 'external_minimum_impression'
        external_minimum_reach = 'external_minimum_reach'
        external_reach = 'external_reach'
        frequency_cap = 'frequency_cap'
        grp_dmas_audience_size = 'grp_dmas_audience_size'
        holdout_percentage = 'holdout_percentage'
        id = 'id'
        instagram_destination_id = 'instagram_destination_id'
        interval_frequency_cap_reset_period = 'interval_frequency_cap_reset_period'
        name = 'name'
        prediction_mode = 'prediction_mode'
        prediction_progress = 'prediction_progress'
        reservation_status = 'reservation_status'
        status = 'status'
        story_event_type = 'story_event_type'
        target_audience_size = 'target_audience_size'
        target_spec = 'target_spec'
        time_created = 'time_created'
        time_updated = 'time_updated'
        budget = 'budget'
        destination_ids = 'destination_ids'
        end_time = 'end_time'
        num_curve_points = 'num_curve_points'
        objective = 'objective'
        reach = 'reach'
        rf_prediction_id_to_share = 'rf_prediction_id_to_share'
        start_time = 'start_time'
        stop_time = 'stop_time'

    class Status:
        expired = 'EXPIRED'
        draft = 'DRAFT'
        pending = 'PENDING'
        active = 'ACTIVE'
        completed = 'COMPLETED'

    @classmethod
    def get_endpoint(cls):
        return 'reachfrequencypredictions'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_reach_frequency_prediction(fields, params, batch, pending)

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
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
            target_class=ReachFrequencyPrediction,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    _field_types = {
        'account_id': 'int',
        'campaign_group_id': 'unsigned int',
        'campaign_id': 'string',
        'campaign_time_start': 'datetime',
        'campaign_time_stop': 'datetime',
        'curve_budget_reach': 'string',
        'destination_id': 'string',
        'expiration_time': 'datetime',
        'external_budget': 'int',
        'external_impression': 'unsigned int',
        'external_maximum_budget': 'int',
        'external_maximum_impression': 'unsigned int',
        'external_maximum_reach': 'unsigned int',
        'external_minimum_budget': 'int',
        'external_minimum_impression': 'unsigned int',
        'external_minimum_reach': 'unsigned int',
        'external_reach': 'unsigned int',
        'frequency_cap': 'unsigned int',
        'grp_dmas_audience_size': 'float',
        'holdout_percentage': 'unsigned int',
        'id': 'string',
        'instagram_destination_id': 'string',
        'interval_frequency_cap_reset_period': 'unsigned int',
        'name': 'string',
        'prediction_mode': 'unsigned int',
        'prediction_progress': 'unsigned int',
        'reservation_status': 'unsigned int',
        'status': 'unsigned int',
        'story_event_type': 'unsigned int',
        'target_audience_size': 'unsigned int',
        'target_spec': 'string',
        'time_created': 'datetime',
        'time_updated': 'datetime',
        'budget': 'unsigned int',
        'destination_ids': 'list<string>',
        'end_time': 'unsigned int',
        'num_curve_points': 'unsigned int',
        'objective': 'string',
        'reach': 'unsigned int',
        'rf_prediction_id_to_share': 'string',
        'start_time': 'unsigned int',
        'stop_time': 'unsigned int',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Status'] = ReachFrequencyPrediction.Status.__dict__.values()
        return field_enum_info
