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
  'name': 'Sample Promoted',
  'object_story_spec': {'page_id':'<pageID>','link_data':{'image_hash':'<imageHash>','link':'<imageURL>','message':'try it out'}},
  'degrees_of_freedom_spec': {'creative_features_spec':'{\'standard_enhancements\':\'{\\\'enroll_status\\\':\\\'OPT_IN\\\'}\'}'},
  'special_ad_categories': [],
}
print AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
)