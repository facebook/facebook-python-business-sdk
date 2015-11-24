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
from facebookads.objects import TargetingSpecsField

ad_account_id = test_config.account_id
campaign_id = fixtures.create_campaign().get_id_assured()
targeting = {
    TargetingSpecsField.geo_locations: {
        TargetingSpecsField.countries: ['US'],
    },
}

# _DOC open [ADSET_CREATE_TARGETING_DATE_RANGE]
# _DOC vars [ad_account_id:s, campaign_id, targeting]
import datetime
from facebookads.objects import AdSet

today = datetime.date.today()
start_time = str(today + datetime.timedelta(weeks=1))
end_time = str(today + datetime.timedelta(weeks=2))

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.daily_budget: 1000,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.bid_amount: 2,
    AdSet.Field.targeting: targeting,
    AdSet.Field.start_time: start_time,
    AdSet.Field.end_time: end_time,
})

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
# _DOC close [ADSET_CREATE_TARGETING_DATE_RANGE]

adset.remote_delete()
