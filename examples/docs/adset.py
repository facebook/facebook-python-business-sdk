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

import time

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
page_id = config['page_id']

FacebookAdsApi.init(app_id, app_secret, access_token)

ad_account = AdAccount(account_id)
rate_cards = ad_account.get_rate_cards()

homepage_campaign = AdCampaign(parent_id=account_id)
homepage_campaign.update({
    AdCampaign.Field.name: 'Homepage Ads',
    AdCampaign.Field.buying_type: AdCampaign.BuyingType.fixed_cpm,
    AdCampaign.Field.objective: AdCampaign.Objective.none,
})
homepage_campaign.remote_create()

homepage_campaign_group_id = homepage_campaign.get_id()
rate = rate_cards[0][RateCard.Field.rate]
country = rate_cards[0][RateCard.Field.country]

# _DOC open [ADSET_CREATE_HOMEPAGE]
#from facebookads.objects import AdSet
lifetime_budget = str(rate * 5000)
start_date = int(time.time())
end_date = int(time.time() + 12 * 3600)

ad_set = AdSet(parent_id=account_id)
ad_set.update({
    AdSet.Field.name: 'Adset Test DocSmith - Homepage Ads',
    AdSet.Field.campaign_group_id: homepage_campaign_group_id,
    AdSet.Field.bid_type: AdSet.BidType.multi_premium,
    AdSet.Field.bid_info: {
        AdSet.Field.BidInfo.clicks: 20,
        AdSet.Field.BidInfo.social: 40,
        AdSet.Field.BidInfo.impressions: 40
    },
    AdSet.Field.lifetime_budget: lifetime_budget,
    AdSet.Field.lifetime_imps: '5000',
    AdSet.Field.start_time: start_date,
    AdSet.Field.end_time: end_date,
    AdSet.Field.targeting: {
        TargetingSpecsField.page_types: ['home'],
        TargetingSpecsField.geo_locations: {
            'countries': [country],
        }
    },
    AdSet.Field.status: 'ACTIVE',
})

ad_set.remote_create()
print ad_set
# _DOC close [ADSET_CREATE_HOMEPAGE]

ad_set.remote_delete()
homepage_campaign.remote_delete()
