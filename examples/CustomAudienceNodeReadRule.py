# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<CUSTOM_AUDIENCE_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
  'name',
  'rule',
]
params = {
}
print CustomAudience(id).get(
  fields=fields,
  params=params,
)