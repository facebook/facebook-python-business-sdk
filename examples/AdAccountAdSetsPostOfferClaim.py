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

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Offer Claim AdSet',
  'lifetime_budget': '56000',
  'start_time': '2019-12-05T23:42:58-0800',
  'end_time': '2019-12-12T23:42:58-0800',
  'campaign_id': '<adCampaignLinkClicksID>',
  'billing_event': 'LINK_CLICKS',
  'optimization_goal': 'LINK_CLICKS',
  'bid_amount': '1000',
  'promoted_object': {'page_id':'<pageID>','offer_id':'<offerID>'},
  'targeting': {'geo_locations':{'countries':['US']},'genders':[1],'age_min':'25','age_max':'55','facebook_positions':['feed']},
}
print AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)