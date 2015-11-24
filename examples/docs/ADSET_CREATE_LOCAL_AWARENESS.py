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
page_id = test_config.page_id
campaign_id = fixtures.create_campaign().get_id()

# _DOC open [ADSET_CREATE_LOCAL_AWARENESS]
# _DOC vars [ad_account_id:s, campaign_id:s, page_id]
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'Local awareness adset',
    AdSet.Field.daily_budget: 10000,
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 300,
    AdSet.Field.promoted_object: {
        'page_id': page_id,
    },
    AdSet.Field.targeting: {
        'page_types': ['mobilefeed'],
        'geo_locations': {
            'custom_locations': [
                {
                    'latitude': 37.48327,
                    'longitude': -122.15033,
                    'radius': 10,
                    'distance_unit': 'mile',
                    'address_string': '1601 Willow Road, Menlo Park, CA 94025',
                },
            ],
            'location_types': [
                'home',
                'recent',
            ],
        },
        'excluded_geo_locations': {
            'zips': [
                {
                    'key': 'US:94040',
                },
            ],
        },
    },
})

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
# _DOC close [ADSET_CREATE_LOCAL_AWARENESS]

adset.remote_delete()
