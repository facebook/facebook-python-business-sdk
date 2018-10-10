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
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAssetFeed(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAssetFeed = True
        super(AdAssetFeed, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account = 'account'
        ad_formats = 'ad_formats'
        additional_data = 'additional_data'
        autotranslate = 'autotranslate'
        id = 'id'
        optimization_type = 'optimization_type'
        images = 'images'
        videos = 'videos'
        bodies = 'bodies'
        call_to_action_types = 'call_to_action_types'
        descriptions = 'descriptions'
        link_urls = 'link_urls'
        titles = 'titles'
        captions = 'captions'
        groups = 'groups'
        target_rules = 'target_rules'
        asset_customization_rules = 'asset_customization_rules'
        call_to_actions = 'call_to_actions'
        image = 'image'
        video = 'video'
        call_to_action_type = 'call_to_action_type'
        default_language = 'default_language'

    class AdFormats:
        automatic_format = 'AUTOMATIC_FORMAT'
        carousel_image = 'CAROUSEL_IMAGE'
        carousel_video = 'CAROUSEL_VIDEO'
        single_image = 'SINGLE_IMAGE'
        single_video = 'SINGLE_VIDEO'

    class CallToActionTypes:
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
        woodhenge_support = 'WOODHENGE_SUPPORT'
        event_rsvp = 'EVENT_RSVP'
        whatsapp_message = 'WHATSAPP_MESSAGE'
        follow_news_storyline = 'FOLLOW_NEWS_STORYLINE'

    class OptimizationType:
        regular = 'REGULAR'
        language = 'LANGUAGE'
        placement = 'PLACEMENT'
        video_bandwidth = 'VIDEO_BANDWIDTH'
        brand = 'BRAND'
        asset_customization = 'ASSET_CUSTOMIZATION'
        dco_parity = 'DCO_PARITY'
        preview_dynamic_rendering = 'PREVIEW_DYNAMIC_RENDERING'

    class CallToActionType:
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
        woodhenge_support = 'WOODHENGE_SUPPORT'
        event_rsvp = 'EVENT_RSVP'
        whatsapp_message = 'WHATSAPP_MESSAGE'
        follow_news_storyline = 'FOLLOW_NEWS_STORYLINE'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adasset_feeds'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_asset_feed(fields, params, batch, pending)

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAssetFeed,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_asset_customization_rules(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/asset_customization_rules',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_bodies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/bodies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_call_to_action_types(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/call_to_action_types',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_captions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/captions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_descriptions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/descriptions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_groups(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_images(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/images',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_link_urls(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/link_urls',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_titles(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/titles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_videos(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'account': 'AdAccount',
        'ad_formats': 'list<string>',
        'additional_data': 'Object',
        'autotranslate': 'list<string>',
        'id': 'string',
        'optimization_type': 'string',
        'images': 'list<Object>',
        'videos': 'list<Object>',
        'bodies': 'list<Object>',
        'call_to_action_types': 'list<CallToActionTypes>',
        'descriptions': 'list<Object>',
        'link_urls': 'list<Object>',
        'titles': 'list<Object>',
        'captions': 'list<Object>',
        'groups': 'list<Object>',
        'target_rules': 'list<Object>',
        'asset_customization_rules': 'list<Object>',
        'call_to_actions': 'list<Object>',
        'image': 'Object',
        'video': 'Object',
        'call_to_action_type': 'CallToActionType',
        'default_language': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AdFormats'] = AdAssetFeed.AdFormats.__dict__.values()
        field_enum_info['CallToActionTypes'] = AdAssetFeed.CallToActionTypes.__dict__.values()
        field_enum_info['OptimizationType'] = AdAssetFeed.OptimizationType.__dict__.values()
        field_enum_info['CallToActionType'] = AdAssetFeed.CallToActionType.__dict__.values()
        return field_enum_info


