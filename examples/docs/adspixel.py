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

from __future__ import print_function
from __future__ import unicode_literals

from facebookads import config


# _DOC open [ADSPIXEL_CREATE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdsPixel

pixel = AdsPixel(parent_id=ad_account_id)
pixel[AdsPixel.Field.name] = 'My new Pixel'

pixel.remote_create()
# _DOC close [ADSPIXEL_CREATE]

pixel_id = pixel.get_id()

# _DOC open [ADSPIXEL_READ_PIXEL_CODE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import AdsPixel, AdAccount

account = AdAccount(ad_account_id)
account.get_ads_pixels(fields=[AdsPixel.Field.code])
# _DOC close [ADSPIXEL_READ_PIXEL_CODE]

destination_account_id = config.secondary_account_id
business_id = config.business_id

# _DOC open [ADSPIXEL_SHARE_ADACCOUNT]
# _DOC vars [business_id:s, destination_account_id:s, pixel_id]
from facebookads.objects import AdsPixel

pixel = AdsPixel(pixel_id)

response = pixel.share_pixel(business_id, destination_account_id)
print(response.body())
# _DOC close [ADSPIXEL_SHARE_ADACCOUNT]

# _DOC open [ADSPIXEL_GET_ADACCOUNTS]
# _DOC vars [business_id:s, pixel_id]
from facebookads.objects import AdsPixel, AdAccount

pixel = AdsPixel(pixel_id)
shared_accounts = pixel.list_ad_accounts(business_id)
for shared_account in shared_accounts:
    print(shared_account[AdAccount.Field.id])
# _DOC close [ADSPIXEL_GET_ADACCOUNTS]

destination_business_id = config.secondary_business_id

# _DOC open [ADSPIXEL_SHARE_BUSINESS]
# _DOC vars [destination_business_id:s, pixel_id, business_id:s]
from facebookads.objects import AdsPixel

pixel = AdsPixel(pixel_id)

response = pixel.share_pixel_agencies(business_id, destination_business_id)
print(response.body())
# _DOC close [ADSPIXEL_SHARE_BUSINESS]

# We shared the pixel with another business but iit's not associate with any
# ad account.
pixel.share_pixel(destination_business_id, destination_account_id)

# _DOC open [ADSPIXEL_GET_SHARED_ADACCOUNTS_BUSINNES]
# _DOC vars [destination_business_id:s, pixel_id]
from facebookads.objects import AdsPixel, AdAccount

pixel = AdsPixel(pixel_id)
shared_accounts = pixel.list_ad_accounts(destination_business_id)
for shared_account in shared_accounts:
    print(shared_account[AdAccount.Field.id])
# _DOC close [ADSPIXEL_GET_SHARED_ADACCOUNTS_BUSINNES]

# _DOC open [ADSPIXEL_GET_BUSINNES]
# _DOC vars [pixel_id]
from facebookads.objects import AdsPixel, Business

pixel = AdsPixel(pixel_id)
shared_business = pixel.list_shared_agencies()
for business in shared_business:
    print(business[Business.Field.id])
# _DOC close [ADSPIXEL_GET_BUSINNES]
