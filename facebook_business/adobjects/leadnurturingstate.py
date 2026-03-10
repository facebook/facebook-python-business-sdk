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

class LeadNurturingState(
    AbstractObject,
):

    def __init__(self, api=None):
        super(LeadNurturingState, self).__init__()
        self._isLeadNurturingState = True
        self._api = api

    class Field(AbstractObject.Field):
        ai_agent_mode = 'ai_agent_mode'
        conversation_summary = 'conversation_summary'
        handoff_reason = 'handoff_reason'
        lead_interest_level = 'lead_interest_level'
        needed_manual_actions = 'needed_manual_actions'
        qualification_details = 'qualification_details'
        qualification_status = 'qualification_status'
        scheduled_time = 'scheduled_time'
        updated_email = 'updated_email'
        updated_phone_number = 'updated_phone_number'

    _field_types = {
        'ai_agent_mode': 'string',
        'conversation_summary': 'string',
        'handoff_reason': 'string',
        'lead_interest_level': 'string',
        'needed_manual_actions': 'list<string>',
        'qualification_details': 'string',
        'qualification_status': 'string',
        'scheduled_time': 'Object',
        'updated_email': 'string',
        'updated_phone_number': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


