from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

# Site contants
SITE_INFO['GOOGLE_ANALYTICS'] = None

# AWS S3
AWS_STORAGE_BUCKET_NAME = 'semicolom-test'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
