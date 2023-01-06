import os
import sys

from .base import *

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += ['icecreamratings.products','icecreamratings.profiles','icecreamratings.ratings']

ROOT_URLCONF = 'config.urls'

ALLOWED_HOSTS = ['localhost']
DEBUG = True

SECRET_KEY = 'django-insecure-m6!x+b@qocdigra8&sbvjc@uuxn=%%2$kkdf(r+i!a0kla8gu6'