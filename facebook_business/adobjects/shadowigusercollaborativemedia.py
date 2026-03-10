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

class ShadowIGUserCollaborativeMedia(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isShadowIGUserCollaborativeMedia = True
        super(ShadowIGUserCollaborativeMedia, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        caption = 'caption'
        comments_count = 'comments_count'
        id = 'id'
        like_count = 'like_count'
        media_product_type = 'media_product_type'
        media_type = 'media_type'
        media_url = 'media_url'
        permalink = 'permalink'
        reposts_count = 'reposts_count'
        saved_count = 'saved_count'
        shares_count = 'shares_count'
        thumbnail_url = 'thumbnail_url'
        timestamp = 'timestamp'
        total_comments_count = 'total_comments_count'
        total_like_count = 'total_like_count'
        total_views_count = 'total_views_count'
        username = 'username'

    _field_types = {
        'caption': 'string',
        'comments_count': 'int',
        'id': 'string',
        'like_count': 'int',
        'media_product_type': 'string',
        'media_type': 'string',
        'media_url': 'string',
        'permalink': 'string',
        'reposts_count': 'int',
        'saved_count': 'int',
        'shares_count': 'int',
        'thumbnail_url': 'string',
        'timestamp': 'datetime',
        'total_comments_count': 'int',
        'total_like_count': 'int',
        'total_views_count': 'int',
        'username': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


