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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdsActionStats(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdsActionStats, self).__init__()
        self._isAdsActionStats = True
        self._api = api

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
        action_converted_product_id = 'action_converted_product_id'
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
        dda = 'dda'
        inline = 'inline'
        interactive_component_sticker_id = 'interactive_component_sticker_id'
        interactive_component_sticker_response = 'interactive_component_sticker_response'
        value = 'value'

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
        'action_converted_product_id': 'string',
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
        'dda': 'string',
        'inline': 'string',
        'interactive_component_sticker_id': 'string',
        'interactive_component_sticker_response': 'string',
        'value': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


