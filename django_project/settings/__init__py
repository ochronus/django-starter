from django_project.settings.common import *
from django_project.settings.util import init_env

# Initialise environment variables
env = environ.Env()
init_env(env)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

django_env = env("DJANGO_ENV")
if not django_env:
    raise RuntimeError("please set DJANGO_ENV")
else:
    match django_env:
        case "development":
            from django_project.settings.development import *
        case "production":
            from django_project.settings.production import *
        case other:
            raise RuntimeError(f"unrecognized DJANGO_ENV setting: {django_env}")
