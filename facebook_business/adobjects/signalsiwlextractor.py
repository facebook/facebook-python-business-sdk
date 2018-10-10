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

class SignalsIWLExtractor(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isSignalsIWLExtractor = True
        super(SignalsIWLExtractor, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        domain_uri = 'domain_uri'
        event_type = 'event_type'
        extractor_config = 'extractor_config'
        extractor_type = 'extractor_type'
        id = 'id'

    class EventType:
        addpaymentinfo = 'AddPaymentInfo'
        addtocart = 'AddToCart'
        addtowishlist = 'AddToWishlist'
        completeregistration = 'CompleteRegistration'
        contact = 'Contact'
        customizeproduct = 'CustomizeProduct'
        donate = 'Donate'
        findlocation = 'FindLocation'
        initiatecheckout = 'InitiateCheckout'
        lead = 'Lead'
        other = 'Other'
        purchase = 'Purchase'
        schedule = 'Schedule'
        search = 'Search'
        starttrial = 'StartTrial'
        submitapplication = 'SubmitApplication'
        subscribe = 'Subscribe'
        viewcontent = 'ViewContent'

    class ExtractorType:
        constant_value = 'CONSTANT_VALUE'
        css = 'CSS'
        global_variable = 'GLOBAL_VARIABLE'
        gtm = 'GTM'
        json_ld = 'JSON_LD'
        meta_tag = 'META_TAG'
        open_graph = 'OPEN_GRAPH'
        rdfa = 'RDFA'
        schema_dot_org = 'SCHEMA_DOT_ORG'
        uri = 'URI'

    def api_delete(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
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
            target_class=SignalsIWLExtractor,
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

    def api_update(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'domain_uri': 'Object',
            'event_type': 'event_type_enum',
            'extractor_config': 'map',
            'extractor_type': 'extractor_type_enum',
        }
        enums = {
            'event_type_enum': SignalsIWLExtractor.EventType.__dict__.values(),
            'extractor_type_enum': SignalsIWLExtractor.ExtractorType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=SignalsIWLExtractor,
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
        'domain_uri': 'string',
        'event_type': 'string',
        'extractor_config': 'Object',
        'extractor_type': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['EventType'] = SignalsIWLExtractor.EventType.__dict__.values()
        field_enum_info['ExtractorType'] = SignalsIWLExtractor.ExtractorType.__dict__.values()
        return field_enum_info


