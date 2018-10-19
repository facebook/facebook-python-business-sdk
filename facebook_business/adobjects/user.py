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

class User(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isUser = True
        super(User, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        about = 'about'
        address = 'address'
        admin_notes = 'admin_notes'
        age_range = 'age_range'
        bio = 'bio'
        birthday = 'birthday'
        can_review_measurement_request = 'can_review_measurement_request'
        context = 'context'
        cover = 'cover'
        currency = 'currency'
        devices = 'devices'
        education = 'education'
        email = 'email'
        employee_number = 'employee_number'
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
        is_famedeeplinkinguser = 'is_famedeeplinkinguser'
        is_shared_login = 'is_shared_login'
        is_verified = 'is_verified'
        labels = 'labels'
        languages = 'languages'
        last_name = 'last_name'
        link = 'link'
        local_news_megaphone_dismiss_status = 'local_news_megaphone_dismiss_status'
        local_news_subscription_status = 'local_news_subscription_status'
        locale = 'locale'
        location = 'location'
        meeting_for = 'meeting_for'
        middle_name = 'middle_name'
        name = 'name'
        name_format = 'name_format'
        payment_pricepoints = 'payment_pricepoints'
        political = 'political'
        profile_pic = 'profile_pic'
        public_key = 'public_key'
        quotes = 'quotes'
        relationship_status = 'relationship_status'
        religion = 'religion'
        security_settings = 'security_settings'
        shared_login_upgrade_required_by = 'shared_login_upgrade_required_by'
        short_name = 'short_name'
        significant_other = 'significant_other'
        sports = 'sports'
        test_group = 'test_group'
        third_party_id = 'third_party_id'
        timezone = 'timezone'
        token_for_business = 'token_for_business'
        updated_time = 'updated_time'
        username = 'username'
        verified = 'verified'
        video_upload_limits = 'video_upload_limits'
        viewer_can_send_gift = 'viewer_can_send_gift'
        website = 'website'
        work = 'work'

    class Tasks:
        manage = 'MANAGE'
        create_content = 'CREATE_CONTENT'
        moderate = 'MODERATE'
        moderate_community = 'MODERATE_COMMUNITY'
        advertise = 'ADVERTISE'
        analyze = 'ANALYZE'

    class LocalNewsMegaphoneDismissStatus:
        yes = 'YES'
        no = 'NO'

    class LocalNewsSubscriptionStatus:
        status_on = 'STATUS_ON'
        status_off = 'STATUS_OFF'

    class ResumeType:
        bot_action = 'BOT_ACTION'
        native = 'NATIVE'

    class Filtering:
        groups = 'groups'
        groups_social = 'groups_social'
        ema = 'ema'

    class Type:
        generic = 'generic'
        content_update = 'content_update'

    class ServiceType:
        aim = 'AIM'
        gadu = 'GADU'
        icq = 'ICQ'
        gtalk = 'GTALK'
        msn = 'MSN'
        skype = 'SKYPE'
        yahoo = 'YAHOO'
        yahoo_jp = 'YAHOO_JP'
        qq = 'QQ'
        nateon = 'NATEON'
        twitter = 'TWITTER'
        hyves = 'HYVES'
        orkut = 'ORKUT'
        myspace = 'MYSPACE'
        groupwise = 'GROUPWISE'
        cyworld = 'CYWORLD'
        mixi = 'MIXI'
        qip = 'QIP'
        rediff_bol = 'REDIFF_BOL'
        vkontakte = 'VKONTAKTE'
        ebuddy = 'EBUDDY'
        mailru = 'MAILRU'
        jabber = 'JABBER'
        icloud = 'ICLOUD'
        bbm = 'BBM'
        bbm_ppid = 'BBM_PPID'
        instagram = 'INSTAGRAM'
        line = 'LINE'
        wechat = 'WECHAT'
        kakaotalk = 'KAKAOTALK'
        others = 'OTHERS'
        snapchat = 'SNAPCHAT'
        tumblr = 'TUMBLR'
        sound_cloud = 'SOUND_CLOUD'
        linked_in = 'LINKED_IN'
        pinterest = 'PINTEREST'
        you_tube = 'YOU_TUBE'
        medium = 'MEDIUM'
        foursquare = 'FOURSQUARE'
        spotify = 'SPOTIFY'
        vimeo = 'VIMEO'
        kik = 'KIK'
        ask_fm = 'ASK_FM'
        ok = 'OK'
        github = 'GITHUB'
        twitch = 'TWITCH'
        whatsapp = 'WHATSAPP'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'password': 'string',
            'name': 'string',
            'firstname': 'string',
            'lastname': 'string',
            'local_news_subscription_status': 'local_news_subscription_status_enum',
            'local_news_megaphone_dismiss_status': 'local_news_megaphone_dismiss_status_enum',
            'label_cohort': 'Object',
            'emoji_color_pref': 'unsigned int',
        }
        enums = {
            'local_news_subscription_status_enum': User.LocalNewsSubscriptionStatus.__dict__.values(),
            'local_news_megaphone_dismiss_status_enum': User.LocalNewsMegaphoneDismissStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
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

    def create_Payment_Currency(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'currency': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/PaymentCurrencies',
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

    def create_access_token(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business_app': 'int',
            'scope': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/access_tokens',
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

    def delete_access_tokens(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/accesstokens',
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

    def get_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'business_id': 'string',
            'is_promotable': 'bool',
            'is_business': 'bool',
            'is_place': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def create_account(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'name': 'string',
            'category': 'int',
            'category_enum': 'string',
            'picture': 'string',
            'cover_photo': 'Object',
            'about': 'string',
            'description': 'string',
            'address': 'string',
            'city_id': 'Object',
            'location': 'Object',
            'zip': 'string',
            'phone': 'string',
            'website': 'string',
            'coordinates': 'Object',
            'category_list': 'list<string>',
            'ignore_coordinate_warnings': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/accounts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def get_achievements(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'app_id_filter': 'int',
            'object': 'Object',
            'type': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/achievements',
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

    def create_achievement(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'to': 'string',
            'client_secret': 'string',
            'preview': 'bool',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'proxied_app_id': 'string',
            'user_selected_tags': 'bool',
            'user_selected_place': 'bool',
            'added': 'string',
            'alias': 'string',
            'fb:channel': 'string',
            'created_time': 'datetime',
            'end_time': 'datetime',
            'expires_in': 'unsigned int',
            'fb:explicitly_shared': 'bool',
            'image:height': 'unsigned int',
            'image:secure_url': 'string',
            'image:type': 'string',
            'image:url': 'string',
            'image:user_generated': 'bool',
            'image:width': 'unsigned int',
            'no_feed_story': 'bool',
            'no_action_link': 'bool',
            'notify': 'bool',
            'message': 'string',
            'place': 'string',
            'privacy': 'Object',
            'ref': 'string',
            'scrape': 'bool',
            'start_time': 'datetime',
            'tags': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/achievements',
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

    def get_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
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

    def get_albums(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.album import Album
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/albums',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Album,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Album, api=self._api),
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

    def create_album(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.album import Album
        param_types = {
            'is_default': 'bool',
            'name': 'string',
            'description': 'string',
            'contributors': 'list<int>',
            'make_shared_album': 'bool',
            'location': 'string',
            'visible': 'string',
            'privacy': 'Object',
            'place': 'Object',
            'tags': 'list<int>',
            'message': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/albums',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Album,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Album, api=self._api),
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

    def create_application(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business_app': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/applications',
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

    def get_app_request_former_recipients(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.apprequestformerrecipient import AppRequestFormerRecipient
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/apprequestformerrecipients',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AppRequestFormerRecipient,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AppRequestFormerRecipient, api=self._api),
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

    def get_app_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.apprequest import AppRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/apprequests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AppRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AppRequest, api=self._api),
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

    def get_asset3_ds(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.withasset3d import WithAsset3D
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/asset3ds',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=WithAsset3D,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=WithAsset3D, api=self._api),
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

    def get_assigned_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_ad_accounts',
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

    def get_assigned_monetization_properties(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.admonetizationproperty import AdMonetizationProperty
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_monetization_properties',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdMonetizationProperty,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AdMonetizationProperty, api=self._api),
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

    def get_assigned_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_pages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def get_assigned_product_catalogs(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/assigned_product_catalogs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
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

    def get_books(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'target_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/books',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def delete_bulk_contacts(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'contact_surface': 'contact_surface_enum',
        }
        enums = {
            'contact_surface_enum': [
                'ORIGINAL',
                'MESSENGER',
                'CONNECTIONS',
                'GROWTH_CONTACT_IMPORTER',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/bulkcontacts',
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

    def get_business_users(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.businessuser import BusinessUser
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/business_users',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=BusinessUser,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=BusinessUser, api=self._api),
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

    def delete_businesses(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'business': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/businesses',
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

    def get_businesses(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.business import Business
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/businesses',
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

    def create_checkin(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'picture': 'string',
            'name': 'string',
            'link': 'string',
            'caption': 'string',
            'description': 'string',
            'quote': 'string',
            'source': 'string',
            'properties': 'Object',
            'object_attachment': 'string',
            'height': 'unsigned int',
            'width': 'unsigned int',
            'expanded_height': 'unsigned int',
            'expanded_width': 'unsigned int',
            'referral_id': 'string',
            'thumbnail': 'file',
            'image_crops': 'map',
            'call_to_action': 'Object',
            'place': 'Object',
            'coordinates': 'Object',
            'message': 'string',
            'tags': 'list<int>',
            'privacy': 'Object',
            'group': 'string',
            'nectar_module': 'string',
            'manual_privacy': 'bool',
            'audience_exp': 'bool',
            'composer_session_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/checkins',
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

    def create_contacts_photo(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'published': 'bool',
            'target_id': 'int',
            'url': 'string',
            'full_res_is_coming_later': 'bool',
            'manual_privacy': 'bool',
            'audience_exp': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/contacts_photos',
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

    def get_conversations(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'tags': 'list<string>',
            'folder': 'string',
            'psid': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/conversations',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UnifiedThread,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UnifiedThread, api=self._api),
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

    def get_custom_labels(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.pageusermessagethreadlabel import PageUserMessageThreadLabel
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/custom_labels',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageUserMessageThreadLabel,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PageUserMessageThreadLabel, api=self._api),
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

    def get_domains(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.domain import Domain
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/domains',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Domain,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Domain, api=self._api),
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

    def get_events(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.event import Event
        param_types = {
            'type': 'type_enum',
            'include_canceled': 'bool',
        }
        enums = {
            'type_enum': Event.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/events',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Event,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Event, api=self._api),
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

    def create_event(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.event import Event
        param_types = {
            'event_info': 'Object',
            'action_context': 'Object',
            'app_context': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/events',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Event,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Event, api=self._api),
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

    def get_family(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/family',
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

    def get_favorite_requests(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.favoriterequest import FavoriteRequest
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/favorite_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FavoriteRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=FavoriteRequest, api=self._api),
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

    def create_favorite_request(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.favoriterequest import FavoriteRequest
        param_types = {
            'api_version': 'api_version_enum',
            'graph_path': 'string',
            'query_params': 'map',
            'http_method': 'http_method_enum',
            'description': 'string',
            'post_params': 'map',
        }
        enums = {
            'api_version_enum': FavoriteRequest.ApiVersion.__dict__.values(),
            'http_method_enum': FavoriteRequest.HttpMethod.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/favorite_requests',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FavoriteRequest,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=FavoriteRequest, api=self._api),
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

    def create_feed(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'picture': 'string',
            'name': 'string',
            'link': 'string',
            'caption': 'string',
            'description': 'string',
            'quote': 'string',
            'source': 'string',
            'properties': 'Object',
            'object_attachment': 'string',
            'height': 'unsigned int',
            'width': 'unsigned int',
            'expanded_height': 'unsigned int',
            'expanded_width': 'unsigned int',
            'referral_id': 'string',
            'thumbnail': 'file',
            'image_crops': 'map',
            'call_to_action': 'Object',
            'time_since_original_post': 'unsigned int',
            'client_mutation_id': 'string',
            'privacy': 'Object',
            'composer_session_id': 'string',
            'content_attachment': 'string',
            'actions': 'Object',
            'targeting': 'Object',
            'feed_targeting': 'Object',
            'ref': 'list<string>',
            'tags': 'list<int>',
            'place': 'Object',
            'is_explicit_location': 'bool',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'og_hide_object_attachment': 'bool',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'published': 'bool',
            'scheduled_publish_time': 'datetime',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'application_id': 'string',
            'proxied_app_id': 'string',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'user_selected_tags': 'bool',
            'nectar_module': 'string',
            'manual_privacy': 'bool',
            'audience_exp': 'bool',
            'coordinates': 'Object',
            'is_explicit_share': 'bool',
            'is_photo_container': 'bool',
            'implicit_with_tags': 'list<int>',
            'child_attachments': 'list<Object>',
            'suggested_place_id': 'Object',
            'attach_place_suggestion': 'bool',
            'viewer_coordinates': 'Object',
            'album_id': 'string',
            'multi_share_optimized': 'bool',
            'multi_share_end_card': 'bool',
            'title': 'string',
            'attached_media': 'list<Object>',
            'home_checkin_city_id': 'Object',
            'text_only_place': 'string',
            'connection_class': 'string',
            'associated_id': 'string',
            'posting_to_redspace': 'posting_to_redspace_enum',
            'place_attachment_setting': 'place_attachment_setting_enum',
            'checkin_entry_point': 'checkin_entry_point_enum',
            'is_backout_draft': 'bool',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
            'sponsor_relationship': 'unsigned int',
            'referenceable_image_ids': 'list<string>',
            'prompt_id': 'string',
            'prompt_tracking_string': 'string',
            'post_surfaces_blacklist': 'list<post_surfaces_blacklist_enum>',
            'tracking_info': 'string',
            'text_format_preset_id': 'string',
            'cta_link': 'string',
            'cta_type': 'string',
            'place_list_data': 'Object',
            'formatting': 'formatting_enum',
            'target_surface': 'target_surface_enum',
            'adaptive_type': 'string',
            'animated_effect_id': 'unsigned int',
            'asked_fun_fact_prompt_id': 'unsigned int',
            'asset3d_id': 'unsigned int',
            'composer_entry_picker': 'string',
            'composer_entry_point': 'string',
            'composer_entry_time': 'unsigned int',
            'composer_session_events_log': 'string',
            'composer_source_surface': 'string',
            'composer_type': 'string',
            'fun_fact_prompt_id': 'string',
            'fun_fact_toastee_id': 'unsigned int',
            'is_group_linking_post': 'bool',
            'has_nickname': 'bool',
            'holiday_card': 'string',
            'instant_game_entry_point_data': 'string',
            'is_boost_intended': 'bool',
            'location_source_id': 'string',
            'message': 'string',
            'offer_like_post_id': 'string',
            'page_recommendation': 'string',
            'place_list': 'string',
            'publish_event_id': 'unsigned int',
            'react_mode_metadata': 'string',
            'sales_promo_id': 'unsigned int',
            'text_format_metadata': 'string',
            'throwback_camera_roll_media': 'string',
            'video_start_time_ms': 'unsigned int',
        }
        enums = {
            'backdated_time_granularity_enum': [
                'year',
                'month',
                'day',
                'hour',
                'min',
                'none',
            ],
            'unpublished_content_type_enum': [
                'SCHEDULED',
                'DRAFT',
                'ADS_POST',
                'INLINE_CREATED',
                'PUBLISHED',
            ],
            'posting_to_redspace_enum': [
                'enabled',
                'disabled',
            ],
            'place_attachment_setting_enum': [
                '1',
                '2',
            ],
            'checkin_entry_point_enum': [
                'BRANDING_CHECKIN',
                'BRANDING_STATUS',
                'BRANDING_PHOTO',
                'BRANDING_OTHER',
            ],
            'post_surfaces_blacklist_enum': [
                '1',
                '2',
                '3',
                '4',
                '5',
            ],
            'formatting_enum': [
                'PLAINTEXT',
                'MARKDOWN',
            ],
            'target_surface_enum': [
                'STORY',
                'TIMELINE',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/feed',
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

    def get_friend_lists(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.friendlist import FriendList
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/friendlists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FriendList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=FriendList, api=self._api),
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

    def create_friend_list(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.friendlist import FriendList
        param_types = {
            'name': 'string',
            'uid': 'int',
            'list_type': 'list_type_enum',
        }
        enums = {
            'list_type_enum': FriendList.ListType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/friendlists',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=FriendList,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=FriendList, api=self._api),
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

    def get_friends(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/friends',
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

    def create_game_item(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'action': 'action_enum',
            'item_id': 'Object',
            'drop_table_id': 'Object',
            'ext_id': 'string',
            'quantity': 'unsigned int',
            'app_id': 'Object',
        }
        enums = {
            'action_enum': [
                'MARK',
                'CONSUME',
                'DROP',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/game_items',
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

    def create_game_time(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'action': 'action_enum',
        }
        enums = {
            'action_enum': [
                'START',
                'HEARTBEAT',
                'END',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/game_times',
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

    def get_games(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'target_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/games',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def create_games_stat(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'stat_name': 'string',
            'set': 'unsigned int',
            'inc': 'unsigned int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/games_stats',
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

    def create_games_achieve(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'to': 'string',
            'client_secret': 'string',
            'preview': 'bool',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'proxied_app_id': 'string',
            'user_selected_tags': 'bool',
            'user_selected_place': 'bool',
            'added': 'string',
            'alias': 'string',
            'fb:channel': 'string',
            'created_time': 'datetime',
            'end_time': 'datetime',
            'expires_in': 'unsigned int',
            'fb:explicitly_shared': 'bool',
            'image:height': 'unsigned int',
            'image:secure_url': 'string',
            'image:type': 'string',
            'image:url': 'string',
            'image:user_generated': 'bool',
            'image:width': 'unsigned int',
            'no_feed_story': 'bool',
            'no_action_link': 'bool',
            'notify': 'bool',
            'message': 'string',
            'place': 'string',
            'privacy': 'Object',
            'ref': 'string',
            'scrape': 'bool',
            'start_time': 'datetime',
            'tags': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/gamesachieves',
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

    def create_games_play(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'to': 'string',
            'client_secret': 'string',
            'preview': 'bool',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'proxied_app_id': 'string',
            'user_selected_tags': 'bool',
            'user_selected_place': 'bool',
            'added': 'string',
            'alias': 'string',
            'fb:channel': 'string',
            'created_time': 'datetime',
            'end_time': 'datetime',
            'expires_in': 'unsigned int',
            'fb:explicitly_shared': 'bool',
            'image:height': 'unsigned int',
            'image:secure_url': 'string',
            'image:type': 'string',
            'image:url': 'string',
            'image:user_generated': 'bool',
            'image:width': 'unsigned int',
            'no_feed_story': 'bool',
            'no_action_link': 'bool',
            'notify': 'bool',
            'message': 'string',
            'place': 'string',
            'privacy': 'Object',
            'ref': 'string',
            'scrape': 'bool',
            'start_time': 'datetime',
            'tags': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/gamesplays',
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

    def get_groups(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.group import Group
        param_types = {
            'parent': 'string',
            'admin_only': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Group,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Group, api=self._api),
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

    def get_ids_for_apps(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.useridforapp import UserIDForApp
        param_types = {
            'app': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ids_for_apps',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UserIDForApp,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UserIDForApp, api=self._api),
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

    def get_ids_for_business(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.useridforapp import UserIDForApp
        param_types = {
            'app': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ids_for_business',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UserIDForApp,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UserIDForApp, api=self._api),
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

    def get_ids_for_pages(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.useridforpage import UserIDForPage
        param_types = {
            'page': 'int',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/ids_for_pages',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UserIDForPage,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UserIDForPage, api=self._api),
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

    def get_invitable_friends(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.userinvitablefriend import UserInvitableFriend
        param_types = {
            'excluded_ids': 'list<Object>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/invitable_friends',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UserInvitableFriend,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UserInvitableFriend, api=self._api),
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

    def delete_likes(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'uid': 'int',
            'url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/likes',
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

    def get_likes(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'target_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def create_like(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'message': 'string',
            'url': 'string',
            'ref': 'string',
            'action': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/likes',
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

    def create_link(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.link import Link
        param_types = {
            'link': 'string',
            'message': 'string',
            'image': 'string',
            'tags': 'list<int>',
            'place': 'Object',
            'published': 'bool',
            'scheduled_publish_time': 'unsigned int',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'targeting': 'Object',
            'privacy': 'Object',
            'application_id': 'string',
            'is_explicit_share': 'bool',
        }
        enums = {
            'unpublished_content_type_enum': Link.UnpublishedContentType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/links',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Link,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Link, api=self._api),
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

    def create_live_encoder(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'device_id': 'string',
            'name': 'string',
            'brand': 'string',
            'model': 'string',
            'version': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/live_encoders',
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

    def get_live_videos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.livevideo import LiveVideo
        param_types = {
            'type': 'type_enum',
            'source': 'source_enum',
            'broadcast_status': 'list<broadcast_status_enum>',
        }
        enums = {
            'type_enum': LiveVideo.Type.__dict__.values(),
            'source_enum': LiveVideo.Source.__dict__.values(),
            'broadcast_status_enum': LiveVideo.BroadcastStatus.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/live_videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LiveVideo, api=self._api),
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

    def create_live_video(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.livevideo import LiveVideo
        param_types = {
            'title': 'string',
            'description': 'string',
            'save_vod': 'bool',
            'published': 'bool',
            'status': 'status_enum',
            'privacy': 'Object',
            'stop_on_delete_stream': 'bool',
            'stream_type': 'stream_type_enum',
            'content_tags': 'list<string>',
            'is_spherical': 'bool',
            'is_audio_only': 'bool',
            'planned_start_time': 'int',
            'schedule_custom_profile_image': 'file',
            'projection': 'projection_enum',
            'spatial_audio_format': 'spatial_audio_format_enum',
            'encoding_settings': 'string',
            'live_encoders': 'list<string>',
            'original_fov': 'unsigned int',
            'fisheye_video_cropped': 'bool',
            'front_z_rotation': 'float',
            'attribution_app_id': 'string',
            'stereoscopic_mode': 'stereoscopic_mode_enum',
        }
        enums = {
            'status_enum': LiveVideo.Status.__dict__.values(),
            'stream_type_enum': LiveVideo.StreamType.__dict__.values(),
            'projection_enum': LiveVideo.Projection.__dict__.values(),
            'spatial_audio_format_enum': LiveVideo.SpatialAudioFormat.__dict__.values(),
            'stereoscopic_mode_enum': LiveVideo.StereoscopicMode.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/live_videos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LiveVideo, api=self._api),
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

    def create_logged_out_push_set_nonce(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'device_id': 'string',
            'existing_nonce': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/loggedoutpushsetnonces',
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

    def create_log_in_approvals_key(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'machine_id': 'string',
            'check_code': 'string',
            'client_time': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/loginapprovalskeys',
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

    def create_mfs_account_pin_reset(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'provider_id': 'string',
            'password_token': 'string',
            'should_bypass_token_proxy': 'bool',
            'resume_type': 'resume_type_enum',
            'resume_payload': 'string',
        }
        enums = {
            'resume_type_enum': User.ResumeType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/mfs_account_pin_reset',
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

    def create_moments_link_invite(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'moments_folder_uuid': 'string',
            'invite_source': 'string',
            'is_aldrin_region': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/moments_link_invite',
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

    def create_moments_link_invite_convert(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'encoded_invite_id': 'string',
            'invite_nonce': 'string',
            'invite_source': 'string',
            'funnel_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/moments_link_invite_convert',
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

    def create_moments_universal_link_invite(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'invite_url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/moments_universal_link_invite',
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

    def get_movies(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'target_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/movies',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def get_music(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'target_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/music',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def create_note(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'message': 'string',
            'subject': 'string',
            'privacy': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/notes',
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

    def create_notification(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'seen': 'bool',
            'read': 'bool',
            'notif_ids': 'list<string>',
            'filtering': 'list<filtering_enum>',
            'template': 'Object',
            'href': 'Object',
            'ref': 'string',
            'type': 'type_enum',
        }
        enums = {
            'filtering_enum': User.Filtering.__dict__.values(),
            'type_enum': User.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/notifications',
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

    def get_objects(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.opengraphobject import OpenGraphObject
        param_types = {
            'type': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/objects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OpenGraphObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OpenGraphObject, api=self._api),
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

    def create_object(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.opengraphobject import OpenGraphObject
        param_types = {
            'type': 'string',
            'object': 'Object',
            'action_properties': 'Object',
            'privacy': 'Object',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'proxied_app_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/objects',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=OpenGraphObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=OpenGraphObject, api=self._api),
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

    def create_open_graph_action_feed(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'to': 'string',
            'client_secret': 'string',
            'preview': 'bool',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'proxied_app_id': 'string',
            'user_selected_tags': 'bool',
            'user_selected_place': 'bool',
            'added': 'string',
            'alias': 'string',
            'fb:channel': 'string',
            'created_time': 'datetime',
            'end_time': 'datetime',
            'expires_in': 'unsigned int',
            'fb:explicitly_shared': 'bool',
            'image:height': 'unsigned int',
            'image:secure_url': 'string',
            'image:type': 'string',
            'image:url': 'string',
            'image:user_generated': 'bool',
            'image:width': 'unsigned int',
            'no_feed_story': 'bool',
            'no_action_link': 'bool',
            'notify': 'bool',
            'message': 'string',
            'place': 'string',
            'privacy': 'Object',
            'ref': 'string',
            'scrape': 'bool',
            'start_time': 'datetime',
            'tags': 'list<int>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/opengraphactionfeed',
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

    def create_payment_account_email(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'user_input_email': 'string',
            'default': 'bool',
            'payment_type': 'payment_type_enum',
        }
        enums = {
            'payment_type_enum': [
                'PAYMENT_SETTINGS',
                'IG_PAYMENT_SETTINGS',
                'UNKNOWN',
                'MP_PAYMENT_SETTINGS',
                'IAP_INSTANT_GAME',
                'IAP_FAN_FUNDING',
                'IAP_GROUP_SUBSCRIPTION',
                'MOR_NONE',
                'MOR_ADS_INVOICE',
                'MOR_DONATIONS',
                'MOR_DONATIONS_MATCHING_CONFIRMATION',
                'MOR_DONATIONS_MATCHING_PLEDGE',
                'MOR_OCULUS_CV1',
                'MOR_OCULUS_LAUNCH_V1',
                'MOR_OCULUS_LAUNCH_V2',
                'MOR_OZONE',
                'MOR_OPEN_GRAPH_PRODUCT',
                'MOR_MESSENGER_COMMERCE',
                'MOR_P2P_TRANSFER',
                'MOR_DUMMY_FIRST_PARTY',
                'MOR_DUMMY_THIRD_PARTY',
                'MOR_GIFTS',
                'MOR_BILL',
                'MOR_AIRMAIL',
                'MOR_EVENT_TICKETING',
                'MOR_PAYMENT_LITE',
                'MOR_MESSENGER_API_FEE',
                'MOR_WORKPLACE_USAGE',
                'MOR_FACEBOOK_SHOP',
                'MOR_FAN_FUNDING',
                'MOR_GAME_TIPPING_TOKEN',
                'MOR_INSTANT_GAMES',
                'MOR_BLUEBIRD',
                'MOR_GROUP_SUBSCRIPTION',
                'NMOR_UNKNOWN',
                'NMOR_NONE',
                'NMOR_PAGES_COMMERCE',
                'NMOR_COMPONENT_FLOW',
                'NMOR_BUSINESS_PLATFORM_COMMERCE',
                'NMOR_SYNCHRONOUS_COMPONENT_FLOW',
                'NMOR_EVENT_TICKETING',
                'NMOR_PLATFORM_SELF_SERVE',
                'NMOR_MESSENGER_PLATFORM',
                'NMOR_MESSENGER_OMNIM',
                'NMOR_BILLING_ENGINE',
                'NMOR_TIP_JAR',
                'NMOR_INSTANT_EXPERIENCES',
                'NMOR_CHECKOUT_EXPERIENCES',
                'NMOR_BUY_ON_FACEBOOK',
                'NMOR_PAYMENT_APP',
                'NMOR_DONATION_P4P',
                'NMOR_WHATSAPP_P2P',
                'NMOR_P2P',
                'NMOR_MOBILE_TOP_UP',
                'NMOR_MFS',
                'NMOR_SHIPPING_LABEL',
                'NMOR_MARKETPLACE_DROPOFF',
                'NMOR_PAGES_SOLUTION',
                'NMOR_BLACKBAUD_RWR_DONATION',
                'NMOR_MARKETPLACE_SHIPPING',
                'NMOR_DUMMY',
                'NMOR_PPGF_DONATION',
                'NMOR_ADVERTISER_SUBSCRIPTION',
                'NMOR_WHATSAPP_P2M',
                'NMOR_MOVIE_TICKETING',
                'IG_NMOR_P2B',
                'NMOR_INSTAGRAM_P2B',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/payment_account_emails',
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

    def create_payment_account_phone(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'raw_input': 'string',
            'country_code': 'string',
            'default': 'bool',
            'payment_type': 'payment_type_enum',
        }
        enums = {
            'payment_type_enum': [
                'PAYMENT_SETTINGS',
                'IG_PAYMENT_SETTINGS',
                'UNKNOWN',
                'MP_PAYMENT_SETTINGS',
                'IAP_INSTANT_GAME',
                'IAP_FAN_FUNDING',
                'IAP_GROUP_SUBSCRIPTION',
                'MOR_NONE',
                'MOR_ADS_INVOICE',
                'MOR_DONATIONS',
                'MOR_DONATIONS_MATCHING_CONFIRMATION',
                'MOR_DONATIONS_MATCHING_PLEDGE',
                'MOR_OCULUS_CV1',
                'MOR_OCULUS_LAUNCH_V1',
                'MOR_OCULUS_LAUNCH_V2',
                'MOR_OZONE',
                'MOR_OPEN_GRAPH_PRODUCT',
                'MOR_MESSENGER_COMMERCE',
                'MOR_P2P_TRANSFER',
                'MOR_DUMMY_FIRST_PARTY',
                'MOR_DUMMY_THIRD_PARTY',
                'MOR_GIFTS',
                'MOR_BILL',
                'MOR_AIRMAIL',
                'MOR_EVENT_TICKETING',
                'MOR_PAYMENT_LITE',
                'MOR_MESSENGER_API_FEE',
                'MOR_WORKPLACE_USAGE',
                'MOR_FACEBOOK_SHOP',
                'MOR_FAN_FUNDING',
                'MOR_GAME_TIPPING_TOKEN',
                'MOR_INSTANT_GAMES',
                'MOR_BLUEBIRD',
                'MOR_GROUP_SUBSCRIPTION',
                'NMOR_UNKNOWN',
                'NMOR_NONE',
                'NMOR_PAGES_COMMERCE',
                'NMOR_COMPONENT_FLOW',
                'NMOR_BUSINESS_PLATFORM_COMMERCE',
                'NMOR_SYNCHRONOUS_COMPONENT_FLOW',
                'NMOR_EVENT_TICKETING',
                'NMOR_PLATFORM_SELF_SERVE',
                'NMOR_MESSENGER_PLATFORM',
                'NMOR_MESSENGER_OMNIM',
                'NMOR_BILLING_ENGINE',
                'NMOR_TIP_JAR',
                'NMOR_INSTANT_EXPERIENCES',
                'NMOR_CHECKOUT_EXPERIENCES',
                'NMOR_BUY_ON_FACEBOOK',
                'NMOR_PAYMENT_APP',
                'NMOR_DONATION_P4P',
                'NMOR_WHATSAPP_P2P',
                'NMOR_P2P',
                'NMOR_MOBILE_TOP_UP',
                'NMOR_MFS',
                'NMOR_SHIPPING_LABEL',
                'NMOR_MARKETPLACE_DROPOFF',
                'NMOR_PAGES_SOLUTION',
                'NMOR_BLACKBAUD_RWR_DONATION',
                'NMOR_MARKETPLACE_SHIPPING',
                'NMOR_DUMMY',
                'NMOR_PPGF_DONATION',
                'NMOR_ADVERTISER_SUBSCRIPTION',
                'NMOR_WHATSAPP_P2M',
                'NMOR_MOVIE_TICKETING',
                'IG_NMOR_P2B',
                'NMOR_INSTAGRAM_P2B',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/payment_account_phones',
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

    def delete_permissions(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'permission': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/permissions',
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

    def get_permissions(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.permission import Permission
        param_types = {
            'permission': 'string',
            'status': 'status_enum',
        }
        enums = {
            'status_enum': Permission.Status.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/permissions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Permission,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Permission, api=self._api),
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

    def get_personal_ad_accounts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.adaccount import AdAccount
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/personal_ad_accounts',
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

    def get_photos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.photo import Photo
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': Photo.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/photos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Photo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Photo, api=self._api),
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

    def create_photo(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.photo import Photo
        param_types = {
            'aid': 'string',
            'caption': 'string',
            'url': 'string',
            'uid': 'int',
            'profile_id': 'int',
            'target_id': 'int',
            'checkin_id': 'Object',
            'vault_image_id': 'string',
            'tags': 'list<Object>',
            'place': 'Object',
            'is_explicit_place': 'bool',
            'is_explicit_location': 'bool',
            'og_action_type_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_icon_id': 'string',
            'og_suggestion_mechanism': 'string',
            'og_set_profile_badge': 'bool',
            'privacy': 'Object',
            'targeting': 'Object',
            'feed_targeting': 'Object',
            'no_story': 'bool',
            'published': 'bool',
            'offline_id': 'unsigned int',
            'attempt': 'unsigned int',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'time_since_original_post': 'unsigned int',
            'filter_type': 'unsigned int',
            'scheduled_publish_time': 'unsigned int',
            'unpublished_content_type': 'unpublished_content_type_enum',
            'full_res_is_coming_later': 'bool',
            'composer_session_id': 'string',
            'qn': 'string',
            'manual_privacy': 'bool',
            'audience_exp': 'bool',
            'proxied_app_id': 'string',
            'ios_bundle_id': 'string',
            'android_key_hash': 'string',
            'user_selected_tags': 'bool',
            'allow_spherical_photo': 'bool',
            'spherical_metadata': 'map',
            'initial_view_heading_override_degrees': 'unsigned int',
            'initial_view_pitch_override_degrees': 'unsigned int',
            'initial_view_vertical_fov_override_degrees': 'unsigned int',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
            'sponsor_relationship': 'unsigned int',
            'application_id': 'string',
            'name': 'string',
            'message': 'string',
        }
        enums = {
            'backdated_time_granularity_enum': Photo.BackdatedTimeGranularity.__dict__.values(),
            'unpublished_content_type_enum': Photo.UnpublishedContentType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/photos',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Photo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Photo, api=self._api),
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
        from facebook_business.adobjects.profilepicturesource import ProfilePictureSource
        param_types = {
            'height': 'int',
            'width': 'int',
            'type': 'type_enum',
            'redirect': 'bool',
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
            response_parser=ObjectParser(target_class=ProfilePictureSource, api=self._api),
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

    def create_place(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'type': 'type_enum',
            'coords': 'Object',
            'name': 'string',
            'description': 'string',
            'topics': 'list<string>',
            'uid': 'int',
            'geometry': 'Object',
            'override_ids': 'list<int>',
            'address': 'Object',
            'privacy': 'Object',
            'phone': 'string',
            'website': 'string',
            'city_id': 'string',
            'neighborhood_name': 'string',
            'pin_source': 'string',
            'custom_provider': 'string',
        }
        enums = {
            'type_enum': [
                'PLACE',
                'CITY',
                'STATE_PROVINCE',
                'COUNTRY',
                'EVENT',
                'RESIDENCE',
                'TEXT',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/places',
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

    def get_promotable_domains(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.domain import Domain
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
            response_parser=ObjectParser(target_class=Domain, api=self._api),
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
        from facebook_business.adobjects.event import Event
        param_types = {
            'is_page_event': 'bool',
            'page_id': 'unsigned int',
            'include_past_events': 'bool',
            'promotable_event_types': 'list<promotable_event_types_enum>',
        }
        enums = {
            'promotable_event_types_enum': Event.PromotableEventTypes.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/promotable_events',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Event,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Event, api=self._api),
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

    def get_request_history(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.requesthistory import RequestHistory
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/request_history',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=RequestHistory,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=RequestHistory, api=self._api),
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

    def get_rich_media_documents(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.canvas import Canvas
        param_types = {
            'query': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/rich_media_documents',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Canvas,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Canvas, api=self._api),
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

    def delete_screen_names(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'service_type': 'service_type_enum',
            'value': 'string',
        }
        enums = {
            'service_type_enum': User.ServiceType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/screennames',
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

    def create_screen_name(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'service_type': 'service_type_enum',
            'value': 'string',
        }
        enums = {
            'service_type_enum': User.ServiceType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/screennames',
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

    def get_session_keys(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.platformsessionkey import PlatformSessionKey
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/session_keys',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PlatformSessionKey,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PlatformSessionKey, api=self._api),
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

    def create_staging_resource(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'file': 'file',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/stagingresources',
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

    def get_stream_filters(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.streamfilter import StreamFilter
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/stream_filters',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=StreamFilter,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=StreamFilter, api=self._api),
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

    def create_subscription(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'object': 'string',
            'fields': 'list<string>',
            'callback_url': 'Object',
            'verify_token': 'string',
            'include_values': 'bool',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/subscriptions',
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

    def get_taggable_friends(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.usertaggablefriend import UserTaggableFriend
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/taggable_friends',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UserTaggableFriend,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UserTaggableFriend, api=self._api),
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

    def get_tagged_places(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.placetag import PlaceTag
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tagged_places',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PlaceTag,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PlaceTag, api=self._api),
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

    def get_television(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.page import Page
        param_types = {
            'target_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/television',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def get_threads(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.unifiedthread import UnifiedThread
        param_types = {
            'tags': 'list<string>',
            'folder': 'string',
            'psid': 'Object',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/threads',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=UnifiedThread,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=UnifiedThread, api=self._api),
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

    def get_video_broadcasts(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.livevideo import LiveVideo
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/video_broadcasts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=LiveVideo,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=LiveVideo, api=self._api),
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

    def get_videos(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': AdVideo.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/videos',
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

    def create_video(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.advideo import AdVideo
        param_types = {
            'title': 'string',
            'source': 'string',
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
            'privacy': 'Object',
            'no_story': 'bool',
            'sponsor_id': 'string',
            'direct_share_status': 'unsigned int',
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
            endpoint='/videos',
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

    _field_types = {
        'about': 'string',
        'address': 'Location',
        'admin_notes': 'list<PageAdminNote>',
        'age_range': 'AgeRange',
        'bio': 'string',
        'birthday': 'string',
        'can_review_measurement_request': 'bool',
        'context': 'UserContext',
        'cover': 'UserCoverPhoto',
        'currency': 'Currency',
        'devices': 'list<UserDevice>',
        'education': 'list<EducationExperience>',
        'email': 'string',
        'employee_number': 'string',
        'favorite_athletes': 'list<Experience>',
        'favorite_teams': 'list<Experience>',
        'first_name': 'string',
        'gender': 'string',
        'hometown': 'Page',
        'id': 'string',
        'inspirational_people': 'list<Experience>',
        'install_type': 'string',
        'installed': 'bool',
        'interested_in': 'list<string>',
        'is_famedeeplinkinguser': 'bool',
        'is_shared_login': 'bool',
        'is_verified': 'bool',
        'labels': 'list<PageLabel>',
        'languages': 'list<Experience>',
        'last_name': 'string',
        'link': 'string',
        'local_news_megaphone_dismiss_status': 'bool',
        'local_news_subscription_status': 'bool',
        'locale': 'string',
        'location': 'Page',
        'meeting_for': 'list<string>',
        'middle_name': 'string',
        'name': 'string',
        'name_format': 'string',
        'payment_pricepoints': 'PaymentPricepoints',
        'political': 'string',
        'profile_pic': 'string',
        'public_key': 'string',
        'quotes': 'string',
        'relationship_status': 'string',
        'religion': 'string',
        'security_settings': 'SecuritySettings',
        'shared_login_upgrade_required_by': 'datetime',
        'short_name': 'string',
        'significant_other': 'User',
        'sports': 'list<Experience>',
        'test_group': 'unsigned int',
        'third_party_id': 'string',
        'timezone': 'float',
        'token_for_business': 'string',
        'updated_time': 'datetime',
        'username': 'string',
        'verified': 'bool',
        'video_upload_limits': 'VideoUploadLimits',
        'viewer_can_send_gift': 'bool',
        'website': 'string',
        'work': 'list<WorkExperience>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Tasks'] = User.Tasks.__dict__.values()
        field_enum_info['LocalNewsMegaphoneDismissStatus'] = User.LocalNewsMegaphoneDismissStatus.__dict__.values()
        field_enum_info['LocalNewsSubscriptionStatus'] = User.LocalNewsSubscriptionStatus.__dict__.values()
        field_enum_info['ResumeType'] = User.ResumeType.__dict__.values()
        field_enum_info['Filtering'] = User.Filtering.__dict__.values()
        field_enum_info['Type'] = User.Type.__dict__.values()
        field_enum_info['ServiceType'] = User.ServiceType.__dict__.values()
        return field_enum_info


