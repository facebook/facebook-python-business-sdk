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
        ad_account_creation_request = 'ad_account_creation_request'
        ad_account_promotable_objects = 'ad_account_promotable_objects'
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
        daily_spend_limit = 'daily_spend_limit'
        direct_deals_tos_accepted = 'direct_deals_tos_accepted'
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
        is_in_3ds_authorization_enabled_market = 'is_in_3ds_authorization_enabled_market'
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

    class Currency:
        aed = 'AED'
        ars = 'ARS'
        aud = 'AUD'
        bdt = 'BDT'
        bob = 'BOB'
        brl = 'BRL'
        cad = 'CAD'
        chf = 'CHF'
        clp = 'CLP'
        cny = 'CNY'
        cop = 'COP'
        crc = 'CRC'
        czk = 'CZK'
        dkk = 'DKK'
        dzd = 'DZD'
        egp = 'EGP'
        eur = 'EUR'
        gbp = 'GBP'
        gtq = 'GTQ'
        hkd = 'HKD'
        hnl = 'HNL'
        huf = 'HUF'
        idr = 'IDR'
        ils = 'ILS'
        inr = 'INR'
        isk = 'ISK'
        jpy = 'JPY'
        kes = 'KES'
        krw = 'KRW'
        mop = 'MOP'
        mxn = 'MXN'
        myr = 'MYR'
        ngn = 'NGN'
        nio = 'NIO'
        nok = 'NOK'
        nzd = 'NZD'
        pen = 'PEN'
        php = 'PHP'
        pkr = 'PKR'
        pln = 'PLN'
        pyg = 'PYG'
        qar = 'QAR'
        ron = 'RON'
        rub = 'RUB'
        sar = 'SAR'
        sek = 'SEK'
        sgd = 'SGD'
        thb = 'THB'
        value_try = 'TRY'
        twd = 'TWD'
        usd = 'USD'
        uyu = 'UYU'
        vef = 'VEF'
        vnd = 'VND'
        zar = 'ZAR'

    class PermittedTasks:
        manage = 'MANAGE'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class Tasks:
        manage = 'MANAGE'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class ClaimObjective:
        automotive_model = 'AUTOMOTIVE_MODEL'
        home_listing = 'HOME_LISTING'
        product = 'PRODUCT'
        travel = 'TRAVEL'
        vehicle = 'VEHICLE'
        vehicle_offer = 'VEHICLE_OFFER'

    class ContentType:
        automotive_model = 'AUTOMOTIVE_MODEL'
        destination = 'DESTINATION'
        flight = 'FLIGHT'
        home_listing = 'HOME_LISTING'
        hotel = 'HOTEL'
        media_title = 'MEDIA_TITLE'
        product = 'PRODUCT'
        vehicle = 'VEHICLE'
        vehicle_offer = 'VEHICLE_OFFER'

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
            'name': 'string',
            'spend_cap_action': 'string',
            'spend_cap': 'float',
            'agency_client_declaration': 'map',
            'business_info': 'map',
            'tos_accepted': 'map',
            'currency': 'currency_enum',
            'timezone_id': 'unsigned int',
            'end_advertiser': 'string',
            'media_agency': 'string',
            'partner': 'string',
            'is_notifications_enabled': 'bool',
            'attribution_spec': 'list<Object>',
        }
        enums = {
            'currency_enum': AdAccount.Currency.__dict__.values(),
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
            'after': 'string',
            'limit': 'int',
            'since': 'datetime',
            'category': 'category_enum',
            'until': 'datetime',
            'uid': 'int',
            'business_id': 'string',
            'oid': 'string',
            'extra_oids': 'list<string>',
            'add_children': 'bool',
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
            'name': 'string',
            'location_types': 'list<location_types_enum>',
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

    def get_ad_studies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adstudy import AdStudy
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ad_studies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdStudy,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdStudy, api=self._api),
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
        from facebook_business.adobjects.adassetfeed import AdAssetFeed
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
            target_class=AdAssetFeed,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAssetFeed, api=self._api),
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

    def create_ad_asset_feed(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adassetfeed import AdAssetFeed
        param_types = {
            'images': 'list<Object>',
            'videos': 'list<Object>',
            'bodies': 'list<Object>',
            'call_to_action_types': 'list<call_to_action_types_enum>',
            'descriptions': 'list<Object>',
            'link_urls': 'list<Object>',
            'titles': 'list<Object>',
            'captions': 'list<Object>',
            'ad_formats': 'list<ad_formats_enum>',
            'groups': 'list<Object>',
            'target_rules': 'list<Object>',
            'asset_customization_rules': 'list<Object>',
            'optimization_type': 'optimization_type_enum',
            'call_to_actions': 'list<Object>',
            'autotranslate': 'list<string>',
            'additional_data': 'map',
        }
        enums = {
            'call_to_action_types_enum': AdAssetFeed.CallToActionTypes.__dict__.values(),
            'ad_formats_enum': AdAssetFeed.AdFormats.__dict__.values(),
            'optimization_type_enum': AdAssetFeed.OptimizationType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adasset_feeds',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAssetFeed,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAssetFeed, api=self._api),
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

    def get_ad_contracts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adcontract import AdContract
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adcontracts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdContract,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdContract, api=self._api),
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
            'actor_id': 'unsigned int',
            'adlabels': 'list<Object>',
            'applink_treatment': 'applink_treatment_enum',
            'asset_feed_id': 'string',
            'asset_feed_spec': 'Object',
            'authorization_category': 'authorization_category_enum',
            'is_dco_internal': 'bool',
            'body': 'string',
            'branded_content_sponsor_page_id': 'string',
            'bundle_folder_id': 'string',
            'categorization_criteria': 'categorization_criteria_enum',
            'category_media_source': 'category_media_source_enum',
            'call_to_action': 'Object',
            'dynamic_ad_voice': 'dynamic_ad_voice_enum',
            'destination_set_id': 'Object',
            'enable_direct_install': 'bool',
            'enable_launch_instant_app': 'bool',
            'image_crops': 'map',
            'image_file': 'string',
            'image_hash': 'string',
            'image_url': 'string',
            'instagram_actor_id': 'string',
            'instagram_permalink_url': 'string',
            'instagram_story_id': 'unsigned int',
            'link_og_id': 'string',
            'link_url': 'string',
            'name': 'string',
            'object_id': 'unsigned int',
            'object_story_id': 'string',
            'object_type': 'string',
            'object_url': 'string',
            'platform_customizations': 'Object',
            'playable_asset_id': 'string',
            'product_set_id': 'string',
            'recommender_settings': 'map',
            'messenger_sponsored_message': 'string',
            'template_url': 'string',
            'template_url_spec': 'Object',
            'thumbnail_url': 'string',
            'title': 'string',
            'url_tags': 'string',
            'use_page_actor_override': 'bool',
            'object_story_spec': 'AdCreativeObjectStorySpec',
        }
        enums = {
            'applink_treatment_enum': AdCreative.ApplinkTreatment.__dict__.values(),
            'authorization_category_enum': AdCreative.AuthorizationCategory.__dict__.values(),
            'categorization_criteria_enum': AdCreative.CategorizationCriteria.__dict__.values(),
            'category_media_source_enum': AdCreative.CategoryMediaSource.__dict__.values(),
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

    def create_ad_creatives_from_mockup(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adcreative import AdCreative
        param_types = {
            'mockup_id': 'string',
            'page_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adcreatives_from_mockups',
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
            'hashes': 'list<string>',
            'minwidth': 'unsigned int',
            'minheight': 'unsigned int',
            'name': 'string',
            'biz_tag_id': 'unsigned int',
            'business_id': 'string',
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
            'zipbytes': 'Object',
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

    def get_ad_language_assets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adassetfeed import AdAssetFeed
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adlanguage_assets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAssetFeed,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAssetFeed, api=self._api),
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
        from facebook_business.adobjects.adassetfeed import AdAssetFeed
        param_types = {
            'image': 'Object',
            'video': 'Object',
            'call_to_action_type': 'call_to_action_type_enum',
            'bodies': 'list<Object>',
            'descriptions': 'list<Object>',
            'titles': 'list<Object>',
            'link_urls': 'list<Object>',
            'default_language': 'string',
        }
        enums = {
            'call_to_action_type_enum': AdAssetFeed.CallToActionType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adlanguage_assets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAssetFeed,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAssetFeed, api=self._api),
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

    def get_ad_playables(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.playablecontent import PlayableContent
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adplayables',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PlayableContent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PlayableContent, api=self._api),
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

    def create_ad_playable(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.playablecontent import PlayableContent
        param_types = {
            'name': 'string',
            'source': 'file',
            'source_url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adplayables',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PlayableContent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PlayableContent, api=self._api),
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

    def delete_ad_report_runs(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adreportruns',
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

    def create_ad_report_schedule(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'name': 'string',
            'user_columns': 'list<string>',
            'user_attribution_windows': 'list<string>',
            'builtin_column_set': 'builtin_column_set_enum',
            'normalized_filter': 'list<Object>',
            'user_filter': 'list<Object>',
            'sort': 'list<Object>',
            'breakdowns': 'list<string>',
            'insights_section': 'Object',
            'level': 'level_enum',
            'date_preset': 'date_preset_enum',
            'date_interval': 'Object',
            'format_version': 'unsigned int',
            'creation_source': 'creation_source_enum',
            'actions_group_by': 'list<actions_group_by_enum>',
            'custom_column_set_id': 'string',
            'data_columns': 'list<string>',
            'emails': 'list<string>',
            'export_columns': 'Object',
            'filters': 'list<Object>',
            'schedule_frequency': 'schedule_frequency_enum',
            'sort_by': 'string',
            'sort_dir': 'string',
            'start_date': 'Object',
            'status': 'status_enum',
            'subscribers': 'list<int>',
            'time_increment': 'string',
        }
        enums = {
            'builtin_column_set_enum': [
                '',
                'APP_ENGAGEMENT',
                'AUDIENCE_DIRECT',
                'BIDDING_AND_OPTIMIZATION',
                'CAROUSEL_ENGAGEMENT',
                'CROSS_DEVICE',
                'DELIVERY',
                'ENGAGEMENT',
                'HOUSEHOLD',
                'MESSAGING_ENGAGEMENT',
                'MESSENGER',
                'OFFLINE_CONVERSIONS',
                'PERFORMANCE',
                'PERFORMANCE_LEGACY',
                'TARGETING_AND_CREATIVE',
                'VIDEO_ENGAGEMENT',
                'VALIDATION_VIEW',
            ],
            'level_enum': [
                'politicalad',
                'ad',
                'adgroup',
                'campaign',
                'campaign_group',
                'account',
            ],
            'date_preset_enum': [
                'today',
                'yesterday',
                'this_month',
                'last_month',
                'this_quarter',
                'lifetime',
                'last_3d',
                'last_7d',
                'last_14d',
                'last_28d',
                'last_30d',
                'last_90d',
                'last_week_mon_sun',
                'last_week_sun_sat',
                'last_quarter',
                'last_year',
                'this_week_mon_today',
                'this_week_sun_today',
                'this_year',
            ],
            'creation_source_enum': [
                'adsManagerReporting',
                'newAdsManager',
                'adsExcelAddin',
            ],
            'actions_group_by_enum': [
                'action_canvas_component_id',
                'action_canvas_component_name',
                'action_carousel_card_id',
                'action_carousel_card_name',
                'action_destination',
                'action_device',
                'action_event_channel',
                'action_target_id',
                'action_type',
                'action_video_sound',
                'action_video_type',
            ],
            'schedule_frequency_enum': [
                'daily',
                'weekly',
                'monthly',
            ],
            'status_enum': [
                'Active',
                'Paused',
                'Deleted',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def create_ad_report_spec(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adreportspec import AdReportSpec
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
            endpoint='/adreportspecs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdReportSpec,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdReportSpec, api=self._api),
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
            'object_id': 'string',
            'action': 'action_enum',
            'hide_no_changes': 'bool',
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

    def get_ad_rules_library(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adrule import AdRule
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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

    def create_ad_rules_library(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adrule import AdRule
        param_types = {
            'account_id': 'string',
            'evaluation_spec': 'Object',
            'execution_spec': 'Object',
            'schedule_spec': 'Object',
            'name': 'string',
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

    def delete_ads(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'delete_strategy': 'delete_strategy_enum',
            'object_count': 'int',
            'before_date': 'datetime',
        }
        enums = {
            'delete_strategy_enum': [
                'DELETE_ANY',
                'DELETE_OLDEST',
                'DELETE_ARCHIVED_BEFORE',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/ads',
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

    def get_ads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.ad import Ad
        param_types = {
            'date_preset': 'date_preset_enum',
            'effective_status': 'list<string>',
            'include_deleted': 'bool',
            'time_range': 'Object',
            'updated_since': 'int',
            'ad_draft_id': 'string',
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
            'audience_id': 'string',
            'adset_id': 'unsigned int',
            'date_format': 'string',
            'include_demolink_hashes': 'bool',
            'creative': 'AdCreative',
            'name': 'string',
            'status': 'status_enum',
            'priority': 'unsigned int',
            'tracking_specs': 'Object',
            'social_prefs': 'list<string>',
            'display_sequence': 'unsigned int',
            'engagement_audience': 'bool',
            'social_required': 'bool',
            'adset_spec': 'AdSet',
            'draft_adgroup_id': 'string',
            'execution_options': 'list<execution_options_enum>',
            'adlabels': 'list<Object>',
            'bid_amount': 'int',
            'source_ad_id': 'string',
        }
        enums = {
            'status_enum': Ad.Status.__dict__.values(),
            'execution_options_enum': Ad.ExecutionOptions.__dict__.values(),
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

    def delete_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'delete_strategy': 'delete_strategy_enum',
            'object_count': 'int',
            'before_date': 'datetime',
        }
        enums = {
            'delete_strategy_enum': [
                'DELETE_ANY',
                'DELETE_OLDEST',
                'DELETE_ARCHIVED_BEFORE',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/adsets',
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

    def get_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adset import AdSet
        param_types = {
            'effective_status': 'list<effective_status_enum>',
            'date_preset': 'date_preset_enum',
            'include_deleted': 'bool',
            'is_completed': 'bool',
            'time_range': 'Object',
            'ad_draft_id': 'string',
        }
        enums = {
            'effective_status_enum': AdSet.EffectiveStatus.__dict__.values(),
            'date_preset_enum': AdSet.DatePreset.__dict__.values(),
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
            'ad_keywords': 'Object',
            'adlabels': 'list<Object>',
            'bid_amount': 'int',
            'bid_adjustments': 'Object',
            'bid_strategy': 'bid_strategy_enum',
            'billing_event': 'billing_event_enum',
            'campaign_id': 'string',
            'campaign_spec': 'Object',
            'adset_schedule': 'list<Object>',
            'status': 'status_enum',
            'creative_sequence': 'list<string>',
            'daily_budget': 'unsigned int',
            'daily_imps': 'unsigned int',
            'daily_min_spend_target': 'unsigned int',
            'daily_spend_cap': 'unsigned int',
            'date_format': 'string',
            'destination_type': 'destination_type_enum',
            'end_time': 'datetime',
            'execution_options': 'list<execution_options_enum>',
            'frequency_cap': 'unsigned int',
            'frequency_cap_reset_period': 'unsigned int',
            'frequency_control_specs': 'list<Object>',
            'is_autobid': 'bool',
            'is_average_price_pacing': 'bool',
            'is_dynamic_creative': 'bool',
            'is_dynamic_creative_optimization': 'bool',
            'lifetime_budget': 'unsigned int',
            'lifetime_frequency_cap': 'unsigned int',
            'lifetime_imps': 'unsigned int',
            'lifetime_min_spend_target': 'unsigned int',
            'lifetime_spend_cap': 'unsigned int',
            'line_number': 'unsigned int',
            'name': 'string',
            'optimization_goal': 'optimization_goal_enum',
            'pacing_type': 'list<string>',
            'promoted_object': 'Object',
            'rb_prediction_id': 'string',
            'rf_prediction_id': 'string',
            'source_adset_id': 'string',
            'start_time': 'datetime',
            'targeting': 'Targeting',
            'time_based_ad_rotation_id_blocks': 'list<list<unsigned int>>',
            'time_based_ad_rotation_intervals': 'list<unsigned int>',
            'time_start': 'datetime',
            'time_stop': 'datetime',
            'topline_id': 'string',
            'upstream_events': 'map',
            'full_funnel_exploration_mode': 'full_funnel_exploration_mode_enum',
            'attribution_spec': 'list<map>',
        }
        enums = {
            'bid_strategy_enum': AdSet.BidStrategy.__dict__.values(),
            'billing_event_enum': AdSet.BillingEvent.__dict__.values(),
            'status_enum': AdSet.Status.__dict__.values(),
            'destination_type_enum': AdSet.DestinationType.__dict__.values(),
            'execution_options_enum': AdSet.ExecutionOptions.__dict__.values(),
            'optimization_goal_enum': AdSet.OptimizationGoal.__dict__.values(),
            'full_funnel_exploration_mode_enum': AdSet.FullFunnelExplorationMode.__dict__.values(),
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
            'sort_by': 'sort_by_enum',
        }
        enums = {
            'sort_by_enum': AdsPixel.SortBy.__dict__.values(),
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

    def get_ad_topline_details(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adtoplinedetail import AdToplineDetail
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adtoplinedetails',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdToplineDetail,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdToplineDetail, api=self._api),
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

    def get_ad_top_lines(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adtopline import AdTopline
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adtoplines',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdTopline,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdTopline, api=self._api),
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
        from facebook_business.adobjects.application import Application
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
            target_class=Application,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Application, api=self._api),
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
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'title': 'string',
            'minlength': 'unsigned int',
            'maxlength': 'unsigned int',
            'minheight': 'unsigned int',
            'maxheight': 'unsigned int',
            'minwidth': 'unsigned int',
            'maxwidth': 'unsigned int',
            'min_aspect_ratio': 'float',
            'max_aspect_ratio': 'float',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/advideos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'title': 'string',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'time_since_original_post': 'unsigned int',
            'file_url': 'string',
            'composer_session_id': 'string',
            'waterfall_id': 'string',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_suggestion_mechanism': 'string',
            'manual_privacy': 'bool',
            'is_explicit_share': 'bool',
            'thumb': 'file',
            'spherical': 'bool',
            'original_projection_type': 'original_projection_type_enum',
            'initial_heading': 'unsigned int',
            'initial_pitch': 'unsigned int',
            'fov': 'unsigned int',
            'original_fov': 'unsigned int',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'guide_enabled': 'bool',
            'guide': 'list<list<unsigned int>>',
            'audio_story_wave_animation_handle': 'string',
            'adaptive_type': 'string',
            'animated_effect_id': 'unsigned int',
            'asked_fun_fact_prompt_id': 'unsigned int',
            'composer_entry_picker': 'string',
            'composer_entry_point': 'string',
            'composer_entry_time': 'unsigned int',
            'composer_session_events_log': 'string',
            'composer_source_surface': 'string',
            'composer_type': 'string',
            'formatting': 'formatting_enum',
            'fun_fact_prompt_id': 'string',
            'fun_fact_toastee_id': 'unsigned int',
            'is_group_linking_post': 'bool',
            'has_nickname': 'bool',
            'holiday_card': 'string',
            'instant_game_entry_point_data': 'string',
            'is_boost_intended': 'bool',
            'location_source_id': 'string',
            'description': 'string',
            'offer_like_post_id': 'string',
            'publish_event_id': 'unsigned int',
            'react_mode_metadata': 'string',
            'sales_promo_id': 'unsigned int',
            'text_format_metadata': 'string',
            'throwback_camera_roll_media': 'string',
            'video_start_time_ms': 'unsigned int',
            'application_id': 'string',
            'upload_phase': 'upload_phase_enum',
            'file_size': 'unsigned int',
            'start_offset': 'unsigned int',
            'end_offset': 'unsigned int',
            'video_file_chunk': 'string',
            'fbuploader_video_file_chunk': 'string',
            'upload_session_id': 'string',
            'is_voice_clip': 'bool',
            'attribution_app_id': 'string',
            'content_category': 'content_category_enum',
            'embeddable': 'bool',
            'slideshow_spec': 'map',
            'upload_setting_properties': 'string',
            'transcode_setting_properties': 'string',
            'container_type': 'container_type_enum',
            'referenced_sticker_id': 'string',
            'replace_video_id': 'string',
            'swap_mode': 'swap_mode_enum',
            'name': 'string',
            'chunk_session_id': 'string',
        }
        enums = {
            'unpublished_content_type_enum': AdVideo.UnpublishedContentType.__dict__.values(),
            'original_projection_type_enum': AdVideo.OriginalProjectionType.__dict__.values(),
            'formatting_enum': AdVideo.Formatting.__dict__.values(),
            'upload_phase_enum': AdVideo.UploadPhase.__dict__.values(),
            'content_category_enum': AdVideo.ContentCategory.__dict__.values(),
            'container_type_enum': AdVideo.ContainerType.__dict__.values(),
            'swap_mode_enum': AdVideo.SwapMode.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/advideos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdVideo,
            api_type='EDGE',
            allow_file_upload=True,
            response_parser=ObjectParser(target_class=AdVideo, api=self._api),
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

    def get_affected_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adset import AdSet
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/affectedadsets',
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

    def get_agencies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/agencies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Business,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Business, api=self._api),
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
        from facebook_business.adobjects.application import Application
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
            target_class=Application,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Application, api=self._api),
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
            'user': 'int',
            'tasks': 'list<tasks_enum>',
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
            'name': 'string',
            'adbatch': 'list<Object>',
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

    def get_async_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.asyncrequest import AsyncRequest
        param_types = {
            'status': 'status_enum',
            'type': 'type_enum',
        }
        enums = {
            'status_enum': AsyncRequest.Status.__dict__.values(),
            'type_enum': AsyncRequest.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/async_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AsyncRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AsyncRequest, api=self._api),
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
            'notification_uri': 'string',
            'notification_mode': 'notification_mode_enum',
        }
        enums = {
            'notification_mode_enum': AdAsyncRequestSet.NotificationMode.__dict__.values(),
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
            'session': 'Object',
            'payload': 'Object',
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

    def create_batch_replace(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'payload': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/batchreplace',
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

    def create_batch_upload(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'payload': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/batchupload',
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

    def create_block_list_draft(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'publisher_urls_file': 'file',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/block_list_drafts',
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

    def get_brand_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.brandaudience import BrandAudience
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/brand_audiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BrandAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BrandAudience, api=self._api),
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

    def get_business_activities(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessactivitylogevent import BusinessActivityLogEvent
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_activities',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessActivityLogEvent,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessActivityLogEvent, api=self._api),
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

    def get_business_projects(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessproject import BusinessProject
        param_types = {
            'business': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/businessprojects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessProject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessProject, api=self._api),
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
        param_types = {
            'delete_strategy': 'delete_strategy_enum',
            'object_count': 'int',
            'before_date': 'datetime',
        }
        enums = {
            'delete_strategy_enum': [
                'DELETE_ANY',
                'DELETE_OLDEST',
                'DELETE_ARCHIVED_BEFORE',
            ],
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
            'effective_status': 'list<effective_status_enum>',
            'date_preset': 'date_preset_enum',
            'is_completed': 'bool',
        }
        enums = {
            'effective_status_enum': Campaign.EffectiveStatus.__dict__.values(),
            'date_preset_enum': Campaign.DatePreset.__dict__.values(),
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
            'name': 'string',
            'objective': 'objective_enum',
            'status': 'status_enum',
            'bid_strategy': 'bid_strategy_enum',
            'budget_rebalance_flag': 'bool',
            'buying_type': 'string',
            'daily_budget': 'unsigned int',
            'lifetime_budget': 'unsigned int',
            'pacing_type': 'list<string>',
            'promoted_object': 'Object',
            'topline_id': 'string',
            'spend_cap': 'unsigned int',
            'execution_options': 'list<execution_options_enum>',
            'upstream_events': 'map',
            'adlabels': 'list<Object>',
            'source_campaign_id': 'string',
            'iterative_split_test_configs': 'list<Object>',
            'kpi_custom_conversion_id': 'string',
            'kpi_type': 'Object',
            'is_autobid': 'bool',
            'is_average_price_pacing': 'bool',
        }
        enums = {
            'objective_enum': Campaign.Objective.__dict__.values(),
            'status_enum': Campaign.Status.__dict__.values(),
            'bid_strategy_enum': Campaign.BidStrategy.__dict__.values(),
            'execution_options_enum': Campaign.ExecutionOptions.__dict__.values(),
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

    def get_contextual_targeting_browse(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountcontextualtargeting import AdAccountContextualTargeting
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/contextual_targeting_browse',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountContextualTargeting,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountContextualTargeting, api=self._api),
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

    def create_coupon(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'coupon_code': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/coupons',
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

    def get_custom_audience_limits(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountcustomaudiencelimits import AdAccountCustomAudienceLimits
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/custom_audience_limits',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountCustomAudienceLimits,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountCustomAudienceLimits, api=self._api),
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
            'pixel_id': 'string',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'business_id': 'string',
        }
        enums = {
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
            'creation_params': 'map',
            'description': 'string',
            'name': 'string',
            'opt_out_link': 'string',
            'parent_audience_id': 'unsigned int',
            'subtype': 'subtype_enum',
            'seed_audience': 'unsigned int',
            'tags': 'list<string>',
            'associated_audience_id': 'unsigned int',
            'is_household': 'bool',
            'is_household_exclusion': 'bool',
            'is_value_based': 'bool',
            'allowed_domains': 'list<string>',
            'is_snapshot': 'bool',
            'lookalike_spec': 'string',
            'retention_days': 'unsigned int',
            'customer_file_source': 'customer_file_source_enum',
            'rev_share_policy_id': 'unsigned int',
            'partner_reference_key': 'string',
            'rule': 'string',
            'prefill': 'bool',
            'pixel_id': 'string',
            'rule_aggregation': 'string',
            'inclusions': 'list<Object>',
            'exclusions': 'list<Object>',
            'countries': 'string',
            'origin_audience_id': 'string',
            'details': 'string',
            'source': 'string',
            'isPrivate': 'bool',
            'additionalMetadata': 'string',
            'minAge': 'unsigned int',
            'maxAge': 'unsigned int',
            'expectedSize': 'unsigned int',
            'gender': 'string',
            'partnerID': 'string',
            'accountID': 'string',
            'claim_objective': 'claim_objective_enum',
            'content_type': 'content_type_enum',
            'event_source_group': 'string',
            'product_set_id': 'string',
            'event_sources': 'list<map>',
            'video_group_ids': 'list<string>',
            'study_spec': 'Object',
            'list_of_accounts': 'list<unsigned int>',
            'dataset_id': 'string',
        }
        enums = {
            'subtype_enum': CustomAudience.Subtype.__dict__.values(),
            'customer_file_source_enum': CustomAudience.CustomerFileSource.__dict__.values(),
            'claim_objective_enum': CustomAudience.ClaimObjective.__dict__.values(),
            'content_type_enum': CustomAudience.ContentType.__dict__.values(),
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

    def get_custom_conversions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
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

    def create_custom_conversion(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.customconversion import CustomConversion
        param_types = {
            'name': 'string',
            'description': 'string',
            'event_source_id': 'string',
            'rule': 'string',
            'default_conversion_value': 'float',
            'custom_event_type': 'custom_event_type_enum',
            'advanced_rule': 'string',
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

    def create_deactivate(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/deactivate',
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

    def get_delivery_estimate(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountdeliveryestimate import AdAccountDeliveryEstimate
        param_types = {
            'targeting_spec': 'Targeting',
            'optimization_goal': 'optimization_goal_enum',
            'promoted_object': 'Object',
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

    def get_deprecated_targeting_ad_sets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adset import AdSet
        param_types = {
            'type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/deprecatedtargetingadsets',
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

    def get_direct_deals(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.directdeal import DirectDeal
        param_types = {
            'status': 'status_enum',
        }
        enums = {
            'status_enum': DirectDeal.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/direct_deals',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=DirectDeal,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=DirectDeal, api=self._api),
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

    def create_direct_deals_to(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/direct_deals_tos',
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

    def create_email_import(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.emailimport import EmailImport
        param_types = {
            'name': 'string',
            'third_party_data': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/emailimport',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=EmailImport,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=EmailImport, api=self._api),
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
            'dynamic_creative_spec': 'Object',
            'interactive': 'bool',
            'post': 'Object',
            'height': 'unsigned int',
            'width': 'unsigned int',
            'place_page_id': 'int',
            'product_item_ids': 'list<string>',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'locale': 'string',
            'render_type': 'render_type_enum',
            'creative': 'AdCreative',
        }
        enums = {
            'ad_format_enum': AdPreview.AdFormat.__dict__.values(),
            'render_type_enum': AdPreview.RenderType.__dict__.values(),
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
            'default_summary': 'bool',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'summary': 'list<string>',
            'sort': 'list<string>',
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'level': 'level_enum',
            'product_id_limit': 'int',
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
            'default_summary': 'bool',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'summary': 'list<string>',
            'sort': 'list<string>',
            'action_attribution_windows': 'list<action_attribution_windows_enum>',
            'action_breakdowns': 'list<action_breakdowns_enum>',
            'action_report_time': 'action_report_time_enum',
            'breakdowns': 'list<breakdowns_enum>',
            'date_preset': 'date_preset_enum',
            'export_columns': 'list<string>',
            'export_format': 'string',
            'export_name': 'string',
            'level': 'level_enum',
            'product_id_limit': 'int',
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

    def create_location_cluster(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'locations': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/locationclusters',
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

    def get_matched_search_applications(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountmatchedsearchapplicationsedgedata import AdAccountMatchedSearchApplicationsEdgeData
        param_types = {
            'app_store': 'app_store_enum',
            'app_store_country': 'string',
            'business_id': 'Object',
            'query_term': 'string',
            'allow_incomplete_app': 'bool',
        }
        enums = {
            'app_store_enum': AdAccountMatchedSearchApplicationsEdgeData.AppStore.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/matched_search_applications',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountMatchedSearchApplicationsEdgeData,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountMatchedSearchApplicationsEdgeData, api=self._api),
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

    def get_max_bid(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountmaxbid import AdAccountMaxBid
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/max_bid',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountMaxBid,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountMaxBid, api=self._api),
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

    def create_mockup(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'mockup_access_token': 'string',
            'source_mockup_id': 'string',
            'page_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/mockups',
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

    def get_partner_integrations(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.partnerintegrationlinked import PartnerIntegrationLinked
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/partner_integrations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PartnerIntegrationLinked,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PartnerIntegrationLinked, api=self._api),
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

    def create_partner_integration(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.partnerintegrationlinked import PartnerIntegrationLinked
        param_types = {
            'external_id': 'string',
            'gtm_account_id': 'string',
            'gtm_container_id': 'string',
            'name': 'string',
            'partner': 'partner_enum',
        }
        enums = {
            'partner_enum': PartnerIntegrationLinked.Partner.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/partner_integrations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PartnerIntegrationLinked,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PartnerIntegrationLinked, api=self._api),
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
            'targeting_type': 'string',
            'private_or_public': 'private_or_public_enum',
            'hide_pc': 'bool',
            'limit': 'unsigned int',
            'is_exclusion': 'bool',
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

    def create_partner_datum(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'upload_id': 'unsigned int',
            'type': 'string',
            'start_new_upload': 'bool',
            'total_expected': 'unsigned int',
            'upload_metadata': 'string',
            'upload_complete': 'bool',
            'ignore_count_check': 'bool',
            'abandon_upload': 'bool',
            'payload': 'list<string>',
            'payload_type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/partnerdata',
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

    def create_partner_request(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'category_ids': 'list<string>',
            'account_ids': 'list<int>',
            'type': 'type_enum',
        }
        enums = {
            'type_enum': [
                'SHARE_PC',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/partnerrequests',
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
            'creation_params': 'map',
            'description': 'string',
            'name': 'string',
            'opt_out_link': 'string',
            'parent_audience_id': 'unsigned int',
            'subtype': 'subtype_enum',
            'seed_audience': 'unsigned int',
            'tags': 'list<string>',
            'associated_audience_id': 'unsigned int',
            'is_household': 'bool',
            'is_household_exclusion': 'bool',
            'is_value_based': 'bool',
            'allowed_domains': 'list<string>',
            'is_snapshot': 'bool',
            'claim_objective': 'claim_objective_enum',
            'content_type': 'content_type_enum',
            'event_source_group': 'string',
            'product_set_id': 'string',
            'rev_share_policy_id': 'unsigned int',
            'event_sources': 'list<map>',
            'inclusions': 'list<Object>',
            'exclusions': 'list<Object>',
        }
        enums = {
            'subtype_enum': AdAccount.Subtype.__dict__.values(),
            'claim_objective_enum': AdAccount.ClaimObjective.__dict__.values(),
            'content_type_enum': AdAccount.ContentType.__dict__.values(),
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
        from facebook_business.adobjects.publisherblocklist import PublisherBlockList
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
            target_class=PublisherBlockList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PublisherBlockList, api=self._api),
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
        from facebook_business.adobjects.publisherblocklist import PublisherBlockList
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
            target_class=PublisherBlockList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PublisherBlockList, api=self._api),
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
            'targeting_spec': 'Targeting',
            'currency': 'string',
            'is_debug': 'bool',
            'optimize_for': 'optimize_for_enum',
            'daily_budget': 'float',
            'creative_action_spec': 'string',
            'adgroup_ids': 'list<string>',
            'concepts': 'string',
            'caller_id': 'string',
            'object_store_url': 'string',
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
            'action': 'action_enum',
            'ad_formats': 'list<map>',
            'target_spec': 'Targeting',
            'start_time': 'unsigned int',
            'stop_time': 'unsigned int',
            'end_time': 'unsigned int',
            'reach': 'unsigned int',
            'impression': 'unsigned int',
            'frequency_cap': 'unsigned int',
            'budget': 'unsigned int',
            'prediction_mode': 'unsigned int',
            'destination_id': 'unsigned int',
            'destination_ids': 'list<string>',
            'story_event_type': 'unsigned int',
            'day_parting_schedule': 'list<Object>',
            'target_cpm': 'unsigned int',
            'buying_type': 'buying_type_enum',
            'objective': 'string',
            'rf_prediction_id': 'string',
            'rf_prediction_id_to_release': 'string',
            'rf_prediction_id_to_share': 'string',
            'num_curve_points': 'unsigned int',
            'interval_frequency_cap_reset_period': 'unsigned int',
            'campaign_group_id': 'string',
            'grp_buying': 'bool',
            'instream_packages': 'list<instream_packages_enum>',
            'is_bonus_media': 'bool',
            'is_conversion_goal': 'bool',
            'is_full_view': 'bool',
            'is_reach_and_frequency_io_buying': 'bool',
            'is_reserved_buying': 'bool',
            'expiration_time': 'unsigned int',
            'existing_campaign_id': 'string',
            'video_view_length_constraint': 'unsigned int',
            'auction_entry_option_index': 'unsigned int',
            'exceptions': 'bool',
        }
        enums = {
            'action_enum': ReachFrequencyPrediction.Action.__dict__.values(),
            'buying_type_enum': ReachFrequencyPrediction.BuyingType.__dict__.values(),
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

    def get_referral(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.referral import Referral
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/referral',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Referral,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Referral, api=self._api),
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

    def create_referral(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.referral import Referral
        param_types = {
            'invite_limit': 'unsigned int',
            'messenger_cta': 'string',
            'messenger_promotion_text': 'string',
            'namespace': 'unsigned int',
            'need_promo_code': 'bool',
            'offer_origin': 'string',
            'promotion_text': 'string',
            'receiver_benefits_text': 'string',
            'referral_link_uri': 'Object',
            'sender_benefits_text': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/referral',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Referral,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Referral, api=self._api),
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

    def create_report_stat(self, fields=None, params=None, batch=None, pending=False):
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
            'summary': 'bool',
        }
        enums = {
            'actions_group_by_enum': [
                'action_canvas_component_id',
                'action_canvas_component_name',
                'action_carousel_card_id',
                'action_carousel_card_name',
                'action_destination',
                'action_device',
                'action_event_channel',
                'action_target_id',
                'action_type',
                'action_video_sound',
                'action_video_type',
            ],
            'date_preset_enum': [
                'today',
                'yesterday',
                'this_month',
                'last_month',
                'this_quarter',
                'lifetime',
                'last_3d',
                'last_7d',
                'last_14d',
                'last_28d',
                'last_30d',
                'last_90d',
                'last_week_mon_sun',
                'last_week_sun_sat',
                'last_quarter',
                'last_year',
                'this_week_mon_today',
                'this_week_sun_today',
                'this_year',
            ],
            'format_enum': [
                'JSON',
                'CSV',
                'XLS',
                'XLSX',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/reportstats',
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

    def get_roas(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountroas import AdAccountRoas
        param_types = {
            'time_increment': 'string',
            'time_range': 'Object',
            'fields': 'list<string>',
            'filtering': 'list<Object>',
        }
        enums = {
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

    def get_saved_audiences(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.savedaudience import SavedAudience
        param_types = {
            'fields': 'list<string>',
            'filtering': 'list<Object>',
            'business_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/saved_audiences',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SavedAudience,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=SavedAudience, api=self._api),
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
            'message_creative_id': 'string',
            'daily_budget': 'unsigned int',
            'bid_amount': 'int',
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

    def get_targeting_sentence_lines(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.targetingsentenceline import TargetingSentenceLine
        param_types = {
            'targeting_spec': 'Targeting',
            'discard_ages': 'bool',
            'discard_placements': 'bool',
            'hide_targeting_spec_from_return': 'bool',
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

    def get_timezone_offsets(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.timezoneoffset import TimezoneOffset
        param_types = {
            'start_year': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/timezoneoffsets',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=TimezoneOffset,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=TimezoneOffset, api=self._api),
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

    def get_tracking(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccounttrackingdata import AdAccountTrackingData
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tracking',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountTrackingData,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountTrackingData, api=self._api),
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

    def delete_user_match(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'payload': 'Object',
            'namespace': 'string',
            'bidirectional': 'bool',
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
            'payload': 'Object',
            'action': 'string',
            'namespace': 'string',
            'retention': 'string',
            'bidirectional': 'bool',
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

    def delete_user_permissions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'email': 'string',
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/userpermissions',
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

    def get_user_permissions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccountuserpermissions import AdAccountUserPermissions
        param_types = {
            'business': 'Object',
            'user': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/userpermissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountUserPermissions,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountUserPermissions, api=self._api),
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

    def create_user_permission(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user': 'int',
            'email': 'string',
            'business': 'string',
            'tasks': 'list<tasks_enum>',
        }
        enums = {
            'tasks_enum': AdAccount.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/userpermissions',
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

    def delete_users(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
            'uids': 'list<string>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/users',
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

    def create_user(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
            'tasks': 'list<tasks_enum>',
        }
        enums = {
            'tasks_enum': AdAccount.Tasks.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/users',
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

    def delete_users_of_any_audience(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'session': 'Object',
            'payload': 'Object',
            'namespace': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/usersofanyaudience',
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

    _field_types = {
        'account_id': 'string',
        'account_status': 'unsigned int',
        'ad_account_creation_request': 'AdAccountCreationRequest',
        'ad_account_promotable_objects': 'AdAccountPromotableObjects',
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
        'daily_spend_limit': 'string',
        'direct_deals_tos_accepted': 'bool',
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
        'is_in_3ds_authorization_enabled_market': 'bool',
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
        field_enum_info['Currency'] = AdAccount.Currency.__dict__.values()
        field_enum_info['PermittedTasks'] = AdAccount.PermittedTasks.__dict__.values()
        field_enum_info['Tasks'] = AdAccount.Tasks.__dict__.values()
        field_enum_info['ClaimObjective'] = AdAccount.ClaimObjective.__dict__.values()
        field_enum_info['ContentType'] = AdAccount.ContentType.__dict__.values()
        field_enum_info['Subtype'] = AdAccount.Subtype.__dict__.values()
        return field_enum_info


