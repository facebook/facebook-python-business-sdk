# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My First Adset',
  'lifetime_budget': '20000',
  'start_time': '2024-07-29T17:55:06-0700',
  'end_time': '2024-08-08T17:55:06-0700',
  'campaign_id': '<adCampaignLinkClicksID>',
  'bid_amount': '500',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'POST_ENGAGEMENT',
  'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':['US'],'regions':[{'key':'4081'}],'cities':[{'key':777934,'radius':10,'distance_unit':'mile'}]},'genders':[1],'age_max':24,'age_min':20,'behaviors':[{'id':6002714895372,'name':'All travelers'}],'life_events':[{'id':6002714398172,'name':'Newlywed (1 year)'}],'publisher_platforms':['facebook'],'device_platforms':['desktop']},
  'status': 'PAUSED',
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)