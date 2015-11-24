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

