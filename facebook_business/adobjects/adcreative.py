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
from facebook_business.mixins import HasAdLabels

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCreative(
    AbstractCrudObject,
    HasAdLabels,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCreative = True
        super(AdCreative, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        actor_id = 'actor_id'
        adlabels = 'adlabels'
        applink_treatment = 'applink_treatment'
        asset_feed_id = 'asset_feed_id'
        asset_feed_spec = 'asset_feed_spec'
        authorization_category = 'authorization_category'
        auto_update = 'auto_update'
        body = 'body'
        branded_content_sponsor_page_id = 'branded_content_sponsor_page_id'
        bundle_folder_id = 'bundle_folder_id'
        call_to_action_type = 'call_to_action_type'
        categorization_criteria = 'categorization_criteria'
        category_media_source = 'category_media_source'
        destination_set_id = 'destination_set_id'
        dynamic_ad_voice = 'dynamic_ad_voice'
        effective_authorization_category = 'effective_authorization_category'
        effective_instagram_story_id = 'effective_instagram_story_id'
        effective_object_story_id = 'effective_object_story_id'
        enable_direct_install = 'enable_direct_install'
        enable_launch_instant_app = 'enable_launch_instant_app'
        id = 'id'
        image_crops = 'image_crops'
        image_hash = 'image_hash'
        image_url = 'image_url'
        instagram_actor_id = 'instagram_actor_id'
        instagram_permalink_url = 'instagram_permalink_url'
        instagram_story_id = 'instagram_story_id'
        link_deep_link_url = 'link_deep_link_url'
        link_og_id = 'link_og_id'
        link_url = 'link_url'
        messenger_sponsored_message = 'messenger_sponsored_message'
        name = 'name'
        object_id = 'object_id'
        object_store_url = 'object_store_url'
        object_story_id = 'object_story_id'
        object_story_spec = 'object_story_spec'
        object_type = 'object_type'
        object_url = 'object_url'
        place_page_set_id = 'place_page_set_id'
        platform_customizations = 'platform_customizations'
        playable_asset_id = 'playable_asset_id'
        product_set_id = 'product_set_id'
        recommender_settings = 'recommender_settings'
        status = 'status'
        template_url = 'template_url'
        template_url_spec = 'template_url_spec'
        thumbnail_url = 'thumbnail_url'
        title = 'title'
        url_tags = 'url_tags'
        use_page_actor_override = 'use_page_actor_override'
        video_id = 'video_id'
        is_dco_internal = 'is_dco_internal'
        call_to_action = 'call_to_action'
        image_file = 'image_file'
        mockup_id = 'mockup_id'
        page_id = 'page_id'

    class ApplinkTreatment:
        deeplink_with_web_fallback = 'deeplink_with_web_fallback'
        deeplink_with_appstore_fallback = 'deeplink_with_appstore_fallback'
        web_only = 'web_only'

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

    class ObjectType:
        application = 'APPLICATION'
        domain = 'DOMAIN'
        event = 'EVENT'
        offer = 'OFFER'
        page = 'PAGE'
        photo = 'PHOTO'
        share = 'SHARE'
        status = 'STATUS'
        store_item = 'STORE_ITEM'
        video = 'VIDEO'
        invalid = 'INVALID'

    class Status:
        active = 'ACTIVE'
        deleted = 'DELETED'

    class AuthorizationCategory:
        none = 'NONE'
        political = 'POLITICAL'

    class CategorizationCriteria:
        brand = 'brand'
        category = 'category'
        product_type = 'product_type'

    class CategoryMediaSource:
        category = 'CATEGORY'
        mixed = 'MIXED'
        products_collage = 'PRODUCTS_COLLAGE'
        products_slideshow = 'PRODUCTS_SLIDESHOW'

    class DynamicAdVoice:
        dynamic = 'DYNAMIC'
        story_owner = 'STORY_OWNER'

    class Operator:
        all = 'ALL'
        any = 'ANY'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adcreatives'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_creative(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'name': 'string',
            'adlabels': 'list<Object>',
            'status': 'status_enum',
        }
        enums = {
            'status_enum': AdCreative.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
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

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'thumbnail_height': 'unsigned int',
            'thumbnail_width': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'account_id': 'string',
            'name': 'string',
            'adlabels': 'list<Object>',
            'status': 'status_enum',
        }
        enums = {
            'status_enum': AdCreative.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
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

    def delete_ad_labels(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adlabels': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adlabels',
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

    def create_ad_label(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adlabels': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdCreative, api=self._api),
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

    def get_previews(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adpreview import AdPreview
        param_types = {
            'ad_format': 'ad_format_enum',
            'dynamic_creative_spec': 'Object',
            'interactive': 'bool',
            'post': 'Object',
            'height': 'unsigned int',
            'width': 'unsigned int',
            'place_page_id': 'int',
            'product_item_ids': 'list<string>',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'locale': 'string',
            'render_type': 'render_type_enum',
        }
        enums = {
            'ad_format_enum': AdPreview.AdFormat.__dict__.values(),
            'render_type_enum': AdPreview.RenderType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/previews',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPreview,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPreview, api=self._api),
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
        'account_id': 'string',
        'actor_id': 'string',
        'adlabels': 'list<AdLabel>',
        'applink_treatment': 'ApplinkTreatment',
        'asset_feed_id': 'string',
        'asset_feed_spec': 'AdAssetFeedSpec',
        'authorization_category': 'string',
        'auto_update': 'bool',
        'body': 'string',
        'branded_content_sponsor_page_id': 'string',
        'bundle_folder_id': 'string',
        'call_to_action_type': 'CallToActionType',
        'categorization_criteria': 'string',
        'category_media_source': 'string',
        'destination_set_id': 'string',
        'dynamic_ad_voice': 'string',
        'effective_authorization_category': 'string',
        'effective_instagram_story_id': 'string',
        'effective_object_story_id': 'string',
        'enable_direct_install': 'bool',
        'enable_launch_instant_app': 'bool',
        'id': 'string',
        'image_crops': 'AdsImageCrops',
        'image_hash': 'string',
        'image_url': 'string',
        'instagram_actor_id': 'string',
        'instagram_permalink_url': 'string',
        'instagram_story_id': 'string',
        'link_deep_link_url': 'string',
        'link_og_id': 'string',
        'link_url': 'string',
        'messenger_sponsored_message': 'string',
        'name': 'string',
        'object_id': 'string',
        'object_store_url': 'string',
        'object_story_id': 'string',
        'object_story_spec': 'AdCreativeObjectStorySpec',
        'object_type': 'ObjectType',
        'object_url': 'string',
        'place_page_set_id': 'string',
        'platform_customizations': 'AdCreativePlatformCustomization',
        'playable_asset_id': 'string',
        'product_set_id': 'string',
        'recommender_settings': 'AdCreativeRecommenderSettings',
        'status': 'Status',
        'template_url': 'string',
        'template_url_spec': 'AdCreativeTemplateURLSpec',
        'thumbnail_url': 'string',
        'title': 'string',
        'url_tags': 'string',
        'use_page_actor_override': 'bool',
        'video_id': 'string',
        'is_dco_internal': 'bool',
        'call_to_action': 'Object',
        'image_file': 'string',
        'mockup_id': 'string',
        'page_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ApplinkTreatment'] = AdCreative.ApplinkTreatment.__dict__.values()
        field_enum_info['CallToActionType'] = AdCreative.CallToActionType.__dict__.values()
        field_enum_info['ObjectType'] = AdCreative.ObjectType.__dict__.values()
        field_enum_info['Status'] = AdCreative.Status.__dict__.values()
        field_enum_info['AuthorizationCategory'] = AdCreative.AuthorizationCategory.__dict__.values()
        field_enum_info['CategorizationCriteria'] = AdCreative.CategorizationCriteria.__dict__.values()
        field_enum_info['CategoryMediaSource'] = AdCreative.CategoryMediaSource.__dict__.values()
        field_enum_info['DynamicAdVoice'] = AdCreative.DynamicAdVoice.__dict__.values()
        field_enum_info['Operator'] = AdCreative.Operator.__dict__.values()
        return field_enum_info


def _setitem_trigger(self, key, value):
    if key == 'id':
        self._data['creative_id'] = self['id']
