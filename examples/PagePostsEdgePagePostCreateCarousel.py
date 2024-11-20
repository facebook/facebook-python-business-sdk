# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.page import Page
from facebook_business.adobjects.pagepost import PagePost
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<PAGE_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'message': 'Browse our latest products',
  'published': '0',
  'child_attachments': [{'link':'<link>','name':'Product 1','description':'$4.99','image_hash':'<imageHash>'},{'link':'<link>','name':'Product 2','description':'$4.99','image_hash':'<imageHash>'},{'link':'<link>','name':'Product 3','description':'$4.99','image_hash':'<imageHash>'},{'link':'<link>','name':'Product 4','description':'$4.99','image_hash':'<imageHash>'}],
  'caption': 'WWW.EXAMPLE.COM',
  'link': 'http://www.example.com/products',
}
print Page(id).get_posts(
  fields=fields,
  params=params,
)