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
from facebook_business.adobjects.helpers.adaccountmixin import AdAccountMixin
from facebook_business.mixins import HasAdLabels

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAccount(
    AdAccountMixin,
    AbstractCrudObject,
    HasAdLabels,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccount = True
        super(AdAccount, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        account_status = 'account_status'
        age = 'age'
        agency_client_declaration = 'agency_client_declaration'
        amount_spent = 'amount_spent'
        attribution_spec = 'attribution_spec'
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
        extended_credit_invoice_group = 'extended_credit_invoice_group'
        failed_delivery_checks = 'failed_delivery_checks'
        funding_source = 'funding_source'
        funding_source_details = 'funding_source_details'
        has_migrated_permissions = 'has_migrated_permissions'
        has_page_authorized_adaccount = 'has_page_authorized_adaccount'
        id = 'id'
        io_number = 'io_number'
        is_attribution_spec_system_default = 'is_attribution_spec_system_default'
        is_direct_deals_enabled = 'is_direct_deals_enabled'
        is_in_middle_of_local_entity_migration = 'is_in_middle_of_local_entity_migration'
        is_notifications_enabled = 'is_notifications_enabled'
        is_personal = 'is_personal'
        is_prepay_account = 'is_prepay_account'
        is_tax_id_required = 'is_tax_id_required'
        line_numbers = 'line_numbers'
        media_agency = 'media_agency'
        min_campaign_group_spend_cap = 'min_campaign_group_spend_cap'
        min_daily_budget = 'min_daily_budget'
        name = 'name'
        offsite_pixels_tos_accepted = 'offsite_pixels_tos_accepted'
        owner = 'owner'
        partner = 'partner'
        rate_limit_reset_time = 'rate_limit_reset_time'
        rf_spec = 'rf_spec'
        show_checkout_experience = 'show_checkout_experience'
        spend_cap = 'spend_cap'
        tax_id = 'tax_id'
        tax_id_status = 'tax_id_status'
        tax_id_type = 'tax_id_type'
        timezone_id = 'timezone_id'
        timezone_name = 'timezone_name'
        timezone_offset_hours_utc = 'timezone_offset_hours_utc'
        tos_accepted = 'tos_accepted'
        user_role = 'user_role'
        user_tos_accepted = 'user_tos_accepted'

    class PermittedTasks:
        manage = 'MANAGE'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class Tasks:
        manage = 'MANAGE'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class Subtype:
        custom = 'CUSTOM'
        website = 'WEBSITE'
        app = 'APP'
        offline_conversion = 'OFFLINE_CONVERSION'
        claim = 'CLAIM'
        partner = 'PARTNER'
        managed = 'MANAGED'
        video = 'VIDEO'
        lookalike = 'LOOKALIKE'
        engagement = 'ENGAGEMENT'
        data_set = 'DATA_SET'
        bag_of_accounts = 'BAG_OF_ACCOUNTS'
        study_rule_audience = 'STUDY_RULE_AUDIENCE'
        fox = 'FOX'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adaccounts'

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
            target_class=AdAccount,
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
            'agency_client_declaration': 'map',
            'attribution_spec': 'list<Object>',
            'business_info': 'map',
            'end_advertiser': 'string',
            'is_notifications_enabled': 'bool',
            'media_agency': 'string',
            'name': 'string',
            'partner': 'string',
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
            target_class=AdAccount,
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

    def get_activities(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adactivity import AdActivity
        param_types = {
            'add_children': 'bool',
            'business_id': 'string',
            'category': 'category_enum',
            'extra_oids': 'list<string>',
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
            response_parser=ObjectParser(target_class=AdActivity, api=self._api),
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

    def get_ad_place_page_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adplacepageset import AdPlacePageSet
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
            response_parser=ObjectParser(target_class=AdPlacePageSet, api=self._api),
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

    def create_ad_place_page_set(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adplacepageset import AdPlacePageSet
        param_types = {
            'location_types': 'list<location_types_enum>',
            'name': 'string',
            'parent_page': 'string',
        }
        enums = {
            'location_types_enum': AdPlacePageSet.LocationTypes.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/ad_place_page_sets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdPlacePageSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdPlacePageSet, api=self._api),
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

    def get_ad_asset_feeds(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adasset_feeds',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_ad_creatives(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adcreative import AdCreative
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
            response_parser=ObjectParser(target_class=AdCreative, api=self._api),
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

    def create_ad_creative(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adcreative import AdCreative
        param_types = {
            'adlabels': 'list<Object>',
            'applink_treatment': 'applink_treatment_enum',
            'authorization_category': 'authorization_category_enum',
            'body': 'string',
            'branded_content_sponsor_page_id': 'string',
            'dynamic_ad_voice': 'dynamic_ad_voice_enum',
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
            'object_story_id': 'string',
            'object_story_spec': 'AdCreativeObjectStorySpec',
            'object_type': 'string',
            'platform_customizations': 'Object',
            'product_set_id': 'string',
            'recommender_settings': 'map',
            'template_url': 'string',
            'template_url_spec': 'Object',
            'thumbnail_url': 'string',
            'title': 'string',
            'url_tags': 'string',
            'use_page_actor_override': 'bool',
        }
        enums = {
            'applink_treatment_enum': AdCreative.ApplinkTreatment.__dict__.values(),
            'authorization_category_enum': AdCreative.AuthorizationCategory.__dict__.values(),
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
            response_parser=ObjectParser(target_class=AdCreative, api=self._api),
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

    def get_ad_creatives_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adcreative import AdCreative
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
            response_parser=ObjectParser(target_class=AdCreative, api=self._api),
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

    def delete_ad_images(self, fields=None, params=None, batch=None, pending=False):
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
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_ad_images(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adimage import AdImage
        param_types = {
            'biz_tag_id': 'unsigned int',
            'business_id': 'string',
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
            response_parser=ObjectParser(target_class=AdImage, api=self._api),
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

    def create_ad_image(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adimage import AdImage
        param_types = {
            'bytes': 'Object',
            'copy_from': 'Object',
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
            response_parser=ObjectParser(target_class=AdImage, api=self._api),
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

    def get_ad_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adlabel import AdLabel
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
            response_parser=ObjectParser(target_class=AdLabel, api=self._api),
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

    def create_ad_label(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adlabel import AdLabel
        param_types = {
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
            response_parser=ObjectParser(target_class=AdLabel, api=self._api),
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

    def create_ad_language_asset(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'bodies': 'list<Object>',
            'call_to_action_type': 'call_to_action_type_enum',
            'default_language': 'string',
            'descriptions': 'list<Object>',
            'image': 'Object',
            'link_urls': 'list<Object>',
            'titles': 'list<Object>',
            'video': 'Object',
        }
        enums = {
            'call_to_action_type_enum': [
                'OPEN_LINK',
                'LIKE_PAGE',
                'SHOP_NOW',
                'PLAY_GAME',
                'INSTALL_APP',
                'USE_APP',
                'CALL',
                'CALL_ME',
                'INSTALL_MOBILE_APP',
                'USE_MOBILE_APP',
                'MOBILE_DOWNLOAD',
                'BOOK_TRAVEL',
                'LISTEN_MUSIC',
                'WATCH_VIDEO',
                'LEARN_MORE',
                'SIGN_UP',
                'DOWNLOAD',
                'WATCH_MORE',
                'NO_BUTTON',
                'VISIT_PAGES_FEED',
                'APPLY_NOW',
                'BUY_NOW',
                'GET_OFFER',
                'GET_OFFER_VIEW',
                'BUY_TICKETS',
                'UPDATE_APP',
                'GET_DIRECTIONS',
                'BUY',
                'MESSAGE_PAGE',
                'DONATE',
                'SUBSCRIBE',
                'SAY_THANKS',
                'SELL_NOW',
                'SHARE',
                'DONATE_NOW',
                'GET_QUOTE',
                'CONTACT_US',
                'ORDER_NOW',
                'ADD_TO_CART',
                'VIDEO_ANNOTATION',
                'MOMENTS',
                'RECORD_NOW',
                'GET_SHOWTIMES',
                'LISTEN_NOW',
                'EVENT_RSVP',
                'WHATSAPP_MESSAGE',
                'FOLLOW_NEWS_STORYLINE',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlanguage_assets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_ad_report_runs(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adreportrun import AdReportRun
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
            response_parser=ObjectParser(target_class=AdReportRun, api=self._api),
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

    def get_ad_report_schedules(self, fields=None, params=None, batch=None, pending=False):
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_ad_rules_history(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountadruleshistory import AdAccountAdRulesHistory
        param_types = {
            'action': 'action_enum',
            'hide_no_changes': 'bool',
            'object_id': 'string',
        }
        enums = {
            'action_enum': AdAccountAdRulesHistory.Action.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adrules_history',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountAdRulesHistory,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountAdRulesHistory, api=self._api),
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

    def create_ad_rules_library(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adrule import AdRule
        param_types = {
            'account_id': 'string',
            'evaluation_spec': 'Object',
            'execution_spec': 'Object',
            'name': 'string',
            'schedule_spec': 'Object',
            'status': 'status_enum',
        }
        enums = {
            'status_enum': AdRule.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adrules_library',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdRule,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdRule, api=self._api),
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

    def get_ads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.ad import Ad
        param_types = {
            'ad_draft_id': 'string',
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<string>',
            'time_range': 'Object',
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
            response_parser=ObjectParser(target_class=Ad, api=self._api),
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

    def create_ad(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.ad import Ad
        param_types = {
            'adlabels': 'list<Object>',
            'adset_id': 'unsigned int',
            'adset_spec': 'AdSet',
            'bid_amount': 'int',
            'creative': 'AdCreative',
            'date_format': 'string',
            'display_sequence': 'unsigned int',
            'execution_options': 'list<execution_options_enum>',
            'name': 'string',
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
            response_parser=ObjectParser(target_class=Ad, api=self._api),
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

    def get_ads_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.ad import Ad
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
            response_parser=ObjectParser(target_class=Ad, api=self._api),
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

    def get_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adset import AdSet
        param_types = {
            'ad_draft_id': 'string',
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<effective_status_enum>',
            'is_completed': 'bool',
            'time_range': 'Object',
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
            response_parser=ObjectParser(target_class=AdSet, api=self._api),
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

    def create_ad_set(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adset import AdSet
        param_types = {
            'adlabels': 'list<Object>',
            'adset_schedule': 'list<Object>',
            'attribution_spec': 'list<map>',
            'bid_amount': 'int',
            'bid_strategy': 'bid_strategy_enum',
            'billing_event': 'billing_event_enum',
            'campaign_id': 'string',
            'campaign_spec': 'Object',
            'creative_sequence': 'list<string>',
            'daily_budget': 'unsigned int',
            'daily_imps': 'unsigned int',
            'daily_min_spend_target': 'unsigned int',
            'daily_spend_cap': 'unsigned int',
            'destination_type': 'destination_type_enum',
            'end_time': 'datetime',
            'execution_options': 'list<execution_options_enum>',
            'frequency_control_specs': 'list<Object>',
            'lifetime_budget': 'unsigned int',
            'lifetime_imps': 'unsigned int',
            'lifetime_min_spend_target': 'unsigned int',
            'lifetime_spend_cap': 'unsigned int',
            'name': 'string',
            'optimization_goal': 'optimization_goal_enum',
            'pacing_type': 'list<string>',
            'promoted_object': 'Object',
            'rf_prediction_id': 'string',
            'start_time': 'datetime',
            'status': 'status_enum',
            'targeting': 'Targeting',
            'time_based_ad_rotation_id_blocks': 'list<list<unsigned int>>',
            'time_based_ad_rotation_intervals': 'list<unsigned int>',
        }
        enums = {
            'bid_strategy_enum': AdSet.BidStrategy.__dict__.values(),
            'billing_event_enum': AdSet.BillingEvent.__dict__.values(),
            'destination_type_enum': AdSet.DestinationType.__dict__.values(),
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
            response_parser=ObjectParser(target_class=AdSet, api=self._api),
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

    def get_ad_sets_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adset import AdSet
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
            response_parser=ObjectParser(target_class=AdSet, api=self._api),
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

    def get_ads_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixel import AdsPixel
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
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
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

    def create_ads_pixel(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adspixel import AdsPixel
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
            response_parser=ObjectParser(target_class=AdsPixel, api=self._api),
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

    def get_advertisable_applications(self, fields=None, params=None, batch=None, pending=False):
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_ad_videos(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'max_aspect_ratio': 'float',
            'maxheight': 'unsigned int',
            'maxlength': 'unsigned int',
            'maxwidth': 'unsigned int',
            'min_aspect_ratio': 'float',
            'minheight': 'unsigned int',
            'minlength': 'unsigned int',
            'minwidth': 'unsigned int',
            'title': 'string',
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def create_ad_video(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'audio_story_wave_animation_handle': 'string',
            'composer_session_id': 'string',
            'description': 'string',
            'end_offset': 'unsigned int',
            'file_size': 'unsigned int',
            'file_url': 'string',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'is_explicit_share': 'bool',
            'manual_privacy': 'bool',
            'name': 'string',
            'og_action_type_id': 'string',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_suggestion_mechanism': 'string',
            'original_fov': 'unsigned int',
            'original_projection_type': 'original_projection_type_enum',
            'react_mode_metadata': 'string',
            'referenced_sticker_id': 'string',
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
            'original_projection_type_enum': [
                'equirectangular',
                'cubemap',
                'equiangular_cubemap',
                'half_equirectangular',
            ],
            'unpublished_content_type_enum': [
                'SCHEDULED',
                'DRAFT',
                'ADS_POST',
                'INLINE_CREATED',
                'PUBLISHED',
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def delete_agencies(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def create_agency(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
            'permitted_tasks': 'list<permitted_tasks_enum>',
        }
        enums = {
            'permitted_tasks_enum': AdAccount.PermittedTasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccount,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccount, api=self._api),
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

    def get_applications(self, fields=None, params=None, batch=None, pending=False):
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def delete_assigned_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/assigned_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_assigned_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.assigneduser import AssignedUser
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AssignedUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AssignedUser, api=self._api),
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

    def create_assigned_user(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tasks': 'list<tasks_enum>',
            'user': 'int',
        }
        enums = {
            'tasks_enum': AdAccount.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/assigned_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccount,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccount, api=self._api),
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

    def create_async_batch_request(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.campaign import Campaign
        param_types = {
            'adbatch': 'list<Object>',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/async_batch_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Campaign,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Campaign, api=self._api),
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

    def get_async_ad_request_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adasyncrequestset import AdAsyncRequestSet
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
            response_parser=ObjectParser(target_class=AdAsyncRequestSet, api=self._api),
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

    def create_async_ad_request_set(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adasyncrequestset import AdAsyncRequestSet
        param_types = {
            'ad_specs': 'list<map>',
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
            response_parser=ObjectParser(target_class=AdAsyncRequestSet, api=self._api),
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

    def create_audience_replace(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'payload': 'Object',
            'session': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/audiencereplace',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_broad_targeting_categories(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.broadtargetingcategories import BroadTargetingCategories
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
            response_parser=ObjectParser(target_class=BroadTargetingCategories, api=self._api),
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

    def delete_campaigns(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.campaign import Campaign
        param_types = {
            'before_date': 'datetime',
            'delete_strategy': 'delete_strategy_enum',
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
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_campaigns(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.campaign import Campaign
        param_types = {
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<effective_status_enum>',
            'is_completed': 'bool',
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
            response_parser=ObjectParser(target_class=Campaign, api=self._api),
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

    def create_campaign(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.campaign import Campaign
        param_types = {
            'adlabels': 'list<Object>',
            'bid_strategy': 'bid_strategy_enum',
            'budget_rebalance_flag': 'bool',
            'buying_type': 'string',
            'daily_budget': 'unsigned int',
            'execution_options': 'list<execution_options_enum>',
            'iterative_split_test_configs': 'list<Object>',
            'lifetime_budget': 'unsigned int',
            'name': 'string',
            'objective': 'objective_enum',
            'promoted_object': 'Object',
            'spend_cap': 'unsigned int',
            'status': 'status_enum',
        }
        enums = {
            'bid_strategy_enum': Campaign.BidStrategy.__dict__.values(),
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
            response_parser=ObjectParser(target_class=Campaign, api=self._api),
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

    def get_campaigns_by_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.campaign import Campaign
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
            response_parser=ObjectParser(target_class=Campaign, api=self._api),
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

    def get_custom_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudience import CustomAudience
        param_types = {
            'business_id': 'string',
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
            response_parser=ObjectParser(target_class=CustomAudience, api=self._api),
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

    def create_custom_audience(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudience import CustomAudience
        param_types = {
            'allowed_domains': 'list<string>',
            'claim_objective': 'claim_objective_enum',
            'content_type': 'content_type_enum',
            'customer_file_source': 'customer_file_source_enum',
            'dataset_id': 'string',
            'description': 'string',
            'event_source_group': 'string',
            'event_sources': 'list<map>',
            'is_value_based': 'bool',
            'list_of_accounts': 'list<unsigned int>',
            'lookalike_spec': 'string',
            'name': 'string',
            'opt_out_link': 'string',
            'origin_audience_id': 'string',
            'pixel_id': 'string',
            'prefill': 'bool',
            'product_set_id': 'string',
            'retention_days': 'unsigned int',
            'rule': 'string',
            'rule_aggregation': 'string',
            'subtype': 'subtype_enum',
        }
        enums = {
            'claim_objective_enum': CustomAudience.ClaimObjective.__dict__.values(),
            'content_type_enum': CustomAudience.ContentType.__dict__.values(),
            'customer_file_source_enum': CustomAudience.CustomerFileSource.__dict__.values(),
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
            response_parser=ObjectParser(target_class=CustomAudience, api=self._api),
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

    def get_custom_audiences_tos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudiencestos import CustomAudiencesTOS
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
            response_parser=ObjectParser(target_class=CustomAudiencesTOS, api=self._api),
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

    def create_custom_conversion(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
            'advanced_rule': 'string',
            'custom_event_type': 'custom_event_type_enum',
            'default_conversion_value': 'float',
            'description': 'string',
            'event_source_id': 'string',
            'name': 'string',
            'rule': 'string',
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
            target_class=CustomConversion,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomConversion, api=self._api),
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

    def get_delivery_estimate(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountdeliveryestimate import AdAccountDeliveryEstimate
        param_types = {
            'optimization_goal': 'optimization_goal_enum',
            'promoted_object': 'Object',
            'targeting_spec': 'Targeting',
        }
        enums = {
            'optimization_goal_enum': AdAccountDeliveryEstimate.OptimizationGoal.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/delivery_estimate',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountDeliveryEstimate,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountDeliveryEstimate, api=self._api),
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

    def get_generate_previews(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adpreview import AdPreview
        param_types = {
            'ad_format': 'ad_format_enum',
            'creative': 'AdCreative',
            'dynamic_creative_spec': 'Object',
            'end_date': 'datetime',
            'height': 'unsigned int',
            'place_page_id': 'int',
            'post': 'Object',
            'product_item_ids': 'list<string>',
            'start_date': 'datetime',
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
            response_parser=ObjectParser(target_class=AdPreview, api=self._api),
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
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'default_summary': 'bool',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'sort': 'list<string>',
            'summary': 'list<summary_enum>',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'Object',
            'time_ranges': 'list<Object>',
            'use_account_attribution_setting': 'bool',
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

    def get_insights_async(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adreportrun import AdReportRun
        from facebook_business.adobjects.adsinsights import AdsInsights
        param_types = {
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'default_summary': 'bool',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'fields': 'list<fields_enum>',
            'filtering': 'list<Object>',
            'level': 'level_enum',
            'product_id_limit': 'int',
            'sort': 'list<string>',
            'summary': 'list<summary_enum>',
            'summary_action_breakdowns': 'list<summary_action_breakdowns_enum>',
            'time_increment': 'string',
            'time_range': 'Object',
            'time_ranges': 'list<Object>',
            'use_account_attribution_setting': 'bool',
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
            response_parser=ObjectParser(target_class=AdReportRun, api=self._api),
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

    def get_instagram_accounts(self, fields=None, params=None, batch=None, pending=False):
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_lead_gen_forms(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.leadgenform import LeadgenForm
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
            response_parser=ObjectParser(target_class=LeadgenForm, api=self._api),
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

    def get_minimum_budgets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.minimumbudget import MinimumBudget
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
            response_parser=ObjectParser(target_class=MinimumBudget, api=self._api),
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

    def get_offline_conversion_data_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.offlineconversiondataset import OfflineConversionDataSet
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
            target_class=OfflineConversionDataSet,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OfflineConversionDataSet, api=self._api),
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

    def get_offsite_pixels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.offsitepixel import OffsitePixel
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
            response_parser=ObjectParser(target_class=OffsitePixel, api=self._api),
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

    def get_partner_categories(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.partnercategory import PartnerCategory
        param_types = {
            'hide_pc': 'bool',
            'is_exclusion': 'bool',
            'private_or_public': 'private_or_public_enum',
            'targeting_type': 'string',
        }
        enums = {
            'private_or_public_enum': PartnerCategory.PrivateOrPublic.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/partnercategories',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PartnerCategory,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PartnerCategory, api=self._api),
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

    def get_partners(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adsdatapartner import AdsDataPartner
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
            response_parser=ObjectParser(target_class=AdsDataPartner, api=self._api),
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

    def create_product_audience(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customaudience import CustomAudience
        param_types = {
            'associated_audience_id': 'unsigned int',
            'creation_params': 'map',
            'description': 'string',
            'event_sources': 'list<map>',
            'exclusions': 'list<Object>',
            'inclusions': 'list<Object>',
            'name': 'string',
            'opt_out_link': 'string',
            'parent_audience_id': 'unsigned int',
            'product_set_id': 'string',
            'subtype': 'subtype_enum',
            'tags': 'list<string>',
        }
        enums = {
            'subtype_enum': AdAccount.Subtype.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/product_audiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CustomAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CustomAudience, api=self._api),
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

    def get_publisher_block_lists(self, fields=None, params=None, batch=None, pending=False):
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def create_publisher_block_list(self, fields=None, params=None, batch=None, pending=False):
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
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_reach_estimate(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.reachestimate import ReachEstimate
        param_types = {
            'object_store_url': 'string',
            'targeting_spec': 'Targeting',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reachestimate',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ReachEstimate,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ReachEstimate, api=self._api),
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

    def get_reach_frequency_predictions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
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
            response_parser=ObjectParser(target_class=ReachFrequencyPrediction, api=self._api),
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

    def create_reach_frequency_prediction(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.reachfrequencyprediction import ReachFrequencyPrediction
        param_types = {
            'budget': 'unsigned int',
            'campaign_group_id': 'string',
            'day_parting_schedule': 'list<Object>',
            'destination_id': 'unsigned int',
            'destination_ids': 'list<string>',
            'end_time': 'unsigned int',
            'frequency_cap': 'unsigned int',
            'instream_packages': 'list<instream_packages_enum>',
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
            'instream_packages_enum': ReachFrequencyPrediction.InstreamPackages.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/reachfrequencypredictions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ReachFrequencyPrediction,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ReachFrequencyPrediction, api=self._api),
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

    def get_roas(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountroas import AdAccountRoas
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
            response_parser=ObjectParser(target_class=AdAccountRoas, api=self._api),
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

    def create_sponsored_message_ad(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'bid_amount': 'int',
            'daily_budget': 'unsigned int',
            'message_creative_id': 'string',
            'targeting': 'Targeting',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/sponsored_message_ads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_targeting_browse(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccounttargetingunified import AdAccountTargetingUnified
        param_types = {
            'include_nodes': 'bool',
            'limit_type': 'limit_type_enum',
        }
        enums = {
            'limit_type_enum': AdAccountTargetingUnified.LimitType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetingbrowse',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountTargetingUnified,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountTargetingUnified, api=self._api),
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

    def get_targeting_search(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccounttargetingunified import AdAccountTargetingUnified
        param_types = {
            'limit_type': 'limit_type_enum',
            'q': 'string',
        }
        enums = {
            'limit_type_enum': AdAccountTargetingUnified.LimitType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetingsearch',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountTargetingUnified,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountTargetingUnified, api=self._api),
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

    def get_targeting_sentence_lines(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.targetingsentenceline import TargetingSentenceLine
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
            response_parser=ObjectParser(target_class=TargetingSentenceLine, api=self._api),
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

    def get_targeting_suggestions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccounttargetingunified import AdAccountTargetingUnified
        param_types = {
            'limit_type': 'limit_type_enum',
            'targeting_list': 'list<Object>',
        }
        enums = {
            'limit_type_enum': AdAccountTargetingUnified.LimitType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetingsuggestions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountTargetingUnified,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountTargetingUnified, api=self._api),
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

    def get_targeting_validation(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccounttargetingunified import AdAccountTargetingUnified
        param_types = {
            'id_list': 'list<unsigned int>',
            'is_exclusion': 'bool',
            'name_list': 'list<string>',
            'targeting_list': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/targetingvalidation',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountTargetingUnified,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountTargetingUnified, api=self._api),
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

    def delete_tracking(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tracking_specs': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/tracking',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def create_tracking(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tracking_specs': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/tracking',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def delete_user_match(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'bidirectional': 'bool',
            'namespace': 'string',
            'payload': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/user_match',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def create_user_match(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'action': 'string',
            'bidirectional': 'bool',
            'namespace': 'string',
            'payload': 'Object',
            'retention': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/user_match',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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

    def get_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountuser import AdAccountUser
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
            response_parser=ObjectParser(target_class=AdAccountUser, api=self._api),
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
        'account_status': 'unsigned int',
        'age': 'float',
        'agency_client_declaration': 'AgencyClientDeclaration',
        'amount_spent': 'string',
        'attribution_spec': 'list<AttributionSpec>',
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
        'extended_credit_invoice_group': 'ExtendedCreditInvoiceGroup',
        'failed_delivery_checks': 'list<DeliveryCheck>',
        'funding_source': 'string',
        'funding_source_details': 'FundingSourceDetails',
        'has_migrated_permissions': 'bool',
        'has_page_authorized_adaccount': 'bool',
        'id': 'string',
        'io_number': 'string',
        'is_attribution_spec_system_default': 'bool',
        'is_direct_deals_enabled': 'bool',
        'is_in_middle_of_local_entity_migration': 'bool',
        'is_notifications_enabled': 'bool',
        'is_personal': 'unsigned int',
        'is_prepay_account': 'bool',
        'is_tax_id_required': 'bool',
        'line_numbers': 'list<int>',
        'media_agency': 'string',
        'min_campaign_group_spend_cap': 'string',
        'min_daily_budget': 'unsigned int',
        'name': 'string',
        'offsite_pixels_tos_accepted': 'bool',
        'owner': 'string',
        'partner': 'string',
        'rate_limit_reset_time': 'string',
        'rf_spec': 'ReachFrequencySpec',
        'show_checkout_experience': 'bool',
        'spend_cap': 'string',
        'tax_id': 'string',
        'tax_id_status': 'unsigned int',
        'tax_id_type': 'string',
        'timezone_id': 'unsigned int',
        'timezone_name': 'string',
        'timezone_offset_hours_utc': 'float',
        'tos_accepted': 'map<string, int>',
        'user_role': 'string',
        'user_tos_accepted': 'map<string, int>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['PermittedTasks'] = AdAccount.PermittedTasks.__dict__.values()
        field_enum_info['Tasks'] = AdAccount.Tasks.__dict__.values()
        field_enum_info['Subtype'] = AdAccount.Subtype.__dict__.values()
        return field_enum_info
