# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# This file is auto-generated

import os
import sys
repo_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
sys.path.insert(1, repo_dir)

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_id = '<APP_ID>'
account_id = 'act_<ACCOUNT_ID>'
page_id = '<PAGE_ID>'
ads_image_hash = '<IMAGE_HASH>'
page_link = '<PAGE_LINK>'
params={}
FacebookAdsApi.init(access_token=access_token, crash_log=False)


# Step 1: Create an ad campaign

fields = [
]
params = {
    'name': 'My campaign',
    'objective': 'OUTCOME_TRAFFIC',
    'status': 'PAUSED',
    'special_ad_categories': [],
}
campaign = AdAccount(account_id).create_campaign(
    fields=fields,
    params=params,
)
campaign_id = campaign.get_id()

print('Your campaign id is: ' + campaign_id)


# Step 2: Create an adset with some buying options

fields = [
]
params = {
    'name': 'My adset',
    'optimization_goal': 'REACH',
    'bid_amount': '2',
    'daily_budget': '1000',
    'campaign_id': campaign_id,
    'targeting': {'geo_locations':{'countries':['US']}},
    'status': 'PAUSED',
    'billing_event': 'IMPRESSIONS',
}
adset = AdAccount(account_id).create_ad_set(
    fields=fields,
    params=params,
)
adset_id = adset.get_id()

print('Your ad set id is: ' + adset_id)


# Step 3: Create an ad creative with your amazing design
#         This ad creative is promoting your page

fields = [
]
params = {
    'name': 'Ad creative',
    'object_story_spec': {'link_data': {'call_to_action':{'type':'LIKE_PAGE','value':{'page':page_id}},'image_hash':ads_image_hash,'link':page_link,'message': 'try it out'},'page_id':page_id},
    'degrees_of_freedom_spec': {'creative_features_spec': {'standard_enhancements': {'enroll_status': 'OPT_IN'}}},
}
adcreative = AdAccount(account_id).create_ad_creative(
    fields=fields,
    params=params,
)
adcreative_id = adcreative.get_id()

print('Your ad creative id is: ' + adcreative_id)


# Step 4: Create an ad under your ad set with your ad creative

fields = [
]
params = {
    'name': 'Ad',
    'adset_id': adset_id,
    'creative': {'creative_id': adcreative_id},
    'status': 'PAUSED',
}
ad = AdAccount(account_id).create_ad(
    fields=fields,
    params=params,
)
ad_id = ad.get_id()

print('Your ad id is: ' + ad_id)
