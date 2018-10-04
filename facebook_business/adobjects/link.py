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

class Link(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isLink = True
        super(Link, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        caption = 'caption'
        created_time = 'created_time'
        description = 'description'
        field_from = 'from'
        icon = 'icon'
        id = 'id'
        link = 'link'
        message = 'message'
        multi_share_optimized = 'multi_share_optimized'
        name = 'name'
        picture = 'picture'
        privacy = 'privacy'
        via = 'via'

    class UnpublishedContentType:
        scheduled = 'SCHEDULED'
        draft = 'DRAFT'
        ads_post = 'ADS_POST'
        inline_created = 'INLINE_CREATED'
        published = 'PUBLISHED'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
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
            target_class=Link,
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

    def get_comments(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.comment import Comment
        param_types = {
            'filter': 'filter_enum',
            'order': 'order_enum',
            'live_filter': 'live_filter_enum',
            'since': 'datetime',
        }
        enums = {
            'filter_enum': Comment.Filter.__dict__.values(),
            'order_enum': Comment.Order.__dict__.values(),
            'live_filter_enum': Comment.LiveFilter.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
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

    def create_comment(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.comment import Comment
        param_types = {
            'object_id': 'string',
            'parent_comment_id': 'Object',
            'nectar_module': 'string',
            'attachment_id': 'string',
            'attachment_url': 'string',
            'attachment_share_url': 'string',
            'feedback_source': 'string',
            'facepile_mentioned_ids': 'list<string>',
            'is_offline': 'bool',
            'comment_privacy_value': 'comment_privacy_value_enum',
            'message': 'string',
            'text': 'string',
            'tracking': 'string',
        }
        enums = {
            'comment_privacy_value_enum': Comment.CommentPrivacyValue.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
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

    def get_leads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.lead import Lead
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Lead,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Lead, api=self._api),
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
            'tracking': 'string',
            'nectar_module': 'string',
            'notify': 'bool',
            'feedback_source': 'string',
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

    def get_likes(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profile import Profile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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
            'tracking': 'string',
            'nectar_module': 'string',
            'notify': 'bool',
            'feedback_source': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Link,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Link, api=self._api),
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

    def get_reactions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.profile import Profile
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': Profile.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reactions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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

    def get_share_d_posts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.post import Post
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sharedposts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Post,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Post, api=self._api),
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
        'caption': 'string',
        'created_time': 'datetime',
        'description': 'string',
        'from': 'Object',
        'icon': 'string',
        'id': 'string',
        'link': 'string',
        'message': 'string',
        'multi_share_optimized': 'bool',
        'name': 'string',
        'picture': 'string',
        'privacy': 'Privacy',
        'via': 'Object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['UnpublishedContentType'] = Link.UnpublishedContentType.__dict__.values()
        return field_enum_info


