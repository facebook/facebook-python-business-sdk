# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

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

class CPASCollaborationRequest(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCPASCollaborationRequest = True
        super(CPASCollaborationRequest, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_account_id = 'ad_account_id'
        ad_account_name = 'ad_account_name'
        brands = 'brands'
        catalog_segment = 'catalog_segment'
        contact_email = 'contact_email'
        contact_first_name = 'contact_first_name'
        contact_last_name = 'contact_last_name'
        creation_time = 'creation_time'
        id = 'id'
        phone_number = 'phone_number'
        receiver_business = 'receiver_business'
        requester_agency_or_brand = 'requester_agency_or_brand'
        seller_id = 'seller_id'
        sender_business = 'sender_business'
        sender_client_business = 'sender_client_business'
        shop_url = 'shop_url'
        source = 'source'
        status = 'status'

    class RequestRole:
        receiver = 'RECEIVER'
        sender = 'SENDER'

    class Source:
        external = 'EXTERNAL'
        internal = 'INTERNAL'
        self_serve = 'SELF_SERVE'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
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
            target_class=CPASCollaborationRequest,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'ad_account_id': 'string',
        'ad_account_name': 'string',
        'brands': 'list<string>',
        'catalog_segment': 'ProductCatalog',
        'contact_email': 'string',
        'contact_first_name': 'string',
        'contact_last_name': 'string',
        'creation_time': 'datetime',
        'id': 'string',
        'phone_number': 'string',
        'receiver_business': 'Business',
        'requester_agency_or_brand': 'string',
        'seller_id': 'string',
        'sender_business': 'Business',
        'sender_client_business': 'Business',
        'shop_url': 'string',
        'source': 'string',
        'status': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['RequestRole'] = CPASCollaborationRequest.RequestRole.__dict__.values()
        field_enum_info['Source'] = CPASCollaborationRequest.Source.__dict__.values()
        return field_enum_info


