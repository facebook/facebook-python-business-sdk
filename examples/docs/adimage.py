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

from facebookads.objects import *
from facebookads.api import *
from facebookads.exceptions import *

config_file = open('./examples/docs/config.json')
config = json.load(config_file)
config_file.close()

account_id = config['account_id']
access_token = config['access_token']
image_path = config['image_jpg']
image_zip_path = config['image_zip']
app_id = config['app_id']
app_secret = config['app_secret']

FacebookAdsApi.init(app_id, app_secret, access_token)

# _DOC open [ADIMAGE_CREATE]
# from facebookads.objects import AdImage

image = AdImage(parent_id=account_id)
image[AdImage.Field.filename] = image_path
image.remote_create()

# Output image Hash
print(image[AdImage.Field.hash])
# _DOC close [ADIMAGE_CREATE]

image_id = image[AdImage.Field.id]
image_hash = image[AdImage.Field.hash]

# _DOC open [ADIMAGE_DELETE]
# from facebookads.objects import AdImage

image = AdImage(image_id, account_id)
image.remote_delete(params={AdImage.Field.hash: image_hash})
# _DOC close [ADIMAGE_DELETE]

# _DOC open [ADIMAGE_CREATE_ZIP]
# from facebookads.objects import AdImage

images = AdImage.remote_create_from_zip(
    filename=image_zip_path,
    parent_id=account_id
)

# Output image hashes.
for image in images:
    print(image[AdImage.Field.hash])
# _DOC close [ADIMAGE_CREATE_ZIP]

image_1_hash = images[0][AdImage.Field.hash]
image_2_hash = images[1][AdImage.Field.hash]

# _DOC open [ADIMAGE_READ_MULTI_WITH_HASH]
# from facebookads.objects import AdAccount

account = AdAccount(account_id)
params = {
    'hashes': [
        image_1_hash,
        image_2_hash,
    ],
}
images = account.get_ad_images(params=params)
# _DOC close [ADIMAGE_READ_MULTI_WITH_HASH]

for _image in images:
    image = AdImage(_image[AdImage.Field.id], account_id)
    image.remote_delete(params={AdImage.Field.hash: image_hash})
