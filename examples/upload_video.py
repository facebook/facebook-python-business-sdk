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
Upload a video to adaccount
"""

import sys
import os

sdk_path = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(1, sdk_path)

from facebook_business import FacebookSession
from facebook_business import FacebookAdsApi
from facebook_business.adobjects.advideo import AdVideo

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
