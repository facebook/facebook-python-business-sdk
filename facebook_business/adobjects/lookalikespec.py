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

class LookalikeSpec(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isLookalikeSpec = True
        super(LookalikeSpec, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        country = 'country'
        is_financial_service = 'is_financial_service'
        origin = 'origin'
        origin_event_name = 'origin_event_name'
        origin_event_source_name = 'origin_event_source_name'
        origin_event_source_type = 'origin_event_source_type'
        product_set_name = 'product_set_name'
        ratio = 'ratio'
        starting_ratio = 'starting_ratio'
        target_countries = 'target_countries'
        target_country_names = 'target_country_names'
        type = 'type'
        id = 'id'

    _field_types = {
        'country': 'string',
        'is_financial_service': 'bool',
        'origin': 'list<Object>',
        'origin_event_name': 'string',
        'origin_event_source_name': 'string',
        'origin_event_source_type': 'string',
        'product_set_name': 'string',
        'ratio': 'float',
        'starting_ratio': 'float',
        'target_countries': 'list<string>',
        'target_country_names': 'list',
        'type': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


