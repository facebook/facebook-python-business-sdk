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

ad_account_id = test_config.account_id
connections_id = test_config.page_id
campaign_id = fixtures.create_campaign().get_id_assured()

# _DOC open [ADSET_CREATE_APP_CONNECTIONS_TARGETING]
# _DOC vars [ad_account_id:s, campaign_id, connections_id]
from facebookads.objects import AdSet, TargetingSpecsField

ad_set = AdSet(parent_id=ad_account_id)
ad_set.update({
    AdSet.Field.name: 'Android Connections Targeting - Ad Set',
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.post_engagement,
    AdSet.Field.billing_event: AdSet.BillingEvent.post_engagement,
    AdSet.Field.bid_amount: 1500,
    AdSet.Field.daily_budget: 10000,
    AdSet.Field.targeting: {
        TargetingSpecsField.geo_locations: {
            'countries': ['US'],
        },
        TargetingSpecsField.connections: [connections_id],
        TargetingSpecsField.user_os: ['Android'],
    },
})

ad_set.remote_create(params={
    'status': AdSet.Status.paused,
})
print(ad_set)
# _DOC close [ADSET_CREATE_APP_CONNECTIONS_TARGETING]
