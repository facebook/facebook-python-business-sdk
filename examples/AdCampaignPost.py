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

from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_SET_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'bid_adjustments': {'user_groups':{'user_bucket':{'event_sources':['<pixelID>','<appID>'],'1':0.1,'2':0.2,'3':0.3,'default':{'gender':{'male':0.99,'female':0.12}}}}},
}
print AdSet(id).update(
  fields=fields,
  params=params,
)