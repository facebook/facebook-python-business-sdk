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

class WhatsAppBusinessPartnerClientVerificationSubmission(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isWhatsAppBusinessPartnerClientVerificationSubmission = True
        super(WhatsAppBusinessPartnerClientVerificationSubmission, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        client_business_id = 'client_business_id'
        id = 'id'
        rejection_reasons = 'rejection_reasons'
        submitted_info = 'submitted_info'
        submitted_time = 'submitted_time'
        update_time = 'update_time'
        verification_status = 'verification_status'

    _field_types = {
        'client_business_id': 'string',
        'id': 'string',
        'rejection_reasons': 'list<string>',
        'submitted_info': 'Object',
        'submitted_time': 'datetime',
        'update_time': 'datetime',
        'verification_status': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


