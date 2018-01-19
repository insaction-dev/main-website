import os

from . import *


def get_secret_key():
    path = os.path.join(BASE_DIR, 'secret')

    secret = '!'
    with open(path, 'r') as file:
        secret = file.read()
    
    if not secret == '!':
        return secret.strip()
    else:
        raise IOError('Could not get secret key.')

SECRET_KEY = get_secret_key()

DEBUG = False

ALLOWED_HOSTS = ['51.255.43.58', 'vps505510.ovh.net', 'insaction.org']


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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insaction',
        'USER': 'insaction_user',
        'PASSWORD': get_database_password(),
        'HOST': 'localhost',
        'PORT': '',
    }
}
