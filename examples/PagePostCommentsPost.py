# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.pagepost import PagePost
from facebook_business.adobjects.comment import Comment
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<PAGE_POST_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'message': 'This is a test value',
}
print PagePost(id).create_comment(
  fields=fields,
  params=params,
)