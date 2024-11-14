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
  'name': 'Test Product Audience',
  'product_set_id': '<productSetID>',
  'inclusions': [{'retention_seconds':86400,'rule':{'event':{'eq':'AddToCart'}}},{'retention_seconds':72000,'rule':{'event':{'eq':'ViewContent'}}}],
  'exclusions': [{'retention_seconds':172800,'rule':{'event':{'eq':'Purchase'}}}],
}
print AdAccount(id).create_product_audience(
  fields=fields,
  params=params,
)