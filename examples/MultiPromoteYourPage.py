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

from facebookads.adobjects.user import User
from facebookads.adobjects.page import Page
from facebookads.adobjects.pagepost import PagePost
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.ad import Ad
from facebookads.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<ID>'
FacebookAdsApi.init(access_token=access_token)

# User get
fields = [
]
params = {
}
user = User(id).get(
  fields=fields,
  params=params,
)
print 'user', user
user_id = user.get_id()
print 'user_id:', user_id, '\n'

# Get page access token and page_id
fields = [
  'access_token',
]
params = {
}
pages = User(id).get_accounts(
  fields=fields,
  params=params,
)
print 'pages', pages
page_id = pages[0].get_id()
print 'page_id:', page_id, '\n'

# Switch access token to page access token
FacebookAdsApi.init(access_token=pages[0].access_token)
# Page feed create
fields = [
]
params = {
  'message': 'This is a test value',
}
pagepost = Page(page_id).create_feed(
  fields=fields,
  params=params,
)
print 'pagepost', pagepost
pagepost_id = pagepost.get_id()
print 'pagepost_id:', pagepost_id, '\n'

# Switch access token back to user access token
FacebookAdsApi.init(access_token=access_token)
# User adaccounts get
fields = [
]
params = {
}
adaccounts = User(user_id).get_ad_accounts(
  fields=fields,
  params=params,
)
print 'adaccounts', adaccounts
adaccount_id = adaccounts[0].get_id()
print 'adaccount_id:', adaccount_id, '\n'

# AdCampaign create
fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
}
adcampaign = AdAccount(adaccount_id).create_campaign(
  fields=fields,
  params=params,
)
print 'adcampaign', adcampaign
adcampaign_id = adcampaign.get_id()
print 'adcampaign_id:', adcampaign_id, '\n'

# AdSet create
fields = [
]
params = {
  'name': 'My Reach Ad Set',
  'optimization_goal': 'REACH',
  'billing_event': 'IMPRESSIONS',
  'bid_amount': '2',
  'daily_budget': '1000',
  'campaign_id': adcampaign_id,
  'targeting': {'geo_locations':{'countries':['US']}},
  'status': 'PAUSED',
  'promoted_object': {'page_id':page_id},
}
adset = AdAccount(adaccount_id).create_ad_set(
  fields=fields,
  params=params,
)
print 'adset', adset
adset_id = adset.get_id()
print 'adset_id:', adset_id, '\n'

# AdCreative create page post
fields = [
]
params = {
  'name': 'Sample Promoted Post',
  'object_story_id': page_id + '_' + pagepost_id,
}
adcreative = AdAccount(adaccount_id).create_ad_creative(
  fields=fields,
  params=params,
)
print 'adcreative', adcreative
adcreative_id = adcreative.get_id()
print 'adcreative_id:', adcreative_id, '\n'

# AdGroup create
fields = [
]
params = {
  'name': 'My Ad',
  'adset_id': adset_id,
  'creative': {'creative_id':adcreative_id},
  'status': 'PAUSED',
}
print AdAccount(adaccount_id).create_ad(
  fields=fields,
  params=params,
)