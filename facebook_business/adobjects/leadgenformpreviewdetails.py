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

class LeadGenFormPreviewDetails(
    AbstractObject,
):

    def __init__(self, api=None):
        super(LeadGenFormPreviewDetails, self).__init__()
        self._isLeadGenFormPreviewDetails = True
        self._api = api

    class Field(AbstractObject.Field):
        call_to_action_title = 'call_to_action_title'
        default_appointment_scheduling_inline_context = 'default_appointment_scheduling_inline_context'
        default_thank_you_page = 'default_thank_you_page'
        edit_text = 'edit_text'
        email_inline_context_text = 'email_inline_context_text'
        next_button_text = 'next_button_text'
        personal_info_text = 'personal_info_text'
        phone_number_inline_context_text = 'phone_number_inline_context_text'
        review_your_info_text = 'review_your_info_text'
        slide_to_submit_text = 'slide_to_submit_text'
        submit_button_text = 'submit_button_text'

    _field_types = {
        'call_to_action_title': 'string',
        'default_appointment_scheduling_inline_context': 'string',
        'default_thank_you_page': 'Object',
        'edit_text': 'string',
        'email_inline_context_text': 'string',
        'next_button_text': 'string',
        'personal_info_text': 'string',
        'phone_number_inline_context_text': 'string',
        'review_your_info_text': 'string',
        'slide_to_submit_text': 'string',
        'submit_button_text': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
