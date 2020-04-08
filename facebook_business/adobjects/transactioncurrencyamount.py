from facebook_business.adobjects.abstractobject import AbstractObject


class TransactionCurrencyAmount(
    AbstractObject,
):

    def __init__(self, api=None):
        super(TransactionCurrencyAmount, self).__init__()
        self._isTransactionCurrencyAmount = True
        self._api = api

    class Field(AbstractObject.Field):
        amount = 'amount'
        currency = 'currency'
        total_amount = 'total_amount'

    _field_types = {
        'amount': 'string',
        'currency': 'string',
        'total_amount': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info