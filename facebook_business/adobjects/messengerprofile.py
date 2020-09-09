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

class MessengerProfile(
    AbstractObject,
):

    def __init__(self, api=None):
        super(MessengerProfile, self).__init__()
        self._isMessengerProfile = True
        self._api = api

    class Field(AbstractObject.Field):
        account_linking_url = 'account_linking_url'
        get_started = 'get_started'
        greeting = 'greeting'
        ice_breakers = 'ice_breakers'
        payment_settings = 'payment_settings'
        persistent_menu = 'persistent_menu'
        target_audience = 'target_audience'
        whitelisted_domains = 'whitelisted_domains'

    _field_types = {
        'account_linking_url': 'string',
        'get_started': 'Object',
        'greeting': 'list<Object>',
        'ice_breakers': 'list<Object>',
        'payment_settings': 'Object',
        'persistent_menu': 'list<Object>',
        'target_audience': 'Object',
        'whitelisted_domains': 'list<string>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


