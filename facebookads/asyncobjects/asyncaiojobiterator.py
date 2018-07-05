import logging
import time
from datetime import datetime

from six import string_types
from requests.exceptions import ConnectionError

from facebookads.asyncobjects.aioedgeiterator import AioEdgeIterator
from facebookads.asyncobjects.asyncaiojob import AsyncAioJob
from facebookads.exceptions import FacebookRequestError, JobFailedException
from facebookads.utils.fberrcodes import FacebookErrorCodes

logger = logging.getLogger("facebookclient")


class AsyncAioJobIterator(AioEdgeIterator):
    def __init__(self, source_object, target_objects_class,
                 fields=None, params=None, include_summary=False,
                 limit=500, stage='async_get_job',
                 no_progress_timeout=1400, not_started_timeout=600,
                 has_action=None, needs_action_device=None, has_filters=False,
                 for_date=None, needs_carousel_name=False):

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
        self.needs_carousel_name = needs_carousel_name

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
            except ConnectionError as exc:
                if i < 4:
                    time.sleep(10 + i * 10)
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
                               has_filters=self.has_filters,
                               needs_carousel_name=self.needs_carousel_name)
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

        # TODO: refactor this into async schema like in regular AioEdgeIterator
        try:
            self.job.remote_read()
        except FacebookRequestError as exc:
            if exc.api_error_code() == FacebookErrorCodes.unsupported_request and \
                    self.failed_with_unsupported_request < 2:
                logger.warning(
                    "job id {} recieved unsupported request error, attempts failed with the "
                    "error {}, job requested at {}, report params: {}, response: '{}'".format(
                        self.job_id, self.failed_with_unsupported_request,
                        datetime.fromtimestamp(self.job_started_at),
                        self.params, str(self.job)))

                time.sleep(3 + 3 * self.failed_with_unsupported_request)
                self.failed_with_unsupported_request += 1
                self.job_last_checked = time.time()
                return self

            elif (exc.api_error_code() in (FacebookErrorCodes.unknown, 2601,
                                           FacebookErrorCodes.temporary)
                  or not exc.is_body_json()) and self.failed_with_unknown_error < 4:
                logger.warning(
                    "job id {} recieved unknown error, attempts failed with the error {}, "
                    "job requested at {}, report params: {}, response: '{}'".format(
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
                raise JobFailedException(
                    "job id {} recieved unsupported request error, attempts failed "
                    "with the error {}, job requested at {}, report params: {}, "
                    "response: '{}'".format(
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
                raise JobFailedException(
                    "job id {} failed for {}, reason unknown, response: {}, "
                    "report params: {}".format(
                        self.job_id, self, str(self.job), self.params))

            # create new job and wait for it to complete
            time.sleep(10 + 10 * self.failed_attempt)
            self.launch_job()

        elif async_status == 'Job Failed':
            if self.failed_attempt >= 4:
                logger.warning(
                    "job id {} failed, failed attempts {}, job requested at {}, "
                    "attempts made {}, report params: {}, response: '{}'".format(
                        self.job_id, self.failed_attempt,
                        datetime.fromtimestamp(self.job_started_at), self.attempt,
                        self.params, str(self.job)))

                if ('filtering' in self.params and self.params['filtering'] and self.attempt >= 1)\
                        or self.attempt >= 3:
                    # we make 4 attempts to get the data and only then fail
                    self.last_error = JobFailedException(
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
                logger.warning(
                    "job id {} is not started yet, job requested at {}, "
                    "attempts made {}, report params: {}, response: '{}'".format(
                        self.job_id, datetime.fromtimestamp(self.job_started_at),
                        self.attempt, self.params, str(self.job)))

                if self.attempt >= 2:
                    self.last_error = JobFailedException(
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
                logger.warning(
                    "job id {} stuck, completion {}, job requested at {}, "
                    "attempts made {}, report params: {}, response: '{}'".format(
                        self.job_id, current_job_completion_value,
                        datetime.fromtimestamp(self.job_started_at), self.attempt,
                        self.params, str(self.job)))

                if self.attempt >= 2:
                    self.last_error = JobFailedException(
                        "job id {} stuck, completion {}, job requested at {}, "
                        "attempts made {}, report params: {}, response: '{}'".format(
                            self.job_id, current_job_completion_value,
                            datetime.fromtimestamp(self.job_started_at), self.attempt,
                            self.params, str(self.job)))
                    self._request_failed = True
                    self.job_last_checked = time.time()
                    return self

                # create new job and wait for it to complete
                time.sleep(10 + 20 * self.attempt)
                self.launch_job()

        if self.job_previous_completion_value != current_job_completion_value:
            self.job_last_completion_change_time = time.time()
        self.job_previous_completion_value = current_job_completion_value
        # we need to return self into thread pool and wait for job completion
        return self
