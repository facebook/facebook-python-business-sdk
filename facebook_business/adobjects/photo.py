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

class Photo(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPhoto = True
        super(Photo, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        album = 'album'
        backdated_time = 'backdated_time'
        backdated_time_granularity = 'backdated_time_granularity'
        can_backdate = 'can_backdate'
        can_delete = 'can_delete'
        can_tag = 'can_tag'
        created_time = 'created_time'
        event = 'event'
        field_from = 'from'
        height = 'height'
        icon = 'icon'
        id = 'id'
        images = 'images'
        link = 'link'
        name = 'name'
        name_tags = 'name_tags'
        page_story_id = 'page_story_id'
        picture = 'picture'
        place = 'place'
        position = 'position'
        source = 'source'
        target = 'target'
        updated_time = 'updated_time'
        webp_images = 'webp_images'
        width = 'width'

    class BackdatedTimeGranularity:
        year = 'year'
        month = 'month'
        day = 'day'
        hour = 'hour'
        min = 'min'
        none = 'none'

    class Type:
        profile = 'profile'
        tagged = 'tagged'
        uploaded = 'uploaded'

    class UnpublishedContentType:
        scheduled = 'SCHEDULED'
        draft = 'DRAFT'
        ads_post = 'ADS_POST'
        inline_created = 'INLINE_CREATED'
        published = 'PUBLISHED'

    class CheckinEntryPoint:
        branding_checkin = 'BRANDING_CHECKIN'
        branding_status = 'BRANDING_STATUS'
        branding_photo = 'BRANDING_PHOTO'
        branding_other = 'BRANDING_OTHER'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'pid': 'string',
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
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

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
            target_class=Photo,
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
            'android_key_hash': 'string',
            'asset3d_id': 'unsigned int',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'checkin_entry_point': 'checkin_entry_point_enum',
            'composer_session_id': 'string',
            'direct_share_status': 'unsigned int',
            'ios_bundle_id': 'string',
            'is_checkin': 'bool',
            'is_cropped': 'bool',
            'is_explicit_location': 'bool',
            'og_action_type_id': 'string',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'place': 'Object',
            'privacy': 'Object',
            'prompt_id': 'string',
            'prompt_tracking_string': 'string',
            'proxied_app_id': 'string',
            'published': 'bool',
            'referenced_sticker_id': 'string',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'tags': 'list<int>',
            'target': 'Object',
            'target_post': 'string',
            'time_since_original_post': 'unsigned int',
        }
        enums = {
            'backdated_time_granularity_enum': Photo.BackdatedTimeGranularity.__dict__.values(),
            'checkin_entry_point_enum': Photo.CheckinEntryPoint.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Photo,
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

    def delete_likes(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/likes',
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

    def create_like(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/likes',
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

    def create_tag(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tag_text': 'string',
            'tag_uid': 'int',
            'tags': 'list<Object>',
            'x': 'float',
            'y': 'float',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/tags',
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
        'album': 'Album',
        'backdated_time': 'datetime',
        'backdated_time_granularity': 'string',
        'can_backdate': 'bool',
        'can_delete': 'bool',
        'can_tag': 'bool',
        'created_time': 'datetime',
        'event': 'Event',
        'from': 'Object',
        'height': 'unsigned int',
        'icon': 'string',
        'id': 'string',
        'images': 'list<Object>',
        'link': 'string',
        'name': 'string',
        'name_tags': 'list<Object>',
        'page_story_id': 'string',
        'picture': 'string',
        'place': 'Object',
        'position': 'unsigned int',
        'source': 'string',
        'target': 'Profile',
        'updated_time': 'datetime',
        'webp_images': 'list<Object>',
        'width': 'unsigned int',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BackdatedTimeGranularity'] = Photo.BackdatedTimeGranularity.__dict__.values()
        field_enum_info['Type'] = Photo.Type.__dict__.values()
        field_enum_info['UnpublishedContentType'] = Photo.UnpublishedContentType.__dict__.values()
        field_enum_info['CheckinEntryPoint'] = Photo.CheckinEntryPoint.__dict__.values()
        return field_enum_info
