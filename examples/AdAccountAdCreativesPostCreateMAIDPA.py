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

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adcreative import AdCreative
from facebookads.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'Dynamic Ad Template Creative Sample',
  'object_story_spec': {'page_id':'<pageID>','template_data':{'call_to_action':{'type':'INSTALL_MOBILE_APP','value':{'link':'http://www.example.com/appstoreurl'}},'message':'Test {{product.name | titleize}}','link':'http://www.example.com/appstoreurl','name':'Headline {{product.price}}','description':'Description {{product.description}}'}},
  'product_set_id': '<productSetID>',
}
print AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
)