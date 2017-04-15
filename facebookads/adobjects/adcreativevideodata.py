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

from facebookads.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCreativeVideoData(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeVideoData, self).__init__()
        self._isAdCreativeVideoData = True
        self._api = api

    class Field(AbstractObject.Field):
        branded_content_sponsor_page_id = 'branded_content_sponsor_page_id'
        branded_content_sponsor_relationship = 'branded_content_sponsor_relationship'
        call_to_action = 'call_to_action'
        description = 'description'
        image_hash = 'image_hash'
        image_url = 'image_url'
        offer_id = 'offer_id'
        page_welcome_message = 'page_welcome_message'
        targeting = 'targeting'
        title = 'title'
        video_id = 'video_id'

    _field_types = {
        'branded_content_sponsor_page_id': 'string',
        'branded_content_sponsor_relationship': 'string',
        'call_to_action': 'AdCreativeLinkDataCallToAction',
        'description': 'string',
        'image_hash': 'string',
        'image_url': 'string',
        'offer_id': 'string',
        'page_welcome_message': 'string',
        'targeting': 'Targeting',
        'title': 'string',
        'video_id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
