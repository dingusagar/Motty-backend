from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!78qo5rkqq+_c!o2f*n+&=hn5^o66i+$9*7t^)-8mh7*g50bq*'

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mottydb',
        'USER': 'motty_user',
        'PASSWORD': 'motty_user',
        'HOST': 'localhost',
        'PORT': '',
    }
}
