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

from examples.docs import fixtures
from facebookads import test_config

pixel = fixtures.create_ads_pixel()
pixel_id = pixel.get_id()
business_id = test_config.business_id
destination_business_id = test_config.secondary_business_id
destination_account_id = test_config.secondary_account_id

# Secondary business needs to be accessible by token
if not fixtures.can_see_business(destination_business_id):
    raise Exception("can't see secondary business " +
                    destination_business_id,
                    )

# Secondary account needs to be accessible by token
if not fixtures.can_see_account(destination_account_id):
    raise Exception("can't see secondary account " +
                    destination_account_id,
                    )


# _DOC open [ADSPIXEL_GET_SHARED_ADACCOUNTS_BUSINESS]
# _DOC vars [destination_business_id:s, pixel_id]
from facebookads.objects import AdsPixel, AdAccount

pixel = AdsPixel(pixel_id)
shared_accounts = pixel.get_ad_accounts(destination_business_id)
for shared_account in shared_accounts:
    print(shared_account[AdAccount.Field.id])
# _DOC close [ADSPIXEL_GET_SHARED_ADACCOUNTS_BUSINESS]
