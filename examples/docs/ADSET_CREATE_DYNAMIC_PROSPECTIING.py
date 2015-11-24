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
product_catalog_id = fixtures.create_product_catalog().get_id()
product_set_id = fixtures.create_product_set(product_catalog_id).get_id()

params = {
    Campaign.Field.objective: Campaign.Objective.product_catalog_sales,
    Campaign.Field.promoted_object: {'product_catalog_id': product_catalog_id},
}

campaign_id = fixtures.create_campaign(params).get_id_assured()

# _DOC open [ADSET_CREATE_DYNAMIC_PROSPECTIING]
# _DOC vars [ad_account_id:s, product_set_id, campaign_id]
from facebookads.objects import AdSet, TargetingSpecsField

adset = AdSet(parent_id=ad_account_id)
adset[AdSet.Field.name] = 'Case 1 Adset'
adset[AdSet.Field.bid_amount] = 3000
adset[AdSet.Field.billing_event] = AdSet.BillingEvent.link_clicks
adset[AdSet.Field.optimization_goal] = AdSet.OptimizationGoal.link_clicks
adset[AdSet.Field.daily_budget] = 15000
adset[AdSet.Field.campaign_id] = campaign_id
adset[AdSet.Field.targeting] = {
    TargetingSpecsField.geo_locations: {
        TargetingSpecsField.countries: ['US'],
    },
    TargetingSpecsField.interests: [{
        'id': 6003397425735,
        'name': 'Tennis',
    }],
}
adset[AdSet.Field.promoted_object] = {'product_set_id': product_set_id}
behavior = 'FALL_BACK_TO_FB_RECOMMENDATIONS'
adset[AdSet.Field.product_ad_behavior] = behavior

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
# _DOC close [ADSET_CREATE_DYNAMIC_PROSPECTIING]

adset.remote_delete()
