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
from facebookads import test_config
from facebookads import FacebookAdsApi

page_id = test_config.page_id
app_id, app_store_url = fixtures.get_promotable_ios_app()
image_hash = fixtures.create_image().get_hash()
deep_link_i = 'facebook://'

FacebookAdsApi.set_default_api(fixtures.get_page_api())

# _DOC open [PAGE_POST_CREATE_CTA_CAROUSEL]
# _DOC vars [page_id, app_store_url:s, image_hash:s, deep_link_i:s]
from facebookads import FacebookAdsApi
from facebookads.specs import AttachmentData

child_attachments = list()

for i in range(3):
    child_attachments.append({
        AttachmentData.Field.link: app_store_url,
        AttachmentData.Field.image_hash: image_hash,
        AttachmentData.Field.call_to_action: {
            'type': 'USE_MOBILE_APP',
            'value': {
                'app_link': deep_link_i,
                'link_title': 'LINK_TITLE_i',
            },
        },
    })

params = {
    'message': 'My description',
    'link': app_store_url,
    'caption': 'WWW.ITUNES.COM',
    'child_attachments': child_attachments,
    'multi_share_optimized': True,
}

data = FacebookAdsApi.get_default_api().\
    call('POST', (page_id, 'feed'), params)
# _DOC close [PAGE_POST_CREATE_CTA_CAROUSEL]

FacebookAdsApi.get_default_api().\
    call('DELETE', (data.json()['id'],))
