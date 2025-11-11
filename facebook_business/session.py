# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""
The purpose of the session module is to encapsulate authentication classes and
utilities.
"""
import hashlib
import hmac
import requests
import os

from facebook_business.apiconfig import get_default_retry_strategy, ads_api_config


class FacebookSession(object):
    """
    FacebookSession manages the Graph API authentication and https
    connection.

    Attributes:
        GRAPH (class): The graph url without an ending forward-slash.
        app_id: The application id.
        app_secret: The application secret.
        access_token: The access token.
        appsecret_proof: The application secret proof.
        proxies: Object containing proxies for 'http' and 'https'
        retry_strategy (Optional[urllib3.Retry]): A optional retry strategy to
            apply to the API call. If `RETRY_MODE` is True in the `apiconfig`
            then we'll use a default Retry strategy.
        requests: The python requests object through which calls to the api can
            be made.
    """
    GRAPH = 'https://graph.facebook.com'

    def __init__(self, app_id=None, app_secret=None, access_token=None,
                 proxies=None, timeout=None, retry_strategy=None, debug=False):
        """
        Initializes and populates the instance attributes with app_id,
        app_secret, access_token, appsecret_proof, proxies, timeout and requests
        given arguments app_id, app_secret, access_token, proxies and timeout.
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token
        self.proxies = proxies
        self.timeout = timeout
        self.debug = debug
        self.requests = requests.Session()
        self.requests.verify = os.path.join(
            os.path.dirname(__file__),
            'fb_ca_chain_bundle.crt',
        )
        params = {
            'access_token': self.access_token
        }
        if app_secret:
            params['appsecret_proof'] = self._gen_appsecret_proof()
        self.requests.params.update(params)

        if self.proxies:
            self.requests.proxies.update(self.proxies)

        self.retry_strategy = self._mount_retry_strategy(retry_strategy)

    def _gen_appsecret_proof(self):
        h = hmac.new(
            self.app_secret.encode('utf-8'),
            msg=self.access_token.encode('utf-8'),
            digestmod=hashlib.sha256
        )

        self.appsecret_proof = h.hexdigest()
        return self.appsecret_proof

    def _mount_retry_strategy(self, retry_strategy):
        """
        Mounts any available retry strategy to the request's session.

        Provides ability to fully specify a Retry strategy, or if RETRY_MODE
        is set on the API Config, then a default retry strategy will be used,
        which is partially configurable.

        Attributes:
            retry_strategy (Optional[urllib3.Retry]): The retry strategy to
                apply to the session and will be used for all API calls
                against the session.
        """
        retry_mode = ads_api_config["RETRY_MODE"]
        if retry_mode and not retry_strategy:
            retry_strategy = get_default_retry_strategy()

        # Return early if no retry strategy was found.
        if not retry_strategy:
            return

        # Inject the Retry strategy into the session directly.
        adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
        self.requests.mount("https://", adapter)
        self.requests.mount("http://", adapter)

        return retry_strategy


__all__ = ['FacebookSession']
