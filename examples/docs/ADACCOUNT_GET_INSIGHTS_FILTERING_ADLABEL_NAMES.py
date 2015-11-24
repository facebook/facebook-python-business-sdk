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
from facebookads.objects import AdLabel

ad_account_id = test_config.account_id
ad_label_name = fixtures.create_adlabel()[AdLabel.Field.name]

# _DOC open [ADACCOUNT_GET_INSIGHTS_FILTERING_ADLABEL_NAMES]
# _DOC vars [ad_account_id:s, ad_label_name:s]
from facebookads.objects import AdAccount, Insights

ad_account = AdAccount(ad_account_id)
params = {
    'fields': [
        Insights.Field.unique_clicks,
        Insights.Field.ctr,
        Insights.Field.total_actions
    ],
    'level': 'ad',
    'filtering': [{
        'field': 'ad.adlabels',
        'operator': 'ANY',
        'value': [ad_label_name]
    }],
    'time_range': {
        'since': '2015-03-01',
        'until': '2015-03-31'
    }
}
stats = ad_account.get_insights(params=params)
print(stats)
# _DOC close [ADACCOUNT_GET_INSIGHTS_FILTERING_ADLABEL_NAMES]
