# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_CREATIVE_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'ad_format': 'DESKTOP_FEED_STANDARD',
  'product_item_ids': ['<productItemID>'],
  'dynamic_customization': {'language':'fr_XX','country':'FR'},
}
print AdCreative(id).get_previews(
  fields=fields,
  params=params,
)