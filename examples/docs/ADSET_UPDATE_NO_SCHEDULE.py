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
from examples.docs import fixtures
from facebookads import test_config
from facebookads.objects import AdSet

ad_account_id = test_config.account_id
ad_set_id = fixtures.create_adset(params={
    AdSet.Field.daily_budget: None,
    AdSet.Field.lifetime_budget: 100000,
    AdSet.Field.end_time: int(time.time() + 7 * 24 * 3600),
    AdSet.Field.pacing_type: [AdSet.PacingType.day_parting],
    AdSet.Field.adset_schedule: [
        {
            'start_minute': 540,
            'end_minute': 720,
            'days': [1, 2, 3, 4, 5],
        },
    ],
}).get_id()

# !_DOC [pruno]
# _DOC open [ADSET_UPDATE_NO_SCHEDULE]
# _DOC vars [ad_account_id:s, ad_set_id]
from facebookads.objects import AdSet

adset = AdSet(fbid=ad_set_id, parent_id=ad_account_id)
adset.update({
    AdSet.Field.pacing_type: [AdSet.PacingType.standard],
    AdSet.Field.adset_schedule: [],
})
adset.remote_update()
# _DOC close [ADSET_UPDATE_NO_SCHEDULE]
