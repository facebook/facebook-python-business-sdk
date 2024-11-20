# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'Test Value-Based lookalike from Pixel',
  'subtype': 'LOOKALIKE',
  'lookalike_spec': {'origin_event_sources':[{'id':'<sourceID>','event_names':['AddToCart']}],'type':'custom_ratio','ratio':0.01,'country':'US'},
}
print AdAccount(id).create_custom_audience(
  fields=fields,
  params=params,
)