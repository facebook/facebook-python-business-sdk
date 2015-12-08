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
page_id = fixtures.get_page_with_locations_id_assured()
campaign_id = fixtures.create_campaign({
    Campaign.Field.objective: Campaign.Objective.local_awareness,
    Campaign.Field.promoted_object: {
        'page_id': page_id,
    },
}).get_id()
ad_place_page_set_id = fixtures.create_ad_place_page_set().get_id()

# _DOC oncall [pruno]
# _DOC open [ADSET_CREATE_DLA]
# _DOC vars [campaign_id, ad_account_id:s, ad_place_page_set_id]
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'Local Awareness Ad Set',
    AdSet.Field.promoted_object: {
        'place_page_set_id': ad_place_page_set_id,
    },
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 2,
    AdSet.Field.daily_budget: 1000,
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.targeting: {
        'geo_locations': {
            'custom_locations': [
                {
                    'latitude': 37.48327,
                    'longitude': -122.15033,
                    'radius': 1,
                },
                {
                    'latitude': 40.73050,
                    'longitude': -73.99157,
                    'radius': 1,
                },
            ],
        },
        'page_types': [
            'mobilefeed',
            'desktopfeed',
        ],
    },
})

adset.remote_create()
# _DOC close [ADSET_CREATE_DLA]

adset.remote_delete()
