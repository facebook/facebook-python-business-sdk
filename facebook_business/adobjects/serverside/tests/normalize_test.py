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

from facebook_business.adobjects.serverside.normalize import Normalize


class NormalizeTest(TestCase):
    def test_normalize_f5first(self):
        self.assertEqual(Normalize.normalize_field('f5first', 'George'), 'georg')
        self.assertEqual(Normalize.normalize_field('f5first', 'John'), 'john')
        self.assertEqual(Normalize.normalize_field('f5first', ''), None)
        self.assertEqual(Normalize.normalize_field('f5first', None), None)

    def test_normalize_f5last(self):
        self.assertEqual(Normalize.normalize_field('f5last', 'Washington'), 'washi')
        self.assertEqual(Normalize.normalize_field('f5last', 'Adams'), 'adams')
        self.assertEqual(Normalize.normalize_field('f5last', ''), None)
        self.assertEqual(Normalize.normalize_field('f5last', None), None)

    def test_normalize_fi(self):
        self.assertEqual(Normalize.normalize_field('fi', 'ABC'), 'a')
        self.assertEqual(Normalize.normalize_field('fi', 'A'), 'a')
        self.assertEqual(Normalize.normalize_field('fi', ''), None)
        self.assertEqual(Normalize.normalize_field('fi', None), None)

    def test_normalize_dobd(self):
        self.assertEqual(Normalize.normalize_field('dobd', '1'), '01')
        self.assertEqual(Normalize.normalize_field('dobd', '9'), '09')
        self.assertEqual(Normalize.normalize_field('dobd', '02'), '02')
        self.assertEqual(Normalize.normalize_field('dobd', '31'), '31')
        self.assertEqual(Normalize.normalize_field('dobd', ''), None)
        self.assertEqual(Normalize.normalize_field('dobd', None), None)

    def test_normalize_dobd_errors(self):
        with self.assertRaisesRegex(ValueError, "Invalid format for dobd: '32'"):
            Normalize.normalize_field('dobd', '32')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobd: '444'"):
            Normalize.normalize_field('dobd', '444')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobd: '0'"):
            Normalize.normalize_field('dobd', '0')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobd: '0a'"):
            Normalize.normalize_field('dobd', '0a')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobd: '-1'"):
            Normalize.normalize_field('dobd', '-1')

    def test_normalize_dobm(self):
        self.assertEqual(Normalize.normalize_field('dobm', '1'), '01')
        self.assertEqual(Normalize.normalize_field('dobm', '9'), '09')
        self.assertEqual(Normalize.normalize_field('dobm', '02'), '02')
        self.assertEqual(Normalize.normalize_field('dobm', '12'), '12')
        self.assertEqual(Normalize.normalize_field('dobm', ''), None)
        self.assertEqual(Normalize.normalize_field('dobm', None), None)

    def test_normalize_dobm_errors(self):
        with self.assertRaisesRegex(ValueError, "Invalid format for dobm: '13'"):
            Normalize.normalize_field('dobm', '13')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobm: '444'"):
            Normalize.normalize_field('dobm', '444')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobm: '0'"):
            Normalize.normalize_field('dobm', '0')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobm: '0a'"):
            Normalize.normalize_field('dobm', '0a')
        with self.assertRaisesRegex(ValueError, "Invalid format for dobm: '-1'"):
            Normalize.normalize_field('dobm', '-1')

    def test_normalize_doby(self):
        self.assertEqual(Normalize.normalize_field('doby', '2000'), '2000')
        self.assertEqual(Normalize.normalize_field('doby', '0000'), '0000')
        self.assertEqual(Normalize.normalize_field('doby', '9999'), '9999')
        self.assertEqual(Normalize.normalize_field('doby', ''), None)
        self.assertEqual(Normalize.normalize_field('doby', None), None)

    def test_normalize_doby_errors(self):
        with self.assertRaisesRegex(ValueError, "Invalid format for doby: '19999'"):
            Normalize.normalize_field('doby', '19999')
        with self.assertRaisesRegex(ValueError, "Invalid format for doby: '1'"):
            Normalize.normalize_field('doby', '1')
        with self.assertRaisesRegex(ValueError, "Invalid format for doby: '-1'"):
            Normalize.normalize_field('doby', '-1')
