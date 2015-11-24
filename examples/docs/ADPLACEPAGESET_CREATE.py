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

from examples.docs import fixtures
from facebookads import test_config

ad_account_id = test_config.account_id
page_id = fixtures.get_page_with_locations_id_assured()

# _DOC oncall [pruno]
# _DOC open [ADPLACEPAGESET_CREATE]
# _DOC vars [ad_account_id:s, page_id]
from facebookads.objects import AdPlacePageSet

ad_place_page_set = AdPlacePageSet(parent_id=ad_account_id)
ad_place_page_set.update({
    AdPlacePageSet.Field.name: 'Ad Place Page Set',
    AdPlacePageSet.Field.parent_page: page_id,
})
ad_place_page_set.remote_create()
# _DOC close [ADPLACEPAGESET_CREATE]

# CannotDelete
