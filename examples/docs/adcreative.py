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

from facebookads.objects import AdImage
from facebookads import test_config
from examples.docs import fixtures

ad_account_id = test_config.account_id
page_id = test_config.page_id

image_hash = fixtures.create_image().get_hash()
link = 'http://example.com'


# _DOC open [ADCREATIVE_CREATE_LINK_AD]
# _DOC vars [ad_account_id:s, image_hash:s, page_id, link:s]
from facebookads.objects import AdCreative
from facebookads.specs import ObjectStorySpec, LinkData

link_data = LinkData()
link_data[LinkData.Field.message] = 'try it out'
link_data[LinkData.Field.link] = link
link_data[LinkData.Field.caption] = 'My caption'
link_data[LinkData.Field.image_hash] = image_hash

object_story_spec = ObjectStorySpec()
object_story_spec[ObjectStorySpec.Field.page_id] = page_id
object_story_spec[ObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

print(creative)
# _DOC close [ADCREATIVE_CREATE_LINK_AD]
creative.remote_delete()


url = 'http://www.domain.com'

# _DOC open [ADCREATIVE_CREATE_LINK_AD_CALL_TO_ACTION]
# _DOC vars [url:s, page_id, ad_account_id:s]
from facebookads.objects import AdCreative
from facebookads.specs import ObjectStorySpec, LinkData

link_data = LinkData()
link_data[LinkData.Field.message] = 'My message'
link_data[LinkData.Field.link] = url
link_data[LinkData.Field.caption] = 'www.domain.com'

call_to_action = {
    'type': 'SIGN_UP',
    'value': {
        'link': url,
        'link_caption': 'Sign up!',
    }
}

link_data[LinkData.Field.call_to_action] = call_to_action

object_story_spec = ObjectStorySpec()
object_story_spec[ObjectStorySpec.Field.page_id] = page_id
object_story_spec[ObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.name] = 'AdCreative for Link Ad with CTA'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()
print(creative)
# _DOC close [ADCREATIVE_CREATE_LINK_AD_CALL_TO_ACTION]
creative.remote_delete()


creative_id = fixtures.create_creative().get_id_assured()
image_hash = fixtures.create_image().get_hash()
url = "http://domain.com"

# _DOC open [ADCREATIVE_CREATE_MULTI_PRODUCT_AD]
# _DOC vars [ad_account_id:s, page_id, url:s, image_hash:s]
from facebookads.objects import AdCreative
from facebookads.specs import ObjectStorySpec, LinkData, AttachmentData

product1 = AttachmentData()
product1[AttachmentData.Field.link] = url + '/product1'
product1[AttachmentData.Field.name] = 'Product 1'
product1[AttachmentData.Field.description] = '$8.99'
product1[AttachmentData.Field.image_hash] = image_hash

product2 = AttachmentData()
product2[AttachmentData.Field.link] = url + '/product2'
product2[AttachmentData.Field.name] = 'Product 2'
product2[AttachmentData.Field.description] = '$9.99'
product2[AttachmentData.Field.image_hash] = image_hash

product3 = AttachmentData()
product3[AttachmentData.Field.link] = url + '/product3'
product3[AttachmentData.Field.name] = 'Product 3'
product3[AttachmentData.Field.description] = '$10.99'
product3[AttachmentData.Field.image_hash] = image_hash

link = LinkData()
link[link.Field.link] = url
link[link.Field.child_attachments] = [product1, product2, product3]
link[link.Field.caption] = 'My caption'

story = ObjectStorySpec()
story[story.Field.page_id] = page_id
story[story.Field.link_data] = link

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.name] = 'MPA Creative'
creative[AdCreative.Field.object_story_spec] = story
creative.remote_create()
print(creative)
# _DOC close [ADCREATIVE_CREATE_MULTI_PRODUCT_AD]


post_id = fixtures.get_promotable_post()['id']

# _DOC open [ADCREATIVE_CREATE_PAGE_POST]
from facebookads.objects import AdCreative

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.object_story_id] = post_id
creative[AdCreative.Field.name] = 'AdCreative with post ID'

creative.remote_create()
print(creative)
# _DOC close [ADCREATIVE_CREATE_PAGE_POST]
creative.remote_delete()


post_id = fixtures.get_promotable_post()['id']

# _DOC open [ADCREATIVE_CREATE_URL_TAG]
# _DOC vars [ad_account_id:s, post_id]
from facebookads.objects import AdCreative

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.object_story_id] = post_id
creative[AdCreative.Field.name] = 'Ad Creative with URL tag'
creative[AdCreative.Field.url_tags] = 'key1=val1&key2=val2'

creative.remote_create()
print(creative)
# _DOC close [ADCREATIVE_CREATE_URL_TAG]


image = fixtures.create_image()
image_url = image[AdImage.Field.url]
video_id = fixtures.create_video().get_id_assured()

# _DOC open [ADCREATIVE_CREATE_VIDEO_PAGE_LIKE_AD]
# _DOC vars [image_url:s, page_id, ad_account_id:s, video_id]
from facebookads.objects import AdCreative
from facebookads.specs import ObjectStorySpec, VideoData
video_data = VideoData()
video_data[VideoData.Field.description] = 'My Description'
video_data[VideoData.Field.video_id] = video_id
video_data[VideoData.Field.image_url] = image_url
video_data[VideoData.Field.call_to_action] = {
    'type': 'LIKE_PAGE',
    'value': {
        'page': page_id,
    }
}

object_story_spec = ObjectStorySpec()
object_story_spec[ObjectStorySpec.Field.page_id] = page_id
object_story_spec[ObjectStorySpec.Field.video_data] = video_data

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.name] = 'Video Ad Creative'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()
# _DOC close [ADCREATIVE_CREATE_VIDEO_PAGE_LIKE_AD]


creative_id = fixtures.create_creative().get_id_assured()

# _DOC open [ADCREATIVE_DELETE]
# _DOC vars [creative_id]
from facebookads.objects import AdCreative

creative = AdCreative(creative_id)
creative.remote_delete()
# _DOC close [ADCREATIVE_DELETE]


creative_id = fixtures.create_creative().get_id_assured()

# _DOC open [ADCREATIVE_READ]
# _DOC vars [creative_id]
from facebookads.objects import AdCreative

creative = AdCreative(creative_id)
creative.remote_read(
    fields=[AdCreative.Field.name, AdCreative.Field.object_story_id]
)
# _DOC close [ADCREATIVE_READ]


creative_id = fixtures.create_creative().get_id_assured()

# _DOC open [ADCREATIVE_READ_THUMBNAIL_WITH_DIMENSIONS]
# _DOC vars [creative_id]
from facebookads.objects import AdCreative

creative = AdCreative(creative_id)
fields = [AdCreative.Field.thumbnail_url]
params = {
    'thumbnail_width': 150,
    'thumbnail_height': 120,
}
creative.remote_read(fields=fields, params=params)

print(creative[AdCreative.Field.thumbnail_url])
# _DOC close [ADCREATIVE_READ_THUMBNAIL_WITH_DIMENSIONS]
creative.remote_delete()


creative_id = fixtures.create_creative().get_id_assured()
creative_name = fixtures.unique_name('Test Creative')

# _DOC open [ADCREATIVE_UPDATE]
# _DOC vars [creative_id, creative_name]
from facebookads.objects import AdCreative

creative = AdCreative(creative_id)
creative[AdCreative.Field.name] = creative_name

creative.remote_update()
print(creative)
# _DOC close [ADCREATIVE_UPDATE]


# _DOC open [ADCREATIVE_CREATE_GET_DIRECTIONS_VIDEO]
# _DOC vars [video_image_url:s, video_id, page_id, ad_account_id:s]
from facebookads.objects import AdCreative

video_data = VideoData()
video_data[VideoData.Field.image_url] = image_url
video_data[VideoData.Field.video_id] = video_id
video_data[VideoData.Field.description]\
    = 'Come check out our new store in Menlo Park!'
video_data[VideoData.Field.call_to_action] = {
    'type': 'GET_DIRECTIONS',
    'value': {
        'link': 'fbgeo://37.48327, -122.15033, "1601 Willow Rd Menlo Park CA"',
    },
}

story = ObjectStorySpec()
story[ObjectStorySpec.Field.page_id] = page_id
story[ObjectStorySpec.Field.video_data] = video_data

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.object_story_spec] = story
creative.remote_create()
# _DOC close [ADCREATIVE_CREATE_GET_DIRECTIONS_VIDEO]
