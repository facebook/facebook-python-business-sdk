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

class AdsReportBuilderSavedReport(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdsReportBuilderSavedReport = True
        super(AdsReportBuilderSavedReport, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_account_id = 'ad_account_id'
        attribution_windows = 'attribution_windows'
        creation_source = 'creation_source'
        creation_time = 'creation_time'
        date_interval = 'date_interval'
        date_preset = 'date_preset'
        dimension_groups = 'dimension_groups'
        dimensions = 'dimensions'
        filtering = 'filtering'
        id = 'id'
        is_mutated = 'is_mutated'
        last_access_time = 'last_access_time'
        last_report_snapshot_id = 'last_report_snapshot_id'
        last_report_snapshot_time = 'last_report_snapshot_time'
        locked_dimensions = 'locked_dimensions'
        metrics = 'metrics'
        old_report_schedule = 'old_report_schedule'
        report_name = 'report_name'
        report_snapshot_async_percent_completion = 'report_snapshot_async_percent_completion'
        report_snapshot_async_status = 'report_snapshot_async_status'
        schedule_frequency = 'schedule_frequency'
        sorting = 'sorting'
        start_date = 'start_date'
        status = 'status'
        subscribers = 'subscribers'
        update_time = 'update_time'
        user = 'user'
        user_dimensions = 'user_dimensions'
        user_metrics = 'user_metrics'

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
            target_class=AdsReportBuilderSavedReport,
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
        'ad_account_id': 'string',
        'attribution_windows': 'list<string>',
        'creation_source': 'string',
        'creation_time': 'datetime',
        'date_interval': 'Object',
        'date_preset': 'string',
        'dimension_groups': 'list<list<string>>',
        'dimensions': 'list<string>',
        'filtering': 'list',
        'id': 'string',
        'is_mutated': 'bool',
        'last_access_time': 'datetime',
        'last_report_snapshot_id': 'string',
        'last_report_snapshot_time': 'datetime',
        'locked_dimensions': 'int',
        'metrics': 'list<string>',
        'old_report_schedule': 'Object',
        'report_name': 'string',
        'report_snapshot_async_percent_completion': 'int',
        'report_snapshot_async_status': 'string',
        'schedule_frequency': 'string',
        'sorting': 'list<Object>',
        'start_date': 'string',
        'status': 'string',
        'subscribers': 'list<string>',
        'update_time': 'datetime',
        'user': 'Profile',
        'user_dimensions': 'list<string>',
        'user_metrics': 'list<string>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


