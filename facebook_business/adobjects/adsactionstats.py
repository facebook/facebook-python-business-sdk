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

class AdsActionStats(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsActionStats = True
        super(AdsActionStats, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        field_1d_click = '1d_click'
        field_1d_view = '1d_view'
        field_28d_click = '28d_click'
        field_28d_view = '28d_view'
        field_7d_click = '7d_click'
        field_7d_view = '7d_view'
        action_canvas_component_id = 'action_canvas_component_id'
        action_canvas_component_name = 'action_canvas_component_name'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_event_channel = 'action_event_channel'
        action_link_click_destination = 'action_link_click_destination'
        action_location_code = 'action_location_code'
        action_reaction = 'action_reaction'
        action_target_id = 'action_target_id'
        action_type = 'action_type'
        action_video_asset_id = 'action_video_asset_id'
        action_video_sound = 'action_video_sound'
        action_video_type = 'action_video_type'
        inline = 'inline'
        value = 'value'
        id = 'id'

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
            target_class=AdsActionStats,
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
        '1d_click': 'string',
        '1d_view': 'string',
        '28d_click': 'string',
        '28d_view': 'string',
        '7d_click': 'string',
        '7d_view': 'string',
        'action_canvas_component_id': 'string',
        'action_canvas_component_name': 'string',
        'action_carousel_card_id': 'string',
        'action_carousel_card_name': 'string',
        'action_destination': 'string',
        'action_device': 'string',
        'action_event_channel': 'string',
        'action_link_click_destination': 'string',
        'action_location_code': 'string',
        'action_reaction': 'string',
        'action_target_id': 'string',
        'action_type': 'string',
        'action_video_asset_id': 'string',
        'action_video_sound': 'string',
        'action_video_type': 'string',
        'inline': 'string',
        'value': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


