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

class AdAccountTargetingUnified(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountTargetingUnified = True
        super(AdAccountTargetingUnified, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        audience_size = 'audience_size'
        description = 'description'
        id = 'id'
        is_recommendation = 'is_recommendation'
        name = 'name'
        path = 'path'
        recommendation_model = 'recommendation_model'
        search_interest_id = 'search_interest_id'
        type = 'type'
        valid = 'valid'

    class LimitType:
        adgroup_id = 'adgroup_id'
        genders = 'genders'
        age_min = 'age_min'
        age_max = 'age_max'
        country_groups = 'country_groups'
        countries = 'countries'
        country = 'country'
        cities = 'cities'
        radius = 'radius'
        regions = 'regions'
        zips = 'zips'
        interests = 'interests'
        keywords = 'keywords'
        education_schools = 'education_schools'
        education_majors = 'education_majors'
        work_positions = 'work_positions'
        work_employers = 'work_employers'
        relationship_statuses = 'relationship_statuses'
        interested_in = 'interested_in'
        locales = 'locales'
        user_adclusters = 'user_adclusters'
        excluded_user_adclusters = 'excluded_user_adclusters'
        conjunctive_user_adclusters = 'conjunctive_user_adclusters'
        custom_audiences = 'custom_audiences'
        excluded_custom_audiences = 'excluded_custom_audiences'
        college_years = 'college_years'
        education_statuses = 'education_statuses'
        connections = 'connections'
        excluded_connections = 'excluded_connections'
        friends_of_connections = 'friends_of_connections'
        user_event = 'user_event'
        dynamic_audience_ids = 'dynamic_audience_ids'
        excluded_dynamic_audience_ids = 'excluded_dynamic_audience_ids'
        rtb_flag = 'rtb_flag'
        site_category = 'site_category'
        geo_locations = 'geo_locations'
        excluded_geo_locations = 'excluded_geo_locations'
        timezones = 'timezones'
        place_page_set_ids = 'place_page_set_ids'
        page_types = 'page_types'
        publisher_platforms = 'publisher_platforms'
        effective_publisher_platforms = 'effective_publisher_platforms'
        facebook_positions = 'facebook_positions'
        effective_facebook_positions = 'effective_facebook_positions'
        instagram_positions = 'instagram_positions'
        effective_instagram_positions = 'effective_instagram_positions'
        messenger_positions = 'messenger_positions'
        effective_messenger_positions = 'effective_messenger_positions'
        device_platforms = 'device_platforms'
        effective_device_platforms = 'effective_device_platforms'
        audience_network_positions = 'audience_network_positions'
        effective_audience_network_positions = 'effective_audience_network_positions'
        excluded_publisher_categories = 'excluded_publisher_categories'
        excluded_publisher_list_ids = 'excluded_publisher_list_ids'
        publisher_visibility_categories = 'publisher_visibility_categories'
        user_device = 'user_device'
        mobile_device_model = 'mobile_device_model'
        excluded_user_device = 'excluded_user_device'
        excluded_mobile_device_model = 'excluded_mobile_device_model'
        user_os = 'user_os'
        wireless_carrier = 'wireless_carrier'
        family_statuses = 'family_statuses'
        industries = 'industries'
        life_events = 'life_events'
        political_views = 'political_views'
        politics = 'politics'
        behaviors = 'behaviors'
        income = 'income'
        net_worth = 'net_worth'
        home_type = 'home_type'
        home_ownership = 'home_ownership'
        home_value = 'home_value'
        ethnic_affinity = 'ethnic_affinity'
        generation = 'generation'
        household_composition = 'household_composition'
        moms = 'moms'
        office_type = 'office_type'
        targeting_optimization = 'targeting_optimization'
        direct_install_devices = 'direct_install_devices'
        engagement_specs = 'engagement_specs'
        excluded_engagement_specs = 'excluded_engagement_specs'
        product_audience_specs = 'product_audience_specs'
        excluded_product_audience_specs = 'excluded_product_audience_specs'
        exclusions = 'exclusions'
        flexible_spec = 'flexible_spec'
        exclude_reached_since = 'exclude_reached_since'
        exclude_previous_days = 'exclude_previous_days'
        app_install_state = 'app_install_state'
        fb_deal_id = 'fb_deal_id'
        interest_defaults_source = 'interest_defaults_source'
        alternate_auto_targeting_option = 'alternate_auto_targeting_option'
        contextual_targeting_categories = 'contextual_targeting_categories'
        topic = 'topic'
        format = 'format'
        trending = 'trending'
        gatekeepers = 'gatekeepers'
        follow_profiles = 'follow_profiles'
        follow_profiles_negative = 'follow_profiles_negative'
        location_categories = 'location_categories'
        user_page_threads = 'user_page_threads'
        user_page_threads_excluded = 'user_page_threads_excluded'
        is_whatsapp_destination_ad = 'is_whatsapp_destination_ad'
        marketplace_product_categories = 'marketplace_product_categories'
        instream_video_sponsorship_placements = 'instream_video_sponsorship_placements'

    _field_types = {
        'audience_size': 'unsigned int',
        'description': 'string',
        'id': 'string',
        'is_recommendation': 'bool',
        'name': 'string',
        'path': 'list<string>',
        'recommendation_model': 'string',
        'search_interest_id': 'string',
        'type': 'string',
        'valid': 'bool',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['LimitType'] = AdAccountTargetingUnified.LimitType.__dict__.values()
        return field_enum_info
