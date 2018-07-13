from facebook_business.objects import AsyncJob
from facebook_business.asyncobjects.abstractcrudaioobject import AbstractCrudAioObject


class AsyncAioJob(AbstractCrudAioObject, AsyncJob):

    def __init__(self, *args, **kwargs):
        self.edge_params = kwargs.pop('edge_params', None)
        self.has_action = kwargs.pop('has_action', None)
        self.needs_action_device = kwargs.pop('needs_action_device', None)
        self.needs_carousel_name = kwargs.pop('needs_carousel_name', None)
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
