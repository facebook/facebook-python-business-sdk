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
  'name': 'Mobile App Installs Ad Set',
  'daily_budget': '1000',
  'bid_amount': '2',
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'APP_INSTALLS',
  'campaign_id': '<adCampaignAppInstallsID>',
  'promoted_object': {'application_id':'<appID>','object_store_url':'<appLink>'},
  'targeting': {'device_platforms':['mobile'],'facebook_positions':['feed'],'geo_locations':{'countries':['US']},'publisher_platforms':['facebook','audience_network'],'user_os':['IOS']},
  'status': 'PAUSED',
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)