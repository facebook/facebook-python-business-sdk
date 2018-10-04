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

class AdAccountRoas(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountRoas = True
        super(AdAccountRoas, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        adgroup_id = 'adgroup_id'
        arpu_180d = 'arpu_180d'
        arpu_1d = 'arpu_1d'
        arpu_30d = 'arpu_30d'
        arpu_365d = 'arpu_365d'
        arpu_3d = 'arpu_3d'
        arpu_7d = 'arpu_7d'
        arpu_90d = 'arpu_90d'
        campaign_group_id = 'campaign_group_id'
        campaign_id = 'campaign_id'
        date_start = 'date_start'
        date_stop = 'date_stop'
        installs = 'installs'
        revenue = 'revenue'
        revenue_180d = 'revenue_180d'
        revenue_1d = 'revenue_1d'
        revenue_30d = 'revenue_30d'
        revenue_365d = 'revenue_365d'
        revenue_3d = 'revenue_3d'
        revenue_7d = 'revenue_7d'
        revenue_90d = 'revenue_90d'
        spend = 'spend'
        yield_180d = 'yield_180d'
        yield_1d = 'yield_1d'
        yield_30d = 'yield_30d'
        yield_365d = 'yield_365d'
        yield_3d = 'yield_3d'
        yield_7d = 'yield_7d'
        yield_90d = 'yield_90d'
        id = 'id'

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
            target_class=AdAccountRoas,
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
        'adgroup_id': 'string',
        'arpu_180d': 'float',
        'arpu_1d': 'float',
        'arpu_30d': 'float',
        'arpu_365d': 'float',
        'arpu_3d': 'float',
        'arpu_7d': 'float',
        'arpu_90d': 'float',
        'campaign_group_id': 'string',
        'campaign_id': 'string',
        'date_start': 'string',
        'date_stop': 'string',
        'installs': 'unsigned int',
        'revenue': 'float',
        'revenue_180d': 'float',
        'revenue_1d': 'float',
        'revenue_30d': 'float',
        'revenue_365d': 'float',
        'revenue_3d': 'float',
        'revenue_7d': 'float',
        'revenue_90d': 'float',
        'spend': 'float',
        'yield_180d': 'float',
        'yield_1d': 'float',
        'yield_30d': 'float',
        'yield_365d': 'float',
        'yield_3d': 'float',
        'yield_7d': 'float',
        'yield_90d': 'float',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


