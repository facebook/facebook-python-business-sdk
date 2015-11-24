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

ad_account_id = test_config.account_id
product_set_id = fixtures.create_product_set().get_id()

# _DOC oncall [pruno]
# _DOC open [PRODUCTAUDIENCE_CREATE_IPHONE_VIEW_NO_PURCHASE]
# _DOC vars [ad_account_id:s, product_set_id]
from facebookads.objects import ProductAudience

product_audience = ProductAudience(parent_id=ad_account_id)
product_audience.update({
    ProductAudience.Field.name: 'Product Audience',
    ProductAudience.Field.product_set_id: product_set_id,
    ProductAudience.Field.inclusions: [
        {
            'retention_seconds': 86400,
            'rule': {
                'and': [
                    {
                        'event': {'eq': 'AddToCart'},
                    },
                    {
                        'userAgent': {'i_contains': 'iPhone'},
                    },
                ],
            },
        },
    ],
    ProductAudience.Field.exclusions: [
        {
            'retention_seconds': 172800,
            'rule': {
                'event': {'eq': 'Purchase'},
            },
        },
    ],
})
product_audience.remote_create()
# _DOC close [PRODUCTAUDIENCE_CREATE_IPHONE_VIEW_NO_PURCHASE]

product_audience.remote_delete()
