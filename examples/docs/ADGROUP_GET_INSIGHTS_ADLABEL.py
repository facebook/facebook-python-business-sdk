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
from facebookads.objects import AdLabel

ad_id = fixtures.create_ad().get_id()
ad_label = fixtures.create_adlabel()
ad_label_name = ad_label[AdLabel.Field.name]

# _DOC open [ADGROUP_GET_INSIGHTS_ADLABEL]
# _DOC vars [ad_label_name, ad_label_id]
from facebookads.objects import Ad, Insights

ad = Ad(ad_id)
params = {
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

fields = [
    Insights.Field.unique_clicks,
    Insights.Field.ctr,
    Insights.Field.total_actions,
]

stats = ad.get_insights(fields, params=params)
print(stats)
# _DOC close [ADGROUP_GET_INSIGHTS_ADLABEL]
