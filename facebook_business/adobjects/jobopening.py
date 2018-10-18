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

class JobOpening(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isJobOpening = True
        super(JobOpening, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        application_callback_url = 'application_callback_url'
        created_time = 'created_time'
        description = 'description'
        errors = 'errors'
        expiration_time = 'expiration_time'
        external_company_facebook_url = 'external_company_facebook_url'
        external_company_full_address = 'external_company_full_address'
        external_company_id = 'external_company_id'
        external_company_name = 'external_company_name'
        external_id = 'external_id'
        hide_from_newsfeed = 'hide_from_newsfeed'
        hide_from_timeline = 'hide_from_timeline'
        id = 'id'
        job_status = 'job_status'
        latitude = 'latitude'
        longitude = 'longitude'
        offsite_application_url = 'offsite_application_url'
        page = 'page'
        photo = 'photo'
        place = 'place'
        platform_review_status = 'platform_review_status'
        post = 'post'
        review_rejection_reasons = 'review_rejection_reasons'
        title = 'title'
        type = 'type'

    class JobStatus:
        open = 'OPEN'
        closed = 'CLOSED'
        draft = 'DRAFT'
        provisional = 'PROVISIONAL'

    class PlatformReviewStatus:
        pending = 'PENDING'
        rejected = 'REJECTED'
        approved = 'APPROVED'

    class ReviewRejectionReasons:
        generic_default = 'GENERIC_DEFAULT'
        discrimination = 'DISCRIMINATION'
        illegal = 'ILLEGAL'
        personal_info = 'PERSONAL_INFO'
        misleading = 'MISLEADING'
        sexual = 'SEXUAL'
        adult_content = 'ADULT_CONTENT'

    class Type:
        full_time = 'FULL_TIME'
        part_time = 'PART_TIME'
        internship = 'INTERNSHIP'
        volunteer = 'VOLUNTEER'
        contract = 'CONTRACT'

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
            target_class=JobOpening,
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
        'address': 'string',
        'application_callback_url': 'string',
        'created_time': 'datetime',
        'description': 'string',
        'errors': 'list<string>',
        'expiration_time': 'datetime',
        'external_company_facebook_url': 'string',
        'external_company_full_address': 'string',
        'external_company_id': 'string',
        'external_company_name': 'string',
        'external_id': 'string',
        'hide_from_newsfeed': 'bool',
        'hide_from_timeline': 'bool',
        'id': 'string',
        'job_status': 'JobStatus',
        'latitude': 'float',
        'longitude': 'float',
        'offsite_application_url': 'string',
        'page': 'Page',
        'photo': 'Photo',
        'place': 'Place',
        'platform_review_status': 'PlatformReviewStatus',
        'post': 'Post',
        'review_rejection_reasons': 'list<ReviewRejectionReasons>',
        'title': 'string',
        'type': 'Type',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['JobStatus'] = JobOpening.JobStatus.__dict__.values()
        field_enum_info['PlatformReviewStatus'] = JobOpening.PlatformReviewStatus.__dict__.values()
        field_enum_info['ReviewRejectionReasons'] = JobOpening.ReviewRejectionReasons.__dict__.values()
        field_enum_info['Type'] = JobOpening.Type.__dict__.values()
        return field_enum_info


