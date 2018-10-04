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

class AutomotiveModel(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAutomotiveModel = True
        super(AutomotiveModel, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        applinks = 'applinks'
        automotive_model_id = 'automotive_model_id'
        availability = 'availability'
        body_style = 'body_style'
        currency = 'currency'
        custom_label_0 = 'custom_label_0'
        description = 'description'
        drivetrain = 'drivetrain'
        exterior_color = 'exterior_color'
        fuel_type = 'fuel_type'
        generation = 'generation'
        id = 'id'
        images = 'images'
        interior_color = 'interior_color'
        interior_upholstery = 'interior_upholstery'
        make = 'make'
        model = 'model'
        price = 'price'
        sanitized_images = 'sanitized_images'
        title = 'title'
        transmission = 'transmission'
        trim = 'trim'
        url = 'url'
        year = 'year'

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
            target_class=AutomotiveModel,
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
        'applinks': 'AppLinks',
        'automotive_model_id': 'string',
        'availability': 'string',
        'body_style': 'string',
        'currency': 'string',
        'custom_label_0': 'string',
        'description': 'string',
        'drivetrain': 'string',
        'exterior_color': 'string',
        'fuel_type': 'string',
        'generation': 'string',
        'id': 'string',
        'images': 'list<string>',
        'interior_color': 'string',
        'interior_upholstery': 'string',
        'make': 'string',
        'model': 'string',
        'price': 'string',
        'sanitized_images': 'list<string>',
        'title': 'string',
        'transmission': 'string',
        'trim': 'string',
        'url': 'string',
        'year': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


