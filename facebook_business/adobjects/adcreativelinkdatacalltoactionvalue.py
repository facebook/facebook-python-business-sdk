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

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCreativeLinkDataCallToActionValue(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeLinkDataCallToActionValue, self).__init__()
        self._isAdCreativeLinkDataCallToActionValue = True
        self._api = api

    class Field(AbstractObject.Field):
        app_destination = 'app_destination'
        app_link = 'app_link'
        application = 'application'
        event_id = 'event_id'
        lead_gen_form_id = 'lead_gen_form_id'
        link = 'link'
        link_caption = 'link_caption'
        link_format = 'link_format'
        page = 'page'
        product_link = 'product_link'
        whatsapp_number = 'whatsapp_number'

    _field_types = {
        'app_destination': 'string',
        'app_link': 'string',
        'application': 'string',
        'event_id': 'string',
        'lead_gen_form_id': 'string',
        'link': 'string',
        'link_caption': 'string',
        'link_format': 'string',
        'page': 'string',
        'product_link': 'string',
        'whatsapp_number': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


