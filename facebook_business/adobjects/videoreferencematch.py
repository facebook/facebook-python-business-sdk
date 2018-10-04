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
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class VideoReferenceMatch(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isVideoReferenceMatch = True
        super(VideoReferenceMatch, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        conflicting_countries = 'conflicting_countries'
        creation_time = 'creation_time'
        dispute_form_data = 'dispute_form_data'
        expiration_time = 'expiration_time'
        id = 'id'
        is_disputable = 'is_disputable'
        is_possible_conflict = 'is_possible_conflict'
        is_viewed = 'is_viewed'
        match_state = 'match_state'
        matched_reference_asset = 'matched_reference_asset'
        matched_reference_copyright = 'matched_reference_copyright'
        matched_reference_owner_id = 'matched_reference_owner_id'
        matched_reference_owner_name = 'matched_reference_owner_name'
        modification_history = 'modification_history'
        reference_asset = 'reference_asset'
        reference_copyright = 'reference_copyright'
        reference_owner_id = 'reference_owner_id'
        reference_owner_name = 'reference_owner_name'
        rejection_form_data = 'rejection_form_data'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoReferenceMatch,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'conflicting_countries': 'VideoCopyrightGeoGate',
        'creation_time': 'datetime',
        'dispute_form_data': 'string',
        'expiration_time': 'datetime',
        'id': 'string',
        'is_disputable': 'bool',
        'is_possible_conflict': 'bool',
        'is_viewed': 'bool',
        'match_state': 'string',
        'matched_reference_asset': 'CopyrightReferenceContainer',
        'matched_reference_copyright': 'Object',
        'matched_reference_owner_id': 'string',
        'matched_reference_owner_name': 'string',
        'modification_history': 'list<Object>',
        'reference_asset': 'CopyrightReferenceContainer',
        'reference_copyright': 'Object',
        'reference_owner_id': 'string',
        'reference_owner_name': 'string',
        'rejection_form_data': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


