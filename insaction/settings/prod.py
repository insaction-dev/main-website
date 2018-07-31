import os

from django.core.management.utils import get_random_secret_key

from . import *


def get_env_secret(var):
    configuring = bool(os.environ.get('APP_CONFIGURING', 'False'))
    if configuring and not var in os.environ:
        return get_random_secret_key()
    elif not var in os.environ:
        raise OSError('Bad environment configuration: Missing APP_SECRET_KEY environment variable')
    return os.environ.get(var)


SECRET_KEY = get_env_secret('APP_SECRET_KEY')

DEBUG = False

SHOW_MAINTENANCE = False

ALLOWED_HOSTS = ['.now.sh', '51.255.43.58', 'vps505510.ovh.net', '.insaction.org']

ADMINS = (('Nathan', 'solarliner@gmail.com'), ('Nathan Graule', 'nathan.graule@insa-cvl.fr'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': 'sys.stdout'
        },
        'admin_notify': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'admin_notify'],
            'level': 'INFO',
            'propagate': True,
            'format': 'default'
        },
    },
    'formatters': {
        'default': {
            'format': "%(asctime)s [%(levelname)s:%(module)s] %(message)s"
        }
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'insaction'),
        'USER': os.environ.get('DB_USER', 'insaction'),
        'PASSWORD': get_env_secret('DB_PASSWD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}
