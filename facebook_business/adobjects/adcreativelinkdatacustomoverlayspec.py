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

class AdCreativeLinkDataCustomOverlaySpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeLinkDataCustomOverlaySpec, self).__init__()
        self._isAdCreativeLinkDataCustomOverlaySpec = True
        self._api = api

    class Field(AbstractObject.Field):
        background_color = 'background_color'
        float_with_margin = 'float_with_margin'
        font = 'font'
        option = 'option'
        position = 'position'
        render_with_icon = 'render_with_icon'
        template = 'template'
        text_color = 'text_color'

    class BackgroundColor:
        background_ffffff = 'background_ffffff'
        background_e50900 = 'background_e50900'
        background_f78400 = 'background_f78400'
        background_00af4c = 'background_00af4c'
        background_0090ff = 'background_0090ff'
        background_755dde = 'background_755dde'
        background_f23474 = 'background_f23474'
        background_595959 = 'background_595959'
        background_000000 = 'background_000000'

    class Font:
        droid_serif_regular = 'droid_serif_regular'
        lato_regular = 'lato_regular'
        nunito_sans_bold = 'nunito_sans_bold'
        open_sans_bold = 'open_sans_bold'
        pt_serif_bold = 'pt_serif_bold'
        roboto_medium = 'roboto_medium'
        roboto_condensed_regular = 'roboto_condensed_regular'
        noto_sans_regular = 'noto_sans_regular'

    class Option:
        bank_transfer = 'bank_transfer'
        boleto = 'boleto'
        discount_with_boleto = 'discount_with_boleto'
        cash_on_delivery = 'cash_on_delivery'
        home_delivery = 'home_delivery'
        free_shipping = 'free_shipping'
        inventory = 'inventory'

    class Position:
        top_left = 'top_left'
        top_right = 'top_right'
        bottom_left = 'bottom_left'
        bottom_right = 'bottom_right'

    class Template:
        pill_with_text = 'pill_with_text'

    class TextColor:
        text_ffffff = 'text_ffffff'
        text_c91b00 = 'text_c91b00'
        text_f78400 = 'text_f78400'
        text_009c2a = 'text_009c2a'
        text_007ad0 = 'text_007ad0'
        text_755dde = 'text_755dde'
        text_f23474 = 'text_f23474'
        text_646464 = 'text_646464'
        text_000000 = 'text_000000'

    _field_types = {
        'background_color': 'BackgroundColor',
        'float_with_margin': 'bool',
        'font': 'Font',
        'option': 'Option',
        'position': 'Position',
        'render_with_icon': 'bool',
        'template': 'Template',
        'text_color': 'TextColor',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BackgroundColor'] = AdCreativeLinkDataCustomOverlaySpec.BackgroundColor.__dict__.values()
        field_enum_info['Font'] = AdCreativeLinkDataCustomOverlaySpec.Font.__dict__.values()
        field_enum_info['Option'] = AdCreativeLinkDataCustomOverlaySpec.Option.__dict__.values()
        field_enum_info['Position'] = AdCreativeLinkDataCustomOverlaySpec.Position.__dict__.values()
        field_enum_info['Template'] = AdCreativeLinkDataCustomOverlaySpec.Template.__dict__.values()
        field_enum_info['TextColor'] = AdCreativeLinkDataCustomOverlaySpec.TextColor.__dict__.values()
        return field_enum_info
