import os
LANGUAGE_CODE = 'ru-ru'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = ')b_1$a+85=l2(6=ucdp!r58$z1#9_pzg6yed=za)5i!%)k)2^t'


DEBUG = True

ALLOWED_HOSTS = ['*']

# FOR TRADITIONAL RUN ON WINDOWS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'menu_app_db',
#         'USER': 'postgres',
#         'PASSWORD': 'admin123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# FOR TRADITIONAL RUN ON LINUX

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'menu_app_db',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# FOR THROUGH DOCKER-COMPOSE RUN

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '123456',
#         'HOST': 'db',
#         'PORT': '5432',
#
#     }
# }


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
