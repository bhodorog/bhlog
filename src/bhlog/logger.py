import logging
import logging.config


from .usefull import current_call_stack


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'bhg_full': {
            'format': '%(name)s %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            },
        'bhg_verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'bhg_simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'bhg_null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'bhg_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'bhg_simple'
        },
        'bhg_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/call_hierarchy.log',
            'formatter': 'bhg_full',
        },
    },
    'loggers': {
        'bhg_call_hierarchy': {
            'handlers': ['bhg_null', 'bhg_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
})
log_ch = logging.getLogger("bhg_call_hierarchy")


def log_ch_debug(msg="", except_modules=[]):
    #TODO ipdb here to see if we can add a file handler in case
    # only bhg-null handler is defined for this
    log_ch.debug("{0}; calls={1}".format(msg, current_call_stack(except_modules)))


def set_logger_level(name, level):
    if name in logging.Logger.manager.loggerDict:
        lgr = logging.getLogger(name)
        lgr.setLevel(level)


def enable_logger(name):
    set_logger_level(name, logging.DEBUG)


def disable_logger(name):
    set_logger_level(name, logging.ERROR)
