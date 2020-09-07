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

class AdAssetFeedSpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdAssetFeedSpec, self).__init__()
        self._isAdAssetFeedSpec = True
        self._api = api

    class Field(AbstractObject.Field):
        ad_formats = 'ad_formats'
        additional_data = 'additional_data'
        asset_customization_rules = 'asset_customization_rules'
        autotranslate = 'autotranslate'
        bodies = 'bodies'
        call_to_action_types = 'call_to_action_types'
        call_to_actions = 'call_to_actions'
        captions = 'captions'
        carousels = 'carousels'
        descriptions = 'descriptions'
        groups = 'groups'
        images = 'images'
        link_urls = 'link_urls'
        optimization_type = 'optimization_type'
        titles = 'titles'
        videos = 'videos'

    class CallToActionTypes:
        add_to_cart = 'ADD_TO_CART'
        apply_now = 'APPLY_NOW'
        book_travel = 'BOOK_TRAVEL'
        buy = 'BUY'
        buy_now = 'BUY_NOW'
        buy_tickets = 'BUY_TICKETS'
        call = 'CALL'
        call_me = 'CALL_ME'
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
        purchase_gift_cards = 'PURCHASE_GIFT_CARDS'
        record_now = 'RECORD_NOW'
        request_time = 'REQUEST_TIME'
        say_thanks = 'SAY_THANKS'
        see_more = 'SEE_MORE'
        sell_now = 'SELL_NOW'
        send_a_gift = 'SEND_A_GIFT'
        share = 'SHARE'
        shop_now = 'SHOP_NOW'
        sign_up = 'SIGN_UP'
        sotto_subscribe = 'SOTTO_SUBSCRIBE'
        subscribe = 'SUBSCRIBE'
        update_app = 'UPDATE_APP'
        use_app = 'USE_APP'
        use_mobile_app = 'USE_MOBILE_APP'
        video_annotation = 'VIDEO_ANNOTATION'
        visit_pages_feed = 'VISIT_PAGES_FEED'
        watch_more = 'WATCH_MORE'
        watch_video = 'WATCH_VIDEO'
        whatsapp_message = 'WHATSAPP_MESSAGE'
        woodhenge_support = 'WOODHENGE_SUPPORT'

    _field_types = {
        'ad_formats': 'list<string>',
        'additional_data': 'Object',
        'asset_customization_rules': 'list<Object>',
        'autotranslate': 'list<string>',
        'bodies': 'list<AdAssetFeedSpecBody>',
        'call_to_action_types': 'list<CallToActionTypes>',
        'call_to_actions': 'list<Object>',
        'captions': 'list<AdAssetFeedSpecCaption>',
        'carousels': 'list<Object>',
        'descriptions': 'list<AdAssetFeedSpecDescription>',
        'groups': 'list<AdAssetFeedSpecGroupRule>',
        'images': 'list<AdAssetFeedSpecImage>',
        'link_urls': 'list<AdAssetFeedSpecLinkURL>',
        'optimization_type': 'string',
        'titles': 'list<AdAssetFeedSpecTitle>',
        'videos': 'list<AdAssetFeedSpecVideo>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CallToActionTypes'] = AdAssetFeedSpec.CallToActionTypes.__dict__.values()
        return field_enum_info


