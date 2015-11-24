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

from facebookads import test_config
from facebookads.specs import LinkData, ObjectStorySpec

ad_account_id = test_config.account_id
page_id = test_config.page_id
url = test_config.app_url

# _DOC open [ADACCOUNT_GET_PREVIEWS_WITH_OBJECT_STORY_SPEC]
# _DOC vars [ad_account_id:s, page_id:s]
from facebookads.objects import AdAccount, AdPreview, AdCreative

link_data = LinkData()
link_data.update({
    LinkData.Field.link: url,
    LinkData.Field.message: "Message",
    LinkData.Field.name: "Name",
    LinkData.Field.description: "Description",
    LinkData.Field.call_to_action: {
        "type": "SIGN_UP",
        "value": {
            "link": url,
            "link_caption": "CTA caption",
        },
    },
})

story = ObjectStorySpec()
story.update({
    ObjectStorySpec.Field.link_data: link_data,
    ObjectStorySpec.Field.page_id: page_id,
})

creative = AdCreative()
creative.update({
    AdCreative.Field.object_story_spec: story,
})

account = AdAccount(ad_account_id)
params = {
    AdPreview.Field.ad_format: AdPreview.AdFormat.desktop_feed_standard,
    AdPreview.Field.creative: creative.export_data(),
}
ad_preview = account.get_ad_preview(params=params)
print(ad_preview)
# _DOC close [ADACCOUNT_GET_PREVIEWS_WITH_OBJECT_STORY_SPEC]
