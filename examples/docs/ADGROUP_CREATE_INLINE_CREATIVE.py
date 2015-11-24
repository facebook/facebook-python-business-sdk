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
image_hash = fixtures.create_image().get_hash()
ad_set_id = fixtures.create_adset().get_id()

# _DOC open [ADGROUP_CREATE_INLINE_CREATIVE]
# _DOC vars [ad_account_id:s, image_hash:s, ad_set_id]
from facebookads.objects import AdCreative, Ad

# First, upload the ad image that you will use in your ad creative
# Please refer to Ad Image Create for details.

# Then, use the image hash returned from above
creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.title] = 'My Test Creative'
creative[AdCreative.Field.body] = 'My Test Ad Creative Body'
creative[AdCreative.Field.object_url] = 'https://www.facebook.com/facebook'
creative[AdCreative.Field.image_hash] = image_hash

# Finally, create your ad along with ad creative.
# Please note that the ad creative is not created independently, rather its
# data structure is appended to the ad group
ad = Ad(parent_id=ad_account_id)
ad[Ad.Field.name] = 'My Ad'
ad[Ad.Field.adset_id] = ad_set_id
ad[Ad.Field.creative] = creative
ad.remote_create(params={
    'status': Ad.Status.paused,
})
# _DOC close [ADGROUP_CREATE_INLINE_CREATIVE]

ad.remote_delete()
