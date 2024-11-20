# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.productcatalog import ProductCatalog
from facebook_business.adobjects.productset import ProductSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<PRODUCT_CATALOG_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'Test Hotel Set',
  'filter': {'brand':{'i_contains':'sample brand'}},
}
print ProductCatalog(id).create_product_set(
  fields=fields,
  params=params,
)