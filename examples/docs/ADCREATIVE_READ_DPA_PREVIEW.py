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

# Excluded from runtime
exit(0)

retailer_id = ''
catalog_id = fixtures.create_product_catalog().get_id()
creative_id = fixtures.create_creative().get_id()

# _DOC open [ADCREATIVE_READ_DPA_PREVIEW]
# _DOC vars [creative_id, catalog_id, retailer_id:s]
import base64
from facebookads.objects import AdCreative, AdCreativePreview, AdPreview

item_id = retailer_id
b64_id = base64.urlsafe_b64encode(item_id.encode('utf8'))
b64_encoded_id = b64_id.decode('utf8')

creative = AdCreative(creative_id)
params = {
    AdCreativePreview.Field.ad_format:
        AdPreview.AdFormat.desktop_feed_standard,
    AdCreativePreview.Field.product_item_ids: [
        "catalog:%s:%s" % (catalog_id, b64_encoded_id),
    ],
}
preview = creative.get_ad_preview(params=params)
# _DOC close [ADCREATIVE_READ_DPA_PREVIEW]
