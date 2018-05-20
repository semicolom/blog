"""
Django settings for Blog project.
"""

import os

import environ

root = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
BASE_DIR = root()
env = environ.Env()
env.read_env(str(root.path('.env')))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='dev')

DEBUG = False

ALLOWED_HOSTS = ['www.semicolom.com']

ADMINS = [
    ('Toni Colom', 'tcolomquetglas@gmail.com')
]
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin')

# Application definition
INSTALLED_APPS = [
    # Local
    'main.apps.MainConfig',
    'blog.apps.BlogConfig',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Third party
    'ckeditor',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.site_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': env('DJANGO_DATABASE_DEFAULT_USER', default='blog'),
        'PASSWORD': env('DJANGO_DATABASE_DEFAULT_PASSWORD', default='blog'),
        'HOST': env('DJANGO_DATABASE_DEFAULT_HOST', default='127.0.0.1'),
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Django debug toolbar settings
DEBUG_TOOLBAR = False

# Loggin
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# Site constants
SITE_INFO = {
    'AUTHOR_NAME': "Toni Colom",
    'SITE_NAME': "semicolom;",
    'SITE_URL': 'http://www.semicolom.com',
    'GITHUB_URL': "https://github.com/semicolom",
    'GOOGLE_ANALYTICS': "UA-110395817-1",
}

# AWS S3
DEFAULT_FILE_STORAGE = 'main.storage_backends.MediaStorage'
AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID', default='AKIAJTAJRCQOOF6ISXXQ')
AWS_SECRET_ACCESS_KEY = env(
    'DJANGO_AWS_SECRET_ACCESS_KEY',
    default='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'
)
AWS_QUERYSTRING_AUTH = False
AWS_STORAGE_BUCKET_NAME = 'semicolom'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('DJANGO_EMAIL_HOST', default='')
EMAIL_PORT = env('DJANGO_EMAIL_PORT', default='')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = True
SERVER_EMAIL = 'no-reply@semicolom.com'
