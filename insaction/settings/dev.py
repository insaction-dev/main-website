from . import *

DEBUG = True
ALLOWED_HOSTS = "*"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gv2ue9ejh4yl$hf+hu7-ai=j)86m$joj^_6!k=9e-mmmhqdmom'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'rules': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
