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
page_id = test_config.page_id

# _DOC oncall [paulbain]
# _DOC open [ADSET_CREATE_DEMOGRAPHIC_TARGETING_2]
# _DOC vars [ad_account_id:s, campaign_id, page_id]
from facebookads.objects import AdSet, TargetingSpecsField

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'My AdSet',
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 150,
    AdSet.Field.daily_budget: 2000,
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.promoted_object: {'page_id': page_id},
    AdSet.Field.targeting: {
        TargetingSpecsField.geo_locations: {
            'countries': ['JP'],
            'regions': [
                {'key': '3886'},
            ],
            'cities': [
                {
                    'key': '2420605',
                    'radius': '10',
                    'distance_unit': 'mile',
                },
            ],
        },
        TargetingSpecsField.genders: [1],
        TargetingSpecsField.age_min: 20,
        TargetingSpecsField.age_max: 24,
        TargetingSpecsField.page_types: ['mobilefeed', 'mobileexternal'],
        TargetingSpecsField.interests: [
            {
                'id': 6003107902433,
                'name': 'Association football (Soccer)',
            },
        ],
        TargetingSpecsField.behaviors: [
            {
                'id': 6002714895372,
                'name': 'All frequent travelers',
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
    },
})
adset.remote_create(params={
    'status': AdSet.Status.active,
})
# _DOC close [ADSET_CREATE_DEMOGRAPHIC_TARGETING_2]

adset.remote_delete()
