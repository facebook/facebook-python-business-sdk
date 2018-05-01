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
from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookBadObjectError
from facebook_business.session import FacebookSession

class TargetingSearch(AbstractObject):

    class DemographicSearchClasses(object):
        demographics = 'demographics'
        ethnic_affinity = 'ethnic_affinity'
        family_statuses = 'family_statuses'
        generation = 'generation'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        income = 'income'
        industries = 'industries'
        life_events = 'life_events'
        markets = 'markets'
        moms = 'moms'
        net_worth = 'net_worth'
        office_type = 'office_type'
        politics = 'politics'

    class TargetingSearchTypes(object):
        country = 'adcountry'
        education = 'adeducationschool'
        employer = 'adworkemployer'
        geolocation = 'adgeolocation'
        geometadata = 'adgeolocationmeta'
        interest = 'adinterest'
        interest_suggestion = 'adinterestsuggestion'
        interest_validate = 'adinterestvalid'
        keyword = 'adkeyword'
        locale = 'adlocale'
        major = 'adeducationmajor'
        position = 'adworkposition'
        radius_suggestion = 'adradiussuggestion'
        targeting_category = 'adtargetingcategory'
        zipcode = 'adzipcode'

    @classmethod
    def search(cls, params=None, api=None):
        api = api or FacebookAdsApi.get_default_api()
        if not api:
            raise FacebookBadObjectError(
                "An Api instance must be provided as an argument or set as "
                "the default Api in FacebookAdsApi.",
            )

        params = {} if not params else params.copy()
        response = api.call(
            FacebookAdsApi.HTTP_METHOD_GET,
            "/".join((
                FacebookSession.GRAPH,
                FacebookAdsApi.API_VERSION,
                'search'
            )),
            params,
        ).json()

        ret_val = []
        if response:
            keys = response['data']
            # The response object can be either a dictionary of dictionaries
            # or a dictionary of lists.
            if isinstance(keys, list):
                for item in keys:
                    search_obj = TargetingSearch()
                    search_obj.update(item)
                    ret_val.append(search_obj)
            elif isinstance(keys, dict):
                for item in keys:
                    search_obj = TargetingSearch()
                    search_obj.update(keys[item])
                    if keys[item]:
                        ret_val.append(search_obj)
        return ret_val
