import sys
sys.path.insert(1, './')

import __main__ as main
import json
from facebookads.session import FacebookSession
from facebookads.api import FacebookAdsApi
from facebookads.objects import *
from facebookads.exceptions import FacebookError


def auth(access_token):
    if not hasattr(main, '__file__'):
        config_file = open('./config.json')
        config = json.load(config_file)
        config_file.close()

        FacebookAdsApi.init(
            config['app_id'],
            config['app_secret'],
            access_token
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
