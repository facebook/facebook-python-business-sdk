# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import time

from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
pixel_id = 'ADS_PIXEL_ID>'

FacebookAdsApi.init(access_token=access_token)

user_data = UserData(
    email='joe@eg.com',
    fbc='fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890',
    fbp='fb.1.1558571054389.1098115397'
)

custom_data = CustomData(
    currency='usd',
    value=123.45
)

event = Event(
    event_name='Purchase',
    event_time=int(time.time()),
    user_data=user_data,
    custom_data=custom_data,
)

events = [event]

event_request = EventRequest(
    events=events,
    pixel_id=pixel_id)

event_response = event_request.execute()
print(event_response)