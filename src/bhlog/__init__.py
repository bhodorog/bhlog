try:
    from django.conf import settings
except:
    pass
else:
    def monkey_patch_django_db():
        """ 1. add a logger to logging.Logger.manager.dictLog (see 3)
            * the logger should have a custom handler which knows how to log
              each request to its own file (using a middleware which should be
              probably monkey-patched)
            * magically add current_call_stack to the logRecord (adapter?)
         2. make sure settings.DEBUG = True (to make sure DebugCursorWrapper is
         used)
         3. Would be nice to intercept the logRecords emitted by
         DebugCursorWrapper and emit them to the above custom
         RotatingFileHandler (add the logger as parrent for
         django.db.backends?)"""
        settings.DEBUG = True
