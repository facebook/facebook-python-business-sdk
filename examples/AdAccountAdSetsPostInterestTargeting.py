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
  'name': 'My First AdSet',
  'daily_budget': '10000',
  'bid_amount': '300',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'REACH',
  'campaign_id': '<adCampaignLinkClicksID>',
  'promoted_object': {'page_id':'<pageID>'},
  'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':['US'],'regions':[{'key':'4081'}],'cities':[{'key':777934,'radius':10,'distance_unit':'mile'}]},'genders':[1],'age_max':24,'age_min':20,'publisher_platforms':['facebook','audience_network'],'device_platforms':['mobile'],'flexible_spec':[{'interests':[{'id':'<adsInterestID>','name':'<adsInterestName>'}]}]},
  'status': 'PAUSED',
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)