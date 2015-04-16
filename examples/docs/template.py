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

from __future__ import print_function
from __future__ import unicode_literals

'''
    This is a template for DocSmith samples in Python.

    Code should follow guidelines at
    https://our.intern.facebook.com/intern/wiki/Solutions_Engineering/DocSmith

    facebookads repo folder must be added to PYTHONPATH in order to run
'''

import sys
import os

this_dir = os.path.dirname(__file__)
repo_dir = os.path.join(this_dir, os.pardir, os.pardir)
sys.path.insert(1, repo_dir)

from facebookads import bootstrap
bootstrap.auth()

'''
    Base file to create new examples for Ads API docs. Copy it and create yours

    Comments on style:
    - IDs should be defined outside of _DOC blocks so they don't appear into the
    docs

'''

from facebookads.objects import AdAccount

if __name__ == '__main__':
    ad_account_id = 'act_831792586836538'
    #! _DOC open [READ_ADACCOUNT]
    print('**** READ AD ACCOUNT ****')
    ad_account = AdAccount(fbid=ad_account_id)
    print(ad_account.remote_read())
    #! _DOC close [READ_ADACCOUNT]
