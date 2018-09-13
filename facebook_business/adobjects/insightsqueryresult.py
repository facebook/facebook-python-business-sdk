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

class InsightsQueryResult(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isInsightsQueryResult = True
        super(InsightsQueryResult, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        breakdowns = 'breakdowns'
        time = 'time'
        value = 'value'
        id = 'id'

    class Aggregateby:
        count = 'COUNT'
        count_identified_users = 'COUNT_IDENTIFIED_USERS'
        users = 'USERS'
        topk = 'TOPK'
        sum = 'SUM'
        sum_per_event = 'SUM_PER_EVENT'
        sum_identified_users = 'SUM_IDENTIFIED_USERS'
        usd_sum = 'USD_SUM'
        usd_sum_per_event = 'USD_SUM_PER_EVENT'
        usd_sum_identified_users = 'USD_SUM_IDENTIFIED_USERS'
        usd_sum_per_user = 'USD_SUM_PER_USER'
        unknown_users = 'UNKNOWN_USERS'
        score = 'SCORE'
        median_value = 'MEDIAN_VALUE'
        median_value_per_user = 'MEDIAN_VALUE_PER_USER'
        dau = 'DAU'
        wau = 'WAU'
        mau = 'MAU'
        percentiles_count = 'PERCENTILES_COUNT'
        percentiles_value = 'PERCENTILES_VALUE'
        percentiles_usd_value = 'PERCENTILES_USD_VALUE'
        overlap = 'OVERLAP'
        count_per_user = 'COUNT_PER_USER'
        value_per_user = 'VALUE_PER_USER'
        usd_value_per_user = 'USD_VALUE_PER_USER'
        sessions_per_journey = 'SESSIONS_PER_JOURNEY'
        converted_journey_percent = 'CONVERTED_JOURNEY_PERCENT'
        median_journey_length = 'MEDIAN_JOURNEY_LENGTH'
        average_journey_length = 'AVERAGE_JOURNEY_LENGTH'
        journey_channel_inclusion = 'JOURNEY_CHANNEL_INCLUSION'
        event_source_ids = 'EVENT_SOURCE_IDS'
        session_bounce_rate = 'SESSION_BOUNCE_RATE'
        journey_inclusion = 'JOURNEY_INCLUSION'
        user_property_user_count = 'USER_PROPERTY_USER_COUNT'

    class Ecosystem:
        game = 'GAME'
        non_game = 'NON_GAME'

    class Period:
        mins_15 = 'mins_15'
        hourly = 'hourly'
        daily = 'daily'
        weekly = 'weekly'
        monthly = 'monthly'
        lifetime = 'lifetime'
        days_28 = 'days_28'
        range = 'range'

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
            target_class=InsightsQueryResult,
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
        'breakdowns': 'map<string, string>',
        'time': 'datetime',
        'value': 'string',
        'id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Aggregateby'] = InsightsQueryResult.Aggregateby.__dict__.values()
        field_enum_info['Ecosystem'] = InsightsQueryResult.Ecosystem.__dict__.values()
        field_enum_info['Period'] = InsightsQueryResult.Period.__dict__.values()
        return field_enum_info
