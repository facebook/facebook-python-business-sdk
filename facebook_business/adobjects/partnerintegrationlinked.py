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

class PartnerIntegrationLinked(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPartnerIntegrationLinked = True
        super(PartnerIntegrationLinked, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ads_pixel = 'ads_pixel'
        application = 'application'
        completed_integration_types = 'completed_integration_types'
        external_id = 'external_id'
        has_oauth_token = 'has_oauth_token'
        id = 'id'
        name = 'name'
        offline_conversion_data_set = 'offline_conversion_data_set'
        partner = 'partner'
        partner_profile = 'partner_profile'
        product_catalog = 'product_catalog'
        setup_status = 'setup_status'
        gtm_account_id = 'gtm_account_id'
        gtm_container_id = 'gtm_container_id'

    class Partner:
        adjust = 'adjust'
        appsflyer = 'appsflyer'
        avana = 'avana'
        backer_founder = 'backer_founder'
        big_commerce = 'big_commerce'
        cart_3d = 'cart_3d'
        value_default = 'default'
        drupal = 'drupal'
        ec_cube3 = 'ec_cube3'
        eventbrite = 'eventbrite'
        feedonomics = 'feedonomics'
        foodkit = 'foodkit'
        google_tag_manager = 'google_tag_manager'
        haravan = 'haravan'
        infusionsoft_zap = 'infusionsoft_zap'
        intern = 'intern'
        invoca = 'invoca'
        jimdo = 'jimdo'
        joomla = 'joomla'
        jumpseller = 'jumpseller'
        kraftly = 'kraftly'
        magento = 'magento'
        magento_2 = 'magento_2'
        marketo = 'marketo'
        meesho = 'meesho'
        m_particle = 'm_particle'
        now_floats = 'now_floats'
        opencart = 'opencart'
        prestashop = 'prestashop'
        productsup = 'productsup'
        ruby_on_rails = 'ruby_on_rails'
        riversoft = 'riversoft'
        salesforce_zap = 'salesforce_zap'
        segment = 'segment'
        shopify = 'shopify'
        shopify_online = 'shopify_online'
        shopline = 'shopline'
        shop_up = 'shop_up'
        sirclo = 'sirclo'
        squarespace = 'squarespace'
        storeden = 'storeden'
        test = 'test'
        verifone = 'verifone'
        waca = 'waca'
        weebly = 'weebly'
        wix = 'wix'
        woocommerce = 'woocommerce'
        wordpress = 'wordpress'
        zoho_zap = 'zoho_zap'
        ticketmaster = 'ticketmaster'

    class CompletedIntegrationTypes:
        value_0 = '0'
        value_1 = '1'
        value_2 = '2'
        value_3 = '3'

    class SetupStatus:
        start = 'START'
        complete = 'COMPLETE'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'partner_integrations'

    def api_create(self, parent_id, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_partner_integration(fields, params, batch, pending)

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'asset_type': 'asset_type_enum',
        }
        enums = {
            'asset_type_enum': [
                '0',
                '1',
                '2',
                '3',
            ],
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
            target_class=PartnerIntegrationLinked,
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
            'ads_pixel_id': 'Object',
            'application_id': 'Object',
            'completed_integration_types': 'list<completed_integration_types_enum>',
            'name': 'string',
            'oauth_partner_integration_id': 'Object',
            'offline_conversion_data_set_id': 'Object',
            'product_catalog_id': 'Object',
            'setup_status': 'setup_status_enum',
        }
        enums = {
            'completed_integration_types_enum': PartnerIntegrationLinked.CompletedIntegrationTypes.__dict__.values(),
            'setup_status_enum': PartnerIntegrationLinked.SetupStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PartnerIntegrationLinked,
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
        'ads_pixel': 'AdsPixel',
        'application': 'Application',
        'completed_integration_types': 'list<string>',
        'external_id': 'string',
        'has_oauth_token': 'bool',
        'id': 'string',
        'name': 'string',
        'offline_conversion_data_set': 'OfflineConversionDataSet',
        'partner': 'string',
        'partner_profile': 'Object',
        'product_catalog': 'ProductCatalog',
        'setup_status': 'string',
        'gtm_account_id': 'string',
        'gtm_container_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Partner'] = PartnerIntegrationLinked.Partner.__dict__.values()
        field_enum_info['CompletedIntegrationTypes'] = PartnerIntegrationLinked.CompletedIntegrationTypes.__dict__.values()
        field_enum_info['SetupStatus'] = PartnerIntegrationLinked.SetupStatus.__dict__.values()
        return field_enum_info


