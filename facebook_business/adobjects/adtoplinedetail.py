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

class AdToplineDetail(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdToplineDetail = True
        super(AdToplineDetail, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        active_status = 'active_status'
        ad_account_id = 'ad_account_id'
        flight_end_date = 'flight_end_date'
        flight_start_date = 'flight_start_date'
        id = 'id'
        io_number = 'io_number'
        line_number = 'line_number'
        price = 'price'
        quantity = 'quantity'
        sf_detail_line_id = 'sf_detail_line_id'
        subline_id = 'subline_id'
        targets = 'targets'
        time_created = 'time_created'
        time_updated = 'time_updated'
        topline_id = 'topline_id'

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
            target_class=AdToplineDetail,
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
        'active_status': 'int',
        'ad_account_id': 'string',
        'flight_end_date': 'datetime',
        'flight_start_date': 'datetime',
        'id': 'string',
        'io_number': 'int',
        'line_number': 'int',
        'price': 'float',
        'quantity': 'float',
        'sf_detail_line_id': 'string',
        'subline_id': 'string',
        'targets': 'string',
        'time_created': 'datetime',
        'time_updated': 'datetime',
        'topline_id': 'AdTopline',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


