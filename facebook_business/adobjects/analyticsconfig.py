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

class AnalyticsConfig(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAnalyticsConfig = True
        super(AnalyticsConfig, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        analytics_access_for_authorized_ad_account = 'analytics_access_for_authorized_ad_account'
        aws_kinesis_firehose_setting = 'aws_kinesis_firehose_setting'
        breakdowns_config = 'breakdowns_config'
        builtin_fields_config = 'builtin_fields_config'
        deprecated_events_config = 'deprecated_events_config'
        events_config = 'events_config'
        ios_purchase_validation_secret = 'ios_purchase_validation_secret'
        is_any_role_able_to_see_restricted_insights = 'is_any_role_able_to_see_restricted_insights'
        is_implicit_purchase_logging_on_android_supported = 'is_implicit_purchase_logging_on_android_supported'
        is_implicit_purchase_logging_on_ios_supported = 'is_implicit_purchase_logging_on_ios_supported'
        is_track_ios_app_uninstall_supported = 'is_track_ios_app_uninstall_supported'
        journey_backfill_status = 'journey_backfill_status'
        journey_conversion_events = 'journey_conversion_events'
        journey_enabled = 'journey_enabled'
        journey_impacting_change_time = 'journey_impacting_change_time'
        journey_timeout = 'journey_timeout'
        latest_sdk_versions = 'latest_sdk_versions'
        log_android_implicit_purchase_events = 'log_android_implicit_purchase_events'
        log_automatic_analytics_events = 'log_automatic_analytics_events'
        log_implicit_purchase_events = 'log_implicit_purchase_events'
        prev_journey_conversion_events = 'prev_journey_conversion_events'
        query_approximation_accuracy_level = 'query_approximation_accuracy_level'
        query_currency = 'query_currency'
        query_timezone = 'query_timezone'
        recent_events_update_time = 'recent_events_update_time'
        session_timeout_interval = 'session_timeout_interval'
        track_ios_app_uninstall = 'track_ios_app_uninstall'
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
            target_class=AnalyticsConfig,
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
        'analytics_access_for_authorized_ad_account': 'bool',
        'aws_kinesis_firehose_setting': 'Object',
        'breakdowns_config': 'list<Object>',
        'builtin_fields_config': 'list<Object>',
        'deprecated_events_config': 'list<Object>',
        'events_config': 'list<Object>',
        'ios_purchase_validation_secret': 'string',
        'is_any_role_able_to_see_restricted_insights': 'bool',
        'is_implicit_purchase_logging_on_android_supported': 'bool',
        'is_implicit_purchase_logging_on_ios_supported': 'bool',
        'is_track_ios_app_uninstall_supported': 'bool',
        'journey_backfill_status': 'string',
        'journey_conversion_events': 'list<string>',
        'journey_enabled': 'bool',
        'journey_impacting_change_time': 'datetime',
        'journey_timeout': 'string',
        'latest_sdk_versions': 'map<string, string>',
        'log_android_implicit_purchase_events': 'bool',
        'log_automatic_analytics_events': 'bool',
        'log_implicit_purchase_events': 'bool',
        'prev_journey_conversion_events': 'list<string>',
        'query_approximation_accuracy_level': 'string',
        'query_currency': 'string',
        'query_timezone': 'string',
        'recent_events_update_time': 'datetime',
        'session_timeout_interval': 'unsigned int',
        'track_ios_app_uninstall': 'bool',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


