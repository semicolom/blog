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

# AWS S3
AWS_STORAGE_BUCKET_NAME = 'semicolom-test'
AWS_ACCESS_KEY_ID = 'AKIAJTAJRCQOOF6ISXXQ'
AWS_SECRET_ACCESS_KEY = '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'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
