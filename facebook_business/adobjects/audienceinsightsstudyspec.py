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

class AudienceInsightsStudySpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AudienceInsightsStudySpec, self).__init__()
        self._isAudienceInsightsStudySpec = True
        self._api = api

    class Field(AbstractObject.Field):
        audience_definition = 'audience_definition'
        author_info = 'author_info'
        creation_time = 'creation_time'
        end_time = 'end_time'
        excluded_rules = 'excluded_rules'
        included_rules = 'included_rules'
        start_time = 'start_time'
        status = 'status'

    _field_types = {
        'audience_definition': 'Object',
        'author_info': 'Object',
        'creation_time': 'int',
        'end_time': 'int',
        'excluded_rules': 'list<Object>',
        'included_rules': 'list<Object>',
        'start_time': 'int',
        'status': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


