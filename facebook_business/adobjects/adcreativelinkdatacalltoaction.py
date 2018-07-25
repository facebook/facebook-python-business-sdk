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

class AdCreativeLinkDataCallToAction(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeLinkDataCallToAction, self).__init__()
        self._isAdCreativeLinkDataCallToAction = True
        self._api = api

    class Field(AbstractObject.Field):
        type = 'type'
        value = 'value'

    class Type:
        open_link = 'OPEN_LINK'
        like_page = 'LIKE_PAGE'
        shop_now = 'SHOP_NOW'
        play_game = 'PLAY_GAME'
        install_app = 'INSTALL_APP'
        use_app = 'USE_APP'
        call = 'CALL'
        call_me = 'CALL_ME'
        install_mobile_app = 'INSTALL_MOBILE_APP'
        use_mobile_app = 'USE_MOBILE_APP'
        mobile_download = 'MOBILE_DOWNLOAD'
        book_travel = 'BOOK_TRAVEL'
        listen_music = 'LISTEN_MUSIC'
        watch_video = 'WATCH_VIDEO'
        learn_more = 'LEARN_MORE'
        sign_up = 'SIGN_UP'
        download = 'DOWNLOAD'
        watch_more = 'WATCH_MORE'
        no_button = 'NO_BUTTON'
        visit_pages_feed = 'VISIT_PAGES_FEED'
        apply_now = 'APPLY_NOW'
        buy_now = 'BUY_NOW'
        get_offer = 'GET_OFFER'
        get_offer_view = 'GET_OFFER_VIEW'
        buy_tickets = 'BUY_TICKETS'
        update_app = 'UPDATE_APP'
        get_directions = 'GET_DIRECTIONS'
        buy = 'BUY'
        message_page = 'MESSAGE_PAGE'
        donate = 'DONATE'
        subscribe = 'SUBSCRIBE'
        say_thanks = 'SAY_THANKS'
        sell_now = 'SELL_NOW'
        share = 'SHARE'
        donate_now = 'DONATE_NOW'
        get_quote = 'GET_QUOTE'
        contact_us = 'CONTACT_US'
        order_now = 'ORDER_NOW'
        add_to_cart = 'ADD_TO_CART'
        video_annotation = 'VIDEO_ANNOTATION'
        moments = 'MOMENTS'
        record_now = 'RECORD_NOW'
        get_showtimes = 'GET_SHOWTIMES'
        listen_now = 'LISTEN_NOW'
        event_rsvp = 'EVENT_RSVP'
        whatsapp_message = 'WHATSAPP_MESSAGE'
        follow_news_storyline = 'FOLLOW_NEWS_STORYLINE'

    _field_types = {
        'type': 'Type',
        'value': 'AdCreativeLinkDataCallToActionValue',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Type'] = AdCreativeLinkDataCallToAction.Type.__dict__.values()
        return field_enum_info
