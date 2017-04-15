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

from facebookads.adobjects.abstractobject import AbstractObject
from facebookads.adobjects.abstractcrudobject import AbstractCrudObject
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdKeywordStats(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdKeywordStats = True
        super(AdKeywordStats, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        actions = 'actions'
        clicks = 'clicks'
        cost_per_total_action = 'cost_per_total_action'
        cost_per_unique_click = 'cost_per_unique_click'
        cpc = 'cpc'
        cpm = 'cpm'
        cpp = 'cpp'
        ctr = 'ctr'
        frequency = 'frequency'
        id = 'id'
        impressions = 'impressions'
        name = 'name'
        reach = 'reach'
        spend = 'spend'
        total_actions = 'total_actions'
        total_unique_actions = 'total_unique_actions'
        unique_actions = 'unique_actions'
        unique_clicks = 'unique_clicks'
        unique_ctr = 'unique_ctr'
        unique_impressions = 'unique_impressions'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'keywordstats'

    _field_types = {
        'actions': 'list<AdsActionStats>',
        'clicks': 'unsigned int',
        'cost_per_total_action': 'float',
        'cost_per_unique_click': 'float',
        'cpc': 'float',
        'cpm': 'float',
        'cpp': 'float',
        'ctr': 'float',
        'frequency': 'float',
        'id': 'string',
        'impressions': 'unsigned int',
        'name': 'string',
        'reach': 'unsigned int',
        'spend': 'float',
        'total_actions': 'unsigned int',
        'total_unique_actions': 'unsigned int',
        'unique_actions': 'list<AdsActionStats>',
        'unique_clicks': 'unsigned int',
        'unique_ctr': 'float',
        'unique_impressions': 'unsigned int',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info
