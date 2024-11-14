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
  'name': 'A CPA Ad Set optimized for App Events',
  'campaign_id': '<adCampaignAppInstallsID>',
  'daily_budget': '300',
  'start_time': '2024-08-05T17:55:15-0700',
  'end_time': '2024-08-12T17:55:15-0700',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'OFFSITE_CONVERSIONS',
  'bid_amount': '100',
  'status': 'PAUSED',
  'promoted_object': {'application_id':'<appID>','object_store_url':'<appLink>','custom_event_type':'PURCHASE'},
  'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':['US']},'user_os':['iOS']},
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)