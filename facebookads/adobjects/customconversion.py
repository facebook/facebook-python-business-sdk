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

class CustomConversion(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCustomConversion = True
        super(CustomConversion, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        creation_time = 'creation_time'
        custom_event_type = 'custom_event_type'
        default_conversion_value = 'default_conversion_value'
        description = 'description'
        first_fired_time = 'first_fired_time'
        id = 'id'
        is_archived = 'is_archived'
        last_fired_time = 'last_fired_time'
        name = 'name'
        pixel = 'pixel'
        pixel_rule = 'pixel_rule'

    class CustomEventType:
        activate_app = 'ACTIVATE_APP'
        complete_registration = 'COMPLETE_REGISTRATION'
        content_view = 'CONTENT_VIEW'
        search = 'SEARCH'
        rate = 'RATE'
        tutorial_completion = 'TUTORIAL_COMPLETION'
        add_to_cart = 'ADD_TO_CART'
        add_to_wishlist = 'ADD_TO_WISHLIST'
        initiated_checkout = 'INITIATED_CHECKOUT'
        add_payment_info = 'ADD_PAYMENT_INFO'
        purchase = 'PURCHASE'
        lead = 'LEAD'
        level_achieved = 'LEVEL_ACHIEVED'
        achievement_unlocked = 'ACHIEVEMENT_UNLOCKED'
        spent_credits = 'SPENT_CREDITS'
        other = 'OTHER'

    @classmethod
    def get_endpoint(cls):
        return 'customconversions'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
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
            target_class=CustomConversion,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'default_conversion_value': 'float',
            'description': 'string',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_stats(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adspixelstatsresult import AdsPixelStatsResult
        self.assure_call()
        param_types = {
            'aggregation': 'aggregation_enum',
            'end_time': 'datetime',
            'start_time': 'datetime',
        }
        enums = {
            'aggregation_enum': AdsPixelStatsResult.Aggregation.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/stats',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixelStatsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixelStatsResult),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    _field_types = {
        'account_id': 'string',
        'creation_time': 'datetime',
        'custom_event_type': 'CustomEventType',
        'default_conversion_value': 'unsigned int',
        'description': 'string',
        'first_fired_time': 'datetime',
        'id': 'string',
        'is_archived': 'bool',
        'last_fired_time': 'datetime',
        'name': 'string',
        'pixel': 'AdsPixel',
        'pixel_rule': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CustomEventType'] = CustomConversion.CustomEventType.__dict__.values()
        return field_enum_info
