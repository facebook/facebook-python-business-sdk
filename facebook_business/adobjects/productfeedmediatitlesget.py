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

class ProductFeedMediaTitlesGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ProductFeedMediaTitlesGet, self).__init__()
        self._isProductFeedMediaTitlesGet = True
        self._api = api

    class Field(AbstractObject.Field):
        data = 'data'
        paging = 'paging'
        summary = 'summary'

    class DisplayFormat:
        carousel_ad = 'CAROUSEL_AD'
        shops_pdp = 'SHOPS_PDP'
        single_ad = 'SINGLE_AD'

    _field_types = {
        'data': 'list<object>',
        'paging': 'object',
        'summary': 'object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DisplayFormat'] = ProductFeedMediaTitlesGet.DisplayFormat.__dict__.values()
        return field_enum_info


