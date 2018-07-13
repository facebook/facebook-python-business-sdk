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

import sys
import os
import traceback
import re

# Use facebook_business SDK from this repo instead of the one installed via pip
this_dir = os.path.dirname(__file__)
repo_dir = os.path.join(this_dir, os.pardir, os.pardir)
sys.path.insert(1, repo_dir)

from facebook_business.api import FacebookAdsApi
from facebook_business.exit_codes import ExitCodesEnum
from facebook_business.exceptions import FacebookRequestError
from facebook_business.exceptions import DocsmithSkipTestError

if __name__ == '__main__':
    files_to_run = sys.argv[1:]
    exit_code = ExitCodesEnum.SUCCESS

    reg_exp = [
        'service\s*temporarily\s*unavailable',
        'try\s*again\s*later',
    ]

    for file_to_run in files_to_run:
        print('Executing file', file_to_run, file=sys.stderr)
        try:
            code_string = open(file_to_run).read()
            code = compile(code_string, file_to_run, 'exec')
            exec(code)
        except Exception as err:
            if isinstance(err, FacebookRequestError):
                # Check if the error was trasient
                if err.api_transient_error() is True:
                    exit_code = ExitCodesEnum.EXTERNAL_ERROR
                else:
                    exit_code = ExitCodesEnum.USER_ERROR

                # String match for service errors. In these cases even
                # if tranient flag is not set, mark it as external error
                for exp in reg_exp:
                    if re.findall(exp, err.get_message().lower()):
                        exit_code = ExitCodesEnum.EXTERNAL_ERROR
                        break

                traceback.print_exc()

            elif isinstance(err, DocsmithSkipTestError):
                print('Skipping Test: ' + err.get_skip_error_msg())
                exit_code = ExitCodesEnum.USER_SKIP
            else:
                exit_code = ExitCodesEnum.FAILURE
                traceback.print_exc()

    exit(exit_code)
