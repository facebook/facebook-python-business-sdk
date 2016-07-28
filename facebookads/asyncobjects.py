import time
import random
import logging
from datetime import datetime

import facebookads.objects as baseobjects
from facebookads.asyncapi import FacebookAdsAsyncApi
from facebookads.exceptions import (FacebookRequestError, FacebookApiTimeout,
    FacebookUnavailablePropertyException, JobFailedException, JobFailedForArchivedDataException)
from facebookads.utils.fberrcodes import FacebookErrorCodes

from six import string_types, text_type, binary_type
try:
    from urlparse import parse_qsl, urlparse, urlunsplit
    from urllib import urlencode
except ImportError:  # python 3 compatibility
    from urllib.parse import parse_qsl, urlparse, urlunsplit, urlencode

logger = logging.getLogger("facebookclient")


class AioEdgeIterator(baseobjects.EdgeIterator):

    """Asyncronously retrieves pages of data from object's connections.
    Each page is a list of dicts with the data.
    And it iterates over the data.

    Examples:
        >>> acc = AdAccount('account_id')
        >>> ad_names = []
        >>> for row in acc.get_ads_aio(fields=[Ad.Field.name]):
        >>>     ad_names.append(row["name"])
        >>> ad_names
    """

    def __init__(self, source_object, target_objects_class,
                 fields=None, params=None, include_summary=True,
                 limit=1000):
        """
        Initializes an iterator over the objects to which there is an edge from
        source_object.

        Args:
            source_object: An AbstractObject instance from which to inspect an
                edge. This object should have an id.
            target_objects_class: Objects traversed over will be initialized
                with this AbstractObject class.
            fields (optional): A list of fields of target_objects_class to
                automatically read in.
            params (optional): A mapping of request parameters where a key
                is the parameter name and its value is a string or an object
                which can be JSON-encoded.
        """
        self.limit = 1000 if limit is None else limit
        self.starting_limit = 1000 if limit is None else limit

        if params is None:
            params = {"limit": self.limit}
        elif not params or "limit" not in params:
            params["limit"] = self.limit

        super(AioEdgeIterator, self).__init__(
                source_object, target_objects_class,
                fields=fields, params=params, include_summary=include_summary)

        # AIO future holder
        self._future = None
        # last loaded response
        self._response = None
        """:type: facebookads.asyncapi.FacebookAsyncResponse"""

        # iterator's state is:
        # self._finished_iteration - True or False
        # self.failed - True or False
        self._request_failed = False
        self._page_ready = False

        self.last_error_type = None
        self.last_error = None
        self.errors_streak = 0
        self.delay_next_call_for = 0

        self.success_cnt = 0
        self.success_streak = 0
        self.last_yield = time.time()

        self.tmp_retries = 25
        self.unknown_retries = 30
        self.too_much_data_retries = 14

    def __getitem__(self, index):
        if not self._queue:
            self.load_next_page()
        return self._queue[index]

    def get_all_results(self):
        """
        :rtype: list[dict]
        """
        return self._queue

    # AIO-based page loader

    def load_next_page(self):
        """Queries server for more nodes and loads them into the internal queue.

        Returns:
            True if successful, else False.
        """
        if self._finished_iteration:
            return False
        if not self._future:
            if not self.submit_next_page_aio():
                return False

        while not self._page_ready or self._request_failed:
            self.extract_results()
            time.sleep(0.2)
        success = self._page_ready and not self._request_failed and self._queue
        self.submit_next_page_aio()
        return success

    # AIO methods

    def submit_next_page_aio(self):
        """Puts future request into thread pool queue.

        Returns:
            True if successful, else False.
        """
        if self._finished_iteration or self._future:
            return False

        if self._include_summary:
            if 'summary' not in self.params:
                self.params['summary'] = True

        self._request_failed = False
        self._page_ready = False
        self._future = self._source_object.get_api_assured().call_future(
                self, 'GET', self._path, params=self.params,
                delay_next_call_for=self.delay_next_call_for)
        return True

    def read_next_page_aio(self, response):
        """
        Parses and returns the data in response.
        Gets the url of the next page in response and sets it as self._path attribute.

        :type response: facebookads.asyncapi.FacebookAsyncResponse
        :return:
        """
        jresp = response.json()
        if not jresp:
            self._finished_iteration = True
            return 0

        if 'paging' in jresp and 'next' in jresp['paging']:
            self._path = jresp['paging']['next']
            pr = urlparse(jresp['paging']['next'])
            self.params = dict(parse_qsl(pr.query, keep_blank_values=True))

            # url components: scheme, netloc, url, query, fragment
            self._path = urlunsplit((pr.scheme, pr.netloc, pr.path, None, None))
        else:
            # Indicate if this was the last page
            self._finished_iteration = True

        if (
            self._include_summary and
            'summary' in jresp and
            'total_count' in jresp['summary']
        ):
            self._total_count = jresp['summary']['total_count']

        return self.build_objects_from_response(jresp)

    def build_objects_from_response(self, response):
        """
        Returns number of iterms in response.
        Gets response data and adds it to self._queue.
        """
        if not isinstance(response, string_types) and 'data' in response and \
                isinstance(response['data'], list):
            new_cnt = len(response['data'])
            self._queue += response['data']

            if new_cnt <= 0:
                # API may return paging.next even for the last page
                self._finished_iteration = True
        else:
            self._finished_iteration = True
            if not isinstance(response, string_types) and 'data' in response:
                data = response['data']
            else:
                data = response
            self._queue.append(data)
            new_cnt = 1
        self._response = None

        return new_cnt

    # results processing and state changes

    def extract_results(self):
        """
        If future is done, removes it from the futures list, dict and iterator itself.
        Then, if future finished successfully,

        :return: FbFutureHolder
        """
        self._request_failed = False

        # If no future in iterator and the iterator is finished, returns the iterator itself.
        if not self._future:
            if self._finished_iteration:
                return self
            raise FacebookUnavailablePropertyException("first submit new async call")

        if self._future.done():
            result = self._future.result()
            self._source_object.get_api_assured().remove_from_futures(self)
            del self._future
            self._future = None

            if self.last_error_type == "rate limit error":
                self.delay_next_call_for -= 10
                if self.delay_next_call_for < 0:
                    self.delay_next_call_for = 0
            else:
                self.delay_next_call_for = 0

            self.last_yield = time.time()
            if result.is_failure():
                self.on_error(result)
            else:
                self.on_success(result)

        else:
            if not self._future.running() and not self._future.cancelled():
                # still not running, just pending in a queue
                self._request_failed = False
                self._page_ready = False
            elif self._future.cancelled():
                # was cancelled
                self.last_yield = time.time()
                self._request_failed = True
                self.delay_next_call_for = 0
                logger.warn("request {} was cancelled, endpoint: {}, params: {}".format(
                        str(self._future), str(self._path), self.params))
                self.last_error = Exception("request {} was cancelled, endpoint: {}, params: {}".format(
                        str(self._future), str(self._path), self.params))
                self._source_object.get_api_assured().remove_from_futures(self)
                del self._future
                self._future = None
            elif int(time.time() - self.last_yield) > 600:
                # running for too long
                self.future_timed_out()
                if self.errors_streak >= 5:
                    return self
                self.last_yield = time.time()
                self.recover_tmp_error(self.last_error)
            else:
                # just running
                self._request_failed = False
                self._page_ready = False
        return self

    def future_timed_out(self):
        self._request_failed = True
        self.delay_next_call_for = 0
        logger.warn("request {} stuck, time: {}, endpoint: {}, params: {}".format(
            str(self._future), int(time.time() - self.last_yield),
            str(self._path), self.params))
        self.last_error = FacebookApiTimeout(
            "request {} stuck, time: {}, endpoint: {}, params: {}".format(
                str(self._future), int(time.time() - self.last_yield),
                str(self._path), self.params))
        self._future.cancel()
        del self._future
        self._future = None

    def on_success(self, response):
        """
        Increments success streak and success count, assigns the next page of response as self._path,
        sets parameter ._page_ready as True.

        If success streak >= 10 and self.limit < starting limit, changes the limit of facebook result data.
        """
        self._response = response
        """:type: facebookads.asyncapi.FacebookAsyncResponse"""
        self.success_streak += 1
        self.success_cnt += 1
        self.read_next_page_aio(self._response)
        self._page_ready = True

        if not self._finished_iteration:
            if self.success_streak >= 10 and self.last_error_type != "too much data error" \
                    and self.limit < self.starting_limit:
                self.change_the_next_page_limit(self.starting_limit, 2)

    def on_error(self, response):
        """
        If request is failed, submits next page, otherwise
        finishes iterations and sets the number of success streaks as 0.
        """
        if not self.is_exception_fatal(response):
            self.submit_next_page_aio()
        else:
            self._finished_iteration = True
            self.success_streak = 0

    # errors handling

    def is_exception_fatal(self, resp):
        """
        If it is unfatal error, tries to recover.
        If it is fatal error, sets _request_failed = True, logs it and sets _last_error = error.
        """
        exc = resp.error()
        if isinstance(exc, FacebookRequestError):
            if exc.api_error_code() == FacebookErrorCodes.temporary:
                self.recover_tmp_error(exc)
            elif exc.api_error_code() == FacebookErrorCodes.unknown:
                if exc.api_error_message().find("educe the amount of data") > 0:
                    self.recover_too_much_data_error(exc)
                else:
                    self.recover_unknown_error(exc)
            elif exc.api_error_code() == FacebookErrorCodes.too_much_data:
                self.recover_too_much_data_error(exc)
            elif exc.api_error_code() == FacebookErrorCodes.rate_limit:
                self.recover_rate_limit_error(exc)
            elif not exc.is_body_json() or \
                    exc.api_error_code() == FacebookErrorCodes.report_cannot_be_accessed:
                self.recover_tmp_error(exc)
            else:
                self.recover_other_graph_error(exc)
        else:
            if resp.body() and isinstance(resp.json(), (string_types, text_type, binary_type)):
                self.recover_tmp_error(exc)
            else:
                self.set_fatal_error(exc)
        return self._request_failed

    def set_fatal_error(self, exc, exception_type="fatal error"):
        self.set_last_error(exception_type)
        self.last_error = exc
        self._request_failed = True
        logger.error("Fatal facebook error while loading url: {}, method GET with params: {}. "
                     "Caught an error: {}".format(
            str(self._path), str(self.params), str(exc)))

    def set_non_fatal_error(self, exc, exception_type="temporary error"):
        self.set_last_error(exception_type)
        self.last_error = exc
        logger.warning("While loading url: {}, method GET with params: {}. "
                       "Caught an error: {}".format(
            str(self._path), str(self.params), str(exc)))

    def recover_other_graph_error(self, exc):
        if exc._http_status and 400 <= exc._http_status < 500:
            self.set_fatal_error(exc)
        else:
            self.recover_unknown_error(exc)

    def recover_tmp_error(self, exc):
        err_type = "temporary error"
        if self.errors_streak >= self.tmp_retries:
            self.set_fatal_error(exc, err_type)
        else:
            self.set_non_fatal_error(exc, err_type)
            self.delay_next_call_for = 5 + 10 * self.errors_streak
            self.change_the_next_page_limit()

    def recover_too_much_data_error(self, exc):
        err_type = "too much data error"
        if self.errors_streak >= self.too_much_data_retries:
            self.set_fatal_error(exc, err_type)
        else:
            self.set_non_fatal_error(exc, err_type)
            self.change_the_next_page_limit(lowest_limit=1)

    def recover_unknown_error(self, exc):
        err_type = "unknown error"
        if self.errors_streak >= self.unknown_retries:
            self.set_fatal_error(exc, err_type)
        else:
            self.set_non_fatal_error(exc, err_type)
            self.delay_next_call_for = 10 + 15 * self.errors_streak
            self.change_the_next_page_limit()

    def recover_rate_limit_error(self, exc):
        err_type = "rate limit error"
        self.set_non_fatal_error(exc, err_type)
        self.delay_next_call_for = random.randint(30, 60) + 30 * self.errors_streak

    # error helpers

    def change_the_next_page_limit(self, new_limit=None, lowest_limit=2):
        if self._finished_iteration:
            return

        if new_limit is None:
            new_limit = int(self.limit / 2)
        self.limit = int(new_limit)
        if self.limit < lowest_limit:
            self.limit = lowest_limit
        elif self.limit < 1:
            self.limit = 1

        if 'limit' in self.params and self.params['limit']:
            self.params['limit'] = self.limit
        else:
            self.params['limit'] = self.starting_limit
        return

    def set_last_error(self, err_type):
        if self.last_error_type == err_type:
            self.errors_streak += 1
        else:
            self.errors_streak = 1
            self.last_error_type = err_type


class EdgeLessIterator(AioEdgeIterator):
    def __init__(self, source_object,
                 fields=None, params=None, include_summary=True,
                 limit=1000):
        super(EdgeLessIterator, self).__init__(
                source_object, type(source_object), fields=fields,
                params=params, include_summary=include_summary,
                limit=limit)
        self._path = (source_object.get_endpoint(),)


class ByIdsIterator(AioEdgeIterator):
    def __init__(self, target_object_class, ids, fields=None, params=None,
                 include_summary=True, limit=50):
        super(ByIdsIterator, self).__init__(
                target_object_class(str(ids[0])), target_object_class, fields=fields,
                params=params, include_summary=include_summary,
                limit=limit)
        self._path = ['/']
        self.params["ids"] = ','.join(map(str, ids))

    def build_objects_from_response(self, response):
        if 'data' in response and isinstance(response['data'], list):
            new_cnt = len(response['data'])
            self._queue += response['data']

            if new_cnt <= 0:
                # API may return paging.next even for the last page
                self._finished_iteration = True
        else:
            self._finished_iteration = True
            data = response['data'] if 'data' in response else response
            if isinstance(data, dict):
                for key, val in data.items():
                    self._queue.append((key, val))
            else:
                self._queue.append(data)
            new_cnt = 1
        self._response = None

        return new_cnt


class AbstractCrudAioObject(object):
    """
    Extends AbstractCrudObject and implements async iter_edge operation.
    """

    @classmethod
    def get_by_ids(cls, ids, params=None, fields=None, api=None, limit=50):
        """Get objects by id list
        :type cls: AbstractCrudObject
        :type ids: list
        :type params: didct
        :type fields: list | tuple
        :type api: FacebookAdsAsyncApi
        :param limit: how big should slices be
        :rtype: list[dict]
        """
        ids = list(ids)
        api = api or FacebookAdsAsyncApi.get_default_api()
        params = dict(params or {})
        cls._assign_fields_to_params(fields, params)
        cnt = 0
        while cnt < len(ids):
            params_tmp = params.copy()
            iter_edge = ByIdsIterator(cls, ids[cnt:cnt+limit], fields=fields,
                                      params=params_tmp, limit=limit)
            iter_edge.submit_next_page_aio()
            cnt += limit

        result = []
        for response in api.get_typed_async_results(cls):
            if response._request_failed:
                raise response.last_error

            for fbid, data in response.get_all_results():
                # obj = cls(fbid, api=api)
                # obj._set_data(data)
                result.append(data)
        return result

    # Getters

    def get_api(self):
        """
        Returns the api associated with the object. If None, returns the
        default api.
        :type self: AbstractCrudObject
        :rtype: FacebookAdsAsyncApi
        """
        return self._api or FacebookAdsAsyncApi.get_default_api()

    # Helpers

    def iterate_edge_aio(self, target_objects_class, fields=None, params=None,
                         include_summary=True, limit=1000):
        """
        Creates, sends it to the futures queue and returns EdgeIterator with argument self as source_object and
        the rest as given __init__ arguments.

        Note: list(iterate_edge_aio(...)) can prefetch all the objects.
        """
        source_object = self
        iterator = AioEdgeIterator(
            source_object,
            target_objects_class,
            fields=fields,
            params=params,
            include_summary=include_summary,
            limit=limit
        )

        iterator.submit_next_page_aio()

        return iterator

    def iterate_edge_async_aio(self, target_objects_class, fields=None, params=None,
                               has_action=None, needs_action_device=None, limit=500,
                               has_filters=False, for_date=None):
        """
        Returns an AsyncAioJob which can be checked using remote_read()
        to verify when the job is completed and the result ready to query
        or download using get_result()
        :type target_objects_class: AbstractCrudObject
        """
        if not params:
            params = {}
        else:
            params = dict(params)

        result = AsyncAioJobIterator(
            self,
            target_objects_class,
            fields=fields, limit=limit,
            params=params, has_action=has_action,
            needs_action_device=needs_action_device,
            has_filters=has_filters, for_date=for_date
        )

        result.launch_job()
        return result


class AdUser(AbstractCrudAioObject, baseobjects.AdUser):
    pass


class Page(AbstractCrudAioObject, baseobjects.Page):
    pass


class AdAccount(AbstractCrudAioObject, baseobjects.AdAccount):
    def add_user(self, user, business, role):
        params = {
            'user': user,
            'business': business,
            'role': role,
        }
        return self.get_api_assured().call(
            'POST',
            (self.get_id_assured(), 'userpermissions'),
            params=params,
        )

    def get_activities_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Activity's associated with this account."""
        return self.iterate_edge_aio(baseobjects.Activity, fields, params, limit=limit)

    def get_ad_users_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdUser's associated with this account."""
        return self.iterate_edge_aio(AdUser, fields, params, limit=limit)

    def get_campaigns_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Campaign's associated with this account."""
        return self.iterate_edge_aio(Campaign, fields, params, limit=limit)

    def get_ad_sets_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdSet's associated with this account."""
        return self.iterate_edge_aio(AdSet, fields, params, limit=limit)

    def get_ads_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Ad's associated with this account."""
        return self.iterate_edge_aio(Ad, fields, params, limit=limit)

    def get_ad_conversion_pixels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over AdConversionPixels associated with this account.
        """
        return self.iterate_edge_aio(AdConversionPixel, fields, params, limit=limit)

    def get_ad_creatives_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdCreative's associated with this account."""
        return self.iterate_edge_aio(AdCreative, fields, params, limit=limit)

    def get_ad_images_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdImage's associated with this account."""
        return self.iterate_edge_aio(AdImage, fields, params, limit=limit)

    def get_broad_category_targeting_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over BroadCategoryTargeting's associated with this
        account.
        """
        return self.iterate_edge_aio(baseobjects.BroadCategoryTargeting, fields, params, limit=limit)

    def get_connection_objects_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over ConnectionObject's associated with this account.
        """
        return self.iterate_edge_aio(baseobjects.ConnectionObject, fields, params, limit=limit)

    def get_custom_audiences_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over CustomAudience's associated with this account.
        """
        return self.iterate_edge_aio(CustomAudience, fields, params, limit=limit)

    def get_partner_categories_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over PartnerCategory's associated with this account.
        """
        return self.iterate_edge_aio(PartnerCategory, fields, params, limit=limit)

    def get_rate_cards_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over RateCard's associated with this account."""
        return self.iterate_edge_aio(baseobjects.RateCard, fields, params, limit=limit)

    def get_reach_estimate_aio(self, fields=None, params=None, limit=1000):
        """
        Returns iterator over ReachEstimate's associated with this account.
        """
        return self.iterate_edge_aio(baseobjects.ReachEstimate, fields, params, limit=limit)

    def get_transactions_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Transaction's associated with this account."""
        return self.iterate_edge_aio(baseobjects.Transaction, fields, params, limit=limit)

    def get_ad_preview_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over previews generated under this account."""
        return self.iterate_edge_aio(baseobjects.GeneratePreview, fields, params, limit=limit)

    def get_ad_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns all the ad labels associated with the ad account
        """
        return self.iterate_edge_aio(baseobjects.AdLabel, fields, params, limit=limit)

    def get_ad_creatives_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad creatives associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.AdCreativesByLabels, fields, params, limit=limit)

    def get_ads_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad Groups associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.AdsByLabels, fields, params, limit=limit)

    def get_adsets_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad sets associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.AdSetsByLabels, fields, params, limit=limit)

    def get_campaigns_by_labels_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad campaigns associated with the ad AdLabel
        """
        return self.iterate_edge_aio(baseobjects.CampaignsByLabels, fields, params, limit=limit)

    def get_minimum_budgets_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the minimum budget associated with the AdAccount
        """
        return self.iterate_edge_aio(baseobjects.MinimumBudget, fields, params,
                                     limit=limit)

    def get_ad_place_page_sets_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the ad place page sets associated with the AdAccount
        """
        return self.iterate_edge_aio(baseobjects.AdPlacePageSet, fields, params, limit=limit)

    def get_custom_conversions_aio(self, fields=None, params=None, limit=1000):
        """
        Returns the custom conversions associated with the AdAccount
        """
        return self.iterate_edge_aio(baseobjects.CustomConversion, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, async=False,
                         has_action=None, needs_action_device=None, has_filters=False, for_date=None):
        """
        If async is False, returns EdgeIterator.

        If async is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if async:
            return self.iterate_edge_async_aio(
                Insights, fields, params, has_action,
                needs_action_device, limit=limit, has_filters=has_filters, for_date=for_date
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )

    def get_ads_pixels_aio(self, fields=None, params=None, limit=100):
        return self.iterate_edge_aio(
            AdsPixel,
            fields,
            params,
            include_summary=False,
            limit=limit
        )


class AdAccountGroup(AbstractCrudAioObject, baseobjects.AdAccountGroup):
    pass


class AdAccountGroupUser(AbstractCrudAioObject, baseobjects.AdAccountGroupUser):
    pass


class Campaign(AbstractCrudAioObject, baseobjects.Campaign):
    def get_ad_sets_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdSet's associated with this campaign."""
        return self.iterate_edge_aio(AdSet, fields, params, limit=limit)

    def get_ads_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Ad's associated with this campaign."""
        return self.iterate_edge_aio(Ad, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, async=False,
                         has_action=None, needs_action_device=None, for_date=None):
        """
        If async is False, returns EdgeIterator.

        If async is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if async:
            return self.iterate_edge_async_aio(
                Insights,
                fields,
                params, has_action, needs_action_device, limit=limit, for_date=for_date
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )


class AdSet(AbstractCrudAioObject, baseobjects.AdSet):
    def get_ads_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over Ad's associated with this set."""
        return self.iterate_edge_aio(Ad, fields, params, limit=limit)

    def get_ad_creatives_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdCreative's associated with this set."""
        return self.iterate_edge_aio(AdCreative, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, async=False,
                         has_action=None, needs_action_device=None):
        """
        If async is False, returns EdgeIterator.

        If async is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if async:
            return self.iterate_edge_async_aio(
                Insights,
                fields,
                params, has_action, needs_action_device, limit=limit
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )


class TargetingSearch(AbstractCrudAioObject, baseobjects.AbstractCrudObject, baseobjects.TargetingSearch):

    # TODO: replace this hack with a paged iterator abstract base
    class Field(object):
        id = 'id'

    class DemographicSearchClasses(object):
        demographics = 'demographics'
        ethnic_affinity = 'ethnic_affinity'
        family_statuses = 'family_statuses'
        generation = 'generation'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        income = 'income'
        industries = 'industries'
        life_events = 'life_events'
        markets = 'markets'
        moms = 'moms'
        net_worth = 'net_worth'
        office_type = 'office_type'
        politics = 'politics'

    class TargetingSearchTypes(object):
        country = 'adcountry'
        education = 'adeducationschool'
        employer = 'adworkemployer'
        geolocation = 'adgeolocation'
        geometadata = 'adgeolocationmeta'
        interest = 'adinterest'
        interest_suggestion = 'adinterestsuggestion'
        interest_validate = 'adinterestvalid'
        keyword = 'adkeyword'
        locale = 'adlocale'
        major = 'adeducationmajor'
        position = 'adworkposition'
        radius_suggestion = 'adradiussuggestion'
        targeting_category = 'adtargetingcategory'
        zipcode = 'adzipcode'

    @classmethod
    def get_endpoint(cls):
        return 'search'

    @classmethod
    def get_all_countries(cls):
        ts = cls('no')
        country_iter = EdgeLessIterator(
                ts, params={'type': ts.TargetingSearchTypes.country})
        country_iter.submit_next_page_aio()
        return [x for x in country_iter]


class Ad(AbstractCrudAioObject, baseobjects.Ad):
    def get_ad_creatives_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over AdCreatives associated with this ad."""
        return self.iterate_edge_aio(AdCreative, fields, params, limit=limit)

    def get_targeting_description_aio(self, fields=None, params=None, limit=1000):
        """Returns TargetingDescription object associated with this ad."""
        return self.edge_object(baseobjects.TargetingDescription, fields, params)

    def get_keyword_stats_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over KeywordStats associated with this ad."""
        return self.edge_object(baseobjects.KeywordStats, fields, params)

    def get_ad_preview_aio(self, fields=None, params=None, limit=1000):
        """Returns AdPreview object associated with this ad."""
        return self.edge_object(baseobjects.AdPreview, fields, params)

    def get_reach_estimate_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over ReachEstimates associated with this ad."""
        return self.iterate_edge_aio(baseobjects.ReachEstimate, fields, params, limit=limit)

    def get_click_tracking_tag_aio(self, fields=None, params=None, limit=1000):
        """Returns iterator over ClickTrackingTags associated with this ad."""
        return self.iterate_edge_aio(ClickTrackingTag, fields, params, limit=limit)

    def get_leads_aio(self, fields=None, params=None, limit=1000):
        """
        Returns all the leads associated with the Ad
        """
        return self.iterate_edge_aio(Lead, fields, params, limit=limit)

    def get_insights_aio(self, fields=None, params=None, limit=1000, async=False,
                         has_action=None, needs_action_device=None):
        """
        If async is False, returns EdgeIterator.

        If async is True, creates a job and job iterator for it and
        returns the job iterator (AsyncAioJobIterator class, subclass of EdgeIterator).

        Regardless the async parameter, it puts the iterator to the queue so that
        the results of execution are later available  through
        FacebookAdsAsyncApi.get_default_api().get_all_async_results() call.
        """
        if async:
            return self.iterate_edge_async_aio(
                Insights,
                fields,
                params, has_action, needs_action_device, limit=limit
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )


class AdConversionPixel(AbstractCrudAioObject, baseobjects.AdConversionPixel):
    pass


class AdsPixel(AbstractCrudAioObject, baseobjects.AdsPixel):
    pass


class AdCreative(AbstractCrudAioObject, baseobjects.AdCreative):
    pass


class AdImage(AbstractCrudAioObject, baseobjects.AdImage):
    pass


class AdVideo(AbstractCrudAioObject, baseobjects.AdVideo):
    pass


class ClickTrackingTag(AbstractCrudAioObject, baseobjects.ClickTrackingTag):
    pass


class CustomAudience(AbstractCrudAioObject, baseobjects.CustomAudience):
    pass


class LookalikeAudience(AbstractCrudAioObject, baseobjects.LookalikeAudience):
    pass


class PartnerCategory(AbstractCrudAioObject, baseobjects.PartnerCategory):
    pass


class ReachFrequencyPrediction(AbstractCrudAioObject, baseobjects.ReachFrequencyPrediction):
    pass


class Business(AbstractCrudAioObject, baseobjects.Business):
    def get_ad_accounts_aio(self, fields=None, params=None, limit=50):
        return self.iterate_edge_aio(AdAccount, fields, params, limit=limit)

    def get_product_catalogs_aio(self, fields=None, params=None):
        return self.iterate_edge_aio(ProductCatalog, fields, params)

    def get_insights_aio(self, fields=None, params=None, limit=500, async=False):
        if async:
            return self.iterate_edge_async_aio(
                Insights,
                fields,
                params, limit=limit
            )
        return self.iterate_edge_aio(
            Insights,
            fields,
            params,
            include_summary=False, limit=limit
        )

    def get_order_id_attributions_aio(self, fields=None, params=None, limit=100, async=False):
        if async:
            return self.iterate_edge_async_aio(
                OrderIdAttributions,
                fields,
                params, limit=limit
            )
        return self.iterate_edge_aio(
            OrderIdAttributions,
            fields,
            params,
            include_summary=False, limit=limit
        )

    def get_business_projects_aio(self, fields=None, params=None, limit=50):
        return self.iterate_edge_aio(BusinessProject, fields, params, limit=limit)


class BusinessProject(AbstractCrudAioObject, baseobjects.AbstractCrudObject):

    class Field(object):
        id = 'id'
        name = 'name'

    @classmethod
    def get_endpoint(cls):
        return 'businessprojects'


class ProductCatalog(AbstractCrudAioObject, baseobjects.ProductCatalog):
    pass


class ProductFeed(AbstractCrudAioObject, baseobjects.ProductFeed):
    pass


class ProductFeedUpload(AbstractCrudAioObject, baseobjects.ProductFeedUpload):
    pass


class ProductFeedUploadError(AbstractCrudAioObject, baseobjects.ProductFeedUploadError):
    pass


class ProductSet(AbstractCrudAioObject, baseobjects.ProductSet):
    pass


class ProductGroup(AbstractCrudAioObject, baseobjects.ProductGroup):
    pass


class Product(AbstractCrudAioObject, baseobjects.Product):
    pass


class ProductAudience(AbstractCrudAioObject, baseobjects.ProductAudience):
    pass


class AdLabel(AbstractCrudAioObject, baseobjects.AdLabel):
    pass


class Lead(AbstractCrudAioObject, baseobjects.Lead):
    pass


class LeadgenForm(AbstractCrudAioObject, baseobjects.LeadgenForm):
    pass


class AdPlacePageSet(AbstractCrudAioObject, baseobjects.AdPlacePageSet):
    pass


class CustomConversion(AbstractCrudAioObject, baseobjects.CustomConversion):
    pass


class Insights(AbstractCrudAioObject, baseobjects.Insights):
    # TODO: implement async get method
    pass


class AsyncAioJob(AbstractCrudAioObject, baseobjects.AsyncJob):

    def __init__(self, *args, **kwargs):
        self.edge_params = kwargs.pop('edge_params', None)
        self.has_action = kwargs.pop('has_action', None)
        self.needs_action_device = kwargs.pop('needs_action_device', None)
        self.has_filters = kwargs.pop('has_filters', False)

        super(AsyncAioJob, self).__init__(*args, **kwargs)

    def get_result(self, params=None, limit=1000):
        """
        Gets the final result from an async job
        Accepts params such as limit
        """

        return self.iterate_edge_aio(
            self.target_objects_class,
            params=params,
            include_summary=False,
            limit=limit
        )

    def __nonzero__(self):
        if self.Field.async_percent_completion not in self._data:
            self.remote_read()
        return self[self.Field.async_percent_completion] == 100

    def get_async_status(self):
        """
        Returns async status, (Job Completed, Job Failed, Job Not Started, Job Started, Job Running)

        :rtype: str
        """
        if self.Field.async_status not in self:
            return 0
        return self[self.Field.async_status]

    def get_async_percent_completion(self):
        """
        Returns percent completion from 0 to 100

        :rtype: int
        """
        return int(self[self.Field.async_percent_completion])


class AsyncAioJobIterator(AioEdgeIterator):
    def __init__(self, source_object, target_objects_class,
                 fields=None, params=None, include_summary=True,
                 limit=500, stage='async_get_job',
                 no_progress_timeout=900, not_started_timeout=600,
                 has_action=None, needs_action_device=None, has_filters=False,
                 for_date=None):

        super(AsyncAioJobIterator, self).__init__(source_object, target_objects_class,
                                                  fields=fields, params=params,
                                                  include_summary=include_summary,
                                                  limit=limit)
        self.job = None
        self.failed_attempt = 0
        self.failed_with_unsupported_request = 0
        self.failed_with_unknown_error = 0
        self.attempt = 0
        self.request_issued = None
        self.job_id = None
        self.stage = None
        self.stage = stage
        self.job_started_at = time.time()
        self.job_last_checked = None

        self.job_previous_completion_value = 0
        self.job_last_completion_change_time = time.time()
        self.no_progress_timeout = no_progress_timeout
        self.not_started_timeout = not_started_timeout

        self.has_action = has_action
        self.needs_action_device = needs_action_device
        self.has_filters = has_filters
        self.for_date = for_date

    def launch_job(self):
        """
        1. Calls POST to create job
        2. Creates and store in attributes AsyncAioJob
        3. Puts self in futures

        :return: None
        """
        # To force an async response from an edge, do a POST instead of GET.
        # The response comes in the format of an AsyncAioJob which
        # indicates the progress of the async request.
        response = {}
        for i in range(5):
            # TODO: refactor this into async schema like in regular AioEdgeIterator
            try:
                response = self._source_object.get_api_assured().call(
                    'POST',
                    (self._source_object.get_id_assured(), self._target_objects_class.get_endpoint()),
                    params=self.params,
                ).json()
            except FacebookRequestError as exc:
                if i < 4 and (exc.api_error_code() in [FacebookErrorCodes.unknown,
                                                       FacebookErrorCodes.temporary] or
                              not exc.is_body_json()):
                    time.sleep(15 + i * 15)
                elif i < 4 and exc.api_error_code() == FacebookErrorCodes.rate_limit:
                    time.sleep(60 + i * 60)
                else:
                    raise exc
            else:
                if isinstance(response, string_types) and i < 4:
                    time.sleep(15 + i * 15)
                else:
                    if isinstance(response, string_types):
                        raise FacebookRequestError(
                            "Facebook response is a string",
                            {"method": "POST", "path": "/{}/{}".format(
                                self._source_object.get_id_assured(),
                                self._target_objects_class.get_endpoint()),
                             "params": self.params},
                            500, {}, response
                        )
                    break

        self.job_started_at = time.time()
        self.attempt += 1
        self.failed_attempt = 0

        if 'report_run_id' in response:
            response['id'] = response['report_run_id']

        # AsyncAioJob stores the real iterator
        # for when the result is ready to be queried
        self.job = AsyncAioJob(self._target_objects_class, edge_params=self.params,
                               has_action=self.has_action,
                               needs_action_device=self.needs_action_device,
                               has_filters=self.has_filters)
        self.job._set_data(response)
        self.job_id = response['id'] if 'id' in response else 'no id'
        self._source_object.get_api_assured().put_in_futures(self)
        logger.debug('started a job, job_id: {}'.format(response['id'] if 'id' in response else 'no id'))

        self.job_last_completion_change_time = time.time()
        self.job_previous_completion_value = 0

    def submit_next_page_aio(self):
        self._source_object.get_api_assured().put_in_futures(self)

    def get_all_results(self):
        return list(self.job.get_result(limit=self.limit))

    def extract_results(self):
        """
        Returns self if the results are not ready, otherwise returns iterator by results
        of class AioEdgeIterator.
        """
        if self.job_last_checked and time.time() - self.job_last_checked < 15:
            return self
        if 'filtering' in self.params and self.params['filtering']:
            exc_class = JobFailedForArchivedDataException
        else:
            exc_class = JobFailedException

        # TODO: refactor this into async schema like in regular AioEdgeIterator
        try:
            self.job.remote_read()
        except FacebookRequestError as exc:
            if exc.api_error_code() == FacebookErrorCodes.unsupported_request and \
                    self.failed_with_unsupported_request < 2:
                logger.warn("job id {} recieved unsupported request error, "
                            "attempts failed with the error {}, job requested at {}, "
                            "report params: {}, response: '{}'".format(
                    self.job_id, self.failed_with_unsupported_request,
                    datetime.fromtimestamp(self.job_started_at),
                    self.params, str(self.job)))

                time.sleep(3 + 3 * self.failed_with_unsupported_request)
                self.failed_with_unsupported_request += 1
                self.job_last_checked = time.time()
                return self

            elif (exc.api_error_code() in (FacebookErrorCodes.unknown, 2601,
                                           FacebookErrorCodes.temporary) or
                      not exc.is_body_json()) and self.failed_with_unknown_error < 4:
                logger.warn("job id {} recieved unknown error,"
                            "attempts failed with the error {}, job requested at {}, "
                            "report params: {}, response: '{}'".format(
                    self.job_id, self.failed_with_unknown_error,
                    datetime.fromtimestamp(self.job_started_at),
                    self.params, str(self.job)))

                time.sleep(5 + 2 * self.failed_with_unknown_error)
                self.failed_with_unknown_error += 1
                self.job_last_checked = time.time()
                return self

            if exc.api_error_code() == FacebookErrorCodes.unsupported_request:
                async_status = 'Job Failed'
                current_job_completion_value = 0
            else:
                raise exc_class("job id {} recieved unsupported request error, "
                                "attempts failed with the error {}, job requested at {}, "
                                "report params: {}, response: '{}'".format(
                    self.job_id, self.failed_with_unsupported_request,
                    datetime.fromtimestamp(self.job_started_at),
                    self.params, str(self.job)))
        else:
            async_status = self.job.get_async_status()
            current_job_completion_value = self.job.get_async_percent_completion()

        self.job_last_checked = time.time()

        logger.debug('job_id: {}, completion: {}, status: {}'.format(
                self.job_id, current_job_completion_value, self.job.get_async_status()))

        if async_status == 'Job Completed':
            if self.job.get_async_percent_completion() == 100:
                self.job_previous_completion_value = current_job_completion_value
                # return new iterator over job's results
                results_iterator = self.job.get_result(limit=self.limit)
                return results_iterator

            elif self.attempt >= 3:
                raise exc_class("job id {} failed for {}, reason unknown, response: {}, "
                         "report params: {}".format(self.job_id, self, str(self.job), self.params))

            # create new job and wait for it to complete
            time.sleep(10 + 10 * self.failed_attempt)
            self.launch_job()

        elif async_status == 'Job Failed':
            if self.failed_attempt >= 4:
                logger.warn("job id {} failed, failed attempts {}, "
                            "job requested at {}, attempts made {}, "
                            "report params: {}, response: '{}'".format(
                    self.job_id, self.failed_attempt,
                    datetime.fromtimestamp(self.job_started_at), self.attempt,
                    self.params, str(self.job)))

                if ('filtering' in self.params and self.params['filtering'] and self.attempt >= 1) or self.attempt >= 3:
                    # we make 4 attempts to get the data and only then fail
                    self.last_error = exc_class(
                        "job id {} failed, failed attempts {}, job requested at {}, "
                        "attempts made {}, report params: {}, response: '{}'".format(
                            self.job_id, self.failed_attempt,
                            datetime.fromtimestamp(self.job_started_at), self.attempt,
                            self.params, str(self.job)))
                    self._request_failed = True
                    self.job_last_checked = time.time()
                    return self

                # if we haven't made 3 attempts, we need to reissue the query
                time.sleep(20 + self.attempt * 90)
                self.launch_job()

            else:
                # job check says that it's failed but really it may be still running
                # we just need to recheck it's status in several seconds
                time.sleep(1 + 2 * self.failed_attempt)
                self.failed_attempt += 1

        elif async_status == "Job Not Started":
            if time.time() - self.job_started_at > (self.not_started_timeout + 660 * self.attempt):
                logger.warn("job id {} is not started yet, "
                            "job requested at {}, attempts made {}, "
                            "report params: {}, response: '{}'".format(
                    self.job_id, datetime.fromtimestamp(self.job_started_at),
                    self.attempt, self.params, str(self.job)))

                if self.attempt >= 2:
                    self.last_error = exc_class(
                        "job id {} is not started yet, job requested at {}, "
                        "attempts made {}, report params: {}, response: '{}'".format(
                            self.job_id, datetime.fromtimestamp(self.job_started_at),
                            self.attempt, self.params, str(self.job)))
                    self._request_failed = True
                    self.job_last_checked = time.time()
                    return self

                time.sleep(10 + 10 * self.attempt)
                self.launch_job()

        else:
            if time.time() - self.job_last_completion_change_time > self.no_progress_timeout:
                logger.warn("job id {} stuck, completion {}, "
                            "job requested at {}, attempts made {}, "
                            "report params: {}, response: '{}'".format(
                    self.job_id, current_job_completion_value,
                    datetime.fromtimestamp(self.job_started_at), self.attempt,
                    self.params, str(self.job)))

                if self.attempt >= 4:
                    self.last_error = exc_class(
                        "job id {} stuck, completion {}, job requested at {}, "
                        "attempts made {}, report params: {}, response: '{}'".format(
                            self.job_id, current_job_completion_value,
                            datetime.fromtimestamp(self.job_started_at), self.attempt,
                            self.params, str(self.job)))
                    self._request_failed = True
                    self.job_last_checked = time.time()
                    return self

                # create new job and wait for it to complete
                time.sleep(10 + 10 * self.attempt)
                self.launch_job()

        if self.job_previous_completion_value != current_job_completion_value:
            self.job_last_completion_change_time = time.time()
        self.job_previous_completion_value = current_job_completion_value
        # we need to return self into thread pool and wait for job completion
        return self


class OrderIdAttributions(AbstractCrudAioObject, baseobjects.OrderIdAttributions):
    pass
