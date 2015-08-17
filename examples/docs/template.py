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

'''
    This is a template for DocSmith samples in Python. Copy it and create yours

    Code should follow guidelines at
    https://our.intern.facebook.com/intern/wiki/Solutions_Engineering/DocSmith

    Each example should be run using facebookads/docs_runner/doc_runner.py

    Comments on style:
    - IDs should be defined outside of _DOC blocks so they don't appear into the
    docs
    - Dependencies, like campaigns, should be generated in the fixtures module
'''

from examples.docs import fixtures

campaign_group_id = fixtures.create_adcampaign().get_id_assured()


#! _DOC open [TEMPLATE]
#! _DOC vars [campaign_group_id]
from facebookads.objects import AdCampaign, AdGroup

ad_campaign = AdCampaign(campaign_group_id)
ad_groups = ad_campaign.get_ad_groups(fields=[AdGroup.Field.name])

for ad_group in ad_groups:
    print(ad_group[AdGroup.Field.name])
#! _DOC close [TEMPLATE]
