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

ad_account_id = test_config.account_id

# _DOC open [ADACCOUNT_READ]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)

account.remote_read(fields=[
    AdAccount.Field.name,
    AdAccount.Field.balance
])
print(account[AdAccount.Field.name])
print(account[AdAccount.Field.balance])
# _DOC close [ADACCOUNT_READ]


# _DOC open [ADACCOUNT_READ_TOS_ACCEPTED]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)
account.remote_read(fields=[AdAccount.Field.tos_accepted])

for tos in account[AdAccount.Field.tos_accepted]:
    print(tos)
# _DOC close [ADACCOUNT_READ_TOS_ACCEPTED]


account = AdAccount(ad_account_id)
account.remote_read(fields=[AdAccount.Field.name])
old_name = account[AdAccount.Field.name]

# _DOC open [ADACCOUNT_UPDATE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)

account[AdAccount.Field.name] = 'New Name'
account.remote_update()
# _DOC close [ADACCOUNT_UPDATE]
account[AdAccount.Field.name] = old_name
account.remote_update()

# _DOC open [ADACCOUNT_GET_ADCAMPAIGNS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, AdCampaign

account = AdAccount(ad_account_id)
campaigns = account.get_ad_campaigns(fields=[
    AdCampaign.Field.name,
])
for campaign in campaigns:
    print(campaign[AdCampaign.Field.name])
# _DOC close [ADACCOUNT_GET_ADCAMPAIGNS]


# _DOC open [ADACCOUNT_UPDATE_SPEND_CAP]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)

account[AdAccount.Field.spend_cap] = 10000
account.remote_update()
# _DOC close [ADACCOUNT_UPDATE_SPEND_CAP]


# _DOC open [ADACCOUNT_GET_ADSETS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, AdSet

account = AdAccount(ad_account_id)
adsets = account.get_ad_sets(fields=[AdSet.Field.name])

for adset in adsets:
    print(adset[AdSet.Field.name])
# _DOC close [ADACCOUNT_GET_ADSETS]


# _DOC open [ADACCOUNT_GET_ADUSERS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, AdUser

account = AdAccount(ad_account_id)
users = account.get_ad_users()
for user in users:
    print(user[AdUser.Field.id])
# _DOC close [ADACCOUNT_GET_ADUSERS]


# _DOC open [ADACCOUNT_GET_CONNECTION_OBJECTS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)
objects = account.get_connection_objects()

for obj in objects:
    print(obj[AdAccount.Field.name])
# _DOC close [ADACCOUNT_GET_CONNECTION_OBJECTS]

# _DOC open [ADACCOUNT_GET_ADCREATIVES]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, AdCreative

ad_account = AdAccount(fbid=ad_account_id)
ad_account.get_ad_creatives(fields=[AdCreative.Field.object_story_id])
# _DOC close [ADACCOUNT_GET_ADCREATIVES]


# _DOC open [ADACCOUNT_GET_ADGROUPS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, AdGroup

ad_account = AdAccount(ad_account_id)
ad_groups = ad_account.get_ad_groups(fields=[AdGroup.Field.name])
for ad_group in ad_groups:
    print(ad_group[AdGroup.Field.name])
# _DOC close [ADACCOUNT_GET_ADGROUPS]


# _DOC open [ADACCOUNT_GET_ADGROUPS_WITH_STATUS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)
params = {
    'adgroup_status': ['ACTIVE', 'PAUSED', 'CAMPAIGN_PAUSED',
                       'CAMPAIGN_GROUP_PAUSED', 'PENDING_REVIEW', 'DISAPPROVED',
                       'PREAPPROVED', 'PENDING_BILLING_INFO', 'ARCHIVED']
}
adgroups = account.get_ad_groups(params=params)
for adgroup in adgroups:
    print(adgroup)
# _DOC close [ADACCOUNT_GET_ADGROUPS_WITH_STATUS]


# _DOC open [ADACCOUNT_GET_ADIMAGES]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

account = AdAccount(ad_account_id)
images = account.get_ad_images()
# _DOC close [ADACCOUNT_GET_ADIMAGES]



# _DOC open [ADACCOUNT_GET_CUSTOMAUDIENCES_NAME]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, CustomAudience

ad_account = AdAccount(ad_account_id)
custom_audiences = ad_account.get_custom_audiences(fields=[
    CustomAudience.Field.name
])
for custom_audience in custom_audiences:
    print(custom_audience[CustomAudience.Field.name])
# _DOC close [ADACCOUNT_GET_CUSTOMAUDIENCES_NAME]


# _DOC open [ADACCOUNT_GET_INSIGHTS_VIDEO_VIEWS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, Insights

account = AdAccount(ad_account_id)

params = {
    'action_breakdowns': Insights.ActionBreakdown.action_video_type,
    'date_preset': Insights.Preset.last_30_days,
    'fields': [
        Insights.Field.actions,
        Insights.Field.video_avg_pct_watched_actions,
        Insights.Field.video_complete_watched_actions,
    ],
}

stats = account.get_insights(params=params)
print(stats)
# _DOC close [ADACCOUNT_GET_INSIGHTS_VIDEO_VIEWS]


# _DOC open [ADACCOUNT_GET_RATECARDS]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount

ad_account = AdAccount(ad_account_id)
rate_cards = ad_account.get_rate_cards()
print(rate_cards)
# _DOC close [ADACCOUNT_GET_RATECARDS]


# _DOC open [ADACCOUNT_GET_TARGETING_DESCRIPTION]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdAccount, TargetingSpecsField

account = AdAccount(ad_account_id)
params = {
    'targeting_spec': {
        TargetingSpecsField.geo_locations: {
            TargetingSpecsField.countries: ['US', 'JP'],
        },
        TargetingSpecsField.genders: [1],
        TargetingSpecsField.age_min: 20,
        TargetingSpecsField.age_max: 24,
    }
}

targeting_description = account.get_targeting_description(params=params)

# Output the targeting description
for description in targeting_description['targetingsentencelines']:
    print(description['content'])
    for child in description['children']:
        print("\t" + child)
# _DOC close [ADACCOUNT_GET_TARGETING_DESCRIPTION]
