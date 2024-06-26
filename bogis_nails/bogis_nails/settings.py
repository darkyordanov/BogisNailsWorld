from pathlib import Path

from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ur7mgx81&-*n#z*-5fysydoyzo)(p7w4gtrr)94u1sqtvhuez8'

DEBUG = True

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'rest_framework',

    'bogis_nails.core',
    'bogis_nails.catalog',
    'bogis_nails.product',
    'bogis_nails.account',
    'bogis_nails.booking',
    'bogis_nails.cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    'bogis_nails.common.middleware.HandlePermissionDeniedMiddleware',
    
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bogis_nails.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'bogis_nails.cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'bogis_nails.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # "NAME": "bogis_nails_db",
        "NAME": "bogis_nails_db_test2",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

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

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = ()


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = (
    BASE_DIR / "static",
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.AccountUser'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('login')
LOGOUT_REDIRECT_URL = reverse_lazy('index')
