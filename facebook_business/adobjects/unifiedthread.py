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

class UnifiedThread(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isUnifiedThread = True
        super(UnifiedThread, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        can_reply = 'can_reply'
        former_participants = 'former_participants'
        id = 'id'
        is_subscribed = 'is_subscribed'
        link = 'link'
        message_count = 'message_count'
        name = 'name'
        participants = 'participants'
        scoped_thread_key = 'scoped_thread_key'
        senders = 'senders'
        snippet = 'snippet'
        subject = 'subject'
        tags = 'tags'
        thread_key = 'thread_key'
        unread_count = 'unread_count'
        updated_time = 'updated_time'
        wallpaper = 'wallpaper'

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
            target_class=UnifiedThread,
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

    def get_messages(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/messages',
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

    def create_message(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'aloha_action': 'string',
            'android_key_hash': 'string',
            'applied_art_data': 'Object',
            'associated_object_id': 'Object',
            'attribution_app_id': 'string',
            'attribution_app_metadata': 'string',
            'audio_duration': 'int',
            'audio_type': 'audio_type_enum',
            'body': 'string',
            'broadcast_recipients': 'map',
            'client_tags': 'map',
            'coordinates': 'Object',
            'copy_attachment': 'string',
            'copy_message': 'string',
            'customizations': 'map',
            'entry_point': 'string',
            'external_attachment_url': 'string',
            'image_type': 'image_type_enum',
            'ios_bundle_id': 'string',
            'is_broadcast': 'bool',
            'is_montage': 'bool',
            'is_voicemail': 'bool',
            'lightweight_action_attachment': 'Object',
            'link': 'string',
            'live_location_attachment': 'Object',
            'location_attachment': 'Object',
            'log_info': 'Object',
            'mark_read_watermark_timestamp': 'int',
            'media': 'list<string>',
            'message_source_data': 'Object',
            'montage_frame_style': 'montage_frame_style_enum',
            'montage_business_platform_data': 'map',
            'montage_overlays': 'list<map>',
            'montage_supported_features': 'list<montage_supported_features_enum>',
            'montage_mentions': 'map',
            'montage_reply_data': 'Object',
            'object_attachment': 'string',
            'offline_threading_id': 'string',
            'platform_xmd': 'string',
            'prng': 'Object',
            'proxied_app_id': 'string',
            'recipients': 'Object',
            'replace_message_id': 'string',
            'replied_to_message_id': 'string',
            'selected_cta_token': 'string',
            'shareable_attachment': 'Object',
            'shown_cta_tokens': 'list<string>',
            'skip_android_hash_check': 'bool',
            'story_id': 'Object',
            'tags': 'list<string>',
            'tid': 'string',
            'tracking': 'string',
            'ttl': 'unsigned int',
            'use_existing_group': 'bool',
            'video_thumbnail': 'file',
            'video_type': 'video_type_enum',
            'message_attempt_id': 'string',
            'is_admin_model_v2_enabled': 'bool',
        }
        enums = {
            'audio_type_enum': [
                'FILE_ATTACHMENT',
                'VOICE_MESSAGE',
                'VOICE_MESSAGE_WITH_TRANSCRIPT',
            ],
            'image_type_enum': [
                'FILE_ATTACHMENT',
                'MESSENGER_CAM',
                'TRANSPARENT',
            ],
            'montage_frame_style_enum': [
                'no_border',
            ],
            'montage_supported_features_enum': [
                'LIGHTWEIGHT_REPLY',
                'SHOW_STORY_IN_MESSENGER_THREAD',
            ],
            'video_type_enum': [
                'FILE_ATTACHMENT',
                'RECORDED_VIDEO',
                'SPEAKING_STICKER',
                'RECORDED_STICKER',
                'VIDEO_MAIL',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/messages',
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
        'can_reply': 'bool',
        'former_participants': 'Object',
        'id': 'string',
        'is_subscribed': 'bool',
        'link': 'string',
        'message_count': 'int',
        'name': 'string',
        'participants': 'Object',
        'scoped_thread_key': 'string',
        'senders': 'Object',
        'snippet': 'string',
        'subject': 'string',
        'tags': 'Object',
        'thread_key': 'string',
        'unread_count': 'int',
        'updated_time': 'datetime',
        'wallpaper': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


