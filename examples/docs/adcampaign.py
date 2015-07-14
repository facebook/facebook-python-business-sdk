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
access_token = config.access_token
app_id = config.app_id
app_secret = config.app_secret

# _DOC open [ADCAMPAIGN_CREATE_WEBSITE_CONVERSIONS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign[AdCampaign.Field.name] = 'My First Campaign'
campaign[AdCampaign.Field.status] = AdCampaign.Status.paused
campaign[AdCampaign.Field.objective] = AdCampaign.Objective.website_conversions

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_WEBSITE_CONVERSIONS]
campaign.remote_delete()

# _DOC open [ADCAMPAIGN_CREATE_HOMEPAGE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign.update({
    AdCampaign.Field.name: 'Homepage Campaign',
    AdCampaign.Field.buying_type: AdCampaign.BuyingType.fixed_cpm,
    AdCampaign.Field.objective: AdCampaign.Objective.none,
    AdCampaign.Field.status: AdCampaign.Status.paused,
})

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_HOMEPAGE]

campaign_group_id = campaign.get_id()

# _DOC open [ADCAMPAIGN_GET_ADGROUPS]
# _DOC vars [campaign_group_id]
from facebookads.objects import AdCampaign, AdGroup

ad_campaign = AdCampaign(campaign_group_id)
ad_group_iter = ad_campaign.get_ad_groups(fields=[AdGroup.Field.name])
for ad_group in ad_group_iter:
    print(ad_group[AdGroup.Field.name])
# _DOC close [ADCAMPAIGN_GET_ADGROUPS]

campaign.remote_delete()

# _DOC open [ADCAMPAIGN_CREATE_VIDEO_VIEWS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=ad_account_id)
campaign.update({
    AdCampaign.Field.name: 'Video Views Campaign',
    AdCampaign.Field.status: AdCampaign.Status.paused,
    AdCampaign.Field.objective: AdCampaign.Objective.video_views,
})

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_VIDEO_VIEWS]

# _DOC open [ADCAMPAIGN_GET_ADGROUPS_WITH_STATUS_ARCHIVED]
# _DOC vars [campaign_group_id]
from facebookads.objects import AdGroup, AdCampaign

adcampaign_group_id = campaign_group_id
adcampaign = AdCampaign(adcampaign_group_id)
params = {
    AdGroup.Field.status: [AdGroup.Status.archived],
}
adgroup_iter = adcampaign.get_ad_groups(
    fields=[AdGroup.Field.name],
    params=params
)

for ad_group in adgroup_iter:
    print(ad_group[AdGroup.Field.name])
# _DOC close [ADCAMPAIGN_GET_ADGROUPS_WITH_STATUS_ARCHIVED]

campaign.remote_delete()
