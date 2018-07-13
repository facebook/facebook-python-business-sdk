from facebook_business.asyncapi import FacebookAdsAsyncApi


class AbstractCrudAioObject(object):
    """
    Extends AbstractCrudObject and implements async iter_edge operation.
    """

    @classmethod
    def get_by_ids(cls, ids, params=None, fields=None, api=None, limit=50):
        """Get objects by id list
        :type cls: AbstractCrudObject
        :type ids: list | set | tuple
        :type params: didct
        :type fields: list | tuple
        :type api: FacebookAdsAsyncApi
        :param limit: how big should slices be
        :rtype: list[dict]
        """
        from facebook_business.asyncobjects.byidsiterator import ByIdsIterator

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
            if response.request_failed:
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
                         include_summary=False, limit=1000):
        """
        Creates, sends it to the futures queue and returns EdgeIterator with argument self as source_object and
        the rest as given __init__ arguments.

        Note: list(iterate_edge_aio(...)) can prefetch all the objects.
        """
        from facebook_business.asyncobjects.aioedgeiterator import AioEdgeIterator

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
                               has_filters=False, for_date=None, needs_carousel_name=False):
        """
        Returns an AsyncAioJob which can be checked using remote_read()
        to verify when the job is completed and the result ready to query
        or download using get_result()
        :type target_objects_class: AbstractCrudObject
        """
        from facebook_business.asyncobjects.asyncaiojobiterator import AsyncAioJobIterator

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
            has_filters=has_filters, for_date=for_date,
            needs_carousel_name=needs_carousel_name
        )

        result.launch_job()
        return result
