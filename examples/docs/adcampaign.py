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

import sys
import os
from facebookads.objects import *
from facebookads.api import *
from facebookads.exceptions import *

this_dir = os.path.dirname(__file__)
repo_dir = os.path.join(this_dir, os.pardir, os.pardir)
sys.path.insert(1, repo_dir)

config_file = open(os.path.join(this_dir, 'config.json'))
config = json.load(config_file)
config_file.close()

account_id = config['account_id']
access_token = config['access_token']
app_id = config['app_id']
app_secret = config['app_secret']

FacebookAdsApi.init(app_id, app_secret, access_token)

# _DOC open [ADCAMPAIGN_CREATE_WEBSITE_CONVERSIONS]
# _DOC vars [account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=account_id)
campaign[AdCampaign.Field.name] = 'My First Campaign'
campaign[AdCampaign.Field.status] = AdCampaign.Status.paused
campaign[AdCampaign.Field.objective] = AdCampaign.Objective.website_conversions

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_WEBSITE_CONVERSIONS]
campaign.remote_delete()

# _DOC open [ADCAMPAIGN_CREATE_HOMEPAGE]
# _DOC vars [account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=account_id)
campaign.update({
    AdCampaign.Field.name: 'Homepage Campaign',
    AdCampaign.Field.buying_type: AdCampaign.BuyingType.fixed_cpm,
    AdCampaign.Field.objective: AdCampaign.Objective.none,
    AdCampaign.Field.status: AdCampaign.Status.paused,
})

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_HOMEPAGE]
campaign.remote_delete()

# _DOC open [ADCAMPAIGN_CREATE_VIDEO_VIEWS]
# _DOC vars [account_id:s]
from facebookads.objects import AdCampaign

campaign = AdCampaign(parent_id=account_id)
campaign.update({
    AdCampaign.Field.name: 'Video Views Campaign',
    AdCampaign.Field.status: AdCampaign.Status.paused,
    AdCampaign.Field.objective: AdCampaign.Objective.video_views,
})

campaign.remote_create()
print(campaign)
# _DOC close [ADCAMPAIGN_CREATE_VIDEO_VIEWS]
campaign.remote_delete()
