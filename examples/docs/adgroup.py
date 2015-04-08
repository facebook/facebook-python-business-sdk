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
app_id = config['app_id']
app_secret = config['app_secret']
image_path = config['image_jpg']

FacebookAdsApi.init(app_id, app_secret, access_token)

campaign = AdCampaign(parent_id=account_id)
campaign[AdCampaign.Field.name] = 'Foo'
campaign.remote_create()

adset = AdSet(parent_id=account_id)
adset[AdSet.Field.name] = 'Foo 2'
adset[AdSet.Field.campaign_group_id] = campaign.get_id()
adset[AdSet.Field.targeting] = {
    'geo_locations': {
        'countries': ['US']
    }
}
adset[AdSet.Field.bid_info] = {'CLICKS': 500}
adset[AdSet.Field.bid_type] = AdSet.BidType.cpc
adset[AdSet.Field.daily_budget] = 1000
adset.remote_create()

# _DOC open [ADGROUP_CREATE_INLINE_CREATIVE]
# from facebookads.objects import AdImage, AdCreative, AdGroup

image = AdImage(parent_id=account_id)
image[image.Field.filename] = image_path
image.remote_create()

creative = AdCreative(parent_id=account_id)
creative[AdCreative.Field.title] = 'My Test Creative'
creative[AdCreative.Field.body] = 'My Test Ad Creative Body'
creative[AdCreative.Field.object_url] = 'https://www.facebook.com/facebook'
creative[AdCreative.Field.image_hash] = image[AdImage.Field.hash]

adgroup = AdGroup(parent_id=account_id)
adgroup[AdGroup.Field.name] = 'My Ad'
adgroup[AdGroup.Field.campaign_id] = adset.get_id()
adgroup[AdGroup.Field.creative] = creative
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_INLINE_CREATIVE]

adgroup.remote_read(fields=[AdGroup.Field.creative])
creative_id = adgroup[AdGroup.Field.creative]['id']
adgroup.remote_delete()
adset.remote_delete()
campaign.remote_delete()
creative = AdCreative(fbid=creative_id)
creative.remote_delete()
image.remote_delete(params={AdImage.Field.hash: image[image.Field.hash]})
