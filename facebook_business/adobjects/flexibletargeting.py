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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class FlexibleTargeting(
    AbstractObject,
):

    def __init__(self, api=None):
        super(FlexibleTargeting, self).__init__()
        self._isFlexibleTargeting = True
        self._api = api

    class Field(AbstractObject.Field):
        behaviors = 'behaviors'
        college_years = 'college_years'
        connections = 'connections'
        custom_audiences = 'custom_audiences'
        education_majors = 'education_majors'
        education_schools = 'education_schools'
        education_statuses = 'education_statuses'
        ethnic_affinity = 'ethnic_affinity'
        family_statuses = 'family_statuses'
        friends_of_connections = 'friends_of_connections'
        generation = 'generation'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        income = 'income'
        industries = 'industries'
        interested_in = 'interested_in'
        interests = 'interests'
        life_events = 'life_events'
        moms = 'moms'
        net_worth = 'net_worth'
        office_type = 'office_type'
        politics = 'politics'
        relationship_statuses = 'relationship_statuses'
        user_adclusters = 'user_adclusters'
        work_employers = 'work_employers'
        work_positions = 'work_positions'

    _field_types = {
        'behaviors': 'list<IDName>',
        'college_years': 'list<unsigned int>',
        'connections': 'list<IDName>',
        'custom_audiences': 'list<IDName>',
        'education_majors': 'list<IDName>',
        'education_schools': 'list<IDName>',
        'education_statuses': 'list<unsigned int>',
        'ethnic_affinity': 'list<IDName>',
        'family_statuses': 'list<IDName>',
        'friends_of_connections': 'list<IDName>',
        'generation': 'list<IDName>',
        'home_ownership': 'list<IDName>',
        'home_type': 'list<IDName>',
        'home_value': 'list<IDName>',
        'household_composition': 'list<IDName>',
        'income': 'list<IDName>',
        'industries': 'list<IDName>',
        'interested_in': 'list<unsigned int>',
        'interests': 'list<IDName>',
        'life_events': 'list<IDName>',
        'moms': 'list<IDName>',
        'net_worth': 'list<IDName>',
        'office_type': 'list<IDName>',
        'politics': 'list<IDName>',
        'relationship_statuses': 'list<unsigned int>',
        'user_adclusters': 'list<IDName>',
        'work_employers': 'list<IDName>',
        'work_positions': 'list<IDName>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


