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
from facebook_business.adobjects.helpers.adreportrunmixin import AdReportRunMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdReportRun(
    AdReportRunMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdReportRun = True
        super(AdReportRun, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        async_percent_completion = 'async_percent_completion'
        async_status = 'async_status'
        date_start = 'date_start'
        date_stop = 'date_stop'
        emails = 'emails'
        friendly_name = 'friendly_name'
        id = 'id'
        is_bookmarked = 'is_bookmarked'
        is_running = 'is_running'
        schedule_id = 'schedule_id'
        time_completed = 'time_completed'
        time_ref = 'time_ref'
        action_attribution_windows = 'action_attribution_windows'
        action_breakdowns = 'action_breakdowns'
        action_report_time = 'action_report_time'
        breakdowns = 'breakdowns'
        date_preset = 'date_preset'
        default_summary = 'default_summary'
        export_columns = 'export_columns'
        export_format = 'export_format'
        export_name = 'export_name'
        fields = 'fields'
        filtering = 'filtering'
        level = 'level'
        product_id_limit = 'product_id_limit'
        sort = 'sort'
        summary = 'summary'
        summary_action_breakdowns = 'summary_action_breakdowns'
        time_increment = 'time_increment'
        time_range = 'time_range'
        time_ranges = 'time_ranges'
        use_account_attribution_setting = 'use_account_attribution_setting'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'insights'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).get_insights_async(fields, params, batch, pending)

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
            target_class=AdReportRun,
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

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, pending=False):
        from facebook_business.adobjects.adsinsights import AdsInsights
        if is_async:
          return self.get_insights_async(fields, params, batch, pending)
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsInsights,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsInsights, api=self._api),
            include_summary=False,
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
        'async_percent_completion': 'unsigned int',
        'async_status': 'string',
        'date_start': 'string',
        'date_stop': 'string',
        'emails': 'list<string>',
        'friendly_name': 'string',
        'id': 'string',
        'is_bookmarked': 'bool',
        'is_running': 'bool',
        'schedule_id': 'string',
        'time_completed': 'unsigned int',
        'time_ref': 'unsigned int',
        'action_attribution_windows': 'list<ActionAttributionWindows>',
        'action_breakdowns': 'list<ActionBreakdowns>',
        'action_report_time': 'ActionReportTime',
        'breakdowns': 'list<Breakdowns>',
        'date_preset': 'DatePreset',
        'default_summary': 'bool',
        'export_columns': 'list<string>',
        'export_format': 'string',
        'export_name': 'string',
        'fields': 'list<Summary>',
        'filtering': 'list<Object>',
        'level': 'Level',
        'product_id_limit': 'int',
        'sort': 'list<string>',
        'summary': 'list<Summary>',
        'summary_action_breakdowns': 'list<SummaryActionBreakdowns>',
        'time_increment': 'string',
        'time_range': 'Object',
        'time_ranges': 'list<Object>',
        'use_account_attribution_setting': 'bool',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
