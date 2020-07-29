import os, subprocess
import sys

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
COMMEND_BASE = "python -m facebook_business.test."

# suffix of file name in the Test folder, which should not be executed
UTILES = "utils"
RUNNER = "runner"
CONSTANT = "constant"

integration_tests = []
for filename in os.listdir(DIRECTORY):
    if filename.endswith(".py") \
        and filename.startswith("integration_") \
        and UTILES not in filename \
        and RUNNER not in filename \
        and CONSTANT not in filename:
            integration_tests.append(filename.split(".")[0])
    else:
        continue

# test will run under release folder
RELEASE_PATH = DIRECTORY + "/../../"

failed = False
for test in integration_tests:
    cmd = COMMEND_BASE + test
    try:
        subprocess.check_output(
            cmd,
            cwd=os.chdir(RELEASE_PATH),
            shell=True,
        )
    except subprocess.CalledProcessError as e:
        failed = True
        continue

if failed:
    exit(1)
