# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'image_hash': '<imageHash>',
  'object_story_spec': {'page_id':'<pageID>','link_data':{'image_hash':'<imageHash>','link':'<canvasURI>','name':'Creative message','call_to_action':{'type':'LEARN_MORE'}}},
}
print AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
)