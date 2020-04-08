from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject


class Transaction(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isTransaction = True
        super(Transaction, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        app_amount = 'app_amount'
        billing_end_time = 'billing_end_time'
        billing_reason = 'billing_reason'
        billing_start_time = 'billing_start_time'
        charge_type = 'charge_type'
        checkout_campaign_group_id = 'checkout_campaign_group_id'
        credential_id = 'credential_id'
        fatura_id = 'fatura_id'
        id = 'id'
        is_business_ec_charge = 'is_business_ec_charge'
        payment_option = 'payment_option'
        product_type = 'product_type'
        provider_amount = 'provider_amount'
        status = 'status'
        time = 'time'
        tracking_id = 'tracking_id'

    class ProductType:
        facebook_ad = 'facebook_ad'
        ig_ad = 'ig_ad'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'transactions'

    _field_types = {
        'account_id': 'string',
        'app_amount': 'TransactionCurrencyAmount',
        'billing_end_time': 'unsigned int',
        'billing_reason': 'string',
        'billing_start_time': 'unsigned int',
        'charge_type': 'string',
        'checkout_campaign_group_id': 'string',
        'credential_id': 'string',
        'fatura_id': 'unsigned int',
        'id': 'string',
        'is_business_ec_charge': 'bool',
        'payment_option': 'string',
        'product_type': 'ProductType',
        'provider_amount': 'TransactionCurrencyAmount',
        'status': 'string',
        'time': 'unsigned int',
        'tracking_id': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ProductType'] = Transaction.ProductType.__dict__.values()
        return field_enum_info