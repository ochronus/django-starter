from pathlib import Path
import environ

print("LOADING PRODUCTION SETTINGS")

# Initialise environment variables
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "https://project.tld",
]

CSRF_TRUSTED_ORIGINS = ["https://project.tld", "https://*.project.tld"]

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
    }
}


# Compressor
COMPRESS_OFFLINE = True

# DJANGO ALLAUTH
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("MAILGUN_SMTP_HOST")
EMAIL_PORT = 587
EMAIL_HOST_USER = env("MAILGUN_SMTP_USER")
EMAIL_HOST_PASSWORD = env("MAILGUN_SMTP_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ""
