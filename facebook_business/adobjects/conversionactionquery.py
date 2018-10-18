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

class ConversionActionQuery(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isConversionActionQuery = True
        super(ConversionActionQuery, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        field_action_type = 'action.type'
        application = 'application'
        conversion_id = 'conversion_id'
        creative = 'creative'
        dataset = 'dataset'
        event = 'event'
        field_event_creator = 'event.creator'
        event_type = 'event_type'
        fb_pixel = 'fb_pixel'
        fb_pixel_event = 'fb_pixel_event'
        leadgen = 'leadgen'
        object = 'object'
        field_object_domain = 'object.domain'
        offer = 'offer'
        field_offer_creator = 'offer.creator'
        offsite_pixel = 'offsite_pixel'
        page = 'page'
        field_page_parent = 'page.parent'
        post = 'post'
        field_post_object = 'post.object'
        field_post_object_wall = 'post.object.wall'
        field_post_wall = 'post.wall'
        question = 'question'
        field_question_creator = 'question.creator'
        response = 'response'
        subtype = 'subtype'
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
            target_class=ConversionActionQuery,
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
        'action.type': 'list<Object>',
        'application': 'list<Object>',
        'conversion_id': 'list<string>',
        'creative': 'list<Object>',
        'dataset': 'list<string>',
        'event': 'list<string>',
        'event.creator': 'list<string>',
        'event_type': 'list<string>',
        'fb_pixel': 'list<string>',
        'fb_pixel_event': 'list<string>',
        'leadgen': 'list<string>',
        'object': 'list<string>',
        'object.domain': 'list<string>',
        'offer': 'list<string>',
        'offer.creator': 'list<string>',
        'offsite_pixel': 'list<string>',
        'page': 'list<string>',
        'page.parent': 'list<string>',
        'post': 'list<string>',
        'post.object': 'list<string>',
        'post.object.wall': 'list<string>',
        'post.wall': 'list<string>',
        'question': 'list<string>',
        'question.creator': 'list<string>',
        'response': 'list<string>',
        'subtype': 'list<string>',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


