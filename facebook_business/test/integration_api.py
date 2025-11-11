import unittest
from unittest.mock import patch

import responses
from six.moves import http_client
from urllib3 import Retry

from facebook_business import FacebookAdsApi, apiconfig
from facebook_business.apiconfig import get_default_retry_strategy
from facebook_business.exceptions import FacebookRequestError
from facebook_business.test.integration_utils import IntegrationTestCase


class FacebookAdsApiTestCase(IntegrationTestCase):

    def setUp(self):
        """
        We're accessing the low-level parts of the API functionality here, so don't want to mock
        the requests in the same way, but want to at least partially conform.
        """
        self.facebook_ads_api = FacebookAdsApi.init(access_token='access_token', crash_log=False)
        self.facebook_ads_api_retry = FacebookAdsApi.init(
            access_token='access_token',
            crash_log=False,
            retry_strategy=get_default_retry_strategy()
        )
        self.url = "http://facebook.com/some/path"

    def tearDown(self):
        ...

    @responses.activate
    def test_is_success_200(self):
        """
        Simple test to show the API call will respond with a 200 status code
        """
        # Arrange - Override the low-level API calls. We just need to make sure these return 200
        # as no real API calls should be made.
        responses.add(responses.GET, self.url, status=http_client.OK)

        # Act
        facebook_response = self.facebook_ads_api.call(method="GET", path=self.url)

        # Assert
        self.assertEqual(facebook_response.status(), http_client.OK)
        self.assertTrue(facebook_response.is_success())

    @responses.activate
    def test_failure_raised_after_service_unavailable(self):
        """
        Tests that the API call will raise an error when getting a non 2xx error code.

        Default is without a Retry strategy.
        """
        # Arrange - Override the low-level API calls. Make sure we start with a 500 then a 200.
        responses.add(responses.GET, self.url, status=http_client.INTERNAL_SERVER_ERROR)
        responses.add(responses.GET, self.url, status=http_client.OK)

        # Act
        with self.assertRaises(FacebookRequestError):
            self.facebook_ads_api.call(method="GET", path=self.url)

    @responses.activate
    def test_success_after_service_unavailable_with_implicit_retry_strategy(self):
        """
        Tests that the API call will return a 200 after an initial service issue.

        Using the default retry strategy.
        """
        # Arrange - Override the low-level API calls. Make sure we start with a 500 then a 200.
        responses.add(responses.GET, self.url, status=http_client.INTERNAL_SERVER_ERROR)
        responses.add(responses.GET, self.url, status=http_client.OK)

        # Act
        facebook_response = self.facebook_ads_api_retry.call(method="GET", path=self.url)

        # Assert
        self.assertEqual(facebook_response.status(), http_client.OK)
        self.assertTrue(facebook_response.is_success())

    @responses.activate
    @patch.dict(apiconfig.ads_api_config["RETRY_STRATEGY"], {"DEFAULT_RETRIES": 1})
    def test_failure_after_service_unavailable_more_than_default_retry_strategy_allows(self):
        """
        Tests that the API call will still raise a `FacebookRequestError` after exhausting retries.

        Using the default retry strategy.
        """
        facebook_ads_api_retry = FacebookAdsApi.init(
            access_token='access_token',
            crash_log=False,
        )

        # Arrange - Override the low-level API calls. Make sure we start with a 500 then a 200.
        responses.add(responses.GET, self.url, status=http_client.INTERNAL_SERVER_ERROR)
        responses.add(responses.GET, self.url, status=http_client.INTERNAL_SERVER_ERROR)
        responses.add(responses.GET, self.url, status=http_client.OK)

        # Ac
        with self.assertRaises(FacebookRequestError):
            facebook_ads_api_retry.call(method="GET", path=self.url)

    @responses.activate
    def test_success_after_service_unavailable_with_explicit_retry_strategy(self):
        """
        Tests that the API call will return a 200 after an initial service issue.

        Using ta custom retry strategy.
        """
        # Arrange - Define the custom retry.
        retry_strategy = Retry(
            total=1,
            status_forcelist=[http_client.INTERNAL_SERVER_ERROR],
            raise_on_status=False,  # To allow consistent handling of response.
        )
        facebook_ads_api_retry = FacebookAdsApi.init(
            access_token='access_token',
            crash_log=False,
            retry_strategy=retry_strategy
        )

        # Arrange - Override the low-level API calls. Make sure we start with a 500 then a 200.
        responses.add(responses.GET, self.url, status=http_client.INTERNAL_SERVER_ERROR)
        responses.add(responses.GET, self.url, status=http_client.OK)

        # Act
        facebook_response = facebook_ads_api_retry.call(method="GET", path=self.url)

        # Assert
        self.assertEqual(facebook_response.status(), http_client.OK)
        self.assertTrue(facebook_response.is_success())

    @responses.activate
    def test_failure_after_service_unavailable_more_than_explicit_retry_strategy_allows(self):
        """
        Tests that the API call will still raise a `FacebookRequestError` after exhausting retries.

        Using a custom retry strategy.
        """
        # Arrange - Define the custom retry.
        retry_strategy = Retry(
            total=1,
            status_forcelist=[http_client.INTERNAL_SERVER_ERROR],
            raise_on_status=False,  # To allow consistent handling of response.
        )
        facebook_ads_api_retry = FacebookAdsApi.init(
            access_token='access_token',
            crash_log=False,
            retry_strategy=retry_strategy
        )

        # Arrange - Override the low-level API calls. Make sure we start with a 500 then a 200.
        responses.add(responses.GET, self.url, status=http_client.INTERNAL_SERVER_ERROR)
        responses.add(responses.GET, self.url, status=http_client.INTERNAL_SERVER_ERROR)
        responses.add(responses.GET, self.url, status=http_client.OK)

        # Ac
        with self.assertRaises(FacebookRequestError):
            facebook_ads_api_retry.call(method="GET", path=self.url)


if __name__ == '__main__':
    unittest.main()
