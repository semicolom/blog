from .test import *

DEBUG = True
SECRET_KEY = 'dev'

# Database
DATABASES['default'].update({
    'USER': 'blog',
    'PASSWORD': 'blog',
    'HOST': '127.0.0.1',
})

# Django debug toolbar settings
DEBUG_TOOLBAR = True
if DEBUG_TOOLBAR:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

# Site contants
SITE_INFO['GOOGLE_ANALYTICS'] = None
SITE_INFO['SITE_URL'] = 'http://127.0.0.1:8000'

# AWS S3
AWS_STORAGE_BUCKET_NAME = 'semicolom-dev'
