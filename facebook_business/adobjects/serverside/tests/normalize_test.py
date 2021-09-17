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
import hashlib

from facebook_business.adobjects.serverside.normalize import Normalize


class NormalizeTest(TestCase):
    def test_normalize_field_f5first(self):
        self.assertEqual(Normalize.normalize_field('f5first', 'George'), Normalize.hash_sha_256('georg'))
        self.assertEqual(Normalize.normalize_field('f5first', 'John'), Normalize.hash_sha_256('john'))
        self.assertEqual(Normalize.normalize_field('f5first', ''), None)
        self.assertEqual(Normalize.normalize_field('f5first', None), None)

    def test_normalize_field_f5last(self):
        self.assertEqual(Normalize.normalize_field('f5last', 'Washington'), Normalize.hash_sha_256('washi'))
        self.assertEqual(Normalize.normalize_field('f5last', 'Adams'), Normalize.hash_sha_256('adams'))
        self.assertEqual(Normalize.normalize_field('f5last', ''), None)
        self.assertEqual(Normalize.normalize_field('f5last', None), None)

    def test_normalize_field_fi(self):
        self.assertEqual(Normalize.normalize_field('fi', 'ABC'), Normalize.hash_sha_256('a'))
        self.assertEqual(Normalize.normalize_field('fi', 'A'), Normalize.hash_sha_256('a'))
        self.assertEqual(Normalize.normalize_field('fi', ''), None)
        self.assertEqual(Normalize.normalize_field('fi', None), None)

    def test_normalize_field_dobd(self):
        self.assertEqual(Normalize.normalize_field('dobd', '1'), Normalize.hash_sha_256('01'))
        self.assertEqual(Normalize.normalize_field('dobd', '9'), Normalize.hash_sha_256('09'))
        self.assertEqual(Normalize.normalize_field('dobd', '02'), Normalize.hash_sha_256('02'))
        self.assertEqual(Normalize.normalize_field('dobd', '31'), Normalize.hash_sha_256('31'))
        self.assertEqual(Normalize.normalize_field('dobd', ''), None)
        self.assertEqual(Normalize.normalize_field('dobd', None), None)

    def test_normalize_field_dobd_errors(self):
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

    def test_normalize_field_dobm(self):
        self.assertEqual(Normalize.normalize_field('dobm', '1'), Normalize.hash_sha_256('01'))
        self.assertEqual(Normalize.normalize_field('dobm', '9'), Normalize.hash_sha_256('09'))
        self.assertEqual(Normalize.normalize_field('dobm', '02'), Normalize.hash_sha_256('02'))
        self.assertEqual(Normalize.normalize_field('dobm', '12'), Normalize.hash_sha_256('12'))
        self.assertEqual(Normalize.normalize_field('dobm', ''), None)
        self.assertEqual(Normalize.normalize_field('dobm', None), None)

    def test_normalize_field_dobm_errors(self):
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

    def test_normalize_field_doby(self):
        self.assertEqual(Normalize.normalize_field('doby', '2000'), Normalize.hash_sha_256('2000'))
        self.assertEqual(Normalize.normalize_field('doby', '0000'), Normalize.hash_sha_256('0000'))
        self.assertEqual(Normalize.normalize_field('doby', '9999'), Normalize.hash_sha_256('9999'))
        self.assertEqual(Normalize.normalize_field('doby', ''), None)
        self.assertEqual(Normalize.normalize_field('doby', None), None)

    def test_normalize_field_doby_errors(self):
        with self.assertRaisesRegex(ValueError, "Invalid format for doby: '19999'"):
            Normalize.normalize_field('doby', '19999')
        with self.assertRaisesRegex(ValueError, "Invalid format for doby: '1'"):
            Normalize.normalize_field('doby', '1')
        with self.assertRaisesRegex(ValueError, "Invalid format for doby: '-1'"):
            Normalize.normalize_field('doby', '-1')

    def test_normalize_field_it_skips_hashing_when_already_hashed(self):
        value = 'a' * 64
        self.assertEqual(Normalize.normalize_field('f5last', value), value)

    def test_normalize_field_it_skips_hashing_when_already_hashed_after_generic_normalizing(self):
        value = " %s " % ('a' * 64)
        self.assertEqual(Normalize.normalize_field('f5last', value), 'a' * 64)

    def test_hash_sha_256_hashes(self):
        value = '2000'
        expected_hashed_value = hashlib.sha256(value.encode('utf-8')).hexdigest()
        self.assertEqual(Normalize.hash_sha_256(value), expected_hashed_value)

    def test_normalize_field_skip_hashing_it_does_not_hash(self):
        value = ' USD '
        self.assertEqual(Normalize.normalize_field_skip_hashing('currency', value), 'usd')

    def test_normalize_validates_email_throws_errors(self):
        emails = [
            'a',
            'abc',
            'a@b',
            '@b.c',
            '.c',
            '@',
        ]
        for email in emails:
            with self.assertRaisesRegex(TypeError, "Invalid email format for the passed email:%s" % email):
                Normalize.normalize_field('em', email)

    def test_normalize_validates_email_then_hashes(self):
        emails = [
            'a@b.c',
            'foo@bar.co',
            'foo@bar.com',
            '"a b"@c.d',
            'a\@b@c.d',
            "f`oo@bar.com",
            "fo'o@bar.com",
            "f\'o\'o@bar.com",
        ]
        for email in emails:
            self.assertEqual(len(Normalize.normalize_field('em', email)), 64)
