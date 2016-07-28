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

"""
The purpose of the session module is to encapsulate authentication classes and
utilities.
"""
import hashlib
import hmac
import requests
import os

from requests.adapters import HTTPAdapter


class FacebookSession(object):
    """
    FacebookSession manages the the Graph API authentication and https
    connection.

    Attributes:
        GRAPH (class): The graph url without an ending forward-slash.
        app_id: The application id.
        app_secret: The application secret.
        access_token: The access token.
        appsecret_proof: The application secret proof.
        requests: The python requests object through which calls to the api can
            be made.
    """
    GRAPH = 'https://graph.facebook.com'

    def __init__(self, app_id=None, app_secret=None, access_token=None,
                 pool_maxsize=10, max_retries=0, pool_block=True):
        """
        Initializes and populates the instance attributes with app_id,
        app_secret, access_token, appsecret_proof, and requests given arguments
        app_id, app_secret, and access_token.

        Args:
            pool_maxsize: you change the default Requests connection pool size
                (useful for multi-threaded data loading scenarios)
            max_retries: Requests library can do retries for you, by default it doesn't
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token

        self.pool_maxsize = pool_maxsize
        self.max_retries = max_retries

        self.requests = requests.Session()
        self.requests.mount(
            'https://',
            HTTPAdapter(pool_maxsize=self.pool_maxsize,
                        max_retries=self.max_retries,
                        pool_block=pool_block))
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

    def _gen_appsecret_proof(self):
        h = hmac.new(
            self.app_secret.encode('utf-8'),
            msg=self.access_token.encode('utf-8'),
            digestmod=hashlib.sha256
        )

        self.appsecret_proof = h.hexdigest()
        return self.appsecret_proof

__all__ = ['FacebookSession']
