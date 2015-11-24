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

# _DOC open [ADSET_CREATE_CUSTOM_LOCATION_TARGETING]
# _DOC vars [ad_account_id:s, campaign_id]
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'My AdSet',
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 150,
    AdSet.Field.daily_budget: 2000,
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.targeting: {
        'geo_locations': {
            'custom_locations': [
                {
                    'address_string': '1601 Willow Road, Menlo Park, CA',
                    'radius': 5,
                },
                {
                    'latitude': 36,
                    'longitude': -121.0,
                    'radius': 5,
                    'distance_unit': 'kilometer',
                },
            ],
            'location_types': ['recent', 'home'],
        },
    },
})
adset.remote_create(params={
    'status': AdSet.Status.active,
})
# _DOC close [ADSET_CREATE_CUSTOM_LOCATION_TARGETING]

adset.remote_delete()
