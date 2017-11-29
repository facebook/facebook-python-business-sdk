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

class AdAssetFeedSpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdAssetFeedSpec, self).__init__()
        self._isAdAssetFeedSpec = True
        self._api = api

    class Field(AbstractObject.Field):
        ad_formats = 'ad_formats'
        bodies = 'bodies'
        call_to_action_types = 'call_to_action_types'
        captions = 'captions'
        descriptions = 'descriptions'
        groups = 'groups'
        images = 'images'
        link_urls = 'link_urls'
        optimization_type = 'optimization_type'
        target_rules = 'target_rules'
        titles = 'titles'
        videos = 'videos'

    class CallToActionTypes:
        open_link = 'OPEN_LINK'
        like_page = 'LIKE_PAGE'
        shop_now = 'SHOP_NOW'
        play_game = 'PLAY_GAME'
        install_app = 'INSTALL_APP'
        use_app = 'USE_APP'
        install_mobile_app = 'INSTALL_MOBILE_APP'
        use_mobile_app = 'USE_MOBILE_APP'
        book_travel = 'BOOK_TRAVEL'
        listen_music = 'LISTEN_MUSIC'
        learn_more = 'LEARN_MORE'
        sign_up = 'SIGN_UP'
        download = 'DOWNLOAD'
        watch_more = 'WATCH_MORE'
        no_button = 'NO_BUTTON'
        call_now = 'CALL_NOW'
        apply_now = 'APPLY_NOW'
        buy_now = 'BUY_NOW'
        get_offer = 'GET_OFFER'
        get_offer_view = 'GET_OFFER_VIEW'
        get_directions = 'GET_DIRECTIONS'
        message_page = 'MESSAGE_PAGE'
        message_user = 'MESSAGE_USER'
        subscribe = 'SUBSCRIBE'
        sell_now = 'SELL_NOW'
        donate_now = 'DONATE_NOW'
        get_quote = 'GET_QUOTE'
        contact_us = 'CONTACT_US'
        start_order = 'START_ORDER'
        record_now = 'RECORD_NOW'
        vote_now = 'VOTE_NOW'
        register_now = 'REGISTER_NOW'
        request_time = 'REQUEST_TIME'
        see_menu = 'SEE_MENU'
        email_now = 'EMAIL_NOW'
        get_showtimes = 'GET_SHOWTIMES'
        try_it = 'TRY_IT'
        listen_now = 'LISTEN_NOW'
        open_movies = 'OPEN_MOVIES'

    _field_types = {
        'ad_formats': 'list<string>',
        'bodies': 'list<AdAssetFeedSpecBody>',
        'call_to_action_types': 'list<CallToActionTypes>',
        'captions': 'list<AdAssetFeedSpecCaption>',
        'descriptions': 'list<AdAssetFeedSpecDescription>',
        'groups': 'list<AdAssetFeedSpecGroupRule>',
        'images': 'list<AdAssetFeedSpecImage>',
        'link_urls': 'list<AdAssetFeedSpecLinkURL>',
        'optimization_type': 'string',
        'target_rules': 'list<AdAssetFeedSpecTargetRule>',
        'titles': 'list<AdAssetFeedSpecTitle>',
        'videos': 'list<AdAssetFeedSpecVideo>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CallToActionTypes'] = AdAssetFeedSpec.CallToActionTypes.__dict__.values()
        return field_enum_info
