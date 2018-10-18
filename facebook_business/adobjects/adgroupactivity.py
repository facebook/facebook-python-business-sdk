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

class AdgroupActivity(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdgroupActivity = True
        super(AdgroupActivity, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_creative_id_new = 'ad_creative_id_new'
        ad_creative_id_old = 'ad_creative_id_old'
        asset_feed_id_new = 'asset_feed_id_new'
        asset_feed_id_old = 'asset_feed_id_old'
        bid_amount_new = 'bid_amount_new'
        bid_amount_old = 'bid_amount_old'
        bid_info_new = 'bid_info_new'
        bid_info_old = 'bid_info_old'
        bid_type_new = 'bid_type_new'
        bid_type_old = 'bid_type_old'
        conversion_specs_new = 'conversion_specs_new'
        conversion_specs_old = 'conversion_specs_old'
        created_time = 'created_time'
        display_sequence_new = 'display_sequence_new'
        display_sequence_old = 'display_sequence_old'
        engagement_audience_new = 'engagement_audience_new'
        engagement_audience_old = 'engagement_audience_old'
        event_time = 'event_time'
        event_type = 'event_type'
        force_run_status_new = 'force_run_status_new'
        force_run_status_old = 'force_run_status_old'
        friendly_name_new = 'friendly_name_new'
        friendly_name_old = 'friendly_name_old'
        id = 'id'
        is_reviewer_admin_new = 'is_reviewer_admin_new'
        is_reviewer_admin_old = 'is_reviewer_admin_old'
        objective_new = 'objective_new'
        objective_old = 'objective_old'
        objective_source_new = 'objective_source_new'
        objective_source_old = 'objective_source_old'
        priority_new = 'priority_new'
        priority_old = 'priority_old'
        reason_new = 'reason_new'
        reason_old = 'reason_old'
        run_status_new = 'run_status_new'
        run_status_old = 'run_status_old'
        source_adgroup_id_new = 'source_adgroup_id_new'
        source_adgroup_id_old = 'source_adgroup_id_old'
        start_time_new = 'start_time_new'
        start_time_old = 'start_time_old'
        stop_time_new = 'stop_time_new'
        stop_time_old = 'stop_time_old'
        target_spec_id_new = 'target_spec_id_new'
        target_spec_id_old = 'target_spec_id_old'
        tracking_pixel_ids_new = 'tracking_pixel_ids_new'
        tracking_pixel_ids_old = 'tracking_pixel_ids_old'
        tracking_specs_new = 'tracking_specs_new'
        tracking_specs_old = 'tracking_specs_old'
        update_time_new = 'update_time_new'
        update_time_old = 'update_time_old'
        view_tags_new = 'view_tags_new'
        view_tags_old = 'view_tags_old'

    class ObjectiveNew:
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

    class ObjectiveOld:
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
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdgroupActivity,
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
        'ad_creative_id_new': 'string',
        'ad_creative_id_old': 'string',
        'asset_feed_id_new': 'string',
        'asset_feed_id_old': 'string',
        'bid_amount_new': 'int',
        'bid_amount_old': 'int',
        'bid_info_new': 'list<Object>',
        'bid_info_old': 'list<Object>',
        'bid_type_new': 'string',
        'bid_type_old': 'string',
        'conversion_specs_new': 'list<Object>',
        'conversion_specs_old': 'list<Object>',
        'created_time': 'datetime',
        'display_sequence_new': 'int',
        'display_sequence_old': 'int',
        'engagement_audience_new': 'bool',
        'engagement_audience_old': 'bool',
        'event_time': 'datetime',
        'event_type': 'string',
        'force_run_status_new': 'bool',
        'force_run_status_old': 'bool',
        'friendly_name_new': 'string',
        'friendly_name_old': 'string',
        'id': 'string',
        'is_reviewer_admin_new': 'bool',
        'is_reviewer_admin_old': 'bool',
        'objective_new': 'ObjectiveNew',
        'objective_old': 'ObjectiveOld',
        'objective_source_new': 'string',
        'objective_source_old': 'string',
        'priority_new': 'int',
        'priority_old': 'int',
        'reason_new': 'string',
        'reason_old': 'string',
        'run_status_new': 'string',
        'run_status_old': 'string',
        'source_adgroup_id_new': 'string',
        'source_adgroup_id_old': 'string',
        'start_time_new': 'datetime',
        'start_time_old': 'datetime',
        'stop_time_new': 'datetime',
        'stop_time_old': 'datetime',
        'target_spec_id_new': 'string',
        'target_spec_id_old': 'string',
        'tracking_pixel_ids_new': 'list<string>',
        'tracking_pixel_ids_old': 'list<string>',
        'tracking_specs_new': 'list<Object>',
        'tracking_specs_old': 'list<Object>',
        'update_time_new': 'datetime',
        'update_time_old': 'datetime',
        'view_tags_new': 'list<string>',
        'view_tags_old': 'list<string>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ObjectiveNew'] = AdgroupActivity.ObjectiveNew.__dict__.values()
        field_enum_info['ObjectiveOld'] = AdgroupActivity.ObjectiveOld.__dict__.values()
        return field_enum_info


