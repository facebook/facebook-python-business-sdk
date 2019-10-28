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

import json
import os

this_dir = os.path.dirname(__file__)
config_filename = os.path.join(this_dir, os.pardir, os.pardir, 'config.json')

import sys
sys.path.insert(1, os.path.join(this_dir, os.pardir, os.pardir))

config_file = open(config_filename)
config = json.load(config_file)
config_file.close()

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.productcatalog import ProductCatalog
from facebook_business.adobjects.productitem import ProductItem

FacebookAdsApi.init(
    config['app_id'],
    config['app_secret'],
    config['access_token'],
)

if __name__ == '__main__':
    catalog_id = '<INSERT_YOUR_CATALOG_ID_HERE>'
    catalog = ProductCatalog(catalog_id)

    items = []
    for line in sys.stdin.readlines():
        if line.endswith('\n'):
            items.append(line[:-1].split(','))
        else:
            items.append(line.split(','))

    for item in items:
        product_id, new_price = item
        if new_price == '-':
            response = catalog.update_product(
                product_id,
                availability=ProductItem.Availability.out_of_stock
            )
            print('Product {} is now out of stock'.format(product_id))
        else:
            # prices should be in cents and be an integer
            new_price_in_cents = int(float(new_price) * 100)
            response = catalog.update_product(
                product_id,
                price=new_price_in_cents,
                availability=ProductItem.Availability.in_stock,
            )
            print('Product {} is now costs R$ {}'.format(product_id, new_price))
