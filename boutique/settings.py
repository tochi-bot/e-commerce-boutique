"""
Django settings for boutique project.

Generated by 'django-admin startproject' using Django 4.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os  # Add this import
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Define the hosts your application can serve. This prevents HTTP Host header attacks.
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '8000-tochibot-ecommercebouti-e72uu2l43y9.ws.codeinstitute-ide.net',  # Add your development or production domains here
    'bourtique-ado-fd30fa01f710.herokuapp.com'
]

# Add trusted origins for CSRF protection. These should match the domains in ALLOWED_HOSTS.
CSRF_TRUSTED_ORIGINS = [
    'https://8000-tochibot-ecommercebouti-e72uu2l43y9.ws.codeinstitute-ide.net',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',  # Required by 'django-allauth'
    'allauth',  # Django-allauth for authentication
    'allauth.account',  # Account management via django-allauth
    'allauth.socialaccount',  # Social account management via django-allauth
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'e_commerce',  # Custom app
    'home',  # Home app
    'products',# products app
    'bag', # bag app
    'checkout', #checkout app

     # Other
    'crispy_forms',
    'profiles',
]

# Authentication backends. Order matters: Django tries them in the given order.
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth authentication backend
)

# Site ID for the django.contrib.sites framework. Must match the ID in your database.
SITE_ID = 1

# Email backend for development purposes. Prints emails to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # Allow login via username or email
ACCOUNT_EMAIL_REQUIRED = True  # Require email during signup
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Require email verification after signup
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True  # Require email to be entered twice during signup
ACCOUNT_USERNAME_MIN_LENGTH = 4  # Minimum length for usernames
LOGIN_URL = '/accounts/login/'  # URL to redirect to for login
LOGIN_REDIRECT_URL = '/'  # URL to redirect to after login
LOGOUT_REDIRECT_URL = '/'  # URL to redirect to after logout

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Middleware for django-allauth
]

ROOT_URLCONF = 'boutique.urls'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')
        ],
        'APP_DIRS': True,  # Enable Django to look for templates in each app's directory
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # Required by django-allauth
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'bag.contexts.bag_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

WSGI_APPLICATION = 'boutique.wsgi.application'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation to enforce strong passwords.
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Language code for the application
TIME_ZONE = 'UTC'  # Time zone for the application
USE_I18N = True  # Enable Django's translation system
USE_TZ = True  # Enable timezone support

# Static files configuration
STATIC_URL = 'static/'  # URL prefix for static files
STATICFILES_DIRS=  (os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default primary key field type


# Stripe
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'usd'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
DEFAULT_FROM_EMAIL = 'boutiqueado@example.com'


