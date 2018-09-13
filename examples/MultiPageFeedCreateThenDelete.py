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
from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<ID>'
FacebookAdsApi.init(access_token=access_token)

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

# Pagepost delete
fields = [
]
params = {
}
print PagePost(pagepost_id).delete(
  fields=fields,
  params=params,
)