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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCreativeCollectionThumbnailInfo(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeCollectionThumbnailInfo, self).__init__()
        self._isAdCreativeCollectionThumbnailInfo = True
        self._api = api

    class Field(AbstractObject.Field):
        element_child_index = 'element_child_index'
        element_crops = 'element_crops'
        element_id = 'element_id'

    _field_types = {
        'element_child_index': 'int',
        'element_crops': 'AdsImageCrops',
        'element_id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
