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

from facebookads import test_config, FacebookAdsApi
from examples.docs import fixtures
from facebookads.objects import AdImage

page_id = test_config.page_id
app_id, app_store_url = fixtures.get_promotable_ios_app()
app_secret = test_config.app_secret
thumbnail_url = fixtures.create_image()[AdImage.Field.url]
video_path = test_config.video_path
FacebookAdsApi.set_default_api(fixtures.get_page_api())

# _DOC open [PAGE_POST_CREATE_VIDEO]
# _DOC vars [page_id, thumbnail_url:s, app_store_url:s, video_path:s]
from facebookads import FacebookAdsApi

params = {
    'name': 'My Video',
    'massage': 'Check out this app!',
    'thumbnail': thumbnail_url,
    'published': 0,
    'call_to_action': {
        'type': 'INSTALL_MOBILE_APP',
        'value': {
            'link': app_store_url,
        },
    },
}

url = 'https://graph-video.facebook.com/' + FacebookAdsApi.API_VERSION
path = "/{}/videos".format(page_id)
files = {'source': open(video_path, 'rb')}

data = FacebookAdsApi.get_default_api().call(
    'POST',
    url + path,
    params=params,
    files=files
)
# _DOC close [PAGE_POST_CREATE_VIDEO]

delete_path = '/' + data.json()['id']
response = FacebookAdsApi.get_default_api().call('DELETE', url + delete_path)
