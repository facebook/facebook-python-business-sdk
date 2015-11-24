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

ad_account_id = test_config.account_id
page_id = test_config.page_id
params = {
    Campaign.Field.objective: Campaign.Objective.page_likes,
    }
campaign_id = fixtures.create_campaign(params=params).get_id_assured()

# _DOC open [ADSET_CREATE_CPC_PROMOTING_PAGE]
# _DOC vars [ad_account_id:s, page_id:s, campaign_id:s]
import time
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.daily_budget: 10000,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.page_likes,
    AdSet.Field.billing_event: AdSet.BillingEvent.page_likes,
    AdSet.Field.bid_amount: 1500,
    AdSet.Field.promoted_object: {'page_id': page_id},
    AdSet.Field.targeting: {
        'geo_locations': {
            'countries': ['US'],
        }
    },
    AdSet.Field.start_time: int(time.time()),
    AdSet.Field.campaign_id: campaign_id,
})

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
print(adset)
# _DOC close [ADSET_CREATE_CPC_PROMOTING_PAGE]

adset.remote_delete()
