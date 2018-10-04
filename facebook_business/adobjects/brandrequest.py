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

class BrandRequest(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBrandRequest = True
        super(BrandRequest, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_contacts = 'additional_contacts'
        approval_level = 'approval_level'
        cells = 'cells'
        countries = 'countries'
        deny_reason = 'deny_reason'
        end_time = 'end_time'
        estimated_reach = 'estimated_reach'
        id = 'id'
        is_multicell = 'is_multicell'
        locale = 'locale'
        max_age = 'max_age'
        min_age = 'min_age'
        questions = 'questions'
        region = 'region'
        request_status = 'request_status'
        review_date = 'review_date'
        start_time = 'start_time'
        status = 'status'
        submit_date = 'submit_date'
        total_budget = 'total_budget'

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
            target_class=BrandRequest,
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
        'additional_contacts': 'list<string>',
        'approval_level': 'unsigned int',
        'cells': 'list<Object>',
        'countries': 'list<string>',
        'deny_reason': 'string',
        'end_time': 'datetime',
        'estimated_reach': 'unsigned int',
        'id': 'string',
        'is_multicell': 'bool',
        'locale': 'string',
        'max_age': 'unsigned int',
        'min_age': 'unsigned int',
        'questions': 'list<Object>',
        'region': 'string',
        'request_status': 'string',
        'review_date': 'datetime',
        'start_time': 'datetime',
        'status': 'string',
        'submit_date': 'datetime',
        'total_budget': 'Object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


