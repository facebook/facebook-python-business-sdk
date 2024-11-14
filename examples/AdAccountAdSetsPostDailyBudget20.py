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
  'daily_budget': '2000',
  'start_time': '2024-07-29T17:54:47-0700',
  'end_time': '2024-08-05T17:54:47-0700',
  'campaign_id': '<adCampaignLinkClicksID>',
  'bid_amount': '100',
  'billing_event': 'LINK_CLICKS',
  'optimization_goal': 'LINK_CLICKS',
  'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':['US']}},
  'status': 'PAUSED',
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)