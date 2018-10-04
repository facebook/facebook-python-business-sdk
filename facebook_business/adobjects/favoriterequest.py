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

class FavoriteRequest(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isFavoriteRequest = True
        super(FavoriteRequest, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        api_version = 'api_version'
        description = 'description'
        graph_path = 'graph_path'
        hash = 'hash'
        http_method = 'http_method'
        id = 'id'
        post_params = 'post_params'
        query_params = 'query_params'

    class HttpMethod:
        get = 'GET'
        post = 'POST'
        delete = 'DELETE'

    class ApiVersion:
        unversioned = 'unversioned'
        v1_0 = 'v1.0'
        v2_0 = 'v2.0'
        v2_1 = 'v2.1'
        v2_2 = 'v2.2'
        v2_3 = 'v2.3'
        v2_4 = 'v2.4'
        v2_5 = 'v2.5'
        v2_6 = 'v2.6'
        v2_7 = 'v2.7'
        v2_8 = 'v2.8'
        v2_9 = 'v2.9'
        v2_10 = 'v2.10'
        v2_11 = 'v2.11'
        v2_12 = 'v2.12'
        v3_0 = 'v3.0'
        v3_1 = 'v3.1'
        v3_2 = 'v3.2'
        v4_0 = 'v4.0'

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
            target_class=FavoriteRequest,
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

    _field_types = {
        'api_version': 'string',
        'description': 'string',
        'graph_path': 'string',
        'hash': 'string',
        'http_method': 'HttpMethod',
        'id': 'string',
        'post_params': 'list<Object>',
        'query_params': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['HttpMethod'] = FavoriteRequest.HttpMethod.__dict__.values()
        field_enum_info['ApiVersion'] = FavoriteRequest.ApiVersion.__dict__.values()
        return field_enum_info


