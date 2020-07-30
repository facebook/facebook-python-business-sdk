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

from unittest import TestCase

from adobjects.serverside.content import Content


class TestContent(TestCase):
    def test_normalize_and_to_dict(self):
        product_id = "product-1"
        dict_fields = {
            "quantity": 2,
            "item_price": 3.14,
            "title": "title4",
            "description": "description5",
            "brand": "brand6",
            "category": "category7",
        }
        normalized_fields = dict_fields.copy()
        normalized_fields["id"] = product_id
        dict_fields["product_id"] = product_id
        content = Content(
            product_id=dict_fields["product_id"],
            quantity=dict_fields["quantity"],
            item_price=dict_fields["item_price"],
            title=dict_fields["title"],
            description=dict_fields["description"],
            brand=dict_fields["brand"],
            category=dict_fields["category"],
        )

        self.assertEqual(content.to_dict(), dict_fields)
        self.assertEqual(content.normalize(), normalized_fields)

    def test_equals(self):
        content1 = Content(
            product_id="product-1",
            quantity=2,
            item_price=3.14,
            title="title4",
            description="description5",
            brand="brand6",
            category="category7",
        )
        content2 = Content(
            product_id="product-1",
            quantity=2,
            item_price=3.14,
            title="title4",
            description="description5",
            brand="brand6",
            category="category7",
        )

        self.assertTrue(content1 == content2)

    def test_not_equals(self):
        content1 = Content(
            product_id="product-1",
            quantity=2,
            item_price=3.14,
            title="title4",
            description="description5",
            brand="brand6",
            category="category7",
        )
        content2 = Content(
            product_id="product-1",
            quantity=2,
            item_price=3.14,
            title="title4",
            # no description
            brand="brand6",
            category="category7",
        )

        self.assertTrue(content1 != content2)
