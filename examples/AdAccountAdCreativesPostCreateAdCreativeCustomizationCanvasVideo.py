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
  'object_story_spec': {'page_id':'<pageID>','video_data':{'video_id':'<videoID>','image_url':'<imageURL>','title':'English Creative title','message':'English Creative message','call_to_action':{'type':'LEARN_MORE','value':{'link':'<canvasURI>'}},'retailer_item_ids':[0,0,0,0],'customization_rules_spec':[{'customization_spec':{'language':'en_XX'}},{'customization_spec':{'language':'fr_XX'},'video_id':'<videoIDFR>','picture':'<imageURLFR>','link':'<canvasURIFR>','name':'French Creative title','message':'French Creative message'}]}},
  'product_set_id': '<productSetID>',
}
print AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
)