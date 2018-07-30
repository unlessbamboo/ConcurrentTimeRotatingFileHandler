# coding:utf8
import os


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': ('%(levelname)s %(asctime)s %(module)s '
                       '%(filename)s:%(lineno)s '
                       '%(process)d %(thread)d %(message)s')
        },
    },
    'filters': {},
    'handlers': {},
    'loggers': {},
}
LOG_DIR = '/data/logs'
ROTATEHANDLER = 'clogtimehandler.ConcurrentTimeRotatingFileHandler'

for name in ('info', 'error'):
    path = os.path.join(LOG_DIR, '{}.log'.format(name))
    handler = {
        'level': 'INFO',
        'class': ROTATEHANDLER,
        'filename': path,
        'formatter': 'verbose',
        'when': 'midnight',
    }
    logger = {
        'handlers': [name],
        'level': 'INFO',
        'propagate': True,
    }
    LOGGING['handlers'][name] = handler
    LOGGING['loggers'][name] = logger
