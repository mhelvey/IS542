__author__ = 'mhelvey'


def get_next():
    i = 0
    while True:
        # create next unique id and yield it.
        i += 1
        yield i


# in the middleware
class MyMiddleware(object):
    def process_request(self, request):
        request.generator = get_next()