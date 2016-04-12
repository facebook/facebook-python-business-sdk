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

from facebookads.adobjects.leadgenform import LeadgenForm
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker
from facebookads.mixins import (
    CannotCreate,
    CannotDelete,
    CannotUpdate,
)

class Page(CannotCreate, CannotDelete, CannotUpdate, AbstractCrudObject):

    class Field(object):
        id = 'id'
        name = 'name'
        category = 'category'
        access_token = 'access_token'
        location = 'location'
        website = 'website'
        phone = 'phone'

    class Location(object):
        city = 'city'
        country = 'country'
        latitude = 'latitude'
        longitude = 'longitude'
        street = 'street'
        zip = 'zip'

    @classmethod
    def get_endpoint(cls):
        return 'accounts'

    def get_leadgen_forms(self, fields=None, params=None):
        """
        Returns all leadgen forms on the page
        """
        return self.iterate_edge(LeadgenForm, fields, params, endpoint='leadgen_forms')
