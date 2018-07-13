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

class AgencyClientDeclaration(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AgencyClientDeclaration, self).__init__()
        self._isAgencyClientDeclaration = True
        self._api = api

    class Field(AbstractObject.Field):
        agency_representing_client = 'agency_representing_client'
        client_based_in_france = 'client_based_in_france'
        client_city = 'client_city'
        client_country_code = 'client_country_code'
        client_email_address = 'client_email_address'
        client_name = 'client_name'
        client_postal_code = 'client_postal_code'
        client_province = 'client_province'
        client_street = 'client_street'
        client_street2 = 'client_street2'
        has_written_mandate_from_advertiser = 'has_written_mandate_from_advertiser'
        is_client_paying_invoices = 'is_client_paying_invoices'

    _field_types = {
        'agency_representing_client': 'unsigned int',
        'client_based_in_france': 'unsigned int',
        'client_city': 'string',
        'client_country_code': 'string',
        'client_email_address': 'string',
        'client_name': 'string',
        'client_postal_code': 'string',
        'client_province': 'string',
        'client_street': 'string',
        'client_street2': 'string',
        'has_written_mandate_from_advertiser': 'unsigned int',
        'is_client_paying_invoices': 'unsigned int',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
