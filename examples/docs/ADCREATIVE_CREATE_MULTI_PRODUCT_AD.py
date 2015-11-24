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

ad_account_id = test_config.account_id
page_id = test_config.page_id
image_hash = fixtures.create_image().get_hash()
url = test_config.app_url
video_id = fixtures.create_video().get_id_assured()

# _DOC open [ADCREATIVE_CREATE_MULTI_PRODUCT_AD]
# _DOC vars [ad_account_id:s, page_id, url:s, image_hash:s, video_id:s]
from facebookads.objects import AdCreative
from facebookads.specs import ObjectStorySpec, LinkData, AttachmentData

product1 = AttachmentData()
product1[AttachmentData.Field.link] = url + '/product1'
product1[AttachmentData.Field.name] = 'Product 1'
product1[AttachmentData.Field.description] = '$8.99'
product1[AttachmentData.Field.image_hash] = image_hash
product1[AttachmentData.Field.video_id] = video_id

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
