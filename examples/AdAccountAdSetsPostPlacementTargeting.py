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
  'name': 'My AdSet',
  'optimization_goal': 'REACH',
  'billing_event': 'IMPRESSIONS',
  'bid_amount': '2',
  'daily_budget': '1000',
  'campaign_id': '<adCampaignLinkClicksID>',
  'targeting': {'geo_locations':{'countries':['US']},'publisher_platforms':['facebook'],'facebook_positions':['feed']},
  'promoted_object': {'page_id':'<pageID>'},
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)