# coding: utf-8
import os
from decouple import Config
from dj_database_url import parse as db_url
from unipath import Path


PROJECT_DIR = Path(__file__).parent


# Workaround to use heroku while decouple doesn't support it.
#def config(param, default=None, cast=lambda v: v):
#    value = os.environ.get(param, default)
#    return cast(value)

config = Config(PROJECT_DIR.child('settings.ini'))


#DEBUG = os.environ.get('DEBUG', '') == 'True'
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Administrator', config('EMAIL_ADMIN')),
)
MANAGERS = ADMINS

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url,
                      default='sqlite:///' + PROJECT_DIR.child('database.db'))
}

ALLOWED_HOSTS = ['.localhost', '.heroku.com', '.herokuapp.com']

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
LANGUAGES = (
    ('pt-br', u'Português'),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '/static/'

SECRET_KEY = config('SECRET_KEY')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zona.urls'

WSGI_APPLICATION = 'zona.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
