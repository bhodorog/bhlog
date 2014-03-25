import logging.handlers
import os.path


class EachRequestRotatingFileHandler(logging.handlers.BaseRotatingHandler):
    def __init__(self, req, mode="a", encoding=None, delay=0):
        self.req = self.req_in_use = req
        super(EachRequestRotatingFileHandler, self).__init__(
            self.req_in_use, mode, encoding, delay)

    def shouldRollover(self, record):
        return self.req != self.req_in_use

    def doRollover(self, record):
        if self.stream:
            self.stream.close()
        self.baseFilename = self._determine_new_filename()
        self.mode = 'w'
        self.stream = self._open()
        self.req_in_use = self.req

    def _determine_new_filename(self):
        host = self.req_in_use.META.get("HTTP_HOST")
        path = self.req_in_use.path.replace(os.path.sep, ".")
        basename = os.path.join(host, path)
        new_filename = os.path.join(
            os.path.dirname(self.baseFilename), basename)
        count = 0
        while os.path.exist(new_filename):
            count += 1
            new_filename = "{0}.{1}".format(new_filename, count)
        return new_filename

