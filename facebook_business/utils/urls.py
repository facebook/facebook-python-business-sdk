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

import six


def quote_with_encoding(val):
    """Quote a string that will be placed in url.
    If the string is unicode, we encode it
    to utf-8 before using `urllib.parse.quote`.
    In case it's not a string (an int for instance),
    we still try to convert it.

    Args:
            val: The string to be properly encoded.
    """
    if not isinstance(val, (six.integer_types, six.string_types)):
        raise ValueError("Cannot encode {} type.".format(type(val)))

    # handle other stuff than strings
    if isinstance(val, six.integer_types):
        val = six.text_type(val).encode('utf-8') if six.PY3 else bytes(val)

    # works with PY2 and PY3
    elif not isinstance(val, bytes):
        val = val.encode("utf-8")

    return six.moves.urllib.parse.quote(val)
