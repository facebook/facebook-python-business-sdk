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

from .. import objects
from .. import specs


class AbstractObjectTestCase(unittest.TestCase):
    def assert_export_nested_object(self):
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

    def assert_export_dict(self):
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

    def assert_export_scalar(self):
        obj = specs.ObjectStorySpec()
        obj['link_data'] = 3
        expected = {
            'link_data': 3
        }
        assert obj.export_data() == expected

    def assert_export_none(self):
        obj = specs.ObjectStorySpec()
        obj['link_data'] = None
        expected = {}
        assert obj.export_data() == expected

    def assert_export_list(self):
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

    def assert_export_no_objects(self):
        obj = specs.ObjectStorySpec()
        obj2 = specs.VideoData()
        obj2['description'] = "foo"
        obj['video_data'] = obj2

        try:
            json.dumps(obj.export_data())
        except:
            self.fail("Objects in object export")

    def runTest(self):
        self.assert_export_nested_object()
        self.assert_export_dict()
        self.assert_export_scalar()
        self.assert_export_no_objects()
        self.assert_export_list()
        self.assert_export_none()


if __name__ == '__main__':
    unittest.main()
