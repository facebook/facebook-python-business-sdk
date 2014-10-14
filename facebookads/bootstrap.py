import sys
import json

sys.path.insert(1, './')

from facebookads.session import FacebookSession
from facebookads.api import FacebookAdsApi
from facebookads.objects import *
from facebookads.exceptions import FacebookError


def auth(access_token):
    if sys.__stdin__.isatty():
        config_file = open('./config.json')
        config = json.load(config_file)
        config_file.close()

        session = FacebookSession(
            config['app_id'],
            config['app_secret'],
            access_token
        )
        api = FacebookAdsApi(session)
        FacebookAdsApi.set_default_api(api)
    else:
        raise FacebookError(
            "bootstrap.auth() should only be used in Python's interactive "
            "shell. Try: python -i facebookads/bootstrap.py"
        )
