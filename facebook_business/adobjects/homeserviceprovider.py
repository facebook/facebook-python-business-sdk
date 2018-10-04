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

class HomeServiceProvider(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isHomeServiceProvider = True
        super(HomeServiceProvider, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        achievement_badges = 'achievement_badges'
        address = 'address'
        applinks = 'applinks'
        bbb_rating = 'bbb_rating'
        bookable_task = 'bookable_task'
        business_hours = 'business_hours'
        business_phone_number = 'business_phone_number'
        business_url = 'business_url'
        company_name = 'company_name'
        company_tagline = 'company_tagline'
        completed_jobs = 'completed_jobs'
        criminal_background_check_date = 'criminal_background_check_date'
        deals = 'deals'
        description = 'description'
        fb_page_id = 'fb_page_id'
        financial_background_check_date = 'financial_background_check_date'
        first_name = 'first_name'
        home_service_provider_id = 'home_service_provider_id'
        id = 'id'
        images = 'images'
        insurance_info = 'insurance_info'
        internal_score = 'internal_score'
        last_name = 'last_name'
        licensing_info = 'licensing_info'
        messaging_inbox_page_id = 'messaging_inbox_page_id'
        partner_verified_date = 'partner_verified_date'
        product_brands_used = 'product_brands_used'
        provider_type = 'provider_type'
        rating_distribution = 'rating_distribution'
        sanitized_images = 'sanitized_images'
        title = 'title'
        transaction_currency = 'transaction_currency'
        url = 'url'
        year_business_started = 'year_business_started'

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
            target_class=HomeServiceProvider,
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
        'achievement_badges': 'string',
        'address': 'Object',
        'applinks': 'AppLinks',
        'bbb_rating': 'string',
        'bookable_task': 'list<Object>',
        'business_hours': 'list<Object>',
        'business_phone_number': 'string',
        'business_url': 'string',
        'company_name': 'string',
        'company_tagline': 'string',
        'completed_jobs': 'Object',
        'criminal_background_check_date': 'string',
        'deals': 'string',
        'description': 'string',
        'fb_page_id': 'Page',
        'financial_background_check_date': 'string',
        'first_name': 'string',
        'home_service_provider_id': 'string',
        'id': 'string',
        'images': 'list<string>',
        'insurance_info': 'string',
        'internal_score': 'float',
        'last_name': 'string',
        'licensing_info': 'string',
        'messaging_inbox_page_id': 'Page',
        'partner_verified_date': 'string',
        'product_brands_used': 'string',
        'provider_type': 'string',
        'rating_distribution': 'list<Object>',
        'sanitized_images': 'list<string>',
        'title': 'string',
        'transaction_currency': 'string',
        'url': 'string',
        'year_business_started': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


