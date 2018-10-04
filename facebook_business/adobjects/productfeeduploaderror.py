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

class ProductFeedUploadError(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductFeedUploadError = True
        super(ProductFeedUploadError, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        affected_surfaces = 'affected_surfaces'
        column_number = 'column_number'
        description = 'description'
        error_type = 'error_type'
        id = 'id'
        row_number = 'row_number'
        severity = 'severity'
        summary = 'summary'
        total_count = 'total_count'

    class AffectedSurfaces:
        dynamic_ads = 'Dynamic Ads'
        marketplace = 'Marketplace'
        us_marketplace = 'US Marketplace'

    class Severity:
        fatal = 'fatal'
        warning = 'warning'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'errors'

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
            target_class=ProductFeedUploadError,
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

    def get_samples(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.productfeeduploaderrorsample import ProductFeedUploadErrorSample
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/samples',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeedUploadErrorSample,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductFeedUploadErrorSample, api=self._api),
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
        'affected_surfaces': 'list<AffectedSurfaces>',
        'column_number': 'unsigned int',
        'description': 'string',
        'error_type': 'string',
        'id': 'string',
        'row_number': 'unsigned int',
        'severity': 'Severity',
        'summary': 'string',
        'total_count': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AffectedSurfaces'] = ProductFeedUploadError.AffectedSurfaces.__dict__.values()
        field_enum_info['Severity'] = ProductFeedUploadError.Severity.__dict__.values()
        return field_enum_info


