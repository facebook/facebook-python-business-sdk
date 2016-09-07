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

class AdPromotedObject(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdPromotedObject, self).__init__()
        self._isAdPromotedObject = True
        self._api = api

    class Field(AbstractObject.Field):
        application_id = 'application_id'
        custom_event_type = 'custom_event_type'
        object_store_url = 'object_store_url'
        offer_id = 'offer_id'
        page_id = 'page_id'
        pixel_id = 'pixel_id'
        place_page_set_id = 'place_page_set_id'
        product_catalog_id = 'product_catalog_id'
        product_set_id = 'product_set_id'

    class CustomEventType:
        complete_registration = 'COMPLETE_REGISTRATION'
        content_view = 'CONTENT_VIEW'
        search = 'SEARCH'
        rate = 'RATE'
        tutorial_completion = 'TUTORIAL_COMPLETION'
        add_to_cart = 'ADD_TO_CART'
        add_to_wishlist = 'ADD_TO_WISHLIST'
        initiated_checkout = 'INITIATED_CHECKOUT'
        add_payment_info = 'ADD_PAYMENT_INFO'
        purchase = 'PURCHASE'
        lead = 'LEAD'
        level_achieved = 'LEVEL_ACHIEVED'
        achievement_unlocked = 'ACHIEVEMENT_UNLOCKED'
        spent_credits = 'SPENT_CREDITS'
        other = 'OTHER'

    _field_types = {
        'application_id': 'string',
        'custom_event_type': 'CustomEventType',
        'object_store_url': 'string',
        'offer_id': 'string',
        'page_id': 'string',
        'pixel_id': 'string',
        'place_page_set_id': 'string',
        'product_catalog_id': 'string',
        'product_set_id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CustomEventType'] = AdPromotedObject.CustomEventType.__dict__.values()
        return field_enum_info
