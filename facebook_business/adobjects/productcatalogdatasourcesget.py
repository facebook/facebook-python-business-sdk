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

class ProductCatalogDataSourcesGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductCatalogDataSourcesGet, self).__init__()
        self._isProductCatalogDataSourcesGet = True
        self._api = api

    class Field(AbstractObject.Field):
        data = 'data'
        paging = 'paging'

    class IngestionSourceType:
        all = 'ALL'
        primary = 'PRIMARY'
        supplementary = 'SUPPLEMENTARY'

    _field_types = {
        'data': 'list<object>',
        'paging': 'object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['IngestionSourceType'] = ProductCatalogDataSourcesGet.IngestionSourceType.__dict__.values()
        return field_enum_info


