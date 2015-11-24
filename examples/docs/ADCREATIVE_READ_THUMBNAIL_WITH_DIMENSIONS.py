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

campaign_id = fixtures.create_campaign().get_id()
creative_id = fixtures.create_creative().get_id()

# _DOC open [ADCREATIVE_READ_THUMBNAIL_WITH_DIMENSIONS]
# _DOC vars [creative_id]
from facebookads.objects import AdCreative

creative = AdCreative(creative_id)
fields = [AdCreative.Field.thumbnail_url]
params = {
    'thumbnail_width': 150,
    'thumbnail_height': 120,
}
creative.remote_read(fields=fields, params=params)

print(creative[AdCreative.Field.thumbnail_url])
# _DOC close [ADCREATIVE_READ_THUMBNAIL_WITH_DIMENSIONS]

creative.remote_delete()
