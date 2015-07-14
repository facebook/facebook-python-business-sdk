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

from facebookads import test_config as config

ad_account_id = config.account_id

# _DOC open [SEARCH_GEOLOCATION_WITH_COUNTRY]
from facebookads.objects import TargetingSearch
params = {
    'q': 'un',
    'type': 'adgeolocation',
    'location_types': ['country'],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_GEOLOCATION_WITH_COUNTRY]

# _DOC open [SEARCH_GEOLOCATION_WITH_REGION]
from facebookads.objects import TargetingSearch
params = {
    'q': 'al',
    'type': 'adgeolocation',
    'location_types': ['region'],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_GEOLOCATION_WITH_REGION]

# _DOC open [SEARCH_GEOLOCATION_WITH_CITY]
from facebookads.objects import TargetingSearch
params = {
    'q': 'dub',
    'type': 'adgeolocation',
    'location_types': ['city'],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_GEOLOCATION_WITH_CITY]

# _DOC open [SEARCH_GEOLOCATION_WITH_ZIP]
from facebookads.objects import TargetingSearch
params = {
    'q': '9',
    'type': 'adgeolocation',
    'location_types': ['zip'],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_GEOLOCATION_WITH_ZIP]

# _DOC open [SEARCH_GEOLOCATION_WITH_GEO_MARKET]
from facebookads.objects import TargetingSearch
params = {
    'q': 'New',
    'type': 'adgeolocation',
    'location_types': ['geo_market'],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_GEOLOCATION_WITH_GEO_MARKET]

# _DOC open [SEARCH_LOCATIONS_METADATA]
from facebookads.objects import TargetingSearch
params = {
    'type': 'adgeolocationmeta',
    'cities': [2418779],
    'zips': ['US:90210'],
    'countries': ['US', 'JP'],
    'regions': [10],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_LOCATIONS_METADATA]

# _DOC open [SEARCH_RADIUS_SUGGESTION]
from facebookads.objects import TargetingSearch
params = {
    'type': 'adradiussuggestion',
    'latitude': 37.449478,
    'longitude': -122.173016,
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_RADIUS_SUGGESTION]

# _DOC open [SEARCH_RADIUS_SUGGESTION_WITH_KILOMETER]
from facebookads.objects import TargetingSearch
params = {
    'type': 'adradiussuggestion',
    'latitude': 37.449478,
    'longitude': -122.173016,
    'distance_unit': 'kilometer',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_RADIUS_SUGGESTION_WITH_KILOMETER]

# _DOC open [SEARCH_INTEREST]
from facebookads.objects import TargetingSearch
params = {
    'q': 'baseball',
    'type': 'adinterest',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_INTEREST]

# _DOC open [SEARCH_INTEREST_SUGGESTION]
from facebookads.objects import TargetingSearch
params = {
    'type': 'adinterestsuggestion',
    'interest_list': ['soccer'],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_INTEREST_SUGGESTION]

# _DOC open [SEARCH_VALIDATION]
from facebookads.objects import TargetingSearch
params = {
    'type': 'adinterestvalid',
    'interest_list': ['Japan', 'nonexistantkeyword'],
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_VALIDATION]

# _DOC open [SEARCH_TARGETING_CATEGORY_WITH_INTERESTS]
from facebookads.objects import TargetingSearch
params = {
    'type': 'adTargetingCategory',
    'class': 'interests',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_TARGETING_CATEGORY_WITH_INTERESTS]

# _DOC open [SEARCH_TARGETING_CATEGORY_WITH_BEHAVIORS]
from facebookads.objects import TargetingSearch
params = {
    'type': 'adTargetingCategory',
    'class': 'behaviors',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_TARGETING_CATEGORY_WITH_BEHAVIORS]

# _DOC open [SEARCH_LOCALE]
from facebookads.objects import TargetingSearch
params = {
    'q': 'en',
    'type': 'adlocale',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_LOCALE]

# _DOC open [SEARCH_EDUCATION_SCHOOL]
from facebookads.objects import TargetingSearch
params = {
    'q': 'ha',
    'type': 'adeducationschool',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_EDUCATION_SCHOOL]

# _DOC open [SEARCH_EDUCATION_MAJOR]
from facebookads.objects import TargetingSearch
params = {
    'q': 'ph',
    'type': 'adeducationmajor',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_EDUCATION_MAJOR]

# _DOC open [SEARCH_WORK_EMPLOYER]
from facebookads.objects import TargetingSearch
params = {
    'q': 'mic',
    'type': 'adworkemployer',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_WORK_EMPLOYER]

# _DOC open [SEARCH_WORK_POSITION]
from facebookads.objects import TargetingSearch
params = {
    'q': 'ana',
    'type': 'adworkposition',
}

resp = TargetingSearch.search(params=params)
print(resp)
# _DOC close [SEARCH_WORK_POSITION]
