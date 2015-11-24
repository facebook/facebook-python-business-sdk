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

params = {
    Campaign.Field.buying_type: Campaign.BuyingType.auction,
}
campaign_id = fixtures.create_campaign(params).get_id()

# _DOC open [ADSET_CREATE_HOMEPAGE]
# _DOC vars [ad_account_id:s, campaign_id]
import time
from facebookads.objects import (
    AdSet,
    TargetingSpecsField
)

end_date = int(time.time() + 24 * 3600)

ad_set = AdSet(parent_id=ad_account_id)
ad_set.update({
    AdSet.Field.name: 'Adset Homepage Ads',
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.daily_budget: 1000,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 100,
    AdSet.Field.targeting: {
        TargetingSpecsField.page_types: ['logout'],
        TargetingSpecsField.geo_locations: {
            'countries': ['US'],
        },
    },
    AdSet.Field.end_time: end_date,
})

ad_set.remote_create()
print(ad_set)
# _DOC close [ADSET_CREATE_HOMEPAGE]

ad_set.remote_delete()
