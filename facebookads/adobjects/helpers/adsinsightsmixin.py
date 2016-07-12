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

class AdsInsightsMixin:

    class Increment(object):
        monthly = 'monthly'
        all_days = 'all_days'

    class Operator(object):
        all = 'ALL'
        any = 'ANY'
        contain = 'CONTAIN'
        equal = 'EQUAL'
        greater_than = 'GREATER_THAN'
        greater_than_or_equal = 'GREATER_THAN_OR_EQUAL'
        in_ = 'IN'
        in_range = 'IN_RANGE'
        less_than = 'LESS_THAN'
        less_than_or_equal = 'LESS_THAN_OR_EQUAL'
        none = 'NONE'
        not_contain = 'NOT_CONTAIN'
        not_equal = 'NOT_EQUAL'
        not_in = 'NOT_IN'
        not_in_range = 'NOT_IN_RANGE'
