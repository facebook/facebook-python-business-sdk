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
from facebookads import test_config

ad_account_id = test_config.account_id
video_path = test_config.video_path


# _DOC open [CUSTOM_AUDIENCE_CREATE]
# _DOC vars [ad_account_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(parent_id=ad_account_id)
audience[CustomAudience.Field.subtype] = CustomAudience.Subtype.custom
audience[CustomAudience.Field.name] = 'My new CA'
audience[CustomAudience.Field.description] = 'People who bought on my website'

audience.remote_create()
# _DOC close [CUSTOM_AUDIENCE_CREATE]


pixel_id = fixtures.create_ads_pixel().get_id_assured()

# _DOC open [CUSTOM_AUDIENCE_CREATE_WCA]
# _DOC vars [ad_account_id:s, pixel_id]
from facebookads.objects import CustomAudience

audience = CustomAudience(parent_id=ad_account_id)
audience[CustomAudience.Field.name] = 'my audience'
audience[CustomAudience.Field.subtype] = CustomAudience.Subtype.website
audience[CustomAudience.Field.retention_days] = 15
audience[CustomAudience.Field.rule] = {'url': {'i_contains': 'shoes'}}
audience[CustomAudience.Field.pixel_id] = pixel_id

audience.remote_create()
# _DOC close [CUSTOM_AUDIENCE_CREATE_WCA]


custom_audience_id = fixtures.create_custom_audience().get_id_assured()

# _DOC open [CUSTOM_AUDIENCE_DELETE]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience.remote_delete()
# _DOC close [CUSTOM_AUDIENCE_DELETE]


custom_audience_id = fixtures.create_custom_audience().get_id_assured()

# _DOC open [CUSTOM_AUDIENCE_READ_RULE]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience.remote_read(fields=[
    CustomAudience.Field.name,
    CustomAudience.Field.rule
])
# _DOC close [CUSTOM_AUDIENCE_READ_RULE]


custom_audience_id = fixtures.create_custom_audience().get_id_assured()

# _DOC open [CUSTOM_AUDIENCE_UPDATE_NAME]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience[CustomAudience.Field.name] = 'Updated name for CA'
audience.remote_update()
# _DOC close [CUSTOM_AUDIENCE_UPDATE_NAME]


custom_audience_id = fixtures.create_custom_audience().get_id_assured()

# _DOC open [CUSTOM_AUDIENCE_UPDATE_OPTOUT]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
audience[CustomAudience.Field.opt_out_link] = 'http://www.yourdomain.com/optout'
audience.remote_update()
# _DOC close [CUSTOM_AUDIENCE_UPDATE_OPTOUT]


custom_audience_id = fixtures.create_custom_audience().get_id_assured()

# _DOC open [CUSTOM_AUDIENCE_USERS_ADD_EMAILS]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
users = ['test1@example.com', 'test2@example.com', 'test3@example.com']

audience.add_users(CustomAudience.Schema.email_hash, users)
# _DOC close [CUSTOM_AUDIENCE_USERS_ADD_EMAILS]


custom_audience_id = fixtures.create_custom_audience().get_id_assured()
user_id_1 = 1234
user_id_2 = 12345
app_id = fixtures.test_config.app_id

# _DOC open [CUSTOM_AUDIENCE_USERS_ADD_ID]
# _DOC vars [custom_audience_id:s, app_id:s, user_id_1:s, user_id_2:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
users = [user_id_1, user_id_2]
apps = [app_id]
audience.add_users(CustomAudience.Schema.uid, users, apps)
# _DOC close [CUSTOM_AUDIENCE_USERS_ADD_ID]


custom_audience_id = fixtures.create_custom_audience().get_id_assured()

# _DOC open [CUSTOM_AUDIENCE_USERS_REMOVE_EMAILS]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
users = ['test1@example.com', 'test2@example.com', 'test3@example.com']

audience.remove_users(CustomAudience.Schema.email_hash, users)
# _DOC close [CUSTOM_AUDIENCE_USERS_REMOVE_EMAILS]


exit(0)

##
# (#2654) Source Audience is Too Small: There aren't enough people in your
# source in the country you chose. Please choose a country that includes at
# least 100 people in your source.

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
