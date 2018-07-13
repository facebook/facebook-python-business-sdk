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

class AdCreativeLinkDataImageOverlaySpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeLinkDataImageOverlaySpec, self).__init__()
        self._isAdCreativeLinkDataImageOverlaySpec = True
        self._api = api

    class Field(AbstractObject.Field):
        custom_text_type = 'custom_text_type'
        float_with_margin = 'float_with_margin'
        overlay_template = 'overlay_template'
        position = 'position'
        text_font = 'text_font'
        text_template_tags = 'text_template_tags'
        text_type = 'text_type'
        theme_color = 'theme_color'

    class CustomTextType:
        free_shipping = 'free_shipping'

    class OverlayTemplate:
        pill_with_text = 'pill_with_text'
        circle_with_text = 'circle_with_text'
        triangle_with_text = 'triangle_with_text'

    class Position:
        top_left = 'top_left'
        top_right = 'top_right'
        bottom_left = 'bottom_left'
        bottom_right = 'bottom_right'

    class TextFont:
        droid_serif_regular = 'droid_serif_regular'
        lato_regular = 'lato_regular'
        nunito_sans_bold = 'nunito_sans_bold'
        open_sans_bold = 'open_sans_bold'
        open_sans_condensed_bold = 'open_sans_condensed_bold'
        pt_serif_bold = 'pt_serif_bold'
        roboto_medium = 'roboto_medium'
        roboto_condensed_regular = 'roboto_condensed_regular'
        noto_sans_regular = 'noto_sans_regular'
        dynads_hybrid_bold = 'dynads_hybrid_bold'

    class TextType:
        price = 'price'
        strikethrough_price = 'strikethrough_price'
        percentage_off = 'percentage_off'
        custom = 'custom'
        from_price = 'from_price'

    class ThemeColor:
        background_e50900_text_ffffff = 'background_e50900_text_ffffff'
        background_f78400_text_ffffff = 'background_f78400_text_ffffff'
        background_00af4c_text_ffffff = 'background_00af4c_text_ffffff'
        background_0090ff_text_ffffff = 'background_0090ff_text_ffffff'
        background_755dde_text_ffffff = 'background_755dde_text_ffffff'
        background_f23474_text_ffffff = 'background_f23474_text_ffffff'
        background_595959_text_ffffff = 'background_595959_text_ffffff'
        background_000000_text_ffffff = 'background_000000_text_ffffff'
        background_ffffff_text_c91b00 = 'background_ffffff_text_c91b00'
        background_ffffff_text_f78400 = 'background_ffffff_text_f78400'
        background_ffffff_text_009c2a = 'background_ffffff_text_009c2a'
        background_ffffff_text_007ad0 = 'background_ffffff_text_007ad0'
        background_ffffff_text_755dde = 'background_ffffff_text_755dde'
        background_ffffff_text_f23474 = 'background_ffffff_text_f23474'
        background_ffffff_text_646464 = 'background_ffffff_text_646464'
        background_ffffff_text_000000 = 'background_ffffff_text_000000'

    _field_types = {
        'custom_text_type': 'CustomTextType',
        'float_with_margin': 'bool',
        'overlay_template': 'OverlayTemplate',
        'position': 'Position',
        'text_font': 'TextFont',
        'text_template_tags': 'list<string>',
        'text_type': 'TextType',
        'theme_color': 'ThemeColor',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CustomTextType'] = AdCreativeLinkDataImageOverlaySpec.CustomTextType.__dict__.values()
        field_enum_info['OverlayTemplate'] = AdCreativeLinkDataImageOverlaySpec.OverlayTemplate.__dict__.values()
        field_enum_info['Position'] = AdCreativeLinkDataImageOverlaySpec.Position.__dict__.values()
        field_enum_info['TextFont'] = AdCreativeLinkDataImageOverlaySpec.TextFont.__dict__.values()
        field_enum_info['TextType'] = AdCreativeLinkDataImageOverlaySpec.TextType.__dict__.values()
        field_enum_info['ThemeColor'] = AdCreativeLinkDataImageOverlaySpec.ThemeColor.__dict__.values()
        return field_enum_info
