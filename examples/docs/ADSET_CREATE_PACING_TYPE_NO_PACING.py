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
campaign_id = fixtures.create_campaign().get_id_assured()

# !_DOC [pruno]
# _DOC open [ADSET_CREATE_PACING_TYPE_NO_PACING]
# _DOC vars [ad_account_id:s, campaign_id]
from facebookads.objects import AdSet, TargetingSpecsField

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'Ad Set without pacing',
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.pacing_type: [AdSet.PacingType.no_pacing],
    AdSet.Field.bid_amount: 2,
    AdSet.Field.daily_budget: 1000,
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.targeting: {
        TargetingSpecsField.geo_locations: {
            'countries': ['US'],
        },
    },
})

adset.remote_create()
# _DOC close [ADSET_CREATE_PACING_TYPE_NO_PACING]

adset.remote_delete()
