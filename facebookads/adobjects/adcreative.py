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
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker
from facebookads.mixins import HasAdLabels

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
        actor_id = 'actor_id'
        actor_image_hash = 'actor_image_hash'
        actor_image_url = 'actor_image_url'
        actor_name = 'actor_name'
        adlabels = 'adlabels'
        applink_treatment = 'applink_treatment'
        body = 'body'
        call_to_action_type = 'call_to_action_type'
        id = 'id'
        image_crops = 'image_crops'
        image_hash = 'image_hash'
        image_url = 'image_url'
        instagram_actor_id = 'instagram_actor_id'
        instagram_permalink_url = 'instagram_permalink_url'
        instagram_story_id = 'instagram_story_id'
        link_og_id = 'link_og_id'
        link_url = 'link_url'
        name = 'name'
        object_id = 'object_id'
        object_story_id = 'object_story_id'
        object_story_spec = 'object_story_spec'
        object_type = 'object_type'
        object_url = 'object_url'
        platform_customizations = 'platform_customizations'
        product_set_id = 'product_set_id'
        run_status = 'run_status'
        template_url = 'template_url'
        thumbnail_url = 'thumbnail_url'
        title = 'title'
        url_tags = 'url_tags'
        action_spec = 'action_spec'
        call_to_action = 'call_to_action'
        dynamic_ad_voice = 'dynamic_ad_voice'
        follow_redirect = 'follow_redirect'
        image_file = 'image_file'
        object_instagram_id = 'object_instagram_id'
        place_page_set_id = 'place_page_set_id'
        video_id = 'video_id'

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
        install_mobile_app = 'INSTALL_MOBILE_APP'
        use_mobile_app = 'USE_MOBILE_APP'
        book_travel = 'BOOK_TRAVEL'
        listen_music = 'LISTEN_MUSIC'
        watch_video = 'WATCH_VIDEO'
        learn_more = 'LEARN_MORE'
        sign_up = 'SIGN_UP'
        download = 'DOWNLOAD'
        watch_more = 'WATCH_MORE'
        no_button = 'NO_BUTTON'
        call_now = 'CALL_NOW'
        buy_now = 'BUY_NOW'
        get_offer = 'GET_OFFER'
        get_offer_view = 'GET_OFFER_VIEW'
        get_directions = 'GET_DIRECTIONS'
        message_page = 'MESSAGE_PAGE'
        subscribe = 'SUBSCRIBE'
        sell_now = 'SELL_NOW'
        donate_now = 'DONATE_NOW'
        get_quote = 'GET_QUOTE'
        contact_us = 'CONTACT_US'
        record_now = 'RECORD_NOW'
        vote_now = 'VOTE_NOW'
        open_movies = 'OPEN_MOVIES'

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
        action_spec = 'ACTION_SPEC'
        instagram_media = 'INSTAGRAM_MEDIA'

    class RunStatus:
        active = 'ACTIVE'
        deleted = 'DELETED'

    class DynamicAdVoice:
        dynamic = 'DYNAMIC'
        story_owner = 'STORY_OWNER'

    class Operator:
        all = 'ALL'
        any = 'ANY'

    @classmethod
    def get_endpoint(cls):
        return 'adcreatives'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_creative(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'account_id': 'string',
            'adlabels': 'list<Object>',
            'id': 'string',
            'name': 'string',
            'run_status': 'unsigned int',
        }
        enums = {
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

        return request if pending else request.execute()

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
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
            target_class=AdCreative,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'account_id': 'string',
            'adlabels': 'list<Object>',
            'id': 'string',
            'name': 'string',
            'run_status': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

        return request if pending else request.execute()

    def delete_ad_labels(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'adlabels': 'list<Object>',
            'id': 'string',
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
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_label(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'adlabels': 'list<Object>',
            'id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_previews(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adpreview import AdPreview
        self.assure_call()
        param_types = {
            'ad_format': 'ad_format_enum',
            'height': 'unsigned int',
            'locale': 'string',
            'post': 'Object',
            'product_item_ids': 'list<string>',
            'width': 'unsigned int',
        }
        enums = {
            'ad_format_enum': AdPreview.AdFormat.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/previews',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPreview,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPreview),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    _field_types = {
        'actor_id': 'string',
        'actor_image_hash': 'string',
        'actor_image_url': 'string',
        'actor_name': 'string',
        'adlabels': 'list<AdLabel>',
        'applink_treatment': 'ApplinkTreatment',
        'body': 'string',
        'call_to_action_type': 'CallToActionType',
        'id': 'string',
        'image_crops': 'AdsImageCrops',
        'image_hash': 'string',
        'image_url': 'string',
        'instagram_actor_id': 'string',
        'instagram_permalink_url': 'string',
        'instagram_story_id': 'string',
        'link_og_id': 'string',
        'link_url': 'string',
        'name': 'string',
        'object_id': 'string',
        'object_story_id': 'string',
        'object_story_spec': 'AdCreativeObjectStorySpec',
        'object_type': 'ObjectType',
        'object_url': 'string',
        'platform_customizations': 'Object',
        'product_set_id': 'string',
        'run_status': 'RunStatus',
        'template_url': 'string',
        'thumbnail_url': 'string',
        'title': 'string',
        'url_tags': 'string',
        'action_spec': 'list<unsigned int>',
        'call_to_action': 'Object',
        'dynamic_ad_voice': 'DynamicAdVoice',
        'follow_redirect': 'bool',
        'image_file': 'string',
        'object_instagram_id': 'unsigned int',
        'place_page_set_id': 'string',
        'video_id': 'unsigned int',
    }

    def _setitem_trigger(self, key, value):
        if key == 'id':
            self._data['creative_id'] = self['id']

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ApplinkTreatment'] = AdCreative.ApplinkTreatment.__dict__.values()
        field_enum_info['CallToActionType'] = AdCreative.CallToActionType.__dict__.values()
        field_enum_info['ObjectType'] = AdCreative.ObjectType.__dict__.values()
        field_enum_info['RunStatus'] = AdCreative.RunStatus.__dict__.values()
        field_enum_info['DynamicAdVoice'] = AdCreative.DynamicAdVoice.__dict__.values()
        field_enum_info['Operator'] = AdCreative.Operator.__dict__.values()
        return field_enum_info
