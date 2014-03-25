import logging.handlers
import os.path


PATH = '/tmp/per_req/'


class EachRequestRotatingFileHandler(logging.handlers.BaseRotatingHandler):
    def __init__(self, req, mode="a", encoding=None, delay=0):
        self.req = self.req_in_use = req
        self.dirname = PATH
        filename = os.path.join(self.dirname, self._extract_basename())
        self._create_missing_dirs(filename)
        super(EachRequestRotatingFileHandler, self).__init__(
            filename, mode, encoding, delay)

    def shouldRollover(self, record):
        return self.req != self.req_in_use

    def doRollover(self):
        if self.stream:
            self.stream.close()
        new_filename = os.path.join(self.dirname, self._extract_basename())
        self.baseFilename = self._rotate(new_filename)
        self._create_missing_dirs(self.baseFilename)
        self.mode = 'w'
        self.stream = self._open()
        self.req_in_use = self.req

    def _create_missing_dirs(self, filename):
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

    def _rotate(self, new_filename):
        count = 0
        while os.path.exists(new_filename):
            count += 1
            new_filename = "{0}.{1}".format(new_filename, count)
        return new_filename

    def _extract_basename(self):
        host = self.req_in_use.META.get("HTTP_HOST")
        path = self.req_in_use.path.replace(os.path.sep, "_")
        return os.path.join(host, path)

