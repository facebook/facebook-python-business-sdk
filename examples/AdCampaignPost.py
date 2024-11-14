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
  'bid_adjustments': {'user_groups':{'user_bucket':{'event_sources':['<pixelID>','<appID>'],'1':0.1,'2':0.2,'3':0.3,'default':{'gender':{'male':0.99,'female':0.12}}}}},
}
print AdSet(id).update(
  fields=fields,
  params=params,
)