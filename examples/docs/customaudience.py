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

from facebookads import test_config as config
from facebookads.objects import *

app_id = config.app_id
ad_account_id = config.account_id
page_id = config.page_id
video_path = config.video_path

api = FacebookAdsApi.get_default_api()

response = api.call(
    'GET',
    'https://graph.facebook.com/' + FacebookAdsApi.API_VERSION + '/me/accounts',
)
data = response.json()['data']

page_token = ''
for page in data:
    if page['id'] == str(page_id):
        page_token = page['access_token']
        break
if page_token == '':
    raise Exception(
        'Page access token for the page id '
        + str(page_id) + ' cannot be found.'
    )

page_session = FacebookSession(config.app_id, config.app_secret, page_token)
page_api = FacebookAdsApi(page_session)

graph_video_upload_url = 'https://graph-video.facebook.com/' \
    + FacebookAdsApi.API_VERSION + '/' + str(page_id) + '/videos'
response = page_api.call(
    'POST',
    graph_video_upload_url,
    files={'source': (video_path, 'multipart/form-data')},
)
video_id = response.json()['id']

# _DOC open [CUSTOM_AUDIENCE_CREATE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(parent_id=ad_account_id)
audience[CustomAudience.Field.name] = 'My new CA'
audience[CustomAudience.Field.description] = 'People who bought on my website'

audience.remote_create()
# _DOC close [CUSTOM_AUDIENCE_CREATE]

custom_audience_id = audience.get_id()

# _DOC open [CUSTOM_AUDIENCE_USERS_ADD_EMAILS]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
users = ['test1@example.com', 'test2@example.com', 'test3@example.com']

audience.add_users(CustomAudience.Schema.email_hash, users)
# _DOC close [CUSTOM_AUDIENCE_USERS_ADD_EMAILS]

# _DOC open [CUSTOM_AUDIENCE_USERS_REMOVE_EMAILS]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
users = ['test1@example.com', 'test2@example.com', 'test3@example.com']

audience.remove_users(CustomAudience.Schema.email_hash, users)
# _DOC close [CUSTOM_AUDIENCE_USERS_REMOVE_EMAILS]

# _DOC open [CUSTOM_AUDIENCE_UPDATE_OPTOUT]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience[CustomAudience.Field.opt_out_link] = 'http://www.yourdomain.com/optout'
audience.remote_update()
# _DOC close [CUSTOM_AUDIENCE_UPDATE_OPTOUT]

audience.remote_delete()

audience = CustomAudience(parent_id=ad_account_id)
audience[CustomAudience.Field.name] = 'My new CA'
audience[CustomAudience.Field.description] = 'Docsmith Example CA'
audience.remote_create()
custom_audience_id = audience.get_id()
user_id_1 = 1234
user_id_2 = 12345

# _DOC open [CUSTOM_AUDIENCE_USERS_ADD_ID]
# _DOC vars [custom_audience_id:s, app_id:s, user_id_1:s, user_id_2:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
users = [user_id_1, user_id_2]
apps = [app_id]
audience.add_users(CustomAudience.Schema.uid, users, apps)
# _DOC close [CUSTOM_AUDIENCE_USERS_ADD_ID]

account = AdAccount(ad_account_id)
pixels = account.get_ads_pixels([AdsPixel.Field.code])
if len(pixels):
    pixel = pixels[0]
else:
    pixel = AdsPixel(parent_id=ad_account_id)
    pixel[AdsPixel.Field.name] = 'My WCA Pixel'
    pixel.remote_create()

pixel_id = pixel[AdsPixel.Field.id]

# _DOC open [CUSTOM_AUDIENCE_CREATE_WCA]
# _DOC vars [ad_account_id:s, pixel_id]
from facebookads.objects import CustomAudience

audience = CustomAudience(parent_id=ad_account_id)
audience[CustomAudience.Field.name] = 'my audience'
audience[CustomAudience.Field.subtype] = 'WEBSITE'
audience[CustomAudience.Field.retention_days] = 15
audience[CustomAudience.Field.rule] = {'url': {'i_contains': 'shoes'}}
audience[CustomAudience.Field.pixel_id] = pixel_id

audience.remote_create()
# _DOC close [CUSTOM_AUDIENCE_CREATE_WCA]

custom_audience_id = audience.get_id()

# _DOC open [CUSTOM_AUDIENCE_UPDATE_NAME]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience[CustomAudience.Field.name] = 'Updated name for CA'
audience.remote_update()
# _DOC close [CUSTOM_AUDIENCE_UPDATE_NAME]

# _DOC open [CUSTOM_AUDIENCE_READ_RULE]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience.remote_read(fields=[
    CustomAudience.Field.name,
    CustomAudience.Field.rule
])
# _DOC close [CUSTOM_AUDIENCE_READ_RULE]

# _DOC open [CUSTOM_AUDIENCE_DELETE]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience.remote_delete()
# _DOC close [CUSTOM_AUDIENCE_DELETE]

# _DOC open [CUSTOM_AUDIENCE_CREATE_VIDEO_VIEWS_RETARGET]
# _DOC vars [ad_account_id:s, video_id]
from facebookads.objects import CustomAudience

lookalike = CustomAudience(parent_id=ad_account_id)
lookalike.update({
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
