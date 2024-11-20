# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adspixel import AdsPixel
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<ADS_PIXEL_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'data': [{'event_name':'PageView','event_time':1721461428,'user_data':{'fbc':'fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890','fbp':'fb.1.1558571054389.1098115397','em':'309a0a5c3e211326ae75ca18196d301a9bdbd1a882a4d2569511033da23f0abd'}}],
}
print AdsPixel(id).create_event(
  fields=fields,
  params=params,
)