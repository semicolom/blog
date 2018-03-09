from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

# Database
DATABASES['default'].update({
    'USER': 'blog',
    'PASSWORD': 'blog',
    'HOST': '127.0.0.1',
})

# Site contants
SITE_INFO['GOOGLE_ANALYTICS'] = None
