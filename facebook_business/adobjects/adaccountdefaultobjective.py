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

class AdAccountDefaultObjective(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountDefaultObjective = True
        super(AdAccountDefaultObjective, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        default_objective_for_user = 'default_objective_for_user'
        objective_for_level = 'objective_for_level'
        id = 'id'

    class DefaultObjectiveForUser:
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        post_engagement = 'POST_ENGAGEMENT'
        website_conversions = 'WEBSITE_CONVERSIONS'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        link_clicks = 'LINK_CLICKS'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        video_views = 'VIDEO_VIEWS'
        local_awareness = 'LOCAL_AWARENESS'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        lead_generation = 'LEAD_GENERATION'
        brand_awareness = 'BRAND_AWARENESS'
        app_installs = 'APP_INSTALLS'
        messages = 'MESSAGES'

    class ObjectiveForLevel:
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        post_engagement = 'POST_ENGAGEMENT'
        website_conversions = 'WEBSITE_CONVERSIONS'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        link_clicks = 'LINK_CLICKS'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        video_views = 'VIDEO_VIEWS'
        local_awareness = 'LOCAL_AWARENESS'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        lead_generation = 'LEAD_GENERATION'
        brand_awareness = 'BRAND_AWARENESS'
        app_installs = 'APP_INSTALLS'
        messages = 'MESSAGES'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'adgroup_id': 'string',
            'campaign_group_id': 'string',
            'campaign_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountDefaultObjective,
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
        'default_objective_for_user': 'DefaultObjectiveForUser',
        'objective_for_level': 'ObjectiveForLevel',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DefaultObjectiveForUser'] = AdAccountDefaultObjective.DefaultObjectiveForUser.__dict__.values()
        field_enum_info['ObjectiveForLevel'] = AdAccountDefaultObjective.ObjectiveForLevel.__dict__.values()
        return field_enum_info


