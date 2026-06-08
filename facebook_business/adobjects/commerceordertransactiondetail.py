# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class CommerceOrderTransactionDetail(
    AbstractObject,
):

    def __init__(self, api=None):
        super(CommerceOrderTransactionDetail, self).__init__()
        self._isCommerceOrderTransactionDetail = True
        self._api = api

    class Field(AbstractObject.Field):
        merchant_order_id = 'merchant_order_id'
        net_payment_amount = 'net_payment_amount'
        order_created = 'order_created'
        order_details = 'order_details'
        order_id = 'order_id'
        payout_reference_id = 'payout_reference_id'
        postal_code = 'postal_code'
        processing_fee = 'processing_fee'
        state = 'state'
        tax_rate = 'tax_rate'
        transaction_date = 'transaction_date'
        transaction_type = 'transaction_type'
        transfer_id = 'transfer_id'

    _field_types = {
        'merchant_order_id': 'string',
        'net_payment_amount': 'Object',
        'order_created': 'string',
        'order_details': 'CommerceOrder',
        'order_id': 'string',
        'payout_reference_id': 'string',
        'postal_code': 'string',
        'processing_fee': 'Object',
        'state': 'string',
        'tax_rate': 'string',
        'transaction_date': 'string',
        'transaction_type': 'string',
        'transfer_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


