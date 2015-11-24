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

ad_account_id = test_config.account_id
ad_label_id = fixtures.create_adlabel().get_id()

# _DOC open [ADACCOUNT_GET_ADGROUPS_BY_LABEL]
# _DOC vars [ad_account_id:s, ad_label_id]
from facebookads.objects import AdAccount, AdLabel, Ad

account = AdAccount(ad_account_id)
params = {'ad_label_ids': [ad_label_id], 'operator': 'ALL'}
adlabels = account.get_ads_by_labels([Ad.Field.name], params=params)

for adlabel in adlabels:
    print(adlabel[AdLabel.Field.name])
# _DOC close [ADACCOUNT_GET_ADGROUPS_BY_LABEL]
