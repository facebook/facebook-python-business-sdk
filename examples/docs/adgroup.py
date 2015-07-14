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
from facebookads.objects import *
from facebookads.specs import *

ad_account_id = config.account_id
access_token = config.access_token
app_id = config.app_id
app_secret = config.app_secret
page_id = config.page_id
image_path = config.image_path

campaign = AdCampaign(parent_id=ad_account_id)
campaign[AdCampaign.Field.name] = 'Foo'
campaign.remote_create()

adset = AdSet(parent_id=ad_account_id)
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
ad_set_id = adset.get_id_assured()

img = AdImage(parent_id=ad_account_id)
img[AdImage.Field.filename] = image_path
img.remote_create()
image_hash = img.get_hash()

link_data = LinkData()
link_data[LinkData.Field.message] = 'try it out'
link_data[LinkData.Field.link] = 'http://example.com'
link_data[LinkData.Field.caption] = 'www.example.com'
link_data[LinkData.Field.image_hash] = image_hash

object_story_spec = ObjectStorySpec()
object_story_spec[ObjectStorySpec.Field.page_id] = page_id
object_story_spec[ObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()
creative_id = creative.get_id_assured()

# _DOC open [ADGROUP_CREATE]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id:s]
from facebookads.objects import AdGroup

adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'My AdGroup'
adgroup[AdGroup.Field.campaign_id] = ad_set_id
adgroup[AdGroup.Field.status] = AdGroup.Status.paused
adgroup[AdGroup.Field.creative] = {
    'creative_id': creative_id,
}
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE]

adgroup.remote_delete()
creative.remote_delete()

# _DOC open [ADGROUP_CREATE_REDOWNLOAD]
# _DOC vars [ad_set_id, creative_id, ad_account_id:s]
from facebookads.objects import AdGroup

adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'My AdGroup'
adgroup[AdGroup.Field.campaign_id] = ad_set_id
adgroup[AdGroup.Field.creative] = {'creative_id': str(creative_id)}
adgroup[AdGroup.Field.status] = AdGroup.Status.paused
adgroup[AdGroup.Field.redownload] = True
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_REDOWNLOAD]

ad_group_id = adgroup.get_id()

# _DOC open [ADGROUP_READ]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_read(fields=[AdGroup.Field.name])
# _DOC close [ADGROUP_READ]

# _DOC open [ADGROUP_READ_CONVERSION_BID]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_read(fields=[AdGroup.Field.conversion_specs, 'bid_type'])
# _DOC close [ADGROUP_READ_CONVERSION_BID]

# _DOC open [ADGROUP_UPDATE]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup[AdGroup.Field.name] = 'New AdGroup Name'
adgroup.remote_update()
# _DOC close [ADGROUP_UPDATE]

# _DOC open [ADGROUP_UPDATE_WITH_REDOWNLOAD]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup[AdGroup.Field.name] = 'New AdGroup Name'
adgroup['redownload'] = True
adgroup.remote_update()
# _DOC close [ADGROUP_UPDATE_WITH_REDOWNLOAD]

# _DOC open [ADGROUP_UPDATE_STATUS]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup[AdGroup.Field.status] = AdGroup.Status.paused
adgroup.remote_update()
# _DOC close [ADGROUP_UPDATE_STATUS]

# _DOC open [ADGROUP_ARCHIVE]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_archive()
# _DOC close [ADGROUP_ARCHIVE]

# _DOC open [ADGROUP_DELETE]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_delete()
# _DOC close [ADGROUP_DELETE]


# _DOC open [ADGROUP_CREATE_INLINE_CREATIVE]
# _DOC vars [ad_account_id:s, image_hash:s, ad_set_id]
from facebookads.objects import AdImage, AdCreative, AdGroup

# First, upload the ad image that you will use in your ad creative
# Please refer to Ad Image Create for details.

# Then, use the image hash returned from above
creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.title] = 'My Test Creative'
creative[AdCreative.Field.body] = 'My Test Ad Creative Body'
creative[AdCreative.Field.object_url] = 'https://www.facebook.com/facebook'
creative[AdCreative.Field.image_hash] = image_hash

# Finally, create your ad along with ad creative.
# Please note that the ad creative is not created independently, rather its
# data structure is appended to the ad group
adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'My Ad'
adgroup[AdGroup.Field.campaign_id] = ad_set_id
adgroup[AdGroup.Field.creative] = creative
adgroup[AdGroup.Field.status] = AdGroup.Status.paused
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_INLINE_CREATIVE]

ad_creatives = adgroup.get_ad_creatives(fields=[AdCreative.Field.name])

# _DOC open [ADGROUP_READ_FAILED_DELIVERY_CHECKS]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_read(fields=[AdGroup.Field.failed_delivery_checks])
# _DOC close [ADGROUP_READ_FAILED_DELIVERY_CHECKS]

# _DOC open [ADGROUP_GET_TARGETING_DESCRIPTION]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
targeting_description = adgroup.get_targeting_description()

# Output the targeting description
for description in targeting_description['targetingsentencelines']:
    print(description['content'])
    for child in description['children']:
        print("\t" + child)
# _DOC close [ADGROUP_GET_TARGETING_DESCRIPTION]

adgroup.remote_delete()
adset.remote_delete()
campaign.remote_delete()
creative = AdCreative(fbid=creative_id)
creative.remote_delete()
for creative in ad_creatives:
    creative = AdCreative(fbid=creative.get_id_assured())
    creative.remote_delete()

img.remote_delete(params={AdImage.Field.hash: image_hash})
