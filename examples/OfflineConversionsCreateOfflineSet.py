# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.business import Business
from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<BUSINESS_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'offline_event_set',
  'description': 'conversion data used for superbowl campaign',
}
print Business(id).create_offline_conversion_data_set(
  fields=fields,
  params=params,
)