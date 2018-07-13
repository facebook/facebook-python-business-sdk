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

class AdStudyCell(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdStudyCell = True
        super(AdStudyCell, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_entities_count = 'ad_entities_count'
        control_percentage = 'control_percentage'
        id = 'id'
        name = 'name'
        treatment_percentage = 'treatment_percentage'

    class CreationTemplate:
        automatic_placements = 'AUTOMATIC_PLACEMENTS'
        brand_awareness = 'BRAND_AWARENESS'
        facebook = 'FACEBOOK'
        facebook_audience_network = 'FACEBOOK_AUDIENCE_NETWORK'
        facebook_instagram = 'FACEBOOK_INSTAGRAM'
        facebook_news_feed = 'FACEBOOK_NEWS_FEED'
        facebook_news_feed_in_stream_video = 'FACEBOOK_NEWS_FEED_IN_STREAM_VIDEO'
        in_stream_video = 'IN_STREAM_VIDEO'
        instagram = 'INSTAGRAM'
        mobile_optimized_video = 'MOBILE_OPTIMIZED_VIDEO'
        page_post_engagement = 'PAGE_POST_ENGAGEMENT'
        reach = 'REACH'
        tv_commercial = 'TV_COMMERCIAL'
        tv_facebook = 'TV_FACEBOOK'
        video_view_optimization = 'VIDEO_VIEW_OPTIMIZATION'
        low_frequency = 'LOW_FREQUENCY'
        medium_frequency = 'MEDIUM_FREQUENCY'
        high_frequency = 'HIGH_FREQUENCY'

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
            target_class=AdStudyCell,
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adaccounts': 'list<unsigned int>',
            'adsets': 'list<string>',
            'campaigns': 'list<string>',
            'creation_template': 'creation_template_enum',
            'description': 'string',
            'name': 'string',
        }
        enums = {
            'creation_template_enum': AdStudyCell.CreationTemplate.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudyCell,
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
        'ad_entities_count': 'unsigned int',
        'control_percentage': 'float',
        'id': 'string',
        'name': 'string',
        'treatment_percentage': 'float',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CreationTemplate'] = AdStudyCell.CreationTemplate.__dict__.values()
        return field_enum_info
