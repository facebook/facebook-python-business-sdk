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

class ReachFrequencyActivity(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ReachFrequencyActivity, self).__init__()
        self._isReachFrequencyActivity = True
        self._api = api

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        campaign_active = 'campaign_active'
        campaign_started = 'campaign_started'
        creative_uploaded = 'creative_uploaded'
        delivered_budget = 'delivered_budget'
        delivered_daily_grp = 'delivered_daily_grp'
        delivered_daily_impression = 'delivered_daily_impression'
        delivered_impression = 'delivered_impression'
        delivered_reach = 'delivered_reach'
        delivered_total_impression = 'delivered_total_impression'
        io_approved = 'io_approved'
        sf_link = 'sf_link'

    _field_types = {
        'account_id': 'string',
        'campaign_active': 'bool',
        'campaign_started': 'bool',
        'creative_uploaded': 'bool',
        'delivered_budget': 'int',
        'delivered_daily_grp': 'list<float>',
        'delivered_daily_impression': 'list<float>',
        'delivered_impression': 'unsigned int',
        'delivered_reach': 'unsigned int',
        'delivered_total_impression': 'unsigned int',
        'io_approved': 'bool',
        'sf_link': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


