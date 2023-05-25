# flake8: noqa

# from utils.environment import get_env_variable, parse_comma_sep_str_to_list
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "INSECURE")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "1"

ALLOWED_HOSTS: list[str] = ["*"]  # type: ignore
CSRF_TRUSTED_ORIGINS: list[str] = []


ROOT_URLCONF = "project.urls"


WSGI_APPLICATION = "project.wsgi.application"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
