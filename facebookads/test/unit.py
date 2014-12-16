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

'''
Unit tests for the Python Facebook Ads API SDK.

How to run:
    python -m facebookads.test.unit
'''

import unittest
import json

from .. import api
from .. import objects
from .. import specs
from .. import exceptions


class CustomAudienceTestCase(unittest.TestCase):
    def test_assert_format_params(self):
        payload = objects.CustomAudience.format_params(
            objects.CustomAudience.Schema.email_hash,
            ["  test  ", "test", "..test.."]
        )
        # This is the value of "test" when it's hashed with sha256
        test_hash = \
            "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        users = payload['payload']['data']
        assert users[0] == test_hash
        assert users[1] == users[0]
        assert users[2] == users[1]

    def test_assert_fail_when_no_app_ids(self):
        def uid_payload():
            objects.CustomAudience.format_params(
                objects.CustomAudience.Schema.uid,
                ["123123"],
            )
        self.assertRaises(
            exceptions.FacebookBadObjectError,
            uid_payload,
        )


class EdgeIteratorTestCase(unittest.TestCase):
    def test_assert_builds_from_array(self):
        """
        Sometimes the response returns an array inside the data
        key. This asserts that we successfully build objects using
        the objects in that array.
        """
        response = {
            "data": [{
                "id": "6019579"
            }, {
                "id": "6018402"
            }]
        }
        ei = objects.EdgeIterator(
            objects.AdAccount(fbid='123'),
            objects.AdGroup,
        )
        objs = ei.build_objects_from_response(response)
        assert len(objs) == 2

    def test_assert_builds_from_object(self):
        """
        Sometimes the response returns a single JSON object. This asserts
        that we're not looking for the data key and that we correctly build
        the object without relying on the data key.
        """
        response = {
            "id": "601957/targetingsentencelines",
            "targetingsentencelines": [{
                "content": "Location - Living In:",
                "children": [
                    "United States"
                ]
            }, {
                "content": "Age:",
                "children": [
                    "18 - 65+"
                ]
            }]
        }
        ei = objects.EdgeIterator(
            objects.AdAccount(fbid='123'),
            objects.AdGroup,
        )
        obj = ei.build_objects_from_response(response)
        assert len(obj) == 1 and obj[0]['id'] == "601957/targetingsentencelines"


class AbstractCrudObjectTestCase(unittest.TestCase):
    def test_assert_delitem_changes_history(self):
        account = objects.AdAccount()
        account['name'] = 'foo'
        assert len(account._changes) > 0
        del account['name']
        assert len(account._changes) == 0


class AbstractObjectTestCase(unittest.TestCase):
    def test_assert_export_nested_object(self):
        obj = specs.ObjectStorySpec()
        obj2 = specs.OfferData()
        obj2['barcode'] = 'foo'
        obj['offer_data'] = obj2
        expected = {
            'offer_data': {
                'barcode': 'foo'
            }
        }
        assert obj.export_data() == expected

    def test_assert_export_dict(self):
        obj = specs.ObjectStorySpec()
        obj['link_data'] = {
            'link_data': 3
        }
        expected = {
            'link_data': {
                'link_data': 3
            }
        }
        assert obj.export_data() == expected

    def test_assert_export_scalar(self):
        obj = specs.ObjectStorySpec()
        obj['link_data'] = 3
        expected = {
            'link_data': 3
        }
        assert obj.export_data() == expected

    def test_assert_export_none(self):
        obj = specs.ObjectStorySpec()
        obj['link_data'] = None
        expected = {}
        assert obj.export_data() == expected

    def test_assert_export_list(self):
        obj = objects.AdCreative()
        obj2 = specs.LinkData()
        obj3 = specs.AttachmentData()
        obj3['description'] = "$100"
        obj2['child_attachments'] = [obj3]
        obj['link_data'] = obj2

        try:
            json.dumps(obj.export_data())
        except:
            self.fail("Objects in crud object export")

    def test_assert_export_no_objects(self):
        obj = specs.ObjectStorySpec()
        obj2 = specs.VideoData()
        obj2['description'] = "foo"
        obj['video_data'] = obj2

        try:
            json.dumps(obj.export_data())
        except:
            self.fail("Objects in object export")

class AbstractCrudObjectTestCase(unittest.TestCase):

    def test_assert_inherits_account_id(self):
        parent_id = 'act_19tg0j239g023jg9230j932'
        api.FacebookAdsApi.set_default_account_id(parent_id)
        ac = objects.AdAccount()
        assert ac.get_parent_id() == parent_id
        api.FacebookAdsApi._default_account_id = None

    def runTest(self):
        self.assert_inherits_account_id()

if __name__ == '__main__':
    unittest.main()
