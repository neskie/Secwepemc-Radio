# Django settings for radio project.
import os
from local_settings import *
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'America/Vancouver'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_URL = 'http://secwepemcradio.ath.cx:8001/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'radio.urls'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.gis',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'weblog',
    'tagging',
    'django_extensions',
    'show',
    'lib',
    'nations',
    'audio',
    'rb',
    'events',
    'treemenus',
)
