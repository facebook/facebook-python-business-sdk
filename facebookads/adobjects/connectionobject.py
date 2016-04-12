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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ConnectionObject(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isConnectionObject = True
        super(ConnectionObject, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        app_installs_tracked = 'app_installs_tracked'
        checkin_capable = 'checkin_capable'
        cpa_access = 'cpa_access'
        event_is_viewer_admin = 'event_is_viewer_admin'
        event_parent_page_id = 'event_parent_page_id'
        event_parent_page_name = 'event_parent_page_name'
        event_start_timestamp = 'event_start_timestamp'
        icon_url = 'icon_url'
        id = 'id'
        is_game = 'is_game'
        logo_url = 'logo_url'
        name = 'name'
        name_with_location_descriptor = 'name_with_location_descriptor'
        native_app_store_ids = 'native_app_store_ids'
        native_app_targeting_ids = 'native_app_targeting_ids'
        object_store_urls = 'object_store_urls'
        og_actions = 'og_actions'
        og_namespace = 'og_namespace'
        og_objects = 'og_objects'
        picture = 'picture'
        supported_platforms = 'supported_platforms'
        tabs = 'tabs'
        type = 'type'
        url = 'url'
        website = 'website'

    @classmethod
    def get_endpoint(cls):
        return 'connectionobjects'

    _field_types = {
        'app_installs_tracked': 'bool',
        'checkin_capable': 'bool',
        'cpa_access': 'map<string, bool>',
        'event_is_viewer_admin': 'bool',
        'event_parent_page_id': 'string',
        'event_parent_page_name': 'string',
        'event_start_timestamp': 'unsigned int',
        'icon_url': 'string',
        'id': 'string',
        'is_game': 'bool',
        'logo_url': 'string',
        'name': 'string',
        'name_with_location_descriptor': 'string',
        'native_app_store_ids': 'map',
        'native_app_targeting_ids': 'map',
        'object_store_urls': 'map',
        'og_actions': 'list<ConnectionObjectOpenGraphAction>',
        'og_namespace': 'string',
        'og_objects': 'list<ConnectionObjectOpenGraphObject>',
        'picture': 'string',
        'supported_platforms': 'list<unsigned int>',
        'tabs': 'map',
        'type': 'unsigned int',
        'url': 'string',
        'website': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
