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

class AdNetworkAnalyticsSyncQueryResult(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdNetworkAnalyticsSyncQueryResult = True
        super(AdNetworkAnalyticsSyncQueryResult, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        query_id = 'query_id'
        results = 'results'
        id = 'id'

    class AggregationPeriod:
        hour = 'HOUR'
        day = 'DAY'
        total = 'TOTAL'

    class Breakdowns:
        age = 'AGE'
        app = 'APP'
        country = 'COUNTRY'
        delivery_method = 'DELIVERY_METHOD'
        display_format = 'DISPLAY_FORMAT'
        deal = 'DEAL'
        deal_ad = 'DEAL_AD'
        deal_page = 'DEAL_PAGE'
        gender = 'GENDER'
        placement = 'PLACEMENT'
        platform = 'PLATFORM'
        property = 'PROPERTY'
        clicked_view_tag = 'CLICKED_VIEW_TAG'
        fail_reason = 'FAIL_REASON'

    class Metrics:
        fb_ad_network_bidding_request = 'FB_AD_NETWORK_BIDDING_REQUEST'
        fb_ad_network_bidding_response = 'FB_AD_NETWORK_BIDDING_RESPONSE'
        fb_ad_network_bidding_bid_rate = 'FB_AD_NETWORK_BIDDING_BID_RATE'
        fb_ad_network_bidding_win_rate = 'FB_AD_NETWORK_BIDDING_WIN_RATE'
        fb_ad_network_request = 'FB_AD_NETWORK_REQUEST'
        fb_ad_network_filled_request = 'FB_AD_NETWORK_FILLED_REQUEST'
        fb_ad_network_fill_rate = 'FB_AD_NETWORK_FILL_RATE'
        fb_ad_network_imp = 'FB_AD_NETWORK_IMP'
        fb_ad_network_show_rate = 'FB_AD_NETWORK_SHOW_RATE'
        fb_ad_network_click = 'FB_AD_NETWORK_CLICK'
        fb_ad_network_ctr = 'FB_AD_NETWORK_CTR'
        fb_ad_network_bidding_revenue = 'FB_AD_NETWORK_BIDDING_REVENUE'
        fb_ad_network_revenue = 'FB_AD_NETWORK_REVENUE'
        fb_ad_network_cpm = 'FB_AD_NETWORK_CPM'
        fb_ad_network_video_guarantee_revenue = 'FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE'
        fb_ad_network_video_view = 'FB_AD_NETWORK_VIDEO_VIEW'
        fb_ad_network_video_view_rate = 'FB_AD_NETWORK_VIDEO_VIEW_RATE'
        fb_ad_network_video_mrc = 'FB_AD_NETWORK_VIDEO_MRC'
        fb_ad_network_video_mrc_rate = 'FB_AD_NETWORK_VIDEO_MRC_RATE'
        fb_ad_network_win_rate = 'FB_AD_NETWORK_WIN_RATE'
        fb_ad_network_direct_total_revenue = 'FB_AD_NETWORK_DIRECT_TOTAL_REVENUE'
        fb_ad_network_direct_publisher_bill = 'FB_AD_NETWORK_DIRECT_PUBLISHER_BILL'
        fb_ad_network_fast_click_rate = 'FB_AD_NETWORK_FAST_CLICK_RATE'
        fb_ad_network_fast_return_rate = 'FB_AD_NETWORK_FAST_RETURN_RATE'
        fb_ad_network_click_value_score = 'FB_AD_NETWORK_CLICK_VALUE_SCORE'
        fb_ad_network_fast_click_numerator = 'FB_AD_NETWORK_FAST_CLICK_NUMERATOR'
        fb_ad_network_fast_click_denominator = 'FB_AD_NETWORK_FAST_CLICK_DENOMINATOR'
        fb_ad_network_fast_return_numerator = 'FB_AD_NETWORK_FAST_RETURN_NUMERATOR'
        fb_ad_network_fast_return_denominator = 'FB_AD_NETWORK_FAST_RETURN_DENOMINATOR'
        fb_ad_network_click_value_score_numerator = 'FB_AD_NETWORK_CLICK_VALUE_SCORE_NUMERATOR'
        fb_ad_network_click_value_score_denominator = 'FB_AD_NETWORK_CLICK_VALUE_SCORE_DENOMINATOR'
        fb_ad_network_no_fill = 'FB_AD_NETWORK_NO_FILL'
        fb_ad_network_no_bid = 'FB_AD_NETWORK_NO_BID'

    class OrderingColumn:
        time = 'TIME'
        value = 'VALUE'
        metric = 'METRIC'

    class OrderingType:
        ascending = 'ASCENDING'
        descending = 'DESCENDING'

    _field_types = {
        'query_id': 'string',
        'results': 'list<Object>',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AggregationPeriod'] = AdNetworkAnalyticsSyncQueryResult.AggregationPeriod.__dict__.values()
        field_enum_info['Breakdowns'] = AdNetworkAnalyticsSyncQueryResult.Breakdowns.__dict__.values()
        field_enum_info['Metrics'] = AdNetworkAnalyticsSyncQueryResult.Metrics.__dict__.values()
        field_enum_info['OrderingColumn'] = AdNetworkAnalyticsSyncQueryResult.OrderingColumn.__dict__.values()
        field_enum_info['OrderingType'] = AdNetworkAnalyticsSyncQueryResult.OrderingType.__dict__.values()
        return field_enum_info


