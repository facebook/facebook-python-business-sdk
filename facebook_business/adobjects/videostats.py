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

class VideoStats(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isVideoStats = True
        super(VideoStats, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        aggregate = 'aggregate'
        error = 'error'
        metadata = 'metadata'
        time_series = 'time_series'
        totals = 'totals'
        x_axis_breakdown = 'x_axis_breakdown'
        id = 'id'

    class Metrics:
        average_watch_time = 'AVERAGE_WATCH_TIME'
        lifetime_comments = 'LIFETIME_COMMENTS'
        lifetime_reactions = 'LIFETIME_REACTIONS'
        lifetime_shares = 'LIFETIME_SHARES'
        lifetime_social_actions = 'LIFETIME_SOCIAL_ACTIONS'
        net_followers = 'NET_FOLLOWERS'
        uploaded_comments = 'UPLOADED_COMMENTS'
        uploaded_reactions = 'UPLOADED_REACTIONS'
        uploaded_shares = 'UPLOADED_SHARES'
        uploaded_social_actions = 'UPLOADED_SOCIAL_ACTIONS'
        uploaded_reach = 'UPLOADED_REACH'
        uploaded_views_3s = 'UPLOADED_VIEWS_3S'
        uploaded_views_3s_organic = 'UPLOADED_VIEWS_3S_ORGANIC'
        uploaded_views_3s_paid = 'UPLOADED_VIEWS_3S_PAID'
        uploaded_watch_time_minutes = 'UPLOADED_WATCH_TIME_MINUTES'
        uploaded_watch_time_minutes_organic = 'UPLOADED_WATCH_TIME_MINUTES_ORGANIC'
        uploaded_watch_time_minutes_paid = 'UPLOADED_WATCH_TIME_MINUTES_PAID'
        ad_cpm = 'AD_CPM'
        ad_impressions = 'AD_IMPRESSIONS'
        revenue = 'REVENUE'
        rpm = 'RPM'
        minute_monetizable_views = 'MINUTE_MONETIZABLE_VIEWS'
        ad_subsidy = 'AD_SUBSIDY'
        earning_with_subsidy = 'EARNING_WITH_SUBSIDY'

    class RequestedFields:
        aggregate = 'AGGREGATE'
        time_series = 'TIME_SERIES'

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
            target_class=VideoStats,
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
        'aggregate': 'list<Object>',
        'error': 'string',
        'metadata': 'list<Object>',
        'time_series': 'list<Object>',
        'totals': 'list<Object>',
        'x_axis_breakdown': 'list<list<Object>>',
        'id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Metrics'] = VideoStats.Metrics.__dict__.values()
        field_enum_info['RequestedFields'] = VideoStats.RequestedFields.__dict__.values()
        return field_enum_info
