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
from facebookads.objects import AdLabel
from examples.docs import fixtures
import string

ad_account_id = test_config.account_id
app_id = test_config.app_id
page_id = test_config.page_id
ad_set_id = fixtures.create_adset().get_id_assured()
ad_group_id = fixtures.create_adgroup().get_id_assured()
creative_id = fixtures.create_creative().get_id_assured()
image_hash = fixtures.create_image().get_hash()


# _DOC open [ADGROUP_CREATE]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id]
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


# _DOC open [ADGROUP_CREATE_TRACKING_APP_INSTALLS]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id, app_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'test'
adgroup[AdGroup.Field.campaign_id] = ad_set_id
adgroup[AdGroup.Field.creative] = {
    'creative_id': creative_id
}
adgroup[AdGroup.Field.tracking_specs] = {
    'action.type': 'app_install',
    'application': app_id
}
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_TRACKING_APP_INSTALLS]
adgroup.remote_delete()

object_story_id = fixtures.create_post(
    message=fixtures.unique_name('Test Post '))['id']

post_id = string.split(object_story_id, '_')[1]

# _DOC open [ADGROUP_CREATE_TRACKING_POST_LIKES]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id, object_story_id, page_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'test'
adgroup[AdGroup.Field.campaign_id] = ad_set_id
adgroup[AdGroup.Field.creative] = {
    'object_story_id': object_story_id
}
adgroup[AdGroup.Field.tracking_specs] = {
    'action.type': 'like',
    'post': post_id,
    'post.wall': page_id
}
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_TRACKING_POST_LIKES]
adgroup.remote_delete()


# _DOC open [ADGROUP_CREATE_TRACKING_LIKE_MENTIONS]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id, post_id, page_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'test'
adgroup[AdGroup.Field.campaign_id] = ad_set_id
adgroup[AdGroup.Field.creative] = {
    'creative_id': creative_id
}
adgroup[AdGroup.Field.tracking_specs] = {
    'action.type': ['like', 'mention'],
    'page': page_id
}
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_TRACKING_LIKE_MENTIONS]
adgroup.remote_delete()


# _DOC open [ADGROUP_CREATE_TRACKING_MUSIC_LISTENS]
# _DOC vars [ad_account_id:s, ad_set_id, creative_id, app_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'test'
adgroup[AdGroup.Field.campaign_id] = ad_set_id
adgroup[AdGroup.Field.creative] = {
    'creative_id': creative_id
}
adgroup[AdGroup.Field.tracking_specs] = {
    'action.type': 'music.listens',
    'application': app_id
}
adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_TRACKING_MUSIC_LISTENS]
adgroup.remote_delete()


# _DOC open [ADGROUP_CREATE_INLINE_CREATIVE]
# _DOC vars [ad_account_id:s, image_hash:s, ad_set_id]
from facebookads.objects import AdCreative, AdGroup

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
adgroup.remote_delete()


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
adgroup.remote_delete()


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


# _DOC open [ADGROUP_READ_FAILED_DELIVERY_CHECKS]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_read(fields=[AdGroup.Field.failed_delivery_checks])
# _DOC close [ADGROUP_READ_FAILED_DELIVERY_CHECKS]


# _DOC open [ADGROUP_UPDATE]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup[AdGroup.Field.name] = 'New AdGroup Name'
adgroup.remote_update()
# _DOC close [ADGROUP_UPDATE]


# _DOC open [ADGROUP_UPDATE_STATUS]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup[AdGroup.Field.status] = AdGroup.Status.paused
adgroup.remote_update()
# _DOC close [ADGROUP_UPDATE_STATUS]


# _DOC open [ADGROUP_UPDATE_WITH_REDOWNLOAD]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup[AdGroup.Field.name] = 'New AdGroup Name'
adgroup['redownload'] = True
adgroup.remote_update()
# _DOC close [ADGROUP_UPDATE_WITH_REDOWNLOAD]


# _DOC open [ADGROUP_ARCHIVE]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_archive()
# _DOC close [ADGROUP_ARCHIVE]


# _DOC open [ADGROUP_GET_ADLABELS]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.get_ad_labels()
# _DOC close [ADGROUP_GET_ADLABELS]


ad_label = fixtures.create_adlabel()
ad_label_id = ad_label.get_id()
ad_group_id = fixtures.create_adgroup().get_id()

# _DOC open [ADGROUP_UPDATE_LABELS]
# _DOC vars [ad_group_id, ad_label_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup[AdGroup.Field.adlabels] = [
    {AdLabel.Field.id: ad_label_id},
    {AdLabel.Field.name: 'New Label Name'},
]
adgroup.remote.update()
# _DOC close [ADGROUP_UPDATE_LABELS]


# _DOC open [ADGROUP_ADD_LABELS]
# _DOC vars [ad_group_id, ad_label_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adlabels = [ad_label_id]
adgroup.add_labels(adlabels)
# _DOC close [ADGROUP_ADD_LABELS]


# _DOC open [ADGROUP_REMOVE_LABELS]
# _DOC vars [ad_group_id, ad_label_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adlabels = [ad_label_id]
adgroup.remove_labels(adlabels)
# _DOC close [ADGROUP_REMOVE_LABELS]


ad_label_name = ad_label[AdLabel.Field.name]

# _DOC open [ADGROUP_GET_INSIGHTS_ADLABEL]
# _DOC vars [ad_label_name, ad_label_id]
from facebookads.objects import AdGroup, Insights

adgroup = AdGroup(ad_group_id)
params = {
    'level': 'adgroup',
    'filtering': [{
        'field': 'adgroup.adlabels',
        'operator': 'ANY',
        'value': [ad_label_name]
    }],
    'time_range': {
        'since': '2015-03-01',
        'until': '2015-03-31'
    }
}

fields = [
    Insights.Field.clicks,
    Insights.Field.cpc,
    Insights.Field.total_actions,
]

stats = adgroup.get_insights(fields, params=params)
print(stats)
# _DOC close [ADGROUP_GET_INSIGHTS_ADLABEL]


# _DOC open [ADGROUP_DELETE]
# _DOC vars [ad_group_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(ad_group_id)
adgroup.remote_delete()
# _DOC close [ADGROUP_DELETE]

campaign_id = ad_set_id
# _DOC open [ADGROUP_CREATE_DYNAMIC_AD]
# _DOC vars [ad_account_id:s, campaign_id, creative_id]
from facebookads.objects import AdGroup

adgroup = AdGroup(parent_id=ad_account_id)
adgroup[AdGroup.Field.name] = 'my dynamic ad'
adgroup[AdGroup.Field.campaign_id] = campaign_id
adgroup[AdGroup.Field.creative] = {'creative_id': creative_id}

adgroup.remote_create()
# _DOC close [ADGROUP_CREATE_DYNAMIC_AD]
adgroup.remote_delete()
