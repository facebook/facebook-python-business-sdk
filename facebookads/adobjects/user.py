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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class User(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isUser = True
        super(User, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        about = 'about'
        admin_notes = 'admin_notes'
        age_range = 'age_range'
        bio = 'bio'
        birthday = 'birthday'
        context = 'context'
        cover = 'cover'
        currency = 'currency'
        devices = 'devices'
        education = 'education'
        email = 'email'
        favorite_athletes = 'favorite_athletes'
        favorite_teams = 'favorite_teams'
        first_name = 'first_name'
        gender = 'gender'
        hometown = 'hometown'
        id = 'id'
        inspirational_people = 'inspirational_people'
        install_type = 'install_type'
        installed = 'installed'
        interested_in = 'interested_in'
        is_shared_login = 'is_shared_login'
        is_verified = 'is_verified'
        labels = 'labels'
        languages = 'languages'
        last_name = 'last_name'
        link = 'link'
        locale = 'locale'
        location = 'location'
        meeting_for = 'meeting_for'
        middle_name = 'middle_name'
        name = 'name'
        name_format = 'name_format'
        payment_pricepoints = 'payment_pricepoints'
        political = 'political'
        public_key = 'public_key'
        quotes = 'quotes'
        relationship_status = 'relationship_status'
        religion = 'religion'
        security_settings = 'security_settings'
        shared_login_upgrade_required_by = 'shared_login_upgrade_required_by'
        significant_other = 'significant_other'
        sports = 'sports'
        test_group = 'test_group'
        third_party_id = 'third_party_id'
        timezone = 'timezone'
        token_for_business = 'token_for_business'
        updated_time = 'updated_time'
        verified = 'verified'
        video_upload_limits = 'video_upload_limits'
        viewer_can_send_gift = 'viewer_can_send_gift'
        website = 'website'
        work = 'work'

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
            target_class=User,
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

    def get_accounts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business_id': 'string',
            'is_business': 'bool',
            'is_place': 'bool',
            'is_promotable': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/accounts',
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
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_ad_account_groups(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccountgroup import AdAccountGroup
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adaccountgroups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountGroup),
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

    def create_ad_account_group(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccountgroup import AdAccountGroup
        param_types = {
            'accounts': 'map',
            'name': 'string',
            'redownload': 'bool',
            'users': 'map',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/adaccountgroups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccountGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccountGroup),
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

    def get_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.adaccount import AdAccount
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/adaccounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdAccount,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdAccount),
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
        from facebookads.adobjects.leadgenform import LeadgenForm
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
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_picture(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.profilepicturesource import ProfilePictureSource
        param_types = {
            'height': 'int',
            'redirect': 'bool',
            'type': 'type_enum',
            'width': 'int',
        }
        enums = {
            'type_enum': ProfilePictureSource.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/picture',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProfilePictureSource,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProfilePictureSource),
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

    def get_promotable_domains(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.domain import Domain
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/promotable_domains',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Domain,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Domain),
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

    def get_promotable_events(self, fields=None, params=None, batch=None, pending=False):
        from facebookads.adobjects.event import Event
        param_types = {
            'is_page_event': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/promotable_events',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Event,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Event),
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
        'about': 'string',
        'admin_notes': 'list<Object>',
        'age_range': 'Object',
        'bio': 'string',
        'birthday': 'string',
        'context': 'Object',
        'cover': 'Object',
        'currency': 'Object',
        'devices': 'list<Object>',
        'education': 'list<Object>',
        'email': 'string',
        'favorite_athletes': 'list<Object>',
        'favorite_teams': 'list<Object>',
        'first_name': 'string',
        'gender': 'string',
        'hometown': 'Object',
        'id': 'string',
        'inspirational_people': 'list<Object>',
        'install_type': 'string',
        'installed': 'bool',
        'interested_in': 'list<string>',
        'is_shared_login': 'bool',
        'is_verified': 'bool',
        'labels': 'list<Object>',
        'languages': 'list<Object>',
        'last_name': 'string',
        'link': 'string',
        'locale': 'string',
        'location': 'Object',
        'meeting_for': 'list<string>',
        'middle_name': 'string',
        'name': 'string',
        'name_format': 'string',
        'payment_pricepoints': 'Object',
        'political': 'string',
        'public_key': 'string',
        'quotes': 'string',
        'relationship_status': 'string',
        'religion': 'string',
        'security_settings': 'Object',
        'shared_login_upgrade_required_by': 'datetime',
        'significant_other': 'User',
        'sports': 'list<Object>',
        'test_group': 'unsigned int',
        'third_party_id': 'string',
        'timezone': 'float',
        'token_for_business': 'string',
        'updated_time': 'datetime',
        'verified': 'bool',
        'video_upload_limits': 'Object',
        'viewer_can_send_gift': 'bool',
        'website': 'string',
        'work': 'list<Object>',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
