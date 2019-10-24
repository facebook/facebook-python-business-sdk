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
Prints account permissions and campaign statistics.
"""

from facebook_business import FacebookSession
from facebook_business import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign as AdCampaign
from facebook_business.adobjects.adaccountuser import AdAccountUser as AdUser

import json
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)
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

    print('\n\n\n********** Reading objects example. **********\n')

    ### Setup user and read the object from the server
    me = AdUser(fbid='me')

    ### Read user permissions
    print('>>> Reading permissions field of user:')
    pp.pprint(me.remote_read(fields=[AdUser.Field.name]))

    ### Get first account connected to the user
    my_account = me.get_ad_account()

    ### Read connections (in this case, the accounts connected to me)

    # Pro tip: Use list(me.get_ad_accounts()) to make a list out of
    # all the elements out of the iterator

    my_accounts_iterator = me.get_ad_accounts()
    print('>>> Reading accounts associated with user')
    for account in my_accounts_iterator:
        pp.pprint(account)

    print(">>> Campaign Stats")
    for campaign in my_account.get_ad_campaigns(fields=[AdCampaign.Field.name]):
        for stat in campaign.get_stats(fields=[
            'impressions',
            'clicks',
            'spent',
            'unique_clicks',
            'actions',
        ]):
            print(campaign[campaign.Field.name])
            for statfield in stat:
                print("\t%s:\t\t%s" % (statfield, stat[statfield]))
