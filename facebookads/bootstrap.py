import sys
sys.path.insert(1, './')

import __main__ as main
import json
from facebookads.session import FacebookSession
from facebookads.api import FacebookAdsApi
from facebookads.objects import *
from facebookads.exceptions import FacebookError


config_file = open('./config.json')
config = json.load(config_file)
config_file.close()


def auth(access_token=None):
    if sys.__stdin__.isatty():
        access_token = access_token or config['access_token']
        FacebookAdsApi.init(
            config['app_id'],
            config['app_secret'],
            access_token,
            config['act_id'],
        )
    else:
        raise FacebookError(
            "\n\n"
            "## (/ o_o)/ ~  _|___|_ \n"
            "## bootstrap.auth() should only be used in Python's interactive "
            "shell. Try: python -i facebookads/bootstrap.py\n"
            "## Or try using FacebookAdsApi.init()"
            "\n"
        )

if config['app_id'] and config['app_secret'] and config['access_token']:
    auth()
