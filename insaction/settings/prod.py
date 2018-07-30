import os

from django.core.management.utils import get_random_secret_key

from . import *

SECRET_KEY = os.environ.get('APP_SECRET_KEY', get_random_secret_key())

DEBUG = False

SHOW_MAINTENANCE = True

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
            'handlers': ['file'],
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


def get_database_password():
    if not 'DB_PASSWD' in os.environ:
        raise OSError('Bad environment configuration: Missing DB_PASSWD in environment variables')
    return os.environ.get('DB_PASSWD')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insaction',
        'USER': 'insaction_user',
        'PASSWORD': get_database_password(),
        'HOST': 'localhost',
        'PORT': '',
    }
}
