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
Pauses all active ad campaigns using batch calls.
"""

from facebook_business import FacebookSession
from facebook_business import FacebookAdsApi
from facebook_business.objects import (
    AdAccount,
    AdCampaign,
)

import batch_utils
import json
import os
from functools import partial

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

    print('**** Pausing all active ad campaigns...')

    active_campaigns_iterator = my_account.get_ad_campaigns(
        fields=[
            AdCampaign.Field.status,
            AdCampaign.Field.name,
        ],
        params={
            AdCampaign.Field.status: [AdCampaign.Status.active],
        }
    )
    CAMPAIGN_UPDATE_BATCH_LIMIT = 25

    # Iterate over batches of active AdCampaign's
    for campaigns in batch_utils.generate_batches(
        active_campaigns_iterator,
        CAMPAIGN_UPDATE_BATCH_LIMIT,
    ):
        api_batch = api.new_batch()

        # Update each campaign but put the remote_update call in api_batch
        for my_campaign in campaigns:
            my_campaign[AdCampaign.Field.status] = AdCampaign.Status.paused

            def callback_success(response, my_campaign=None):
                print(
                    "Paused %s successfully."
                    % my_campaign[AdCampaign.Field.name]
                )
            callback_success = partial(
                callback_success,
                my_campaign=my_campaign,
            )

            def callback_failure(response, my_campaign=None):
                print(
                    "FAILED to pause %s."
                    % my_campaign[AdCampaign.Field.name]
                )
                raise response.error()
            callback_failure = partial(
                callback_failure,
                my_campaign=my_campaign,
            )

            my_campaign.remote_update(
                batch=api_batch,
                success=callback_success,
                failure=callback_failure,
            )

        api_batch.execute()
    else:
        print("**** No active campaign found.")

    # Print out api statistics
    print("\nHTTP Request Statistics: %s attempted, %s succeeded." % (
        api.get_num_requests_attempted(),
        api.get_num_requests_succeeded(),
    ))
