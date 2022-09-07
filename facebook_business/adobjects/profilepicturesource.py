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

class ProfilePictureSource(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProfilePictureSource, self).__init__()
        self._isProfilePictureSource = True
        self._api = api

    class Field(AbstractObject.Field):
        bottom = 'bottom'
        cache_key = 'cache_key'
        height = 'height'
        is_silhouette = 'is_silhouette'
        left = 'left'
        right = 'right'
        top = 'top'
        url = 'url'
        width = 'width'

    class Type:
        album = 'album'
        small = 'small'
        thumbnail = 'thumbnail'

    class BreakingChange:
        profile_picture = 'PROFILE_PICTURE'

    _field_types = {
        'bottom': 'unsigned int',
        'cache_key': 'string',
        'height': 'unsigned int',
        'is_silhouette': 'bool',
        'left': 'unsigned int',
        'right': 'unsigned int',
        'top': 'unsigned int',
        'url': 'string',
        'width': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Type'] = ProfilePictureSource.Type.__dict__.values()
        field_enum_info['BreakingChange'] = ProfilePictureSource.BreakingChange.__dict__.values()
        return field_enum_info


