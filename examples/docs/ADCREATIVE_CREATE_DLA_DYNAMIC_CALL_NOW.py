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

url = test_config.app_url
image_url = fixtures.create_image()[AdImage.Field.url]
page_id = fixtures.get_page_with_locations_id_assured()
ad_account_id = test_config.account_id
ad_place_page_set_id = fixtures.create_ad_place_page_set().get_id()

# _DOC oncall [pruno]
# _DOC open [ADCREATIVE_CREATE_DLA_DYNAMIC_CALL_NOW]
# _DOC vars [url:s, image_url:s, page_id, ad_account_id:s, ad_place_page_set_id]
from facebookads.objects import AdCreative
from facebookads.specs import TemplateData, ObjectStorySpec

template = TemplateData()
template.update({
    TemplateData.Field.name: '{{page.name}}',
    TemplateData.Field.message: 'Ad Message',
    TemplateData.Field.description: 'Ad Description',
    TemplateData.Field.link: url,
    TemplateData.Field.picture: image_url,
    TemplateData.Field.call_to_action: {
        'type': 'CALL_NOW',
    },
})

story = ObjectStorySpec()
story.update({
    ObjectStorySpec.Field.page_id: page_id,
    ObjectStorySpec.Field.template_data: template,
})

creative = AdCreative(parent_id=ad_account_id)
creative.update({
    AdCreative.Field.place_page_set_id: ad_place_page_set_id,
    AdCreative.Field.dynamic_ad_voice: 'DYNAMIC',
    AdCreative.Field.object_story_spec: story,
})
creative.remote_create()
# _DOC close [ADCREATIVE_CREATE_DLA_DYNAMIC_CALL_NOW]

creative.remote_delete()
