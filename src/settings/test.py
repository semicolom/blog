from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

# Database
DATABASES['default'].update({
    'USER': 'blog',
    'PASSWORD': 'blog',
    'HOST': '127.0.0.1',
})
