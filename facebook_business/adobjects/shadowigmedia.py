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

class ShadowIGMedia(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isShadowIGMedia = True
        super(ShadowIGMedia, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        caption = 'caption'
        comments_count = 'comments_count'
        id = 'id'
        ig_id = 'ig_id'
        is_comment_enabled = 'is_comment_enabled'
        like_count = 'like_count'
        media_type = 'media_type'
        media_url = 'media_url'
        owner = 'owner'
        permalink = 'permalink'
        shortcode = 'shortcode'
        thumbnail_url = 'thumbnail_url'
        timestamp = 'timestamp'
        username = 'username'

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
            target_class=ShadowIGMedia,
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
            'comment_enabled': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ShadowIGMedia,
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
        from facebook_business.adobjects.shadowigcomment import ShadowIGComment
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ShadowIGComment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ShadowIGComment, api=self._api),
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
        from facebook_business.adobjects.shadowigcomment import ShadowIGComment
        param_types = {
            'message': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ShadowIGComment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ShadowIGComment, api=self._api),
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

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, pending=False):
        from facebook_business.adobjects.instagraminsightsresult import InstagramInsightsResult
        if is_async:
          return self.get_insights_async(fields, params, batch, pending)
        param_types = {
            'metric': 'list<metric_enum>',
            'period': 'list<period_enum>',
        }
        enums = {
            'metric_enum': InstagramInsightsResult.Metric.__dict__.values(),
            'period_enum': InstagramInsightsResult.Period.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InstagramInsightsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InstagramInsightsResult, api=self._api),
            include_summary=False,
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
        'comments_count': 'int',
        'id': 'string',
        'ig_id': 'string',
        'is_comment_enabled': 'bool',
        'like_count': 'int',
        'media_type': 'string',
        'media_url': 'string',
        'owner': 'ShadowIGUser',
        'permalink': 'string',
        'shortcode': 'string',
        'thumbnail_url': 'string',
        'timestamp': 'datetime',
        'username': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
