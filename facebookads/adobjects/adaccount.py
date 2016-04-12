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

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker
from facebookads.adobjects.helpers.adaccountmixin import AdAccountMixin
from facebookads.mixins import HasAdLabels

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAccount(
    AbstractCrudObject,
    AdAccountMixin,
    HasAdLabels,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccount = True
        super(AdAccount, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_groups = 'account_groups'
        account_id = 'account_id'
        account_status = 'account_status'
        age = 'age'
        agency_client_declaration = 'agency_client_declaration'
        amount_spent = 'amount_spent'
        balance = 'balance'
        business = 'business'
        business_city = 'business_city'
        business_country_code = 'business_country_code'
        business_name = 'business_name'
        business_state = 'business_state'
        business_street = 'business_street'
        business_street2 = 'business_street2'
        business_zip = 'business_zip'
        can_create_brand_lift_study = 'can_create_brand_lift_study'
        capabilities = 'capabilities'
        created_time = 'created_time'
        currency = 'currency'
        disable_reason = 'disable_reason'
        end_advertiser = 'end_advertiser'
        end_advertiser_name = 'end_advertiser_name'
        failed_delivery_checks = 'failed_delivery_checks'
        funding_source = 'funding_source'
        funding_source_details = 'funding_source_details'
        has_migrated_permissions = 'has_migrated_permissions'
        id = 'id'
        io_number = 'io_number'
        is_notifications_enabled = 'is_notifications_enabled'
        is_personal = 'is_personal'
        is_prepay_account = 'is_prepay_account'
        is_tax_id_required = 'is_tax_id_required'
        last_used_time = 'last_used_time'
        line_numbers = 'line_numbers'
        media_agency = 'media_agency'
        min_campaign_group_spend_cap = 'min_campaign_group_spend_cap'
        min_daily_budget = 'min_daily_budget'
        name = 'name'
        offsite_pixels_tos_accepted = 'offsite_pixels_tos_accepted'
        owner = 'owner'
        owner_business = 'owner_business'
        partner = 'partner'
        rf_spec = 'rf_spec'
        spend_cap = 'spend_cap'
        tax_id = 'tax_id'
        tax_id_status = 'tax_id_status'
        tax_id_type = 'tax_id_type'
        timezone_id = 'timezone_id'
        timezone_name = 'timezone_name'
        timezone_offset_hours_utc = 'timezone_offset_hours_utc'
        tos_accepted = 'tos_accepted'
        user_role = 'user_role'

    class AccessType:
        owner = 'OWNER'
        agency = 'AGENCY'

    class PermittedRoles:
        admin = 'ADMIN'
        general_user = 'GENERAL_USER'
        reports_only = 'REPORTS_ONLY'
        instagram_advertiser = 'INSTAGRAM_ADVERTISER'
        instagram_manager = 'INSTAGRAM_MANAGER'
        fb_employee_dso_advertiser = 'FB_EMPLOYEE_DSO_ADVERTISER'

    @classmethod
    def get_endpoint(cls):
        return 'adaccounts'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
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
            target_class=AdAccount,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'agency_client_declaration': 'map',
            'business_info': 'map',
            'default_dataset': 'Object',
            'end_advertiser': 'string',
            'id': 'string',
            'is_notifications_enabled': 'bool',
            'media_agency': 'string',
            'name': 'string',
            'partner': 'string',
            'redownload': 'bool',
            'spend_cap': 'float',
            'spend_cap_action': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

        return request if pending else request.execute()

    def get_activities(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adactivity import AdActivity
        self.assure_call()
        param_types = {
            'add_children': 'bool',
            'after': 'string',
            'business_id': 'string',
            'category': 'category_enum',
            'extra_oids': 'list<string>',
            'limit': 'int',
            'oid': 'string',
            'since': 'datetime',
            'uid': 'int',
            'until': 'datetime',
        }
        enums = {
            'category_enum': AdActivity.Category.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/activities',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdActivity,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdActivity),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_place_page_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adplacepageset import AdPlacePageSet
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ad_place_page_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPlacePageSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPlacePageSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_place_page_set(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adplacepageset import AdPlacePageSet
        self.assure_call()
        param_types = {
            'id': 'string',
            'name': 'string',
            'parent_page': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/ad_place_page_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPlacePageSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPlacePageSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_creatives(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adcreative import AdCreative
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adcreatives',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdCreative),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_creative(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adcreative import AdCreative
        self.assure_call()
        param_types = {
            'action_spec': 'list<unsigned int>',
            'actor_id': 'unsigned int',
            'actor_image_hash': 'string',
            'actor_image_url': 'string',
            'actor_name': 'string',
            'adlabels': 'list<Object>',
            'applink_treatment': 'applink_treatment_enum',
            'body': 'string',
            'call_to_action': 'Object',
            'dynamic_ad_voice': 'dynamic_ad_voice_enum',
            'follow_redirect': 'bool',
            'id': 'string',
            'image_crops': 'map',
            'image_file': 'string',
            'image_hash': 'string',
            'image_url': 'string',
            'instagram_actor_id': 'string',
            'instagram_permalink_url': 'string',
            'link_og_id': 'string',
            'link_url': 'string',
            'name': 'string',
            'object_id': 'unsigned int',
            'object_instagram_id': 'unsigned int',
            'object_story_id': 'string',
            'object_story_spec': 'AdCreativeObjectStorySpec',
            'object_type': 'string',
            'object_url': 'string',
            'place_page_set_id': 'string',
            'platform_customizations': 'Object',
            'product_set_id': 'string',
            'template_url': 'string',
            'thumbnail_url': 'string',
            'title': 'string',
            'url_tags': 'string',
            'video_id': 'unsigned int',
        }
        enums = {
            'applink_treatment_enum': AdCreative.ApplinkTreatment.__dict__.values(),
            'dynamic_ad_voice_enum': AdCreative.DynamicAdVoice.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adcreatives',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdCreative),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_creatives_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adcreative import AdCreative
        self.assure_call()
        param_types = {
            'ad_label_ids': 'list<string>',
            'operator': 'operator_enum',
        }
        enums = {
            'operator_enum': AdCreative.Operator.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adcreativesbylabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCreative,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdCreative),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def delete_ad_images(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adimage import AdImage
        self.assure_call()
        param_types = {
            'hash': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adimages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdImage,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdImage),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_images(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adimage import AdImage
        self.assure_call()
        param_types = {
            'hashes': 'list<string>',
            'minheight': 'unsigned int',
            'minwidth': 'unsigned int',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adimages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdImage,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdImage),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_image(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adimage import AdImage
        self.assure_call()
        param_types = {
            'bytes': 'string',
            'copy_from': 'Object',
            'zipbytes': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adimages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdImage,
            api_type='EDGE',
            allow_file_upload=True,
            response_parser=ObjectParser(target_class=AdImage),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adlabel import AdLabel
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdLabel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdLabel),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_label(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adlabel import AdLabel
        self.assure_call()
        param_types = {
            'id': 'string',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdLabel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdLabel),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_report_runs(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adreportrun import AdReportRun
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adreportruns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdReportRun,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdReportRun),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_report_schedules(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adreportschedules',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ads(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.ad import Ad
        self.assure_call()
        param_types = {
            'ad_draft_id': 'string',
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<string>',
            'include_deleted': 'bool',
            'time_range': 'map',
            'updated_since': 'int',
        }
        enums = {
            'date_preset_enum': Ad.DatePreset.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Ad,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Ad),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.ad import Ad
        self.assure_call()
        param_types = {
            'adlabels': 'list<Object>',
            'adset_id': 'unsigned int',
            'bid_amount': 'int',
            'creative': 'AdCreative',
            'date_format': 'string',
            'display_sequence': 'unsigned int',
            'execution_options': 'list<execution_options_enum>',
            'name': 'string',
            'redownload': 'bool',
            'status': 'status_enum',
            'tracking_specs': 'Object',
        }
        enums = {
            'execution_options_enum': Ad.ExecutionOptions.__dict__.values(),
            'status_enum': Ad.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/ads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Ad,
            api_type='EDGE',
            allow_file_upload=True,
            response_parser=ObjectParser(target_class=Ad),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ads_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.ad import Ad
        self.assure_call()
        param_types = {
            'ad_label_ids': 'list<string>',
            'operator': 'operator_enum',
        }
        enums = {
            'operator_enum': Ad.Operator.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adsbylabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Ad,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Ad),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adset import AdSet
        self.assure_call()
        param_types = {
            'ad_draft_id': 'string',
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<effective_status_enum>',
            'include_deleted': 'bool',
            'is_completed': 'bool',
            'time_range': 'map',
        }
        enums = {
            'date_preset_enum': AdSet.DatePreset.__dict__.values(),
            'effective_status_enum': AdSet.EffectiveStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adsets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_set(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adset import AdSet
        self.assure_call()
        param_types = {
            'adlabels': 'list<Object>',
            'adset_schedule': 'list<Object>',
            'bid_amount': 'int',
            'billing_event': 'billing_event_enum',
            'campaign_id': 'string',
            'creative_sequence': 'list<string>',
            'daily_budget': 'unsigned int',
            'daily_imps': 'unsigned int',
            'end_time': 'datetime',
            'execution_options': 'list<execution_options_enum>',
            'frequency_control_specs': 'list<Object>',
            'is_autobid': 'bool',
            'lifetime_budget': 'unsigned int',
            'lifetime_imps': 'unsigned int',
            'name': 'string',
            'optimization_goal': 'optimization_goal_enum',
            'pacing_type': 'list<string>',
            'promoted_object': 'Object',
            'redownload': 'bool',
            'rf_prediction_id': 'string',
            'rtb_flag': 'bool',
            'start_time': 'datetime',
            'status': 'status_enum',
            'targeting': 'Targeting',
        }
        enums = {
            'billing_event_enum': AdSet.BillingEvent.__dict__.values(),
            'execution_options_enum': AdSet.ExecutionOptions.__dict__.values(),
            'optimization_goal_enum': AdSet.OptimizationGoal.__dict__.values(),
            'status_enum': AdSet.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adsets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_sets_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adset import AdSet
        self.assure_call()
        param_types = {
            'ad_label_ids': 'list<string>',
            'operator': 'operator_enum',
        }
        enums = {
            'operator_enum': AdSet.Operator.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adsetsbylabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ads_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adspixel import AdsPixel
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adspixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ads_pixel(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adspixel import AdsPixel
        self.assure_call()
        param_types = {
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adspixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsPixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsPixel),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_advertisable_applications(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'app_id': 'string',
            'business_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/advertisable_applications',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_ad_videos(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/advideos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_ad_video(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.video import Video
        self.assure_call()
        param_types = {
            'composer_session_id': 'string',
            'description': 'string',
            'file_size': 'unsigned int',
            'file_url': 'string',
            'id': 'string',
            'is_explicit_share': 'bool',
            'manual_privacy': 'bool',
            'name': 'string',
            'og_action_type_id': 'string',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_suggestion_mechanism': 'string',
            'overwrite_id': 'string',
            'slideshow_spec': 'map',
            'start_offset': 'unsigned int',
            'time_since_original_post': 'unsigned int',
            'title': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'upload_phase': 'upload_phase_enum',
            'upload_session_id': 'string',
            'video_file_chunk': 'string',
        }
        enums = {
            'unpublished_content_type_enum': [
                'SCHEDULED',
                'DRAFT',
                'ADS_POST',
            ],
            'upload_phase_enum': [
                'start',
                'transfer',
                'finish',
                'cancel',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/advideos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            allow_file_upload=True,
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_applications(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/applications',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_async_ad_request_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adasyncrequestset import AdAsyncRequestSet
        self.assure_call()
        param_types = {
            'is_completed': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/asyncadrequestsets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAsyncRequestSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAsyncRequestSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_async_ad_request_set(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adasyncrequestset import AdAsyncRequestSet
        self.assure_call()
        param_types = {
            'ad_specs': 'list<map>',
            'id': 'string',
            'name': 'string',
            'notification_mode': 'notification_mode_enum',
            'notification_uri': 'string',
        }
        enums = {
            'notification_mode_enum': [
                'OFF',
                'ON_COMPLETE',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/asyncadrequestsets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAsyncRequestSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAsyncRequestSet),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_broad_targeting_categories(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.broadtargetingcategories import BroadTargetingCategories
        self.assure_call()
        param_types = {
            'custom_categories_only': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/broadtargetingcategories',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BroadTargetingCategories,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BroadTargetingCategories),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def delete_campaigns(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.campaign import Campaign
        self.assure_call()
        param_types = {
            'before_date': 'datetime',
            'delete_strategy': 'delete_strategy_enum',
            'id': 'string',
            'object_count': 'int',
        }
        enums = {
            'delete_strategy_enum': Campaign.DeleteStrategy.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/campaigns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_campaigns(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.campaign import Campaign
        self.assure_call()
        param_types = {
            'ad_draft_id': 'string',
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<effective_status_enum>',
            'is_completed': 'bool',
            'time_range': 'map',
        }
        enums = {
            'date_preset_enum': Campaign.DatePreset.__dict__.values(),
            'effective_status_enum': Campaign.EffectiveStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/campaigns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_campaign(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.campaign import Campaign
        self.assure_call()
        param_types = {
            'adlabels': 'list<Object>',
            'buying_type': 'string',
            'execution_options': 'list<execution_options_enum>',
            'name': 'string',
            'objective': 'objective_enum',
            'promoted_object': 'Object',
            'spend_cap': 'unsigned int',
            'status': 'status_enum',
        }
        enums = {
            'execution_options_enum': Campaign.ExecutionOptions.__dict__.values(),
            'objective_enum': Campaign.Objective.__dict__.values(),
            'status_enum': Campaign.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/campaigns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_campaigns_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.campaign import Campaign
        self.assure_call()
        param_types = {
            'ad_label_ids': 'list<string>',
            'operator': 'operator_enum',
        }
        enums = {
            'operator_enum': Campaign.Operator.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/campaignsbylabels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_custom_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.customaudience import CustomAudience
        self.assure_call()
        param_types = {
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'pixel_id': 'string',
        }
        enums = {
            'fields_enum': CustomAudience.Fields.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/customaudiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudience),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_custom_audience(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.customaudience import CustomAudience
        self.assure_call()
        param_types = {
            'content_type': 'content_type_enum',
            'description': 'string',
            'exclusions': 'list<Object>',
            'id': 'string',
            'inclusions': 'list<Object>',
            'list_of_accounts': 'list<unsigned int>',
            'lookalike_spec': 'string',
            'name': 'string',
            'opt_out_link': 'string',
            'origin_audience_id': 'string',
            'pixel_id': 'unsigned int',
            'prefill': 'bool',
            'product_set_id': 'string',
            'retention_days': 'unsigned int',
            'rule': 'string',
            'subtype': 'subtype_enum',
        }
        enums = {
            'content_type_enum': CustomAudience.ContentType.__dict__.values(),
            'subtype_enum': CustomAudience.Subtype.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/customaudiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudience),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_custom_audiences_tos(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.customaudiencestos import CustomAudiencesTOS
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/customaudiencestos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudiencesTOS,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudiencesTOS),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_custom_conversion(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.customconversion import CustomConversion
        self.assure_call()
        param_types = {
            'custom_event_type': 'custom_event_type_enum',
            'default_conversion_value': 'float',
            'description': 'string',
            'id': 'string',
            'name': 'string',
            'pixel_id': 'string',
            'pixel_rule': 'string',
        }
        enums = {
            'custom_event_type_enum': CustomConversion.CustomEventType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/customconversions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_generate_previews(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adpreview import AdPreview
        self.assure_call()
        param_types = {
            'ad_format': 'ad_format_enum',
            'creative': 'AdCreative',
            'height': 'unsigned int',
            'locale': 'string',
            'post': 'Object',
            'product_item_ids': 'list<int>',
            'width': 'unsigned int',
        }
        enums = {
            'ad_format_enum': AdPreview.AdFormat.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/generatepreviews',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPreview,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPreview),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_insights(self, fields=None, params=None, async=False, batch=None, pending=False):
        from facebookads.adobjects.adsinsights import AdsInsights
        if async:
          return self.get_insights_async(fields, params, batch, pending)
        self.assure_call()
        param_types = {
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'default_summary': 'bool',
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'sort': 'list<string>',
            'summary': 'list<summary_enum>',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'map',
            'time_ranges': 'list<map>',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'summary_enum': AdsInsights.Summary.__dict__.values(),
            'level_enum': AdsInsights.Level.__dict__.values(),
            'summary_action_breakdowns_enum': AdsInsights.SummaryActionBreakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsInsights,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsInsights),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_insights_async(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adreportrun import AdReportRun
        from facebookads.adobjects.adsinsights import AdsInsights
        self.assure_call()
        param_types = {
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'default_summary': 'bool',
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'sort': 'list<string>',
            'summary': 'list<summary_enum>',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'map',
            'time_ranges': 'list<map>',
        }
        enums = {
            'action_attribution_windows_enum': AdsInsights.ActionAttributionWindows.__dict__.values(),
            'action_breakdowns_enum': AdsInsights.ActionBreakdowns.__dict__.values(),
            'action_report_time_enum': AdsInsights.ActionReportTime.__dict__.values(),
            'breakdowns_enum': AdsInsights.Breakdowns.__dict__.values(),
            'date_preset_enum': AdsInsights.DatePreset.__dict__.values(),
            'summary_enum': AdsInsights.Summary.__dict__.values(),
            'level_enum': AdsInsights.Level.__dict__.values(),
            'summary_action_breakdowns_enum': AdsInsights.SummaryActionBreakdowns.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdReportRun,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdReportRun),
            include_summary=False,
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_instagram_accounts(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/instagram_accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_lead_gen_forms(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.leadgenform import LeadgenForm
        self.assure_call()
        param_types = {
            'query': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/leadgen_forms',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LeadgenForm,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LeadgenForm),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_minimum_budgets(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.minimumbudget import MinimumBudget
        self.assure_call()
        param_types = {
            'bid_amount': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/minimum_budgets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=MinimumBudget,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=MinimumBudget),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_offline_conversion_data_sets(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/offline_conversion_data_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_offline_conversion(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'event': 'string',
            'id': 'string',
            'payload': 'list<Object>',
            'pixel_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/offlineconversions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_offsite_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.offsitepixel import OffsitePixel
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/offsitepixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OffsitePixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OffsitePixel),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_offsite_pixel(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.offsitepixel import OffsitePixel
        self.assure_call()
        param_types = {
            'id': 'string',
            'name': 'string',
            'tag': 'tag_enum',
        }
        enums = {
            'tag_enum': OffsitePixel.Tag.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/offsitepixels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OffsitePixel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OffsitePixel),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_partner_categories(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.partnercategory import PartnerCategory
        self.assure_call()
        param_types = {
            'hide_pc': 'bool',
            'private_or_public': 'string',
            'targeting_type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/partnercategories',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PartnerCategory,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PartnerCategory),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_partners(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adsdatapartner import AdsDataPartner
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/partners',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdsDataPartner,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdsDataPartner),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_product_audience(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'associated_audience_id': 'unsigned int',
            'content_type': 'content_type_enum',
            'creation_params': 'map',
            'description': 'string',
            'exclusions': 'list<Object>',
            'id': 'string',
            'inclusions': 'list<Object>',
            'name': 'string',
            'opt_out_link': 'string',
            'parent_audience_id': 'unsigned int',
            'product_set_id': 'string',
            'subtype': 'subtype_enum',
            'tags': 'list<string>',
        }
        enums = {
            'content_type_enum': [
                'HOTEL',
                'FLIGHT',
            ],
            'subtype_enum': [
                'CUSTOM',
                'WEBSITE',
                'APP',
                'CLAIM',
                'PARTNER',
                'MANAGED',
                'VIDEO',
                'LOOKALIKE',
                'ENGAGEMENT',
                'DATA_SET',
                'BAG_OF_ACCOUNTS',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/product_audiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_publisher_block_lists(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/publisher_block_lists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_publisher_block_list(self, fields=None, params=None, batch=None, pending=False):
        self.assure_call()
        param_types = {
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/publisher_block_lists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_rate_card(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.ratecard import RateCard
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ratecard',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=RateCard,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=RateCard),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_reach_estimate(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.reachestimate import ReachEstimate
        self.assure_call()
        param_types = {
            'currency': 'string',
            'daily_budget': 'float',
            'object_store_url': 'string',
            'optimize_for': 'optimize_for_enum',
            'targeting_spec': 'Targeting',
        }
        enums = {
            'optimize_for_enum': ReachEstimate.OptimizeFor.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reachestimate',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ReachEstimate,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ReachEstimate),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_reach_frequency_predictions(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reachfrequencypredictions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ReachFrequencyPrediction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ReachFrequencyPrediction),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def create_reach_frequency_prediction(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
        self.assure_call()
        param_types = {
            'budget': 'unsigned int',
            'campaign_group_id': 'string',
            'destination_id': 'unsigned int',
            'destination_ids': 'list<string>',
            'end_time': 'unsigned int',
            'frequency_cap': 'unsigned int',
            'interval_frequency_cap_reset_period': 'unsigned int',
            'num_curve_points': 'unsigned int',
            'objective': 'string',
            'prediction_mode': 'unsigned int',
            'reach': 'unsigned int',
            'rf_prediction_id_to_share': 'string',
            'start_time': 'unsigned int',
            'stop_time': 'unsigned int',
            'story_event_type': 'unsigned int',
            'target_spec': 'Targeting',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/reachfrequencypredictions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ReachFrequencyPrediction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ReachFrequencyPrediction),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_roas(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccountroas import AdAccountRoas
        self.assure_call()
        param_types = {
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'time_increment': 'string',
            'time_range': 'Object',
        }
        enums = {
            'fields_enum': AdAccountRoas.Fields.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/roas',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountRoas,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountRoas),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_targeting_insights(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccounttargetinginsights import AdAccountTargetingInsights
        self.assure_call()
        param_types = {
            'mode': 'mode_enum',
            'objective': 'objective_enum',
            'rank_mode': 'rank_mode_enum',
        }
        enums = {
            'mode_enum': AdAccountTargetingInsights.Mode.__dict__.values(),
            'objective_enum': AdAccountTargetingInsights.Objective.__dict__.values(),
            'rank_mode_enum': AdAccountTargetingInsights.RankMode.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetinginsights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountTargetingInsights,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountTargetingInsights),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_targeting_sentence_lines(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.targetingsentenceline import TargetingSentenceLine
        self.assure_call()
        param_types = {
            'discard_ages': 'bool',
            'discard_placements': 'bool',
            'targeting_spec': 'Targeting',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetingsentencelines',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=TargetingSentenceLine,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=TargetingSentenceLine),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_transactions(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.transaction import Transaction
        self.assure_call()
        param_types = {
            'time_start': 'int',
            'time_stop': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/transactions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Transaction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Transaction),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    def get_users(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccountuser import AdAccountUser
        self.assure_call()
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountUser),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request

        return request if pending else request.execute()

    _field_types = {
        'account_groups': 'list<AdAccountGroupResult>',
        'account_id': 'string',
        'account_status': 'unsigned int',
        'age': 'float',
        'agency_client_declaration': 'AgencyClientDeclaration',
        'amount_spent': 'string',
        'balance': 'string',
        'business': 'Business',
        'business_city': 'string',
        'business_country_code': 'string',
        'business_name': 'string',
        'business_state': 'string',
        'business_street': 'string',
        'business_street2': 'string',
        'business_zip': 'string',
        'can_create_brand_lift_study': 'bool',
        'capabilities': 'list<string>',
        'created_time': 'datetime',
        'currency': 'string',
        'disable_reason': 'unsigned int',
        'end_advertiser': 'string',
        'end_advertiser_name': 'string',
        'failed_delivery_checks': 'list<DeliveryCheck>',
        'funding_source': 'string',
        'funding_source_details': 'FundingSourceDetails',
        'has_migrated_permissions': 'bool',
        'id': 'string',
        'io_number': 'string',
        'is_notifications_enabled': 'bool',
        'is_personal': 'unsigned int',
        'is_prepay_account': 'bool',
        'is_tax_id_required': 'bool',
        'last_used_time': 'datetime',
        'line_numbers': 'list<int>',
        'media_agency': 'string',
        'min_campaign_group_spend_cap': 'string',
        'min_daily_budget': 'unsigned int',
        'name': 'string',
        'offsite_pixels_tos_accepted': 'bool',
        'owner': 'string',
        'owner_business': 'Business',
        'partner': 'string',
        'rf_spec': 'ReachFrequencySpec',
        'spend_cap': 'string',
        'tax_id': 'string',
        'tax_id_status': 'unsigned int',
        'tax_id_type': 'string',
        'timezone_id': 'unsigned int',
        'timezone_name': 'string',
        'timezone_offset_hours_utc': 'float',
        'tos_accepted': 'map<string, int>',
        'user_role': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AccessType'] = AdAccount.AccessType.__dict__.values()
        field_enum_info['PermittedRoles'] = AdAccount.PermittedRoles.__dict__.values()
        return field_enum_info
