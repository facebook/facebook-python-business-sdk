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

class AdgroupMetadata(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdgroupMetadata, self).__init__()
        self._isAdgroupMetadata = True
        self._api = api

    class Field(AbstractObject.Field):
        ad_standard_enhancements_edit_source = 'ad_standard_enhancements_edit_source'
        adgroup_creation_source = 'adgroup_creation_source'
        adgroup_edit_source = 'adgroup_edit_source'
        carousel_style = 'carousel_style'
        carousel_with_static_card_style = 'carousel_with_static_card_style'

    _field_types = {
        'ad_standard_enhancements_edit_source': 'int',
        'adgroup_creation_source': 'string',
        'adgroup_edit_source': 'string',
        'carousel_style': 'string',
        'carousel_with_static_card_style': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


