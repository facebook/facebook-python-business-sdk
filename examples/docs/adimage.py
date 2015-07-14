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

from facebookads import test_config as config

ad_account_id = config.account_id
image_path = config.image_path
image_zip_path = config.images_zip_path

# _DOC open [ADIMAGE_CREATE]
# _DOC vars [ad_account_id:s, image_path:s]
from facebookads.objects import AdImage

image = AdImage(parent_id=ad_account_id)
image[AdImage.Field.filename] = image_path
image.remote_create()

# Output image Hash
print(image[AdImage.Field.hash])
# _DOC close [ADIMAGE_CREATE]

image_id = image[AdImage.Field.id]
image_hash = image[AdImage.Field.hash]

# _DOC open [ADIMAGE_DELETE]
# _DOC vars [image_id, ad_account_id:s, image_hash:s]
from facebookads.objects import AdImage

image = AdImage(image_id, ad_account_id)
image.remote_delete(params={AdImage.Field.hash: image_hash})
# _DOC close [ADIMAGE_DELETE]

# _DOC open [ADIMAGE_CREATE_ZIP]
# _DOC vars [image_zip_path:s, ad_account_id:s]
from facebookads.objects import AdImage

images = AdImage.remote_create_from_zip(
    filename=image_zip_path,
    parent_id=ad_account_id
)

# Output image hashes.
for image in images:
    print(image[AdImage.Field.hash])
# _DOC close [ADIMAGE_CREATE_ZIP]

image_1_hash = images[0][AdImage.Field.hash]
image_2_hash = images[1][AdImage.Field.hash]

# _DOC open [ADIMAGE_READ_MULTI_WITH_HASH]
# _DOC vars [ad_account_id:s, image_1_hash, image_2_hash]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)
params = {
    'hashes': [
        image_1_hash,
        image_2_hash,
    ],
}
images = account.get_ad_images(params=params)
# _DOC close [ADIMAGE_READ_MULTI_WITH_HASH]

for _image in images:
    image = AdImage(_image[AdImage.Field.id], ad_account_id)
    image.remote_delete(params={AdImage.Field.hash: _image[AdImage.Field.hash]})
