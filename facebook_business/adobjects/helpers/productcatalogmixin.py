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

import base64
from facebook_business.api import FacebookAdsApi
from facebook_business.session import FacebookSession
from facebook_business.exceptions import FacebookError

class ProductCatalogMixin:

    class Role(object):
        admin = 'ADMIN'

    class Availability(object):
        available_for_order = 'available for order'
        in_stock = 'in stock'
        out_of_stock = 'out of stock'
        preorder = 'preorder'

    class AgeGroup(object):
        adult = 'adult'
        infant = 'infant'
        kids = 'kids'
        newborn = 'newborn'
        toddler = 'toddler'

    class Gender(object):
        men = 'men'
        women = 'women'
        unisex = 'unisex'

    class Condition(object):
        new = 'new'
        refurbished = 'refurbished'
        used = 'used'

    def add_user(self, user, role):
        params = {
            'user': user,
            'role': role,
        }
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'userpermissions'),
            params=params,
        )

    def remove_user(self, user):
        params = {
            'user': user,
        }
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'userpermissions'),
            params=params,
        )

    def add_external_event_sources(self, pixel_ids):
        params = {
            'external_event_sources': pixel_ids,
        }
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'external_event_sources'),
            params=params,
        )

    def remove_external_event_sources(self, pixel_ids):
        params = {
            'external_event_sources': pixel_ids,
        }
        return self.get_api_assured().call(
            'DELETE',
            (self.get_id_assured(), 'external_event_sources'),
            params=params,
        )

    def update_product(self, retailer_id, **kwargs):
        """Updates a product stored in a product catalog

        Args:
            retailer_id: product id from product feed. g:price tag in Google
                Shopping feed
            kwargs: key-value pairs to update on the object, being key the
                field name and value the updated value

        Returns:
            The FacebookResponse object.
        """
        if not kwargs:
            raise FacebookError(
                """No fields to update provided. Example:
                   catalog = ProductCatalog('catalog_id')
                   catalog.update_product(
                       retailer_id,
                       price=100,
                       availability=Product.Availability.out_of_stock
                   )
                """,
            )

        product_endpoint = ':'.join((
            'catalog',
            self.get_id_assured(),
            self.b64_encoded_id(retailer_id),
        ))

        url = '/'.join((
            FacebookSession.GRAPH,
            FacebookAdsApi.API_VERSION,
            product_endpoint,
        ))

        return self.get_api_assured().call(
            'POST',
            url,
            params=kwargs,
        )

    def b64_encoded_id(self, retailer_id):
        # # we need a byte string for base64.b64encode argument
        b64_id = base64.urlsafe_b64encode(retailer_id.encode('utf8'))

        # and we need a str to join with other url snippets
        return b64_id.decode('utf8')
