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
campaign_id = fixtures.create_campaign().get_id()
product_set_id_1 = fixtures.create_product_set().get_id()
product_set_id_2 = fixtures.create_product_set().get_id()

# _DOC open [ADSET_CREATE_DYNAMIC_RETARGETING]
# _DOC vars [ad_account_id:s, product_set_id_1, product_set_id_2, campaign_id]
from facebookads.objects import AdSet, TargetingSpecsField

adset = AdSet(parent_id=ad_account_id)
adset[AdSet.Field.name] = 'My cross sell ad set'
adset[AdSet.Field.bid_amount] = 3000
adset[AdSet.Field.billing_event] = 'LINK_CLICKS'
adset[AdSet.Field.optimization_goal] = 'LINK_CLICKS'
adset[AdSet.Field.daily_budget] = 15000
adset[AdSet.Field.campaign_id] = campaign_id
adset[AdSet.Field.targeting] = {
    TargetingSpecsField.geo_locations: {
        TargetingSpecsField.countries: ['US'],
    },
    TargetingSpecsField.product_audience_specs: [{
        'product_set_id': product_set_id_2,
        'inclusions': [{
            'retention_seconds': 432000,
            'rule': {'event': {'eq': 'ViewContent'}},
        }],
        'exclusions': [{
            'retention_seconds': 432000,
            'rule': {'event': {'eq': 'Purchase'}},
        }],
    }],
    TargetingSpecsField.excluded_product_audience_specs: [{
        'product_set_id': product_set_id_2,
        'inclusions': [{
            'retention_seconds': 259200,
            'rule': {'event': {'eq': 'ViewContent'}},
        }],
    }],
}
adset[AdSet.Field.promoted_object] = {
    'product_set_id': product_set_id_1,
}
behavior = 'FALL_BACK_TO_FB_RECOMMENDATIONS'
adset[AdSet.Field.product_ad_behavior] = behavior

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
# _DOC close [ADSET_CREATE_DYNAMIC_RETARGETING]

adset.remote_delete()
