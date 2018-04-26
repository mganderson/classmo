# settings.py meta-data
# last updated: 2018-03-01 @6:21 PM
# last updated by: Jeury Mejia
# file version: 1.2

"""
Django settings for classmo project.
Generated by 'django-admin startproject' using Django 2.0.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o433m!h@^t#g@v==p(u-oku=-n03g*&7dvrftc93-)-&021te2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

## Modified by Mehtab Sidhu
## on 03/17/18
ALLOWED_HOSTS = ['web', 'localhost']


# Application definition

INSTALLED_APPS = [
    'discussions.apps.DiscussionsConfig',
    'schedules.apps.SchedulesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'classmo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'schedules.context_processors.global_context'# custom context processor  
            ],
        },
    },
]


WSGI_APPLICATION = 'classmo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if os.getenv('DOCKER_CONTAINER'):
    POSTGRES_HOST = 'db'
else:
    POSTGRES_HOST = '127.0.0.1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'classmodb',
        ##'NAME': 'postgres',
        'USER': 'classmouser',
        'PASSWORD': 'classmopassword',
        ##'HOST': '127.0.0.1',
        ##'HOST': POSTGRES_HOST,
        'HOST': 'db',
        'PORT': '5432',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'classmodb',
#        'USER': 'classmouser',
#        'PASSWORD': 'classmopassword',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# login redirect
LOGIN_REDIRECT_URL = '/schedules/'

GROUPS = {
    "INSTRUCTORS":"Instructors", 
    "MANAGERS":"Managers",
    "STUDENTS":"Students"
}

# message tags
"""
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert alert-success',
    messages.ERROR: 'alert alert-danger',
    messages.INFO: 'alert alert-info',
    messages.WARNING: 'alert alert-warning'
}
"""
