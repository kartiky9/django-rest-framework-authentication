"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from pathlib import Path

from drf_firebase_auth.utils import map_firebase_uid_to_username

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@rhqoo4b1nybud$k3u0*v*l1e%j$hxn&11%ftsvkd8w=sw$#$a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # libraries
    'corsheaders',
    'rest_framework',
    # 'rest_framework.authtoken',
    'drf_firebase_auth',

    # apps
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # CORS
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'users.User'


# CORS Settings (django-cors-headers)
CORS_ALLOW_ALL_ORIGINS = True

# -----------------------------------

# Rest Framework settings (djangorestframework)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'drf_firebase_auth.authentication.FirebaseAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}


# ------------------------------------

# DRF Firebase Auth

DRF_FIREBASE_AUTH = {
    # allow anonymous requests without Authorization header set
    'ALLOW_ANONYMOUS_REQUESTS': os.getenv('ALLOW_ANONYMOUS_REQUESTS', False),
    # path to JSON file with firebase secrets
    # can be generated in Firebase Project settings -> Service Accounts
    'FIREBASE_SERVICE_ACCOUNT_KEY':
        os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY',
                  './firebase-admin-secrets.json'),
    # allow creation of new local user in db
    'FIREBASE_CREATE_LOCAL_USER':
        os.getenv('FIREBASE_CREATE_LOCAL_USER', True),
    # attempt to split firebase user.display_name and set local user
    # first_name and last_name
    'FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME':
        os.getenv('FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME', True),
    # commonly JWT or Bearer (e.g. JWT <token>)
    'FIREBASE_AUTH_HEADER_PREFIX':
        os.getenv('FIREBASE_AUTH_HEADER_PREFIX', 'JWT'),
    # verify that JWT has not been revoked
    'FIREBASE_CHECK_JWT_REVOKED':
        os.getenv('FIREBASE_CHECK_JWT_REVOKED', True),
    # require that firebase user.email_verified is True
    'FIREBASE_AUTH_EMAIL_VERIFICATION':
        os.getenv('FIREBASE_AUTH_EMAIL_VERIFICATION', False),
    # function should accept firebase_admin.auth.UserRecord as argument
    # and return str
    'FIREBASE_USERNAME_MAPPING_FUNC': map_firebase_uid_to_username
}

# ------------------------------------
