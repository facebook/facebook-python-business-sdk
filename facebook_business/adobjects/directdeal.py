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

class DirectDeal(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isDirectDeal = True
        super(DirectDeal, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        adbreaks_enabled = 'adbreaks_enabled'
        adset = 'adset'
        advertiser = 'advertiser'
        advertiser_lead_email = 'advertiser_lead_email'
        advertiser_page = 'advertiser_page'
        cpe_amount = 'cpe_amount'
        cpe_currency = 'cpe_currency'
        end_time = 'end_time'
        id = 'id'
        lifetime_budget_amount = 'lifetime_budget_amount'
        lifetime_budget_currency = 'lifetime_budget_currency'
        lifetime_impressions = 'lifetime_impressions'
        name = 'name'
        pages = 'pages'
        placements = 'placements'
        priced_by = 'priced_by'
        publisher_name = 'publisher_name'
        review_requirement = 'review_requirement'
        sales_lead_email = 'sales_lead_email'
        start_time = 'start_time'
        status = 'status'
        targeting = 'targeting'

    class Status:
        value_0 = '0'
        value_1 = '1'
        value_2 = '2'
        value_3 = '3'
        value_4 = '4'
        value_5 = '5'
        value_6 = '6'

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
            target_class=DirectDeal,
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
        'adbreaks_enabled': 'bool',
        'adset': 'AdSet',
        'advertiser': 'Object',
        'advertiser_lead_email': 'string',
        'advertiser_page': 'string',
        'cpe_amount': 'int',
        'cpe_currency': 'string',
        'end_time': 'int',
        'id': 'string',
        'lifetime_budget_amount': 'int',
        'lifetime_budget_currency': 'string',
        'lifetime_impressions': 'int',
        'name': 'string',
        'pages': 'list<string>',
        'placements': 'list<string>',
        'priced_by': 'string',
        'publisher_name': 'string',
        'review_requirement': 'string',
        'sales_lead_email': 'string',
        'start_time': 'int',
        'status': 'string',
        'targeting': 'Targeting',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Status'] = DirectDeal.Status.__dict__.values()
        return field_enum_info
