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

class CatalogSegmentAllMatchCountLaser(
    AbstractObject,
):

    def __init__(self, api=None):
        super(CatalogSegmentAllMatchCountLaser, self).__init__()
        self._isCatalogSegmentAllMatchCountLaser = True
        self._api = api

    class Field(AbstractObject.Field):
        date_start = 'date_start'
        date_stop = 'date_stop'
        event = 'event'
        source = 'source'
        total_matched_content_ids = 'total_matched_content_ids'
        unique_matched_content_ids = 'unique_matched_content_ids'

    _field_types = {
        'date_start': 'string',
        'date_stop': 'string',
        'event': 'string',
        'source': 'ExternalEventSource',
        'total_matched_content_ids': 'int',
        'unique_matched_content_ids': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


