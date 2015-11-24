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

from examples.docs import fixtures
from facebookads import test_config
from facebookads.objects import Campaign
from facebookads.objects import AdSet
import time

params = {
    Campaign.Field.name: 'My First Campaign',
    Campaign.Field.objective: Campaign.Objective.link_clicks,
}
ad_account_id = test_config.account_id
campaign_id = fixtures.create_campaign(params).get_id()
optimization_goal = AdSet.OptimizationGoal.post_engagement
start_time = int(time.time())
end_time = int(time.time() + 100000)

# _DOC open [ADSET_CREATE_OPTIMIZE_POST_ENGAGEMENT_PAY_PER_IMPRESSION]
# _DOC vars [ad_account_id:s, page_id:s, campaign_id, start_time, end_time]
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset[AdSet.Field.name] = 'My First AdSet'
adset[AdSet.Field.daily_budget] = 20000
adset[AdSet.Field.start_time] = start_time
adset[AdSet.Field.end_time] = end_time
adset[AdSet.Field.campaign_id] = campaign_id
adset[AdSet.Field.bid_amount] = 500
adset[AdSet.Field.billing_event] = AdSet.BillingEvent.impressions
adset[AdSet.Field.optimization_goal] = optimization_goal
adset[AdSet.Field.targeting] = {
    'geo_locations': {
        'countries': ['JP'],
        'regions': [{'key': '3886'}],
        'cities': [
            {
                'key': '2420605',
                'radius': 10,
                'distance_unit': 'mile',
            },
        ],
    },
    'genders': [1],
    'age_min': 20,
    'age_max': 24,
    'interests': [
        {
            'id': 6003107902433,
            'name': 'Association football (Soccer)',
        },
    ],
    'behaviors': [{'id': 6002714895372, 'name': 'All travelers'}],
    'life_events': [{'id': 6002714398172, 'name': 'Newlywed (1 year)'}],
    'home_ownership': [{'id': 6006371327132, 'name': 'Renters'}],
    'page_types': ['desktopfeed', 'rightcolumn'],
}

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
# _DOC close [ADSET_CREATE_OPTIMIZE_POST_ENGAGEMENT_PAY_PER_IMPRESSION]

adset.remote_delete()
