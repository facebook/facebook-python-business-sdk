# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'creative': {'instagram_actor_id':'<instagramActorID>','object_story_spec':{'link_data':{'call_to_action':{'type':'LEARN_MORE','value':{'link':'<url>'}},'caption':'www.example.com','image_hash':'<imageHash>','link':'<url>','message':'Message'},'page_id':'<pageID>'}},
  'ad_format': 'INSTAGRAM_STANDARD',
}
print AdAccount(id).get_generate_previews(
  fields=fields,
  params=params,
)