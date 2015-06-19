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

from facebookads.objects import *
from facebookads.api import *
from facebookads.exceptions import *

config_file = open('./examples/docs/config.json')
config = json.load(config_file)
config_file.close()

account_id = config['account_id']
access_token = config['access_token']
app_id = config['app_id']
app_secret = config['app_secret']

FacebookAdsApi.init(app_id, app_secret, access_token)

# _DOC open [CUSTOM_AUDIENCE_CREATE]
# _DOC vars [account_id:s]
from facebookads.objects import CustomAudience
audience = CustomAudience(parent_id=account_id)

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

# _DOC open [CUSTOM_AUDIENCE_UPDATE_NAME]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience
audience = CustomAudience(custom_audience_id)
audience[CustomAudience.Field.name] = 'Updated name for CA'
audience.remote_update()
# _DOC close [CUSTOM_AUDIENCE_UPDATE_NAME]

# _DOC open [CUSTOM_AUDIENCE_UPDATE_OPTOUT]
# _DOC vars [custom_audience_id:s]
from facebookads.objects import CustomAudience
audience = CustomAudience(custom_audience_id)
audience[CustomAudience.Field.opt_out_link] = 'http://www.yourdomain.com/optout'
audience.remote_update()
# _DOC close [CUSTOM_AUDIENCE_UPDATE_OPTOUT]

audience.remote_delete()

audience = CustomAudience(parent_id=account_id)
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

audience.remote_delete()
