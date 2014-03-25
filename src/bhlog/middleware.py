import bhlog.handlers
import logging


class LogEachRequest(object):
    def process_request(self, request):
        logger = logging.getLogger('per_request')
        req_handler = filter(
            lambda ll : isinstance(
                ll, bhlog.handlers.EachRequestRotatingFileHandler),
            logger.handlers)
        if not req_handler:
            logger.addHandler(
                bhlog.handlers.EachRequestRotatingFileHandler(request))
        req_handler = filter(
            lambda ll : isinstance(ll, bhlog.handlers.EachRequestRotatingFileHandler),
            logger.handlers)
        req_handler.req = request


def make_handler(req='/tmp/per_request/start.log'):
    hndl = bhlog.handlers.EachRequestRotatingFileHandler(req)
    hndl.setLevel(logging.DEBUG)
    hndl.setFormatter("")
    return hndl

