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

from facebookads import test_config
from examples.docs import fixtures

product_catalog_id = fixtures.create_product_catalog().get_id()
pixel_id = fixtures.create_ads_pixel().get_id()
app_id = test_config.app_id

# _DOC oncall [pruno]
# _DOC open [PRODUCTCATALOG_ADD_EXTERNAL_EVENT_SOURCES]
# _DOC vars [product_catalog_id, pixel_id, app_id]
from facebookads.objects import ProductCatalog

product_catalog = ProductCatalog(product_catalog_id)
product_catalog.add_external_event_sources([
    pixel_id,
    app_id,
])
# _DOC close [PRODUCTCATALOG_ADD_EXTERNAL_EVENT_SOURCES]
