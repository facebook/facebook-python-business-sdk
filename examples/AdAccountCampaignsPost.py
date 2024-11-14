# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'OUTCOME_TRAFFIC',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'Lead generation campaign',
  'objective': 'OUTCOME_LEADS',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'Local ad campaign',
  'objective': 'OUTCOME_AWARENESS',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'Mobile App Installs Campaign',
  'objective': 'OUTCOME_APP_PROMOTION',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'App Installs Campaign with Dynamic Product Ads',
  'objective': 'OUTCOME_APP_PROMOTION',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'Video Views campaign',
  'objective': 'OUTCOME_ENGAGEMENT',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'My First Campaign',
  'objective': 'OUTCOME_ENGAGEMENT',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'My First Campaign',
  'objective': 'OUTCOME_ENGAGEMENT',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'My First Campaign with daily budget',
  'objective': 'OUTCOME_LEADS',
  'status': 'PAUSED',
  'daily_budget': '1000',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

fields = [
]
params = {
  'name': 'My First Campaign with special ad categories',
  'objective': 'OUTCOME_LEADS',
  'status': 'PAUSED',
  'daily_budget': '1000',
  'special_ad_categories': [],
  'special_ad_category_country': ['MX'],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)