"""
Django settings for blpass project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$_a!^h6i^ctsa^60%vzd4p6c#1g=#9c%c$!0=udq8o@zaph-g9'

# APP ADMINISTRATORS
ADMINS = (
    ('pedro rivera', 'pedrorivera@emdyp.me'),
)

MANAGERS = ADMINS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


TEMPLATE_DEBUG = True
ALLOWED_HOSTS = [u'localhost',
                 u'blpass-emdyptests.rhcloud.com',
                 u'.prod.rhcloud.com',
                 u'.prod.rhcloud.com']

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'blpass.wsgi.application'

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registers',
    'citizens',
    'blocks',
    'keys',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blpass.urls'

WSGI_APPLICATION = 'blpass.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Static root

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

#STATICFILES_STORAGE = STATIC_ROOT

# Media roots and url
#abspath = os.path.abspath(__file__)
#MEDIA_ROOT = os.sep.join(abspath.split(os.sep)[:-2] + ['media'])
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')

MEDIA_URL = '/media/'

# Admin module's settings

# GRAPPELLI SETTINGS
if 'grappelli' in INSTALLED_APPS:
    TEMPLATE_CONEXT_PROCESSORS = (
        'django.core.context_processors.request')
    GRAPPELLI_ADMIN_TITLE = 'Coinfest Bogota 2015 - Emdyp'
# BOOTSTRAP ADMIN SETTINGS
elif 'bootstrap_admin' in INSTALLED_APPS:
    from django.conf import global_settings
    temp_contest_processors = global_settings.TEMPLATE_CONTEXT_PROCESSORS
    TEMPLATE_CONTEXT_PROCESSORS = temp_contest_processors + (
        'django.core.context_processors.request',
    )
    BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

# OPENSHIFT CONFIGS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__),'..','registers','templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__),'..','citizens','templates').replace('\\','/'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
