import os

from django.core.management import utils

from . import *

SECRET_KEY = os.environ.get('APP_SECRET_KEY')

DEBUG = False

SHOW_MAINTENANCE = True

ALLOWED_HOSTS = ['51.255.43.58', 'vps505510.ovh.net', 'insaction.org']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
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
    path = os.path.join(BASE_DIR, 'psswd')

    psswd = '!'
    with open(path, 'r') as file:
        psswd = file.read()

    if not psswd == '!':
        return psswd.strip()
    else:
        raise IOError('Cannot get database password.')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('GB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST')
    }
}
