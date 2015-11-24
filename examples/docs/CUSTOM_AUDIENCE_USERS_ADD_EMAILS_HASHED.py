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

# _DOC open [CUSTOM_AUDIENCE_USERS_ADD_EMAILS_HASHED]
# _DOC vars [custom_audience_id]
from facebookads.objects import CustomAudience

audience = CustomAudience(custom_audience_id)
users = ['f1904cf1a9d73a55fa5de0ac823c4403ded71afd4c3248d00bdcd0866552bb79',
         'ff8d9819fc0e12bf0d24892e45987e249a28dce836a85cad60e28eaaa8c6d976',
         '5ff860bf1190596c7188ab851db691f0f3169c453936e9e1eba2f9a47f7a0018',
         ]

audience.add_users(CustomAudience.Schema.email_hash, users, None, True)
# _DOC close [CUSTOM_AUDIENCE_USERS_ADD_EMAILS_HASHED]
