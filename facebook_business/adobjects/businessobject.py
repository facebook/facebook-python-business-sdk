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

class BusinessObject(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusinessObject = True
        super(BusinessObject, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        asset = 'asset'
        asset_type = 'asset_type'
        id = 'id'
        name = 'name'
        picture = 'picture'

    class Type:
        page = 'page'
        ad_account = 'ad-account'
        product_catalog = 'product-catalog'
        app = 'app'
        pixel = 'pixel'
        system_user = 'system-user'
        brand = 'brand'
        user = 'user'
        project = 'project'
        instagram_account = 'instagram-account'
        atlas_advertiser = 'atlas-advertiser'
        funding_source = 'funding-source'
        legacy_login = 'legacy-login'
        business_request = 'business_request'
        example_cat = 'example-cat'
        monetization_property = 'monetization-property'
        grp_plan = 'grp-plan'
        persona = 'persona'
        credit_partition = 'credit-partition'
        payout_method = 'payout-method'
        ad_study = 'ad-study'
        saved_audience = 'saved-audience'
        shared_audience = 'shared-audience'
        shared_platform_audience = 'shared-platform-audience'
        event_source_group = 'event-source-group'
        offline_event_set = 'offline-event-set'
        ad_image = 'ad-image'
        photo = 'photo'
        block_list = 'block-list'
        finance = 'finance'
        ip = 'ip'
        credit_partition_config = 'credit-partition-config'
        video_asset = 'video-asset'
        business_unit = 'business-unit'
        page_locations = 'page-locations'
        ad_account_creation_request = 'ad-account-creation-request'
        reseller_vetting_oe_request = 'reseller_vetting_oe_request'
        registered_trademark = 'registered-trademark'
        custom_conversion = 'custom-conversion'
        leads_access = 'leads-access'
        spaco_ds_data_collection = 'spaco-ds-data-collection'
        owned_domain = 'owned-domain'
        whatsapp_business_account = 'whatsapp-business-account'
        business_resource_group = 'business-resource-group'
        hotel_price_fetcher_pull_config = 'hotel-price-fetcher-pull-config'
        news_page = 'news-page'
        place_page_set = 'place_page_set'
        business_locations_wrapper = 'business-locations-wrapper'

    class AssetType:
        page = 'PAGE'
        ad_account = 'AD_ACCOUNT'
        product_catalog = 'PRODUCT_CATALOG'
        app = 'APP'
        pixel = 'PIXEL'
        system_user = 'SYSTEM_USER'
        brand = 'BRAND'
        user = 'USER'
        project = 'PROJECT'
        instagram_account = 'INSTAGRAM_ACCOUNT'
        atlas_advertiser = 'ATLAS_ADVERTISER'
        funding_source = 'FUNDING_SOURCE'
        legacy_login = 'LEGACY_LOGIN'
        business_request = 'BUSINESS_REQUEST'
        example_cat = 'EXAMPLE_CAT'
        monetization_property = 'MONETIZATION_PROPERTY'
        grp_plan = 'GRP_PLAN'
        persona = 'PERSONA'
        credit_partition = 'CREDIT_PARTITION'
        payout_account = 'PAYOUT_ACCOUNT'
        ad_study = 'AD_STUDY'
        saved_audience = 'SAVED_AUDIENCE'
        custom_audience = 'CUSTOM_AUDIENCE'
        platform_custom_audience = 'PLATFORM_CUSTOM_AUDIENCE'
        event_source_group = 'EVENT_SOURCE_GROUP'
        offline_conversion_data_set = 'OFFLINE_CONVERSION_DATA_SET'
        ad_image = 'AD_IMAGE'
        photo = 'PHOTO'
        block_list = 'BLOCK_LIST'
        finance = 'FINANCE'
        ip = 'IP'
        credit_partition_config = 'CREDIT_PARTITION_CONFIG'
        video_asset = 'VIDEO_ASSET'
        business_unit = 'BUSINESS_UNIT'
        page_for_locations = 'PAGE_FOR_LOCATIONS'
        ad_account_creation_request = 'AD_ACCOUNT_CREATION_REQUEST'
        reseller_vetting_oe_request = 'RESELLER_VETTING_OE_REQUEST'
        registered_trademark = 'REGISTERED_TRADEMARK'
        custom_conversion = 'CUSTOM_CONVERSION'
        leads_access = 'LEADS_ACCESS'
        spaco_ds_data_collection = 'SPACO_DS_DATA_COLLECTION'
        owned_domain = 'OWNED_DOMAIN'
        whatsapp_business_account = 'WHATSAPP_BUSINESS_ACCOUNT'
        business_resource_group = 'BUSINESS_RESOURCE_GROUP'
        hotel_price_fetcher_pull_config = 'HOTEL_PRICE_FETCHER_PULL_CONFIG'
        news_page = 'NEWS_PAGE'
        place_page_set = 'PLACE_PAGE_SET'
        business_locations_wrapper = 'BUSINESS_LOCATIONS_WRAPPER'

    class Types:
        custom_audience = 'custom_audience'
        saved_audience = 'saved_audience'

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
            target_class=BusinessObject,
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
        'asset': 'Object',
        'asset_type': 'string',
        'id': 'string',
        'name': 'string',
        'picture': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Type'] = BusinessObject.Type.__dict__.values()
        field_enum_info['AssetType'] = BusinessObject.AssetType.__dict__.values()
        field_enum_info['Types'] = BusinessObject.Types.__dict__.values()
        return field_enum_info
