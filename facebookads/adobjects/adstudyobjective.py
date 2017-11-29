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

class AdStudyObjective(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdStudyObjective = True
        super(AdStudyObjective, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        custom_attributes = 'custom_attributes'
        id = 'id'
        is_primary = 'is_primary'
        last_updated_results = 'last_updated_results'
        name = 'name'
        results = 'results'
        type = 'type'

    class Breakdowns:
        age = 'age'
        cell_id = 'cell_id'
        gender = 'gender'
        country = 'country'

    class Type:
        sales = 'SALES'
        nonsales = 'NONSALES'
        mae = 'MAE'
        telco = 'TELCO'
        ftl = 'FTL'
        mai = 'MAI'
        partner = 'PARTNER'
        brandlift = 'BRANDLIFT'
        brand = 'BRAND'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'breakdowns': 'list<breakdowns_enum>',
        }
        enums = {
            'breakdowns_enum': AdStudyObjective.Breakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudyObjective,
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
        'custom_attributes': 'list<string>',
        'id': 'string',
        'is_primary': 'bool',
        'last_updated_results': 'string',
        'name': 'string',
        'results': 'list<string>',
        'type': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Breakdowns'] = AdStudyObjective.Breakdowns.__dict__.values()
        field_enum_info['Type'] = AdStudyObjective.Type.__dict__.values()
        return field_enum_info
