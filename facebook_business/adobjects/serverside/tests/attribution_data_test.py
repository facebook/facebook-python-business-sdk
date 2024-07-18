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

from unittest import TestCase

from facebook_business.adobjects.serverside.attribution_data import AttributionData


class AttributionDataTest(TestCase):
    def test_normalize(self):
        expected = {
            scope: 'click',
            visit_time: 12345,
            ad_id: '123',
            adset_id: '234',
            campaign_id: '456',
            attr_window: 7,
            attribution_share: 0.5,
            attribution_model: 'last_click',
        }
        attribution_data = AttributionData(
            scope=expected['scope'],
            visit_time=expected['visit_time'],
            ad_id=expected['ad_id'],
            adset_id=expected['adset_id'],
            campaign_id=expected['campaign_id'],
            attr_window=expected['attr_window'],
            attribution_share=expected['attribution_share'],
            attribution_model=expected['attribution_model'],
        )

        self.assertEqual(attribution_data.normalize(), expected)

    def test_emptyobject_normalize(self):
        attribution_data = AttributionData()

        self.assertEqual(attribution_data.normalize(), {})
