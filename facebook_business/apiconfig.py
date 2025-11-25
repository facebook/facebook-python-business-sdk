# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
from six.moves import http_client
from urllib3 import Retry


ads_api_config = {
  'API_VERSION': 'v24.0',
  'SDK_VERSION': 'v24.0.0',
  'STRICT_MODE': False

  # Whether to enable a retry strategy on any API calls being made. When set
  # to True, a default strategy is used, which is also configurable in this
  # config.
  'RETRY_MODE': False,
  'RETRY_STRATEGY': {
    'DEFAULT_RETRIES': 5,
    'DEFAULT_BACKOFF_FACTOR': 0.5,  # Time doubles between API calls.
    'RETRY_HTTP_CODES': [
      http_client.REQUEST_TIMEOUT,
      http_client.TOO_MANY_REQUESTS,
      http_client.INTERNAL_SERVER_ERROR,
      http_client.SERVICE_UNAVAILABLE,
      http_client.GATEWAY_TIMEOUT,
    ],
  }
}


def get_default_retry_strategy():
    """Gets the default retry strategy, based on the API config."""
    retry_config = ads_api_config['RETRY_STRATEGY']
    return Retry(
        total=retry_config["DEFAULT_RETRIES"],
        status_forcelist=retry_config["RETRY_HTTP_CODES"],
        backoff_factor=retry_config["DEFAULT_BACKOFF_FACTOR"],
        raise_on_status=False,  # To allow consistent handling of response.
        respect_retry_after_header=True,
    )
