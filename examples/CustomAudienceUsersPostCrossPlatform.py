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

from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<CUSTOM_AUDIENCE_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'payload': {'schema':['EMAIL','MADID','APPUID','LOOKALIKE_VALUE'],'app_ids':['<appID>'],'data':[['b36a83701f1c3191e19722d6f90274bc1b5501fe69ebf33313e440fe4b0fe210','6032d997-3ab0-4de0-aa16-8af0e5b482fb','1234567890','0.9'],['2b3b2b9ce842ab8b6a6c614cb1f9604bb8a0d502d1af49c526b72b10894e95b5','B67385F8-9A82-4670-8C0A-6F9EA7513F5F','','0'],['898628e28890f937bdf009391def42879c401a4bcf1b5fd24e738d9f5da8cbbb','','9876543210','0.4']]},
}
print CustomAudience(id).create_user(
  fields=fields,
  params=params,
)