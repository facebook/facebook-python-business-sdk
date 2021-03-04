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

class AdoptablePet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdoptablePet = True
        super(AdoptablePet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        adoptable_pet_id = 'adoptable_pet_id'
        adoption_application_form_url = 'adoption_application_form_url'
        age_bucket = 'age_bucket'
        animal_type = 'animal_type'
        applinks = 'applinks'
        availability = 'availability'
        breed = 'breed'
        category_specific_fields = 'category_specific_fields'
        coat_length = 'coat_length'
        color = 'color'
        currency = 'currency'
        description = 'description'
        features = 'features'
        gender = 'gender'
        id = 'id'
        images = 'images'
        name = 'name'
        price = 'price'
        sanitized_images = 'sanitized_images'
        secondary_color = 'secondary_color'
        shelter_email = 'shelter_email'
        shelter_name = 'shelter_name'
        shelter_page_id = 'shelter_page_id'
        shelter_phone = 'shelter_phone'
        size = 'size'
        tertiary_color = 'tertiary_color'
        url = 'url'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            target_class=AdoptablePet,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'address': 'Object',
        'adoptable_pet_id': 'string',
        'adoption_application_form_url': 'string',
        'age_bucket': 'string',
        'animal_type': 'string',
        'applinks': 'CatalogItemAppLinks',
        'availability': 'string',
        'breed': 'string',
        'category_specific_fields': 'CatalogSubVerticalList',
        'coat_length': 'string',
        'color': 'string',
        'currency': 'string',
        'description': 'string',
        'features': 'list<string>',
        'gender': 'string',
        'id': 'string',
        'images': 'list<string>',
        'name': 'string',
        'price': 'string',
        'sanitized_images': 'list<string>',
        'secondary_color': 'string',
        'shelter_email': 'string',
        'shelter_name': 'string',
        'shelter_page_id': 'Page',
        'shelter_phone': 'string',
        'size': 'string',
        'tertiary_color': 'string',
        'url': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


