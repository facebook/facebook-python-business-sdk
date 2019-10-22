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

"""
Creates several ads using batch calls.
"""

from facebook_business import FacebookSession
from facebook_business import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adset import AdSet
from . import ad_creation_utils

import json
import os

this_dir = os.path.dirname(__file__)
config_filename = os.path.join(this_dir, 'config.json')

config_file = open(config_filename)
config = json.load(config_file)
config_file.close()

### Setup session and api objects
session = FacebookSession(
    config['app_id'],
    config['app_secret'],
    config['access_token'],
)
api = FacebookAdsApi(session)

if __name__ == '__main__':
    FacebookAdsApi.set_default_api(api)

    # Get my account (first account associated with the user associated with the
    #                 session of the default api)
    my_account = AdAccount.get_my_account()

    #####################
    # Create multiple ads
    #####################

    print('**** Creating multiple ads...')

    # Create my ads (will use batch calling)
    my_ads = ad_creation_utils.create_multiple_website_clicks_ads(
        account=my_account,

        name="Visit Seattle - Many Ads Experiment",
        country='US',

        titles=["Visit Seattle", "Seattle Tourism"],
        bodies=[
            "New York Alki",
            "Pittsburgh of the west",
            "The Queen City",
            "Jet City",
            "Lesser Seattle",
            "The Emerald City",
            "The Next City",
        ],
        urls=["http://www.seattle.gov/visiting/"],
        image_paths=[
            os.path.join(
                os.path.dirname(__file__),
                os.pardir,
                'facebook_business/test/misc/image.png'
            )
        ],

        bid_strategy=AdSet.BidStrategy.lowest_cost_without_cap,
        daily_budget=3000,  # $30.00 per day

        age_min=13,
        age_max=65,

        paused=True,  # Default is False but let's keep this test ad paused
    )

    for ad in my_ads:
        print("created ad: %s" % str(ad[Ad.Field.creative]))

    # Print out api statistics
    print("\nHTTP Request Statistics: %s attempted, %s succeeded." % (
        api.get_num_requests_attempted(),
        api.get_num_requests_succeeded(),
    ))
