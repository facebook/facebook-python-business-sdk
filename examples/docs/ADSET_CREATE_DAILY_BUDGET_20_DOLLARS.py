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
from facebookads.objects import Campaign, TargetingSpecsField
from facebookads.objects import AdSet
import time

params = {
    Campaign.Field.name: 'My First Campaign',
    Campaign.Field.objective: Campaign.Objective.link_clicks,
}
ad_account_id = test_config.account_id
campaign_id = fixtures.create_campaign(params).get_id()
targeting = {
    TargetingSpecsField.page_types: [
        'desktopfeed',
        'mobilefeed',
        'mobileexternal',
    ],
    TargetingSpecsField.geo_locations: {
        'countries': ['BR'],
    },
}
optimization_goal = AdSet.OptimizationGoal.post_engagement
start_time = int(time.time())
bid_amount = 150
billing_event = AdSet.BillingEvent.post_engagement

# _DOC open [ADSET_CREATE_DAILY_BUDGET_20_DOLLARS]
# _DOC vars [ad_account_id:s, page_id:s, campaign_id, targeting, bid_amount, billing_event, start_time:s]
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset[AdSet.Field.name] = 'My First AdSet'
adset[AdSet.Field.daily_budget] = 2000
adset[AdSet.Field.start_time] = start_time
adset[AdSet.Field.campaign_id] = campaign_id
adset[AdSet.Field.bid_amount] = bid_amount
adset[AdSet.Field.billing_event] = billing_event
adset[AdSet.Field.optimization_goal] = optimization_goal
adset[AdSet.Field.targeting] = targeting

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
# _DOC close [ADSET_CREATE_DAILY_BUDGET_20_DOLLARS]

adset.remote_delete()
