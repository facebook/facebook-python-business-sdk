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

##
# (#2654) Source Audience is Too Small: There aren't enough people in your
# source in the country you chose. Please choose a country that includes at
# least 100 people in your source.
from facebookads import test_config

exit(0)

ad_account_id = test_config.account_id
video_path = test_config.video_path

custom_audience_id = fixtures.create_custom_audience().get_id_assured()
video_id = fixtures.upload_video(video_path)['id']

# _DOC open [CUSTOM_AUDIENCE_CREATE_VIDEO_VIEWS_RETARGET]
# _DOC vars [ad_account_id:s, video_id]
from facebookads.objects import CustomAudience

lookalike = CustomAudience(parent_id=ad_account_id)
lookalike.update({
    CustomAudience.Field.subtype: CustomAudience.Subtype.lookalike,
    CustomAudience.Field.lookalike_spec: {
        'ratio': 0.01,
        'country': 'US',
        'engagement_specs': [
            {
                'action.type': 'video_view',
                'post': video_id,
            },
        ],
        'conversion_type': 'dynamic_rule',
    },
})

lookalike.remote_create()
print(lookalike)
# _DOC close [CUSTOM_AUDIENCE_CREATE_VIDEO_VIEWS_RETARGET]
lookalike.remote_delete()
