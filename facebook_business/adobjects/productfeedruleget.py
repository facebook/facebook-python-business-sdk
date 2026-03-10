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

class ProductFeedRuleGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductFeedRuleGet = True
        super(ProductFeedRuleGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        attribute = 'attribute'
        id = 'id'
        params = 'params'
        rule_type = 'rule_type'

    class RuleType:
        fallback_rule = 'FALLBACK_RULE'
        letter_case_rule = 'LETTER_CASE_RULE'
        mapping_rule = 'MAPPING_RULE'
        regex_replace_rule = 'REGEX_REPLACE_RULE'
        value_mapping_rule = 'VALUE_MAPPING_RULE'

    _field_types = {
        'attribute': 'string',
        'id': 'string',
        'params': 'map<string, string>',
        'rule_type': 'RuleType',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['RuleType'] = ProductFeedRuleGet.RuleType.__dict__.values()
        return field_enum_info


