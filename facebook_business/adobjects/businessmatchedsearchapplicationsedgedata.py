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

class BusinessMatchedSearchApplicationsEdgeData(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusinessMatchedSearchApplicationsEdgeData = True
        super(BusinessMatchedSearchApplicationsEdgeData, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        app_id = 'app_id'
        icon_url = 'icon_url'
        name = 'name'
        search_source_store = 'search_source_store'
        store = 'store'
        unique_id = 'unique_id'
        url = 'url'
        id = 'id'

    class AppStore:
        amazon_app_store = 'AMAZON_APP_STORE'
        google_play = 'GOOGLE_PLAY'
        itunes = 'ITUNES'
        itunes_ipad = 'ITUNES_IPAD'
        fb_canvas = 'FB_CANVAS'
        fb_gameroom = 'FB_GAMEROOM'
        windows_store = 'WINDOWS_STORE'
        fb_android_store = 'FB_ANDROID_STORE'
        windows_10_store = 'WINDOWS_10_STORE'
        roku_store = 'ROKU_STORE'
        instant_game = 'INSTANT_GAME'
        does_not_exist = 'DOES_NOT_EXIST'

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
            target_class=BusinessMatchedSearchApplicationsEdgeData,
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
        'app_id': 'string',
        'icon_url': 'string',
        'name': 'string',
        'search_source_store': 'string',
        'store': 'string',
        'unique_id': 'string',
        'url': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AppStore'] = BusinessMatchedSearchApplicationsEdgeData.AppStore.__dict__.values()
        return field_enum_info


