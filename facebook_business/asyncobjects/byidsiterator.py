from facebook_business.asyncobjects.aioedgeiterator import AioEdgeIterator


class ByIdsIterator(AioEdgeIterator):
    def __init__(self, target_object_class, ids, fields=None, params=None,
                 include_summary=False, limit=50):
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
