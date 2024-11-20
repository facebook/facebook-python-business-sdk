# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_CAMPAIGN_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
  'impressions',
  'ad_id',
]
params = {
  'level': 'ad',
}
print Campaign(id).get_insights(
  fields=fields,
  params=params,
)