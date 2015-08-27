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
from facebookads.objects import AdCampaign

ad_account_id = test_config.account_id
page_id = test_config.page_id
connections_id = page_id
campaign_group_id = fixtures.create_adcampaign().get_id_assured()
ad_set_id = fixtures.create_adset().get_id_assured()
product_catalog_id = test_config.product_catalog_id
product_set_id = test_config.product_set_id

# _DOC open [ADSET_CREATE]
# _DOC vars [ad_account_id:s, campaign_group_id]
from facebookads.objects import AdSet, TargetingSpecsField

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.campaign_group_id: campaign_group_id,
    AdSet.Field.daily_budget: 1000,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.bid_amount: 2,
    AdSet.Field.targeting: {
        TargetingSpecsField.geo_locations: {
            'countries': ['US'],
        },
    },
    AdSet.Field.status: AdSet.Status.paused,
})

adset.remote_create()
print(adset)
# _DOC close [ADSET_CREATE]
adset.remote_delete()



# _DOC open [ADSET_CREATE_APP_CONNECTIONS_TARGETING]
# _DOC vars [ad_account_id:s, campaign_group_id, connections_id]
from facebookads.objects import AdSet, TargetingSpecsField

ad_set = AdSet(parent_id=ad_account_id)
ad_set.update({
    AdSet.Field.name: 'Android Connections Targeting - Ad Set',
    AdSet.Field.campaign_group_id: campaign_group_id,
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
    AdSet.Field.status: AdSet.Status.paused,
})

ad_set.remote_create()
print(ad_set)
# _DOC close [ADSET_CREATE_APP_CONNECTIONS_TARGETING]


# _DOC open [ADSET_CREATE_CPC_PROMOTING_PAGE]
# _DOC vars [ad_account_id:s, page_id:s, campaign_group_id:s]
import time
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.status: AdSet.Status.paused,
    AdSet.Field.daily_budget: 10000,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.page_likes,
    AdSet.Field.billing_event: AdSet.BillingEvent.page_likes,
    AdSet.Field.bid_amount: 1500,
    AdSet.Field.promoted_object: {'page_id': page_id},
    AdSet.Field.targeting: {
        'geo_locations': {
            'countries': ['US'],
        }
    },
    AdSet.Field.start_time: int(time.time()),
    AdSet.Field.campaign_group_id: campaign_group_id
})
adset.remote_create()

print(adset)
# _DOC close [ADSET_CREATE_CPC_PROMOTING_PAGE]
adset.remote_delete()


params = {
    AdCampaign.Field.buying_type: AdCampaign.BuyingType.fixed_cpm
}

campaign_group_id = fixtures.create_adcampaign(params).get_id_assured()

# _DOC open [ADSET_CREATE_HOMEPAGE]
# _DOC vars [ad_account_id:s, campaign_group_id]
import time
from facebookads.objects import (
    AdAccount,
    AdSet,
    RateCard,
    TargetingSpecsField
)

ad_account = AdAccount(ad_account_id)
rate_cards = ad_account.get_rate_cards()
country = rate_cards[0][RateCard.Field.country]
rate = rate_cards[0][RateCard.Field.rate]

impressions = 5000
lifetime_budget = str(rate * 5000)
end_date = int(time.time() + 12 * 3600)

ad_set = AdSet(parent_id=ad_account_id)
ad_set.update({
    AdSet.Field.name: 'Adset Homepage Ads',
    AdSet.Field.campaign_group_id: campaign_group_id,
    AdSet.Field.lifetime_budget: lifetime_budget,
    AdSet.Field.lifetime_imps: impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 100,
    AdSet.Field.targeting: {
        TargetingSpecsField.page_types: ['logout'],
        TargetingSpecsField.geo_locations: {
            'countries': [country],
        }
    },
    AdSet.Field.end_time: end_date,
})

ad_set.remote_create()
print(ad_set)
# _DOC close [ADSET_CREATE_HOMEPAGE]


ad_set_id = fixtures.create_adset().get_id_assured()

# _DOC open [ADSET_GET_ADGROUPS]
# _DOC vars [ad_set_id]
from facebookads.objects import AdSet, AdGroup

ad_set = AdSet(ad_set_id)
ad_group_iter = ad_set.get_ad_groups(fields=[AdGroup.Field.name])
for ad_group in ad_group_iter:
    print(ad_group[AdGroup.Field.name])
# _DOC close [ADSET_GET_ADGROUPS]


ad_set_id = fixtures.create_adset().get_id_assured()

# _DOC open [ADSET_READ_ADCREATIVE]
# _DOC vars [ad_set_id]
from facebookads.objects import AdSet, AdCreative

adset = AdSet(fbid=ad_set_id)
adset.get_ad_creatives([AdCreative.Field.object_story_id])
# _DOC close [ADSET_READ_ADCREATIVE]


campaign_group_id = fixtures.create_adcampaign().get_id_assured()

# _DOC open [ADSET_CREATE_LOCAL_AWARENESS]
# _DOC vars [ad_account_id:s, campaign_group_id:s]
from facebookads.objects import AdSet

adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'Local awareness adset',
    AdSet.Field.daily_budget: 10000,
    AdSet.Field.status: AdSet.Status.paused,
    AdSet.Field.campaign_group_id: campaign_group_id,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.bid_amount: 300,
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

adset.remote_create()
# _DOC close [ADSET_CREATE_LOCAL_AWARENESS]
adset.remote_delete()


campaign_group_id = fixtures.create_adcampaign().get_id_assured()

# _DOC open [ADSET_CREATE_OCPM]
# _DOC vars [ad_account_id:s, campaign_group_id:s]
from facebookads.objects import AdSet

# Create an Ad Set with bid_type set to oCPM
adset = AdSet(parent_id=ad_account_id)
adset.update({
    AdSet.Field.name: 'My Ad Set for oCPM',
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.link_clicks,
    AdSet.Field.bid_amount: 150,
    AdSet.Field.campaign_group_id: campaign_group_id,
    AdSet.Field.daily_budget: 1000,
    AdSet.Field.targeting: {
        TargetingSpecsField.geo_locations: {
            'countries': ['US'],
        },
    },
    AdSet.Field.status: AdSet.Status.paused,
})
adset.remote_create()

# _DOC close [ADSET_CREATE_OCPM]
adset.remote_delete()


# _DOC open [ADSET_GET_INSIGHTS]
# _DOC vars [ad_set_id]
from facebookads.objects import AdSet, Insights

adset = AdSet(fbid=ad_set_id)
params = {
    'level': Insights.Level.adgroup
}

stats = adset.get_insights(params=params)
print(stats)
# _DOC close [ADSET_GET_INSIGHTS]


ad_set_id = fixtures.create_adset().get_id()

# _DOC open [ADSET_GET_INSIGHTS_SORT]
# _DOC vars [ad_set_id]
from facebookads.objects import AdSet

adset = AdSet(fbid=ad_set_id)
params = {
    'sort': 'reach_descending'
}

stats = adset.get_insights(params=params)
print(stats)
# _DOC close [ADSET_GET_INSIGHTS_SORT]


# _DOC open [ADSET_GET_INSIGHTS_LEVEL_ADGROUP]
# _DOC vars [ad_set_id]
from facebookads.objects import AdSet, Insights

adset = AdSet(fbid=ad_set_id)
params = {
    'level': Insights.Level.adgroup
}

stats = adset.get_insights(params=params)
print(stats)
# _DOC close [ADSET_GET_INSIGHTS_LEVEL_ADGROUP]

params = {
    AdCampaign.Field.objective: AdCampaign.Objective.product_catalog_sales,
    AdCampaign.Field.promoted_object: {'product_catalog_id': product_catalog_id}
}

campaign_group_id = fixtures.create_adcampaign(params).get_id_assured()

# _DOC open [ADSET_CREATE_DYNAMIC_PROSPECTIING]
# _DOC vars [ad_account_id:s, product_set_id, campaign_group_id]
from facebookads.objects import AdSet, TargetingSpecsField

adset = AdSet(parent_id=ad_account_id)
adset[AdSet.Field.name] = 'Case 1 Adset'
adset[AdSet.Field.bid_amount] = 3000
adset[AdSet.Field.billing_event] = AdSet.BillingEvent.link_clicks
adset[AdSet.Field.optimization_goal] = AdSet.OptimizationGoal.link_clicks
adset[AdSet.Field.status] = AdSet.Status.active
adset[AdSet.Field.daily_budget] = 15000
adset[AdSet.Field.campaign_group_id] = campaign_group_id
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

adset.remote_create()
# _DOC close [ADSET_CREATE_DYNAMIC_PROSPECTIING]
adset.remote_delete()

product_set_id_1 = product_set_id
product_set_id_2 = product_set_id

# _DOC open [ADSET_CREATE_DYNAMIC_RETARGETING]
# _DOC vars [ad_account_id:s, product_set_id_1, product_set_id_2, campaign_group_id]
from facebookads.objects import AdSet, TargetingSpecsField

adset = AdSet(parent_id=ad_account_id)
adset[AdSet.Field.name] = 'My cross sell ad set'
adset[AdSet.Field.bid_amount] = 3000
adset[AdSet.Field.billing_event] = 'LINK_CLICKS'
adset[AdSet.Field.optimization_goal] = 'LINK_CLICKS'
adset[AdSet.Field.status] = AdSet.Status.active
adset[AdSet.Field.daily_budget] = 15000
adset[AdSet.Field.campaign_group_id] = campaign_group_id
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
    'product_set_id': product_set_id_1
}
behavior = 'FALL_BACK_TO_FB_RECOMMENDATIONS'
adset[AdSet.Field.product_ad_behavior] = behavior

adset.remote_create()
# _DOC close [ADSET_CREATE_DYNAMIC_RETARGETING]
adset.remote_delete()
