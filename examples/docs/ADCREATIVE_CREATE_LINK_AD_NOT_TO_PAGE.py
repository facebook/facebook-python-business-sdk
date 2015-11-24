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
image_hash = fixtures.create_image().get_hash()

# _DOC open [ADCREATIVE_CREATE_LINK_AD_NOT_TO_PAGE]
# _DOC vars [ad_account_id:s, image_hash:s]
from facebookads.objects import AdCreative

creative = AdCreative(parent_id=ad_account_id)
creative[AdCreative.Field.title] = 'my title'
creative[AdCreative.Field.body] = 'my body'
creative[AdCreative.Field.object_url] = 'https://www.link.com'
creative[AdCreative.Field.link_url] = 'https://www.link.com'
creative[AdCreative.Field.image_hash] = image_hash

creative.remote_create()
# _DOC close [ADCREATIVE_CREATE_LINK_AD_NOT_TO_PAGE]

creative.remote_delete()
