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

class CheckBatchRequestStatus(
    AbstractObject,
):

    def __init__(self, api=None):
        super(CheckBatchRequestStatus, self).__init__()
        self._isCheckBatchRequestStatus = True
        self._api = api

    class Field(AbstractObject.Field):
        errors = 'errors'
        errors_total_count = 'errors_total_count'
        handle = 'handle'
        ids_of_invalid_requests = 'ids_of_invalid_requests'
        status = 'status'
        warnings = 'warnings'
        warnings_total_count = 'warnings_total_count'

    class ErrorPriority:
        high = 'HIGH'
        low = 'LOW'
        medium = 'MEDIUM'

    _field_types = {
        'errors': 'list<Object>',
        'errors_total_count': 'int',
        'handle': 'string',
        'ids_of_invalid_requests': 'list<string>',
        'status': 'string',
        'warnings': 'list<Object>',
        'warnings_total_count': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ErrorPriority'] = CheckBatchRequestStatus.ErrorPriority.__dict__.values()
        return field_enum_info


