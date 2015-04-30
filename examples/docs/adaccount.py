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

FacebookAdsApi.init(app_id, app_secret, access_token)

# _DOC open [ADACCOUNT_READ]
from facebookads.objects import AdAccount

account = AdAccount(account_id)

account.remote_read(fields=[
    AdAccount.Field.name,
    AdAccount.Field.balance
])
print(account[AdAccount.Field.name])
print(account[AdAccount.Field.balance])
# _DOC close [ADACCOUNT_READ]

from facebookads.objects import AdAccount

account = AdAccount(account_id)
account.remote_read(fields=[AdAccount.Field.name])
old_name = account[AdAccount.Field.name]

# _DOC open [ADACCOUNT_UPDATE]
from facebookads.objects import AdAccount

account = AdAccount(account_id)

account[AdAccount.Field.name] = 'New Name'
account.remote_update()
# _DOC close [ADACCOUNT_UPDATE]

account[AdAccount.Field.name] = old_name
account.remote_update()

# _DOC open [ADACCOUNT_GET_ADCAMPAIGNS]
from facebookads.objects import AdAccount, AdCampaign

account = AdAccount(account_id)
campaigns = account.get_ad_campaigns(fields=[
    AdCampaign.Field.name,
])
for campaign in campaigns:
    print(campaign[AdCampaign.Field.name])
# _DOC close [ADACCOUNT_GET_ADCAMPAIGNS]

old_spend_cap = account.remote_read(fields=[
    AdAccount.Field.spend_cap
])[AdAccount.Field.spend_cap]

# _DOC open [ADACCOUNT_UPDATE_SPEND_CAP]
from facebookads.objects import AdAccount

account = AdAccount(account_id)

account[AdAccount.Field.spend_cap] = 10000
account.remote_update()
# _DOC close [ADACCOUNT_UPDATE_SPEND_CAP]

account[AdAccount.Field.spend_cap] = old_spend_cap
account.remote_update()

# _DOC open [ADACCOUNT_GET_ADSETS]
from facebookads.objects import AdAccount, AdSet

account = AdAccount(account_id)
adsets = account.get_ad_sets(fields=[AdSet.Field.name])

for adset in adsets:
    print(adset[AdSet.Field.name])
# _DOC close [ADACCOUNT_GET_ADSETS]

# _DOC open [ADACCOUNT_GET_CONNECTION_OBJECTS]
from facebookads.objects import AdAccount

account = AdAccount(account_id)
objects = account.get_connection_objects()

for obj in objects:
    print(obj[AdAccount.Field.name])
# _DOC close [ADACCOUNT_GET_CONNECTION_OBJECTS]

# _DOC open [ADACCOUNT_GET_ADUSERS]
from facebookads.objects import AdAccount, AdUser

account = AdAccount(account_id)
users = account.get_ad_users()
for user in users:
    print(user[AdUser.Field.id])
# _DOC close [ADACCOUNT_GET_ADUSERS]

# _DOC open [ADACCOUNT_READ_TOS_ACCEPTED]
from facebookads.objects import AdAccount

account = AdAccount(account_id)
account.remote_read(fields=[AdAccount.Field.tos_accepted])

for tos in account[AdAccount.Field.tos_accepted]:
    print(tos)
# _DOC close [ADACCOUNT_READ_TOS_ACCEPTED]

# _DOC open [ADACCOUNT_GET_ADIMAGES]
# from facebookads.objects import AdAccount

account = AdAccount(account_id)
images = account.get_ad_images()
# _DOC close [ADACCOUNT_GET_ADIMAGES]

# _DOC open [ADACCOUNT_GET_RATECARDS]
#from facebookads.objects import AdAccount

ad_account = AdAccount(account_id)
rate_cards = ad_account.get_rate_cards()
print rate_cards
# _DOC close [ADACCOUNT_GET_RATECARDS]
