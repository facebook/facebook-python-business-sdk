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

from __future__ import print_function
from __future__ import unicode_literals
from facebookads.objects import TargetingSearch
from facebookads.api import FacebookAdsApi
from facebookads.exceptions import *

config_file = open('./examples/docs/config.json')
config = json.load(config_file)
config_file.close()

account_id = config['account_id']
access_token = config['access_token']
app_id = config['app_id']
app_secret = config['app_secret']

FacebookAdsApi.init(app_id, app_secret, access_token)

#_DOC open [TGT_SEARCH_COUNTRY_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'un',
    'type': 'adgeolocation',
    'location_types': ['country'],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_COUNTRY_EXAMPLE]

#_DOC open [TGT_SEARCH_REGION_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'al',
    'type': 'adgeolocation',
    'location_types': ['region'],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_REGION_EXAMPLE]

#_DOC open [TGT_SEARCH_CITY_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'dub',
    'type': 'adgeolocation',
    'location_types': ['city'],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_CITY_EXAMPLE]

#_DOC open [TGT_SEARCH_ZIP_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': '9',
    'type': 'adgeolocation',
    'location_types': ['zip'],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_ZIP_EXAMPLE]

#_DOC open [TGT_SEARCH_GEO_MARKET_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'New',
    'type': 'adgeolocation',
    'location_types': ['geo_market'],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_GEO_MARKET_EXAMPLE]

#_DOC open [TGT_SEARCH_LOC_METADATA_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'type': 'adgeolocationmeta',
    'cities': [2418779],
    'zips': ['US:90210'],
    'countries': ['US', 'JP'],
    'regions': [10],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_LOC_METADATA_EXAMPLE]

#_DOC open [TGT_SEARCH_RADIUS_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'type': 'adradiussuggestion',
    'latitude': 37.449478,
    'longitude': -122.173016,
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_RADIUS_EXAMPLE

#_DOC open [TGT_SEARCH_RADIUS_KM_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'type': 'adradiussuggestion',
    'latitude': 37.449478,
    'longitude': -122.173016,
    'distance_unit': 'kilometer',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_RADIUS_KM_EXAMPLE

#_DOC open [TGT_SEARCH_INTEREST_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'baseball',
    'type': 'adinterest',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_INTEREST_EXAMPLE

#_DOC open [TGT_SEARCH_SUGGESTION_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'type': 'adinterestsuggestion',
    'interest_list': ['soccer'],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_SUGGESTION_EXAMPLE

#_DOC open [TGT_SEARCH_VALIDATION_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'type': 'adinterestvalid',
    'interest_list': ['Japan', 'nonexistantkeyword'],
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_VALIDATION_EXAMPLE]

#_DOC open [TGT_SEARCH_BROWSE_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'type': 'adTargetingCategory',
    'class': 'interests',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_BROWSE_EXAMPLE]

#_DOC open [TGT_SEARCH_BEHAVIOR_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'type': 'adTargetingCategory',
    'class': 'behaviors',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_BEHAVIOR_EXAMPLE]

#_DOC open [TGT_SEARCH_LOCALE_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'en',
    'type': 'adlocale',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_LOCALE_EXAMPLE]

#_DOC open [TGT_SEARCH_SCHOOL_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'ha',
    'type': 'adeducationschool',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_SCHOOL_EXAMPLE]

#_DOC open [TGT_SEARCH_EDUCATION_MAJOR_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'ph',
    'type': 'adeducationmajor',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_EDUCATION_MAJOR_EXAMPLE]

#_DOC open [TGT_SEARCH_WORK_EMPLOYER_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'mic',
    'type': 'adworkemployer',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_WORK_EMPLOYER_EXAMPLE]

#_DOC open [TGT_SEARCH_JOB_TITLE_EXAMPLE]
#from facebookads.objects import TargetingSearch
params = {
    'q': 'ana',
    'type': 'adworkposition',
}

resp = TargetingSearch.search(params=params)
print(resp)
#_DOC close [TGT_SEARCH_JOB_TITLE_EXAMPLE]
