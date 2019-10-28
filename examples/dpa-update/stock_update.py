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

from __future__ import print_function
from __future__ import unicode_literals

USAGE = """
Usage: python stock_update.py path/to/xml/feed.xml [n]

Simple script to simulate products that had updates on price or got out of
stock on a Google Shopping feed. First column is product id and second is
new price. If product is out of stock, a '-' is printed instead.

Sample output for 'python stock_update.py path/to/xml/feed.xml 5'
    ID_1,-
    ID_2,11.99 BRL
    ID_3,-
    ID_4,15.99 BRL
    ID_5,2.99 BRL
"""

import sys
import random

import xml.etree.cElementTree as ET

# namespaces used in Google Shopping files
ns = {'g': 'http://base.google.com/ns/1.0'}

# actions possible on a product
actions = ['new-price', 'out-of-stock']
num_products_to_update = 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(
            USAGE,
            file=sys.stderr
        )
        sys.exit(1)

    if len(sys.argv) == 3:
        num_products_to_update = int(sys.argv[2])

    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    items = root.findall('./channel/item', ns)

    if len(items) < num_products_to_update:
        num_products_to_update = len(items)

    items_to_update = random.sample(items, num_products_to_update)

    for item in items_to_update:
        gid = item.find('g:id', ns)
        gprice = item.find('g:price', ns)
        if gid is None or gprice is None :
            continue
        gprice = gprice.text
        if gprice is None :
            continue
        product_id = gid.text
        price = float(gprice.split(' ')[0])  # 9.99 BRL

        action = random.choice(actions)

        new_price = '-'
        if action == 'new-price':
            # prices can go up or down up to 20%
            change = random.choice([.8, .9, 1.1, 1.2])
            new_price = '{:.2f}'.format(price * change)

        # print updates to stdout
        if product_id is None :
            continue
        print(','.join([product_id, new_price]))
