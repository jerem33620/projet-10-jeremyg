import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

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

sentry_sdk.init(
    dsn="https://48ef1996e7a543ea81d57253a30f5e7b@o397917.ingest.sentry.io/5252938",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)