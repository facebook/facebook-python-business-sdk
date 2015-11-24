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
from facebookads import test_config, FacebookAdsApi

ad_account_id = test_config.account_id
page_id = test_config.page_id
image_hash = fixtures.create_image().get_hash()
url = test_config.app_url
video_id = fixtures.create_video().get_id_assured()

FacebookAdsApi.set_default_api(fixtures.get_page_api())

# _DOC open [PAGE_POST_CREATE_CAROUSEL]
# _DOC vars [page_id, url:s, image_hash:s, video_id:s]
from facebookads import FacebookAdsApi

params = {
    'link': url,
    'message': 'Browse our latest products',
    'caption': 'My caption',
    'child_attachments': [
        {
            'link': url + '/product1',
            'name': 'Product 1',
            'description': '$8.99',
            'image_hash': image_hash,
            'video_id': video_id,
        },
        {
            'link': url + '/product2',
            'name': 'Product 2',
            'description': '$18.99',
            'image_hash': image_hash,
            'video_id': video_id,
        },
        {
            'link': url + '/product3',
            'name': 'Product 3',
            'description': '$28.99',
            'image_hash': image_hash,
            'video_id': video_id,
        },
    ],
}

data = FacebookAdsApi.get_default_api().\
    call('POST', (page_id, 'feed'), params)
# _DOC close [PAGE_POST_CREATE_CAROUSEL]

FacebookAdsApi.get_default_api().\
    call('DELETE', (data.json()['id'],))
