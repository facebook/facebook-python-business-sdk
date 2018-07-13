from facebook_business.asyncobjects import AioEdgeIterator


class EdgeLessIterator(AioEdgeIterator):
    def __init__(self, source_object,
                 fields=None, params=None, include_summary=False,
                 limit=1000):
        super(EdgeLessIterator, self).__init__(
                source_object, type(source_object), fields=fields,
                params=params, include_summary=include_summary,
                limit=limit)
        self._path = (source_object.get_endpoint(),)
