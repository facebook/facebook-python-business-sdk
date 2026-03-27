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

class ProductFeedUploadGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductFeedUploadGet = True
        super(ProductFeedUploadGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        end_time = 'end_time'
        error_count = 'error_count'
        error_report = 'error_report'
        errors = 'errors'
        filename = 'filename'
        id = 'id'
        input_method = 'input_method'
        num_deleted_items = 'num_deleted_items'
        num_detected_items = 'num_detected_items'
        num_invalid_items = 'num_invalid_items'
        num_persisted_items = 'num_persisted_items'
        progresses = 'progresses'
        start_time = 'start_time'
        upload_complete = 'upload_complete'
        url = 'url'
        warning_count = 'warning_count'

    class InputMethod:
        google_sheets_fetch = 'GOOGLE_SHEETS_FETCH'
        manual_upload = 'MANUAL_UPLOAD'
        reupload_existing = 'REUPLOAD_EXISTING'
        reupload_last_file = 'REUPLOAD_LAST_FILE'
        server_fetch = 'SERVER_FETCH'
        user_initiated_server_fetch = 'USER_INITIATED_SERVER_FETCH'

    _field_types = {
        'end_time': 'string',
        'error_count': 'int',
        'error_report': 'object',
        'errors': 'object',
        'filename': 'string',
        'id': 'int',
        'input_method': 'InputMethod',
        'num_deleted_items': 'int',
        'num_detected_items': 'int',
        'num_invalid_items': 'int',
        'num_persisted_items': 'int',
        'progresses': 'object',
        'start_time': 'string',
        'upload_complete': 'bool',
        'url': 'string',
        'warning_count': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['InputMethod'] = ProductFeedUploadGet.InputMethod.__dict__.values()
        return field_enum_info


