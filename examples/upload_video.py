"""
Upload a video to adaccount
"""

import sys
import os

sdk_path = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(1, sdk_path)

from facebook_business.objects import *

config_filename = os.path.join(sdk_path, './config.json')

config_file = open(config_filename)
config = json.load(config_file)
config_file.close()

### Setup session and api objects
session = FacebookSession(
    config['app_id'],
    config['app_secret'],
    config['access_token'],
)

FacebookAdsApi.set_default_api(FacebookAdsApi(session))

if __name__ == '__main__':
    # create video object
    video = AdVideo(parent_id=config['act_id'])

    video_path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        'facebook_business/test/misc/video.mp4'
    )

    # set video fields
    video[AdVideo.Field.filepath] = video_path

    # remote create
    video.remote_create()
    video.waitUntilEncodingReady()

    print(video)
