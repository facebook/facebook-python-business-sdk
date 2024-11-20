# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_SET_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'billing_event': 'IMPRESSIONS',
  'optimization_goal': 'LINK_CLICKS',
  'bid_amount': '200',
  'targeting': {'geo_locations':{'countries':['US']},'facebook_positions':['feed']},
}
print AdSet(id).update(
  fields=fields,
  params=params,
)