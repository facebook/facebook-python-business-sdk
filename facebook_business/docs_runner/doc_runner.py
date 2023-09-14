# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

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
                # Check if the error was transient
                if err.api_transient_error() is True:
                    exit_code = ExitCodesEnum.EXTERNAL_ERROR
                else:
                    exit_code = ExitCodesEnum.USER_ERROR

                # String match for service errors. In these cases even
                # if transient flag is not set, mark it as external error
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
