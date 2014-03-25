import bhlog.handlers
import logging
import os.path


class LogEachRequest(object):
    def process_request(self, request):
        logger = logging.getLogger('django.db')
        req_handler = filter(
            lambda ll : isinstance(
                ll, bhlog.handlers.EachRequestRotatingFileHandler),
            logger.handlers)
        if not req_handler:
            logger.addHandler(make_handler(request))
        req_handler = filter(
            lambda ll : isinstance(ll, bhlog.handlers.EachRequestRotatingFileHandler),
            logger.handlers).pop()
        req_handler.req = request


def make_handler(req):
    hndl = bhlog.handlers.EachRequestRotatingFileHandler(req)
    hndl.setLevel(logging.DEBUG)
    hndl.setFormatter("")
    return hndl

