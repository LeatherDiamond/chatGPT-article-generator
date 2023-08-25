import os
from pathlib import Path

import dj_database_url

from dotenv import find_dotenv, load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(find_dotenv())


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG_MODE", "False")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "rest_framework",
    "gpt_generator",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = "proj.urls"

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "proj.wsgi.application"


DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("PRIMARY_DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    ),
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "ChatGPT content generator Backend",
    "DESCRIPTION": "AI-driven content generator. Crafting text or images effortlessly using chatGPT's capabilities.",
    "VERSION": "1.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
