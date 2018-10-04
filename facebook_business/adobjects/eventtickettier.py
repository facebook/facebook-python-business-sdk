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

class EventTicketTier(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isEventTicketTier = True
        super(EventTicketTier, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        currency = 'currency'
        description = 'description'
        end_sales_time = 'end_sales_time'
        end_show_time = 'end_show_time'
        fee_settings = 'fee_settings'
        id = 'id'
        maximum_quantity = 'maximum_quantity'
        metadata = 'metadata'
        minimum_quantity = 'minimum_quantity'
        name = 'name'
        price = 'price'
        priority = 'priority'
        retailer_id = 'retailer_id'
        seating_map_image_url = 'seating_map_image_url'
        start_sales_time = 'start_sales_time'
        start_show_time = 'start_show_time'
        status = 'status'
        total_quantity = 'total_quantity'

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
            target_class=EventTicketTier,
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
        'currency': 'string',
        'description': 'string',
        'end_sales_time': 'datetime',
        'end_show_time': 'datetime',
        'fee_settings': 'string',
        'id': 'string',
        'maximum_quantity': 'int',
        'metadata': 'string',
        'minimum_quantity': 'int',
        'name': 'string',
        'price': 'int',
        'priority': 'int',
        'retailer_id': 'string',
        'seating_map_image_url': 'string',
        'start_sales_time': 'datetime',
        'start_show_time': 'datetime',
        'status': 'string',
        'total_quantity': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


