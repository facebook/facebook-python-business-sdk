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
  'name': 'A CPA Ad Set',
  'campaign_id': '<adCampaignLinkClicksID>',
  'daily_budget': '5000',
  'start_time': '2024-07-27T00:47:13-0700',
  'end_time': '2024-08-03T00:47:13-0700',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'REACH',
  'bid_amount': '1000',
  'promoted_object': {'page_id':'<pageID>'},
  'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':['US']}},
  'user_os': 'iOS',
  'publisher_platforms': 'facebook',
  'device_platforms': 'mobile',
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)