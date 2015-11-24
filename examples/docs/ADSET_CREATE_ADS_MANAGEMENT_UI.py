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
import time

ad_account_id = test_config.account_id
start_time = int(time.time())
end_time = start_time + 3600 * 24 * 7
campaign_id = fixtures.create_campaign().get_id()

# _DOC oncall [pruno]
# _DOC open [ADSET_CREATE_ADS_MANAGEMENT_UI]
# _DOC vars [ad_account_id:s, start_time, end_time, campaign_id]
from facebookads.objects import AdSet, TargetingSpecsField

ad_set = AdSet(parent_id=ad_account_id)
ad_set.update({
    AdSet.Field.name: 'My First AdSet',
    AdSet.Field.lifetime_budget: 20000,
    AdSet.Field.start_time: start_time,
    AdSet.Field.end_time: end_time,
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.bid_amount: 500,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.post_engagement,
    AdSet.Field.targeting: {
        TargetingSpecsField.geo_locations: {
            'countries': ['JP'],
        },
        TargetingSpecsField.genders: [1],
        TargetingSpecsField.age_min: 20,
        TargetingSpecsField.age_max: 24,
        TargetingSpecsField.interests: [
            {
                'id': 6003107902433,
                'name': 'Association football (Soccer)',
            },
        ],
        TargetingSpecsField.behaviors: [
            {
                'id': 6002714895372,
                'name': 'All travelers',
            },
        ],
        TargetingSpecsField.life_events: [
            {
                'id': 6002714398172,
                'name': 'Newlywed (1 year)',
            },
        ],
        TargetingSpecsField.home_ownership: [
            {
                'id': 6006371327132,
                'name': 'Renters',
            },
        ],
        TargetingSpecsField.page_types: [
            'desktopfeed',
            'rightcolumn',
            'mobilefeed',
            'mobileexternal',
        ],
    },
})
ad_set.remote_create(params={
    'status': AdSet.Status.paused,
})
# _DOC close [ADSET_CREATE_ADS_MANAGEMENT_UI]

ad_set.remote_delete()
