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
from facebookads.specs import *
from facebookads.api import *
from facebookads.session import *
from facebookads.exceptions import *

config_file = open('./examples/docs/config.json')
config = json.load(config_file)
config_file.close()

account_id = config['account_id']
access_token = config['access_token']
image_jpg = config['image_jpg']
image_zip = config['image_zip']
object_id = config['object_id']
object_url = config['object_url']
hash_1 = config['hash_1']
hash_2 = config['hash_2']
app_id = config['app_id']
app_secret = config['app_secret']

FacebookAdsApi.init(app_id, app_secret, access_token)

campaign = AdCampaign(parent_id=account_id)
campaign['name'] = 'Foo'
campaign.remote_create()

adset = AdSet(parent_id=account_id)
adset['name'] = 'Foo 2'
adset['campaign_group_id'] = campaign.get_id()
adset['targeting'] = {
    'geo_locations': {
        'countries': ['US']
    }
}
adset['bid_info'] = {'CLICKS': 500}
adset['bid_type'] = 'CPC'
adset['daily_budget'] = 1000
adset.remote_create()


# _DOC open [ADIMAGE_CREATE_ZIP]
# from facebookads.objects import AdImage

images = AdImage.remote_create_from_zip(
    filename=image_zip,
    parent_id=account_id
)

# Output image hashes.
for image in images:
    print image[AdImage.Field.hash]
# _DOC close [ADIMAGE_CREATE_ZIP]

# _DOC open [ADIMAGE_CREATE]
# from facebookads.objects import AdImage

image = AdImage(parent_id=account_id)
image[AdImage.Field.filename] = image_jpg
image.remote_create()

# Output image Hash
print image[AdImage.Field.hash]
# _DOC close [ADIMAGE_CREATE]

# _DOC open [ADIMAGE_CREATE_HASH]
# from facebook.objects import AdCreative, AdGroup, AdImage

image = AdImage(parent_id=account_id)
image[AdImage.Field.filename] = image_jpg
image.remote_create()

creative = AdCreative(parent_id=account_id)
creative[AdCreative.Field.title] = 'My Test Creative'
creative[AdCreative.Field.body] = 'My Test Ad Creative Body'
creative[AdCreative.Field.object_url] = object_url
creative[AdCreative.Field.image_hash] = image[AdImage.Field.hash]
creative.remote_create()
# _DOC close [ADIMAGE_CREATE_HASH]

# _DOC open [ADIMAGE_ADGROUP_CREATE]
group = AdGroup(parent_id=account_id)
group[AdGroup.Field.status] = AdGroup.Status.paused
group[AdGroup.Field.name] = 'My ad'
group[AdGroup.Field.campaign_id] = adset.get_id()
group[AdGroup.Field.creative] = {
    'creative_id': creative[AdCreative.Field.id]
}
group.remote_create()
# _DOC close [ADIMAGE_ADGROUP_CREATE]

# _DOC open [ADIMAGE_READ]
# from facebookads.objects import AdImage

account = AdAccount(account_id)
images = account.get_ad_images()
# _DOC close [ADIMAGE_READ]

# _DOC open [ADIMAGE_READ_MULTI_WITH_HASH]
# from facebookads.objects import AdAccount

account = AdAccount(account_id)
params = {
    'hashes': [
        hash_1,
        hash_2,
    ],
}
images = account.get_ad_images(params=params)
# _DOC close [ADIMAGE_READ_MULTI_WITH_HASH]
