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
from facebookads.objects import AdImage

ad_account_id = test_config.account_id
page_id = test_config.page_id
video_id = fixtures.create_video().get_id()
thumbnail_url = fixtures.create_image()[AdImage.Field.url]
app_id, app_store_url = fixtures.get_promotable_ios_app()

# _DOC open [ADCREATIVE_CREATE_VIDEO_APP_INSTALL_AD]
# _DOC vars [thumbnail_url:s, page_id, ad_account_id:s, video_id, app_store_url:s]
from facebookads.objects import AdCreative
from facebookads.specs import ObjectStorySpec, VideoData

video_data = VideoData()
video_data[VideoData.Field.description] = 'try it out'
video_data[VideoData.Field.video_id] = video_id
video_data[VideoData.Field.image_url] = thumbnail_url
video_data[VideoData.Field.call_to_action] = {
    'type': 'INSTALL_MOBILE_APP',
    'value': {
        'link': app_store_url,
        'link_title': 'Facebook',
    },
}

object_story_spec = ObjectStorySpec()
object_story_spec[ObjectStorySpec.Field.page_id] = page_id
object_story_spec[ObjectStorySpec.Field.video_data] = video_data

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.name] = 'Sample Creative'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()
# _DOC close [ADCREATIVE_CREATE_VIDEO_APP_INSTALL_AD]

creative.remote_delete()
