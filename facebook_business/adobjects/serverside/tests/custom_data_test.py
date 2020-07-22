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

from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData


class CustomDataTest(TestCase):
    def test_normalize(self):
        content = Content(product_id='id0', quantity='quantity1', item_price=3.99)
        custom_properties = {'custom1': 'property1', 'custom2': 'property2'}
        expected = {
            'value': 0.5,
            'currency': 'usd',
            'content_name': 'content-content1',
            'content_category': 'content-category2',
            'content_ids': ['id1', 'id2'],
            'content_type': 'content-type3',
            'contents': [
                {
                    'id': content.product_id,
                    'quantity': content.quantity,
                    'item_price': content.item_price,
                }
            ],
            'order_id': 'order-id4',
            'predicted_ltv': 5.99,
            'num_items': 6,
            'status': 'status7',
            'search_string': 'search-string8',
            'item_number': 'item-number9',
            'custom1': 'property1',
            'custom2': 'property2',
        }
        custom_data = CustomData(
            value=expected['value'],
            currency=expected['currency'],
            content_name=expected['content_name'],
            content_category=expected['content_category'],
            content_ids=expected['content_ids'],
            contents=[content],
            content_type=expected['content_type'],
            order_id=expected['order_id'],
            predicted_ltv=expected['predicted_ltv'],
            num_items=expected['num_items'],
            status=expected['status'],
            search_string=expected['search_string'],
            item_number=expected['item_number'],
            custom_properties=custom_properties,
        )

        self.assertEqual(custom_data.normalize(), expected)
