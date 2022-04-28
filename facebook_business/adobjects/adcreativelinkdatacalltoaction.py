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
        add_to_cart = 'ADD_TO_CART'
        apply_now = 'APPLY_NOW'
        book_travel = 'BOOK_TRAVEL'
        buy = 'BUY'
        buy_now = 'BUY_NOW'
        buy_tickets = 'BUY_TICKETS'
        call = 'CALL'
        call_me = 'CALL_ME'
        call_now = 'CALL_NOW'
        contact = 'CONTACT'
        contact_us = 'CONTACT_US'
        donate = 'DONATE'
        donate_now = 'DONATE_NOW'
        download = 'DOWNLOAD'
        event_rsvp = 'EVENT_RSVP'
        find_a_group = 'FIND_A_GROUP'
        find_your_groups = 'FIND_YOUR_GROUPS'
        follow_news_storyline = 'FOLLOW_NEWS_STORYLINE'
        follow_page = 'FOLLOW_PAGE'
        follow_user = 'FOLLOW_USER'
        get_directions = 'GET_DIRECTIONS'
        get_offer = 'GET_OFFER'
        get_offer_view = 'GET_OFFER_VIEW'
        get_quote = 'GET_QUOTE'
        get_showtimes = 'GET_SHOWTIMES'
        install_app = 'INSTALL_APP'
        install_mobile_app = 'INSTALL_MOBILE_APP'
        learn_more = 'LEARN_MORE'
        like_page = 'LIKE_PAGE'
        listen_music = 'LISTEN_MUSIC'
        listen_now = 'LISTEN_NOW'
        message_page = 'MESSAGE_PAGE'
        mobile_download = 'MOBILE_DOWNLOAD'
        moments = 'MOMENTS'
        no_button = 'NO_BUTTON'
        open_link = 'OPEN_LINK'
        order_now = 'ORDER_NOW'
        pay_to_access = 'PAY_TO_ACCESS'
        play_game = 'PLAY_GAME'
        play_game_on_facebook = 'PLAY_GAME_ON_FACEBOOK'
        purchase_gift_cards = 'PURCHASE_GIFT_CARDS'
        record_now = 'RECORD_NOW'
        refer_friends = 'REFER_FRIENDS'
        request_time = 'REQUEST_TIME'
        say_thanks = 'SAY_THANKS'
        see_more = 'SEE_MORE'
        sell_now = 'SELL_NOW'
        send_a_gift = 'SEND_A_GIFT'
        send_gift_money = 'SEND_GIFT_MONEY'
        share = 'SHARE'
        shop_now = 'SHOP_NOW'
        sign_up = 'SIGN_UP'
        sotto_subscribe = 'SOTTO_SUBSCRIBE'
        start_order = 'START_ORDER'
        subscribe = 'SUBSCRIBE'
        swipe_up_product = 'SWIPE_UP_PRODUCT'
        swipe_up_shop = 'SWIPE_UP_SHOP'
        update_app = 'UPDATE_APP'
        use_app = 'USE_APP'
        use_mobile_app = 'USE_MOBILE_APP'
        video_annotation = 'VIDEO_ANNOTATION'
        video_call = 'VIDEO_CALL'
        visit_pages_feed = 'VISIT_PAGES_FEED'
        watch_more = 'WATCH_MORE'
        watch_video = 'WATCH_VIDEO'
        whatsapp_message = 'WHATSAPP_MESSAGE'
        woodhenge_support = 'WOODHENGE_SUPPORT'

    _field_types = {
        'type': 'Type',
        'value': 'AdCreativeLinkDataCallToActionValue',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Type'] = AdCreativeLinkDataCallToAction.Type.__dict__.values()
        return field_enum_info


