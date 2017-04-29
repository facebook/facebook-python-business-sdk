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

class PartnerCategory(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPartnerCategory = True
        super(PartnerCategory, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        approximate_count = 'approximate_count'
        country = 'country'
        description = 'description'
        details = 'details'
        id = 'id'
        is_private = 'is_private'
        name = 'name'
        parent_category = 'parent_category'
        source = 'source'
        status = 'status'
        targeting_type = 'targeting_type'

    class PrivateOrPublic:
        private = 'PRIVATE'
        public = 'PUBLIC'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'partnercategories'

    _field_types = {
        'approximate_count': 'int',
        'country': 'string',
        'description': 'string',
        'details': 'string',
        'id': 'string',
        'is_private': 'bool',
        'name': 'string',
        'parent_category': 'string',
        'source': 'string',
        'status': 'string',
        'targeting_type': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['PrivateOrPublic'] = PartnerCategory.PrivateOrPublic.__dict__.values()
        return field_enum_info
