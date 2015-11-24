# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
from examples.docs import fixtures

from facebookads import test_config

ad_account_id = test_config.account_id
product_catalog_id = fixtures.create_product_catalog().get_id()

# _DOC open [ADCAMPAIGN_CREATE_OBJECTIVE_PRODUCT_CATELOG_SALES]
# _DOC vars [ad_account_id:s, product_catalog_id]
from facebookads.objects import Campaign

campaign = Campaign(parent_id=ad_account_id)
campaign[Campaign.Field.name] = 'Product Catalog Sales Campaign Group'
objective = Campaign.Objective.product_catalog_sales
campaign[Campaign.Field.objective] = objective
campaign[Campaign.Field.promoted_object] = {
    'product_catalog_id': product_catalog_id,
}

campaign.remote_create(params={
    'status': Campaign.Status.paused,
})
# _DOC close [ADCAMPAIGN_CREATE_OBJECTIVE_PRODUCT_CATELOG_SALES]

campaign.remote_delete()
