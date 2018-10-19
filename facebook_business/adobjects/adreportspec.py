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

class AdReportSpec(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdReportSpec = True
        super(AdReportSpec, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        actions_group_by = 'actions_group_by'
        creation_source = 'creation_source'
        data_columns = 'data_columns'
        date_preset = 'date_preset'
        export_columns = 'export_columns'
        filters = 'filters'
        format_version = 'format_version'
        id = 'id'
        insights_section = 'insights_section'
        name = 'name'
        report_schedule = 'report_schedule'
        report_schedule_id = 'report_schedule_id'
        sort_by = 'sort_by'
        sort_dir = 'sort_dir'
        time_increment = 'time_increment'
        time_interval = 'time_interval'
        time_ranges = 'time_ranges'
        format = 'format'
        report_run_id = 'report_run_id'
        user_report = 'user_report'
        business_id = 'business_id'
        limit = 'limit'
        bypass_async = 'bypass_async'

    class ActionsGroupBy:
        action_canvas_component_id = 'action_canvas_component_id'
        action_canvas_component_name = 'action_canvas_component_name'
        action_carousel_card_id = 'action_carousel_card_id'
        action_carousel_card_name = 'action_carousel_card_name'
        action_destination = 'action_destination'
        action_device = 'action_device'
        action_event_channel = 'action_event_channel'
        action_target_id = 'action_target_id'
        action_type = 'action_type'
        action_video_sound = 'action_video_sound'
        action_video_type = 'action_video_type'

    class CreationSource:
        adsmanagerreporting = 'adsManagerReporting'
        newadsmanager = 'newAdsManager'
        adsexceladdin = 'adsExcelAddin'

    class DatePreset:
        today = 'today'
        yesterday = 'yesterday'
        this_month = 'this_month'
        last_month = 'last_month'
        this_quarter = 'this_quarter'
        lifetime = 'lifetime'
        last_3d = 'last_3d'
        last_7d = 'last_7d'
        last_14d = 'last_14d'
        last_28d = 'last_28d'
        last_30d = 'last_30d'
        last_90d = 'last_90d'
        last_week_mon_sun = 'last_week_mon_sun'
        last_week_sun_sat = 'last_week_sun_sat'
        last_quarter = 'last_quarter'
        last_year = 'last_year'
        this_week_mon_today = 'this_week_mon_today'
        this_week_sun_today = 'this_week_sun_today'
        this_year = 'this_year'

    class Format:
        json = 'JSON'
        csv = 'CSV'
        xls = 'XLS'
        xlsx = 'XLSX'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adreportspecs'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_report_spec(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
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
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

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
            target_class=AdReportSpec,
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
            'time_ranges': 'Object',
            'data_columns': 'list<string>',
            'actions_group_by': 'list<actions_group_by_enum>',
            'filters': 'list<Object>',
            'sort_by': 'string',
            'sort_dir': 'string',
            'time_increment': 'string',
            'time_interval': 'Object',
            'date_preset': 'date_preset_enum',
            'format': 'format_enum',
            'export_columns': 'Object',
            'report_run_id': 'string',
            'name': 'string',
            'user_report': 'bool',
            'business_id': 'string',
            'limit': 'int',
            'bypass_async': 'bool',
            'report_schedule_id': 'string',
            'insights_section': 'Object',
            'creation_source': 'creation_source_enum',
            'format_version': 'unsigned int',
        }
        enums = {
            'actions_group_by_enum': AdReportSpec.ActionsGroupBy.__dict__.values(),
            'date_preset_enum': AdReportSpec.DatePreset.__dict__.values(),
            'format_enum': AdReportSpec.Format.__dict__.values(),
            'creation_source_enum': AdReportSpec.CreationSource.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdReportSpec,
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
        'account_id': 'string',
        'actions_group_by': 'list<string>',
        'creation_source': 'string',
        'data_columns': 'list<string>',
        'date_preset': 'string',
        'export_columns': 'list<string>',
        'filters': 'list<Object>',
        'format_version': 'int',
        'id': 'string',
        'insights_section': 'Object',
        'name': 'string',
        'report_schedule': 'Object',
        'report_schedule_id': 'string',
        'sort_by': 'string',
        'sort_dir': 'string',
        'time_increment': 'string',
        'time_interval': 'Object',
        'time_ranges': 'list<Object>',
        'format': 'Format',
        'report_run_id': 'string',
        'user_report': 'bool',
        'business_id': 'string',
        'limit': 'int',
        'bypass_async': 'bool',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ActionsGroupBy'] = AdReportSpec.ActionsGroupBy.__dict__.values()
        field_enum_info['CreationSource'] = AdReportSpec.CreationSource.__dict__.values()
        field_enum_info['DatePreset'] = AdReportSpec.DatePreset.__dict__.values()
        field_enum_info['Format'] = AdReportSpec.Format.__dict__.values()
        return field_enum_info


