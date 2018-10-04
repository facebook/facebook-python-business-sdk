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

class EventTour(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isEventTour = True
        super(EventTour, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        description = 'description'
        dominant_color = 'dominant_color'
        end_time = 'end_time'
        id = 'id'
        is_past = 'is_past'
        last_event_timestamp = 'last_event_timestamp'
        name = 'name'
        num_events = 'num_events'
        photo = 'photo'
        publishing_state = 'publishing_state'
        scheduled_publish_timestamp = 'scheduled_publish_timestamp'
        start_time = 'start_time'
        ticketing_uri = 'ticketing_uri'
        video = 'video'

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
            target_class=EventTour,
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

    def get_events(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.event import Event
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/events',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Event,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Event, api=self._api),
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

    def get_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/pages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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
        'description': 'string',
        'dominant_color': 'string',
        'end_time': 'string',
        'id': 'string',
        'is_past': 'bool',
        'last_event_timestamp': 'int',
        'name': 'string',
        'num_events': 'int',
        'photo': 'Photo',
        'publishing_state': 'string',
        'scheduled_publish_timestamp': 'int',
        'start_time': 'string',
        'ticketing_uri': 'string',
        'video': 'AdVideo',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


