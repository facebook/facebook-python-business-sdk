# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import time

from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
pixel_id = 'ADS_PIXEL_ID>'

FacebookAdsApi.init(access_token=access_token)

user_data = UserData(
    emails=['joe@eg.com'],
    phones=['12345678901', '14251234567'],
    lead_id=['525645896321548'],

)

custom_data = CustomData(
    custom_properties={'lead_event_source': 'Salesforce'},
)

event = Event(
    event_name='QualifiedLead',
    event_time=int(time.time()),
    user_data=user_data,
    custom_data=custom_data,
    action_source=ActionSource.SYSTEM_GENERATED,
)

events = [event]

event_request = EventRequest(
    events=events,
    pixel_id=pixel_id,
)

event_response = event_request.execute()
print(event_response)