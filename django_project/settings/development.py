from pathlib import Path
import environ

print("LOADING DEVELPOMENT SETTINGS")

# Initialise environment variables
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.local.sqlite",  # This is where you put the name of the db file.
        # If one doesn't exist, it will be created at migration time.
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
