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

class StonehengeSubscriptionPublisher(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isStonehengeSubscriptionPublisher = True
        super(StonehengeSubscriptionPublisher, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        application_id = 'application_id'
        article_url_patterns = 'article_url_patterns'
        content_tier_breakdown = 'content_tier_breakdown'
        default_content_tier = 'default_content_tier'
        id = 'id'
        is_test = 'is_test'
        meter_tracker = 'meter_tracker'
        owner = 'owner'
        packages = 'packages'
        paywall_tracker = 'paywall_tracker'
        subscription_pixel_tracking = 'subscription_pixel_tracking'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'content_tier_breakdown_days': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=StonehengeSubscriptionPublisher,
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
        'application_id': 'string',
        'article_url_patterns': 'list<Object>',
        'content_tier_breakdown': 'list<Object>',
        'default_content_tier': 'string',
        'id': 'string',
        'is_test': 'bool',
        'meter_tracker': 'Object',
        'owner': 'Page',
        'packages': 'list<Object>',
        'paywall_tracker': 'Object',
        'subscription_pixel_tracking': 'Object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


