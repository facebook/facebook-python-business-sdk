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

class Targeting(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isTargeting = True
        super(Targeting, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        adgroup_id = 'adgroup_id'
        age_max = 'age_max'
        age_min = 'age_min'
        alternate_auto_targeting_option = 'alternate_auto_targeting_option'
        app_install_state = 'app_install_state'
        audience_network_positions = 'audience_network_positions'
        behaviors = 'behaviors'
        cities = 'cities'
        college_years = 'college_years'
        connections = 'connections'
        contextual_targeting_categories = 'contextual_targeting_categories'
        countries = 'countries'
        country = 'country'
        country_groups = 'country_groups'
        custom_audiences = 'custom_audiences'
        device_platforms = 'device_platforms'
        direct_install_devices = 'direct_install_devices'
        dynamic_audience_ids = 'dynamic_audience_ids'
        education_majors = 'education_majors'
        education_schools = 'education_schools'
        education_statuses = 'education_statuses'
        effective_audience_network_positions = 'effective_audience_network_positions'
        effective_device_platforms = 'effective_device_platforms'
        effective_facebook_positions = 'effective_facebook_positions'
        effective_instagram_positions = 'effective_instagram_positions'
        effective_messenger_positions = 'effective_messenger_positions'
        effective_publisher_platforms = 'effective_publisher_platforms'
        engagement_specs = 'engagement_specs'
        ethnic_affinity = 'ethnic_affinity'
        exclude_reached_since = 'exclude_reached_since'
        excluded_connections = 'excluded_connections'
        excluded_custom_audiences = 'excluded_custom_audiences'
        excluded_dynamic_audience_ids = 'excluded_dynamic_audience_ids'
        excluded_engagement_specs = 'excluded_engagement_specs'
        excluded_geo_locations = 'excluded_geo_locations'
        excluded_mobile_device_model = 'excluded_mobile_device_model'
        excluded_product_audience_specs = 'excluded_product_audience_specs'
        excluded_publisher_categories = 'excluded_publisher_categories'
        excluded_publisher_list_ids = 'excluded_publisher_list_ids'
        excluded_user_device = 'excluded_user_device'
        exclusions = 'exclusions'
        facebook_positions = 'facebook_positions'
        family_statuses = 'family_statuses'
        fb_deal_id = 'fb_deal_id'
        flexible_spec = 'flexible_spec'
        friends_of_connections = 'friends_of_connections'
        genders = 'genders'
        generation = 'generation'
        geo_locations = 'geo_locations'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        income = 'income'
        industries = 'industries'
        instagram_positions = 'instagram_positions'
        instream_video_sponsorship_placements = 'instream_video_sponsorship_placements'
        interested_in = 'interested_in'
        interests = 'interests'
        is_whatsapp_destination_ad = 'is_whatsapp_destination_ad'
        keywords = 'keywords'
        life_events = 'life_events'
        locales = 'locales'
        messenger_positions = 'messenger_positions'
        moms = 'moms'
        net_worth = 'net_worth'
        office_type = 'office_type'
        page_types = 'page_types'
        place_page_set_ids = 'place_page_set_ids'
        political_views = 'political_views'
        politics = 'politics'
        product_audience_specs = 'product_audience_specs'
        prospecting_audience = 'prospecting_audience'
        publisher_platforms = 'publisher_platforms'
        publisher_visibility_categories = 'publisher_visibility_categories'
        radius = 'radius'
        regions = 'regions'
        relationship_statuses = 'relationship_statuses'
        rtb_flag = 'rtb_flag'
        site_category = 'site_category'
        targeting_optimization = 'targeting_optimization'
        user_adclusters = 'user_adclusters'
        user_device = 'user_device'
        user_event = 'user_event'
        user_os = 'user_os'
        wireless_carrier = 'wireless_carrier'
        work_employers = 'work_employers'
        work_positions = 'work_positions'
        zips = 'zips'
        id = 'id'

    class DevicePlatforms:
        mobile = 'mobile'
        desktop = 'desktop'
        connected_tv = 'connected_tv'

    class EffectiveDevicePlatforms:
        mobile = 'mobile'
        desktop = 'desktop'
        connected_tv = 'connected_tv'

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
            target_class=Targeting,
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
        'adgroup_id': 'string',
        'age_max': 'unsigned int',
        'age_min': 'unsigned int',
        'alternate_auto_targeting_option': 'string',
        'app_install_state': 'string',
        'audience_network_positions': 'list<string>',
        'behaviors': 'list<IDName>',
        'cities': 'list<IDName>',
        'college_years': 'list<unsigned int>',
        'connections': 'list<IDName>',
        'contextual_targeting_categories': 'list<IDName>',
        'countries': 'list<string>',
        'country': 'list<string>',
        'country_groups': 'list<string>',
        'custom_audiences': 'list<RawCustomAudience>',
        'device_platforms': 'list<DevicePlatforms>',
        'direct_install_devices': 'bool',
        'dynamic_audience_ids': 'list<string>',
        'education_majors': 'list<IDName>',
        'education_schools': 'list<IDName>',
        'education_statuses': 'list<unsigned int>',
        'effective_audience_network_positions': 'list<string>',
        'effective_device_platforms': 'list<EffectiveDevicePlatforms>',
        'effective_facebook_positions': 'list<string>',
        'effective_instagram_positions': 'list<string>',
        'effective_messenger_positions': 'list<string>',
        'effective_publisher_platforms': 'list<string>',
        'engagement_specs': 'list<TargetingDynamicRule>',
        'ethnic_affinity': 'list<IDName>',
        'exclude_reached_since': 'list<string>',
        'excluded_connections': 'list<IDName>',
        'excluded_custom_audiences': 'list<IDName>',
        'excluded_dynamic_audience_ids': 'list<string>',
        'excluded_engagement_specs': 'list<TargetingDynamicRule>',
        'excluded_geo_locations': 'TargetingGeoLocation',
        'excluded_mobile_device_model': 'list<string>',
        'excluded_product_audience_specs': 'list<TargetingProductAudienceSpec>',
        'excluded_publisher_categories': 'list<string>',
        'excluded_publisher_list_ids': 'list<string>',
        'excluded_user_device': 'list<string>',
        'exclusions': 'FlexibleTargeting',
        'facebook_positions': 'list<string>',
        'family_statuses': 'list<IDName>',
        'fb_deal_id': 'string',
        'flexible_spec': 'list<FlexibleTargeting>',
        'friends_of_connections': 'list<IDName>',
        'genders': 'list<unsigned int>',
        'generation': 'list<IDName>',
        'geo_locations': 'TargetingGeoLocation',
        'home_ownership': 'list<IDName>',
        'home_type': 'list<IDName>',
        'home_value': 'list<IDName>',
        'household_composition': 'list<IDName>',
        'income': 'list<IDName>',
        'industries': 'list<IDName>',
        'instagram_positions': 'list<string>',
        'instream_video_sponsorship_placements': 'list<string>',
        'interested_in': 'list<unsigned int>',
        'interests': 'list<IDName>',
        'is_whatsapp_destination_ad': 'bool',
        'keywords': 'list<string>',
        'life_events': 'list<IDName>',
        'locales': 'list<unsigned int>',
        'messenger_positions': 'list<string>',
        'moms': 'list<IDName>',
        'net_worth': 'list<IDName>',
        'office_type': 'list<IDName>',
        'page_types': 'list<string>',
        'place_page_set_ids': 'list<string>',
        'political_views': 'list<unsigned int>',
        'politics': 'list<IDName>',
        'product_audience_specs': 'list<TargetingProductAudienceSpec>',
        'prospecting_audience': 'TargetingProspectingAudience',
        'publisher_platforms': 'list<string>',
        'publisher_visibility_categories': 'list<string>',
        'radius': 'string',
        'regions': 'list<IDName>',
        'relationship_statuses': 'list<unsigned int>',
        'rtb_flag': 'bool',
        'site_category': 'list<string>',
        'targeting_optimization': 'string',
        'user_adclusters': 'list<IDName>',
        'user_device': 'list<string>',
        'user_event': 'list<unsigned int>',
        'user_os': 'list<string>',
        'wireless_carrier': 'list<string>',
        'work_employers': 'list<IDName>',
        'work_positions': 'list<IDName>',
        'zips': 'list<string>',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DevicePlatforms'] = Targeting.DevicePlatforms.__dict__.values()
        field_enum_info['EffectiveDevicePlatforms'] = Targeting.EffectiveDevicePlatforms.__dict__.values()
        return field_enum_info


