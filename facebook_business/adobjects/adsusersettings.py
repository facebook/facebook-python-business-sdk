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

class AdsUserSettings(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsUserSettings = True
        super(AdsUserSettings, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        adgroup_column_visibility = 'adgroup_column_visibility'
        adgroup_name_template = 'adgroup_name_template'
        adgroup_widths = 'adgroup_widths'
        ads_tool_visits = 'ads_tool_visits'
        bookmarked_pages = 'bookmarked_pages'
        campaign_column_visibility = 'campaign_column_visibility'
        campaign_group_column_visibility = 'campaign_group_column_visibility'
        campaign_group_name_template = 'campaign_group_name_template'
        campaign_group_widths = 'campaign_group_widths'
        campaign_name_template = 'campaign_name_template'
        campaign_widths = 'campaign_widths'
        default_creation_mode = 'default_creation_mode'
        id = 'id'
        last_used_post_format = 'last_used_post_format'
        last_visited_time = 'last_visited_time'
        open_tabs = 'open_tabs'
        selected_ad_account = 'selected_ad_account'
        selected_comparison_timerange = 'selected_comparison_timerange'
        selected_page = 'selected_page'
        selected_page_section = 'selected_page_section'
        selected_power_editor_pane = 'selected_power_editor_pane'
        selected_stat_range = 'selected_stat_range'
        should_not_show_publish_message_on_editor_close = 'should_not_show_publish_message_on_editor_close'
        unowned_pages = 'unowned_pages'
        use_pe_create_flow = 'use_pe_create_flow'
        use_stepper_primary_entry = 'use_stepper_primary_entry'
        user = 'user'

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
            target_class=AdsUserSettings,
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
        'adgroup_column_visibility': 'list<Object>',
        'adgroup_name_template': 'Object',
        'adgroup_widths': 'list<Object>',
        'ads_tool_visits': 'list<Object>',
        'bookmarked_pages': 'list<Page>',
        'campaign_column_visibility': 'list<Object>',
        'campaign_group_column_visibility': 'list<Object>',
        'campaign_group_name_template': 'Object',
        'campaign_group_widths': 'list<Object>',
        'campaign_name_template': 'Object',
        'campaign_widths': 'list<Object>',
        'default_creation_mode': 'string',
        'id': 'string',
        'last_used_post_format': 'string',
        'last_visited_time': 'datetime',
        'open_tabs': 'list<string>',
        'selected_ad_account': 'AdAccount',
        'selected_comparison_timerange': 'Object',
        'selected_page': 'Page',
        'selected_page_section': 'string',
        'selected_power_editor_pane': 'string',
        'selected_stat_range': 'Object',
        'should_not_show_publish_message_on_editor_close': 'bool',
        'unowned_pages': 'list<Page>',
        'use_pe_create_flow': 'bool',
        'use_stepper_primary_entry': 'bool',
        'user': 'User',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


