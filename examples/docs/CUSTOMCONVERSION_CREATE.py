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
pixel_id = fixtures.create_ads_pixel().get_id()

"""
Needs to be whitelisted to delete this object. Also,
we can't create a CustomConversion object with the
same rule.
"""
try:
    # _DOC open [CUSTOMCONVERSION_CREATE]
    # _DOC vars [ad_account_id:s, pixel_id]
    from facebookads.objects import CustomConversion

    custom_conversion = CustomConversion(parent_id=ad_account_id)
    custom_conversion.update({
        CustomConversion.Field.name: 'Example Custom Conversion',
        CustomConversion.Field.pixel_id: pixel_id,
        CustomConversion.Field.pixel_rule: {
            'url': {'i_contains': 'thankyou.html'},
        },
        CustomConversion.Field.custom_event_type: 'PURCHASE',
    })

    custom_conversion.remote_create()
# _DOC close [CUSTOMCONVERSION_CREATE]
except:
    pass
