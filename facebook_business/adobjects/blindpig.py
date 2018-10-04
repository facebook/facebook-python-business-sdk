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

class BlindPig(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBlindPig = True
        super(BlindPig, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        all_phone_numbers = 'all_phone_numbers'
        alternately_named_field = 'alternately_named_field'
        always_null = 'always_null'
        always_secret_pattern_time = 'always_secret_pattern_time'
        always_secret_time = 'always_secret_time'
        ambience = 'ambience'
        async_drinks_info = 'async_drinks_info'
        average_customer_age = 'average_customer_age'
        awesomeness = 'awesomeness'
        bar_game_ids = 'bar_game_ids'
        beer_types = 'beer_types'
        blind_pig_profile = 'blind_pig_profile'
        cards_accepted = 'cards_accepted'
        category = 'category'
        celebrity = 'celebrity'
        chair_count = 'chair_count'
        cocktails = 'cocktails'
        color = 'color'
        company_name = 'company_name'
        country_of_origin = 'country_of_origin'
        creation_time_from_tao_server = 'creation_time_from_tao_server'
        creator = 'creator'
        creator_as_field = 'creator_as_field'
        currency_code = 'currency_code'
        days_open = 'days_open'
        drinks_info = 'drinks_info'
        dynamically_named_field = 'dynamically_named_field'
        ein = 'ein'
        email_address_blacklist = 'email_address_blacklist'
        embedded_updated_time = 'embedded_updated_time'
        even_number = 'even_number'
        favorite_meal = 'favorite_meal'
        favorite_person = 'favorite_person'
        favorite_person_again = 'favorite_person_again'
        favorite_place = 'favorite_place'
        feedback_list = 'feedback_list'
        field_on_shadow_ent_pattern = 'field_on_shadow_ent_pattern'
        field_on_trait = 'field_on_trait'
        founded_time = 'founded_time'
        geocities_page_uri = 'geocities_page_uri'
        id = 'id'
        instruments = 'instruments'
        is_illegal = 'is_illegal'
        is_in_blanket = 'is_in_blanket'
        last_drink_bottle_broken_date = 'last_drink_bottle_broken_date'
        latitude = 'latitude'
        locale = 'locale'
        longitude = 'longitude'
        lucky_numbers = 'lucky_numbers'
        marketing_uri = 'marketing_uri'
        max_allowance = 'max_allowance'
        meals = 'meals'
        mobile_github_uri = 'mobile_github_uri'
        monthly_profit = 'monthly_profit'
        name = 'name'
        overrideable_thing = 'overrideable_thing'
        phone_directory = 'phone_directory'
        phone_numbers = 'phone_numbers'
        price = 'price'
        proprietor = 'proprietor'
        request_box = 'request_box'
        revert_name = 'revert_name'
        second_favorite_person = 'second_favorite_person'
        secret_even_number = 'secret_even_number'
        secret_even_pattern_number = 'secret_even_pattern_number'
        secret_odd_number = 'secret_odd_number'
        secret_pattern_time = 'secret_pattern_time'
        secret_time = 'secret_time'
        see_also = 'see_also'
        snacks = 'snacks'
        store_number = 'store_number'
        street_address = 'street_address'
        subpattern_address = 'subpattern_address'
        subpattern_dynamic_field = 'subpattern_dynamic_field'
        subpattern_name = 'subpattern_name'
        throne_chair_id = 'throne_chair_id'
        todays_special = 'todays_special'
        unique_bar_game_ids = 'unique_bar_game_ids'
        update_time_from_tao_server = 'update_time_from_tao_server'
        vip = 'vip'
        year_founded = 'year_founded'

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
            target_class=BlindPig,
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

    def get_bar_games(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.application import Application
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/bar_games',
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

    def get_card_holders(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/card_holders',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=User,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=User, api=self._api),
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

    def get_known_patrons(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/known_patrons',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=User,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=User, api=self._api),
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

    def get_supervisors(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.user import User
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/supervisors',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=User,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=User, api=self._api),
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

    def get_unique_bar_games(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.application import Application
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/unique_bar_games',
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

    _field_types = {
        'all_phone_numbers': 'list<string>',
        'alternately_named_field': 'int',
        'always_null': 'User',
        'always_secret_pattern_time': 'datetime',
        'always_secret_time': 'datetime',
        'ambience': 'string',
        'async_drinks_info': 'list<Object>',
        'average_customer_age': 'float',
        'awesomeness': 'string',
        'bar_game_ids': 'string',
        'beer_types': 'list<string>',
        'blind_pig_profile': 'Profile',
        'cards_accepted': 'bool',
        'category': 'string',
        'celebrity': 'string',
        'chair_count': 'Object',
        'cocktails': 'list<string>',
        'color': 'string',
        'company_name': 'string',
        'country_of_origin': 'string',
        'creation_time_from_tao_server': 'datetime',
        'creator': 'User',
        'creator_as_field': 'User',
        'currency_code': 'string',
        'days_open': 'string',
        'drinks_info': 'list<Object>',
        'dynamically_named_field': 'int',
        'ein': 'string',
        'email_address_blacklist': 'list<string>',
        'embedded_updated_time': 'datetime',
        'even_number': 'int',
        'favorite_meal': 'string',
        'favorite_person': 'User',
        'favorite_person_again': 'User',
        'favorite_place': 'string',
        'feedback_list': 'list<Object>',
        'field_on_shadow_ent_pattern': 'string',
        'field_on_trait': 'string',
        'founded_time': 'datetime',
        'geocities_page_uri': 'string',
        'id': 'string',
        'instruments': 'list<string>',
        'is_illegal': 'bool',
        'is_in_blanket': 'bool',
        'last_drink_bottle_broken_date': 'datetime',
        'latitude': 'float',
        'locale': 'string',
        'longitude': 'float',
        'lucky_numbers': 'list<int>',
        'marketing_uri': 'string',
        'max_allowance': 'Object',
        'meals': 'list<string>',
        'mobile_github_uri': 'string',
        'monthly_profit': 'list<Object>',
        'name': 'string',
        'overrideable_thing': 'string',
        'phone_directory': 'list<Object>',
        'phone_numbers': 'list<string>',
        'price': 'list<Object>',
        'proprietor': 'User',
        'request_box': 'string',
        'revert_name': 'string',
        'second_favorite_person': 'User',
        'secret_even_number': 'int',
        'secret_even_pattern_number': 'int',
        'secret_odd_number': 'int',
        'secret_pattern_time': 'datetime',
        'secret_time': 'datetime',
        'see_also': 'list<string>',
        'snacks': 'list<string>',
        'store_number': 'string',
        'street_address': 'string',
        'subpattern_address': 'string',
        'subpattern_dynamic_field': 'int',
        'subpattern_name': 'string',
        'throne_chair_id': 'string',
        'todays_special': 'Object',
        'unique_bar_game_ids': 'list<string>',
        'update_time_from_tao_server': 'datetime',
        'vip': 'User',
        'year_founded': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


