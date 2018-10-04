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

class AdAccountActivity(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountActivity = True
        super(AdAccountActivity, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        billing_address_new = 'billing_address_new'
        billing_address_old = 'billing_address_old'
        created_by = 'created_by'
        created_time = 'created_time'
        credit_new = 'credit_new'
        credit_old = 'credit_old'
        credit_status_new = 'credit_status_new'
        credit_status_old = 'credit_status_old'
        currency_new = 'currency_new'
        currency_old = 'currency_old'
        daily_spend_limit_new = 'daily_spend_limit_new'
        daily_spend_limit_old = 'daily_spend_limit_old'
        event_time = 'event_time'
        event_type = 'event_type'
        funding_id_new = 'funding_id_new'
        funding_id_old = 'funding_id_old'
        grace_period_time_new = 'grace_period_time_new'
        grace_period_time_old = 'grace_period_time_old'
        id = 'id'
        manager_id_new = 'manager_id_new'
        manager_id_old = 'manager_id_old'
        name_new = 'name_new'
        name_old = 'name_old'
        spend_cap_new = 'spend_cap_new'
        spend_cap_old = 'spend_cap_old'
        status_new = 'status_new'
        status_old = 'status_old'
        terms_new = 'terms_new'
        terms_old = 'terms_old'
        tier_new = 'tier_new'
        tier_old = 'tier_old'
        time_updated_new = 'time_updated_new'
        time_updated_old = 'time_updated_old'

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
            target_class=AdAccountActivity,
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
        'billing_address_new': 'string',
        'billing_address_old': 'string',
        'created_by': 'string',
        'created_time': 'datetime',
        'credit_new': 'Object',
        'credit_old': 'Object',
        'credit_status_new': 'string',
        'credit_status_old': 'string',
        'currency_new': 'string',
        'currency_old': 'string',
        'daily_spend_limit_new': 'Object',
        'daily_spend_limit_old': 'Object',
        'event_time': 'datetime',
        'event_type': 'string',
        'funding_id_new': 'string',
        'funding_id_old': 'string',
        'grace_period_time_new': 'int',
        'grace_period_time_old': 'int',
        'id': 'string',
        'manager_id_new': 'string',
        'manager_id_old': 'string',
        'name_new': 'string',
        'name_old': 'string',
        'spend_cap_new': 'Object',
        'spend_cap_old': 'Object',
        'status_new': 'string',
        'status_old': 'string',
        'terms_new': 'int',
        'terms_old': 'int',
        'tier_new': 'string',
        'tier_old': 'string',
        'time_updated_new': 'datetime',
        'time_updated_old': 'datetime',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


