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
from facebookads.objects import AdImage

page_id = test_config.page_id
image_url = fixtures.create_image()[AdImage.Field.url]

FacebookAdsApi.set_default_api(fixtures.get_page_api())

# _DOC oncall [pruno]
# _DOC open [PAGE_POST_CREATE_GET_DIRECTIONS]
# _DOC vars [image_url:s, page_id]
from facebookads import FacebookAdsApi

link = 'fbgeo://37.48327, -122.15033, "1601 Willow Rd Menlo Park CA"'

params = {
    'message': 'Come check out our new store in Menlo Park!',
    'link': 'https://www.facebook.com/' + str(page_id),
    'picture': image_url,
    'published': 0,
    'call_to_action': {
        'type': 'GET_DIRECTIONS',
        'value': {
            'link': link,
        },
    },
}

data = FacebookAdsApi.get_default_api().\
    call('POST', (page_id, 'feed'), params)
# _DOC close [PAGE_POST_CREATE_GET_DIRECTIONS]

FacebookAdsApi.get_default_api().\
    call('DELETE', (data.json()['id'],))
