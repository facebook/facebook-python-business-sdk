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

from examples.docs import fixtures

product_catalog_id = fixtures.create_product_catalog().get_id()

# _DOC open [PRODUCTFEED_CREATE]
# _DOC vars [product_catalog_id]
from facebookads.objects import ProductFeed

product_feed = ProductFeed(parent_id=product_catalog_id)

product_feed[ProductFeed.Field.name] = 'Test Feed'
product_feed[ProductFeed.Field.schedule] = {
    'interval': 'DAILY',
    'url': 'http://www.example.com/sample_feed.tsv',
    'hour': 22,
}

product_feed.remote_create()
# _DOC close [PRODUCTFEED_CREATE]

product_feed.remote_delete()
