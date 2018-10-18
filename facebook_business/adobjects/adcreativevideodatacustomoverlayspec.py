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

class AdCreativeVideoDataCustomOverlaySpec(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCreativeVideoDataCustomOverlaySpec = True
        super(AdCreativeVideoDataCustomOverlaySpec, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        background_color = 'background_color'
        background_opacity = 'background_opacity'
        duration = 'duration'
        float_with_margin = 'float_with_margin'
        full_width = 'full_width'
        option = 'option'
        position = 'position'
        start = 'start'
        template = 'template'
        text_color = 'text_color'
        id = 'id'

    class BackgroundOpacity:
        solid = 'solid'
        half = 'half'

    class Option:
        bank_transfer = 'bank_transfer'
        boleto = 'boleto'
        discount_with_boleto = 'discount_with_boleto'
        cash_on_delivery = 'cash_on_delivery'
        home_delivery = 'home_delivery'
        free_shipping = 'free_shipping'
        inventory = 'inventory'
        pay_on_arrival = 'pay_on_arrival'
        pay_at_hotel = 'pay_at_hotel'
        fast_delivery = 'fast_delivery'

    class Position:
        top_left = 'top_left'
        top_center = 'top_center'
        top_right = 'top_right'
        middle_left = 'middle_left'
        middle_center = 'middle_center'
        middle_right = 'middle_right'

    class Template:
        rectangle_with_text = 'rectangle_with_text'

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
            target_class=AdCreativeVideoDataCustomOverlaySpec,
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
        'background_color': 'string',
        'background_opacity': 'BackgroundOpacity',
        'duration': 'int',
        'float_with_margin': 'bool',
        'full_width': 'bool',
        'option': 'Option',
        'position': 'Position',
        'start': 'int',
        'template': 'Template',
        'text_color': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BackgroundOpacity'] = AdCreativeVideoDataCustomOverlaySpec.BackgroundOpacity.__dict__.values()
        field_enum_info['Option'] = AdCreativeVideoDataCustomOverlaySpec.Option.__dict__.values()
        field_enum_info['Position'] = AdCreativeVideoDataCustomOverlaySpec.Position.__dict__.values()
        field_enum_info['Template'] = AdCreativeVideoDataCustomOverlaySpec.Template.__dict__.values()
        return field_enum_info


