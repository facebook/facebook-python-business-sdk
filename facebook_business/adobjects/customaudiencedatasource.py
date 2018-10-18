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

class CustomAudienceDataSource(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCustomAudienceDataSource = True
        super(CustomAudienceDataSource, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        creation_params = 'creation_params'
        sub_type = 'sub_type'
        type = 'type'
        id = 'id'

    class SubType:
        anything = 'ANYTHING'
        nothing = 'NOTHING'
        hashes = 'HASHES'
        user_ids = 'USER_IDS'
        hashes_or_user_ids = 'HASHES_OR_USER_IDS'
        mobile_advertiser_ids = 'MOBILE_ADVERTISER_IDS'
        external_ids = 'EXTERNAL_IDS'
        multi_hashes = 'MULTI_HASHES'
        tokens = 'TOKENS'
        external_ids_mix = 'EXTERNAL_IDS_MIX'
        household_expansion = 'HOUSEHOLD_EXPANSION'
        web_pixel_hits = 'WEB_PIXEL_HITS'
        mobile_app_events = 'MOBILE_APP_EVENTS'
        mobile_app_combination_events = 'MOBILE_APP_COMBINATION_EVENTS'
        video_events = 'VIDEO_EVENTS'
        web_pixel_combination_events = 'WEB_PIXEL_COMBINATION_EVENTS'
        platform = 'PLATFORM'
        multi_data_events = 'MULTI_DATA_EVENTS'
        ig_business_events = 'IG_BUSINESS_EVENTS'
        store_visit_events = 'STORE_VISIT_EVENTS'
        instant_article_events = 'INSTANT_ARTICLE_EVENTS'
        fb_event_signals = 'FB_EVENT_SIGNALS'
        engagement_event_users = 'ENGAGEMENT_EVENT_USERS'
        custom_audience_users = 'CUSTOM_AUDIENCE_USERS'
        page_fans = 'PAGE_FANS'
        conversion_pixel_hits = 'CONVERSION_PIXEL_HITS'
        app_users = 'APP_USERS'
        s_expr = 'S_EXPR'
        dynamic_rule = 'DYNAMIC_RULE'
        campaign_conversions = 'CAMPAIGN_CONVERSIONS'
        web_pixel_hits_custom_audience_users = 'WEB_PIXEL_HITS_CUSTOM_AUDIENCE_USERS'
        mobile_app_custom_audience_users = 'MOBILE_APP_CUSTOM_AUDIENCE_USERS'
        combination_custom_audience_users = 'COMBINATION_CUSTOM_AUDIENCE_USERS'
        video_event_users = 'VIDEO_EVENT_USERS'
        fb_pixel_hits = 'FB_PIXEL_HITS'
        ig_promoted_post = 'IG_PROMOTED_POST'
        place_visits = 'PLACE_VISITS'
        offline_event_users = 'OFFLINE_EVENT_USERS'
        expanded_audience = 'EXPANDED_AUDIENCE'
        seed_list = 'SEED_LIST'
        partner_category_users = 'PARTNER_CATEGORY_USERS'
        page_smart_audience = 'PAGE_SMART_AUDIENCE'
        multicountry_combination = 'MULTICOUNTRY_COMBINATION'
        platform_users = 'PLATFORM_USERS'
        multi_event_source = 'MULTI_EVENT_SOURCE'
        smart_audience = 'SMART_AUDIENCE'
        lookalike_platform = 'LOOKALIKE_PLATFORM'
        mail_chimp_email_hashes = 'MAIL_CHIMP_EMAIL_HASHES'
        constant_contacts_email_hashes = 'CONSTANT_CONTACTS_EMAIL_HASHES'
        copy_paste_email_hashes = 'COPY_PASTE_EMAIL_HASHES'
        contact_importer = 'CONTACT_IMPORTER'
        data_file = 'DATA_FILE'

    class Type:
        unknown = 'UNKNOWN'
        file_imported = 'FILE_IMPORTED'
        event_based = 'EVENT_BASED'
        seed_based = 'SEED_BASED'
        third_party_imported = 'THIRD_PARTY_IMPORTED'
        copy_paste = 'COPY_PASTE'
        contact_importer = 'CONTACT_IMPORTER'
        household_audience = 'HOUSEHOLD_AUDIENCE'

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
            target_class=CustomAudienceDataSource,
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
        'creation_params': 'string',
        'sub_type': 'SubType',
        'type': 'Type',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['SubType'] = CustomAudienceDataSource.SubType.__dict__.values()
        field_enum_info['Type'] = CustomAudienceDataSource.Type.__dict__.values()
        return field_enum_info


