"""
Django settings for grammar project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta
import grammar.middleware


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# GrammarAzi/grammar/settings.py
JWT_SIGNING_KEY = os.getenv("JWT_SIGNING_KEY", "django-insecure-^@ws^%f(+gq+pyu-r_!_t!j8fdn9!f#n*4y7m_(^)7$3_-")

# SECURITY WARNING: don't run with debug turned on in production!
# Quick-start development settings - unsuitable for production
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-^@ws^%f(+gq+pyu-r_!_t!j8fdn9!f#n*4y7m_(^)7$3_-")


BOT_TOKEN = "7000740386:AAHpAFzAWsyqnuMmhLYs_L-5-A_ySaLexq0"
BOT_URL = "https://api.telegram.org/bot%s/"%BOT_TOKEN
CHAT_ID = '-4957206808'
# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'blog',
    'account',
    'grammars',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'django_filters',
    "corsheaders",
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'grammar.middleware.UpdateLastActivityMiddleware',
    'grammar.middleware.UpdateLastOwnActivityMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://grammar-azi.vercel.app",
    "https://user-service-grammar-azi.onrender.com", 
]



ROOT_URLCONF = 'grammar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


WSGI_APPLICATION = 'grammar.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
CSRF_TRUSTED_ORIGINS = [
    'https://grammarbackendpub-14.onrender.com',
    'https://grammarazi.onrender.com',
    'https://user-service-grammar-azi.onrender.com',
]

import os
import dj_database_url

DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("EXTERNAL_DATABASE_URL"))
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("POSTGRES_DB", "postgres"),
#         "USER": os.getenv("POSTGRES_USER", "postgres"),
#         "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
#         "HOST": os.getenv("POSTGRES_HOST", "localhost"),
#         "PORT": os.getenv("POSTGRES_PORT", "5432"),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),  
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": os.getenv("SECRET_KEY", "django-insecure-^@ws^%f(+gq+pyu-r_!_t!j8fdn9!f#n*4y7m_(^)7$3_-"),
    "AUTH_HEADER_TYPES": ('Bearer',),
}

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('az', 'Azerbaijan'),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Baku'  

USE_I18N = True

USE_TZ = True

# AUTH_USER_MODEL = 'account.User'
AUTH_USER_MODEL = "account.CustomUser"

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

REST_FRAMEWORK = { 
	"DEFAULT_AUTHENTICATION_CLASSES": [ 
		"rest_framework_simplejwt.authentication.JWTAuthentication", 
	], 
}

# Celery
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# Email Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Path and URL of media files
MEDIA_URL = "/media/" 
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Swagger configuration
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
    "DEFAULT_API_URL": "https://grammar-post.onrender.com/",
}
