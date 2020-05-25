from . import *


SECRET_KEY = os.getenv("SECRET_KEY", '^pt(p+)xv+9s9mnywpf3gkjn2^nkmwm&wi)@7$!dy0#pqlqpq)')

DEBUG = False

ALLOWED_HOSTS = ["localhost", '127.0.0.1', '206.189.117.65']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'purbeurre',
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_USE_TLS = True