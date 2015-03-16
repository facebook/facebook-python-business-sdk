"""
Upload a video to adaccount
"""

from facebookads import FacebookAdsApi
from facebookads.objects import AdAccount, AdVideo

import configparser
import os

config = configparser.RawConfigParser()
this_dir = os.path.dirname(__file__)
config_filename = os.path.join(this_dir, 'my_app_session.cfg')

with open(config_filename) as config_file:
    config.readfp(config_file)

FacebookAdsApi.init(
    config.get('Authentication', 'app_id'),
    config.get('Authentication', 'app_secret'),
    config.get('Authentication', 'access_token'),
)

if __name__ == '__main__':
    my_account = AdAccount('act_<AD_ACCOUNT_ID>')

    # create video object
    video = AdVideo(parent_id=my_account.get_id_assured())

    # set video fields
    video[AdVideo.Field.filepath] = os.path.join(this_dir, 'test_video.mp4')

    # remove create
    video.remote_create()
    video.waitUntilEncodingReady()

    print(video)
