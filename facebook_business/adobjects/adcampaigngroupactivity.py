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

class AdCampaignGroupActivity(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCampaignGroupActivity = True
        super(AdCampaignGroupActivity, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        budget_limit_new = 'budget_limit_new'
        budget_limit_old = 'budget_limit_old'
        buying_type_new = 'buying_type_new'
        buying_type_old = 'buying_type_old'
        event_time = 'event_time'
        event_type = 'event_type'
        id = 'id'
        is_autobid_new = 'is_autobid_new'
        is_autobid_old = 'is_autobid_old'
        is_average_price_pacing_new = 'is_average_price_pacing_new'
        is_average_price_pacing_old = 'is_average_price_pacing_old'
        name_new = 'name_new'
        name_old = 'name_old'
        objective_new = 'objective_new'
        objective_old = 'objective_old'
        pacing_type = 'pacing_type'
        run_status_new = 'run_status_new'
        run_status_old = 'run_status_old'
        spend_cap_new = 'spend_cap_new'
        spend_cap_old = 'spend_cap_old'
        time_created = 'time_created'
        time_updated_new = 'time_updated_new'
        time_updated_old = 'time_updated_old'

    class ObjectiveNew:
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        local_awareness = 'LOCAL_AWARENESS'
        messages = 'MESSAGES'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        video_views = 'VIDEO_VIEWS'
        website_conversions = 'WEBSITE_CONVERSIONS'

    class ObjectiveOld:
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        canvas_app_engagement = 'CANVAS_APP_ENGAGEMENT'
        canvas_app_installs = 'CANVAS_APP_INSTALLS'
        event_responses = 'EVENT_RESPONSES'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        local_awareness = 'LOCAL_AWARENESS'
        messages = 'MESSAGES'
        mobile_app_engagement = 'MOBILE_APP_ENGAGEMENT'
        mobile_app_installs = 'MOBILE_APP_INSTALLS'
        none = 'NONE'
        offer_claims = 'OFFER_CLAIMS'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        video_views = 'VIDEO_VIEWS'
        website_conversions = 'WEBSITE_CONVERSIONS'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            target_class=AdCampaignGroupActivity,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'budget_limit_new': 'Object',
        'budget_limit_old': 'Object',
        'buying_type_new': 'string',
        'buying_type_old': 'string',
        'event_time': 'datetime',
        'event_type': 'string',
        'id': 'string',
        'is_autobid_new': 'bool',
        'is_autobid_old': 'bool',
        'is_average_price_pacing_new': 'bool',
        'is_average_price_pacing_old': 'bool',
        'name_new': 'string',
        'name_old': 'string',
        'objective_new': 'ObjectiveNew',
        'objective_old': 'ObjectiveOld',
        'pacing_type': 'int',
        'run_status_new': 'string',
        'run_status_old': 'string',
        'spend_cap_new': 'int',
        'spend_cap_old': 'int',
        'time_created': 'datetime',
        'time_updated_new': 'datetime',
        'time_updated_old': 'datetime',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ObjectiveNew'] = AdCampaignGroupActivity.ObjectiveNew.__dict__.values()
        field_enum_info['ObjectiveOld'] = AdCampaignGroupActivity.ObjectiveOld.__dict__.values()
        return field_enum_info


