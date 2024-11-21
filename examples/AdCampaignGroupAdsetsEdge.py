# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_CAMPAIGN_ID>'
FacebookAdsApi.init(access_token=access_token, app_secret=app_secret, app_id=app_id)

fields = [
  'name',
  'start_time',
  'end_time',
  'daily_budget',
  'lifetime_budget',
]

campaign = Campaign(id)
ad_sets = campaign.get_ad_sets(fields=fields)

for ad_set in ad_sets:
    print(ad_set)