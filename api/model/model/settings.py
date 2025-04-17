import os
from pathlib import Path
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Load environment variables from .env
load_dotenv()

# Initialize Sentry if DSN is provided
if os.environ.get("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        auto_session_tracking=False,
        traces_sample_rate=0
    )

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "16600cc09a28b8dd3b4b8e7cfb4e81ff7958a87ab81809386ba7dcff9d68547e"
)

# Debug & Hosts
DEBUG = os.environ.get("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = ["*"] if DEBUG else [os.environ.get("HOSTNAME", "api.ai4mde.localhost"), "localhost"]

# Installed Apps
INSTALLED_APPS = [
    "daphne",  # ASGI server
    "model",
    "metadata",
    "diagram",
    "prompt",
    "prose",
    "generator",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
]

# Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL & WSGI/ASGI
ROOT_URLCONF = "model.urls"
WSGI_APPLICATION = "model.wsgi.application"
ASGI_APPLICATION = "model.asgi.application"

# Templates
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

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),  # <-- fallback for local dev
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        "NAME": os.environ.get("POSTGRES_DB", "ai4mdestudio"),
        "USER": os.environ.get("POSTGRES_USER", "ai4mdestudio"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "ai4mdestudio"),
    }
}

# Password validation
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

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CSRF & CORS
HOSTNAME = os.environ.get("HOSTNAME", "api.ai4mde.localhost")
STUDIO_HOSTNAME = os.environ.get("STUDIO_HOSTNAME", "ai4mde.localhost")

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://localhost:5173",
    f"http://{HOSTNAME}",
    f"https://{HOSTNAME}",
    f"http://{STUDIO_HOSTNAME}",
    f"https://{STUDIO_HOSTNAME}",
]

CSRF_COOKIE_DOMAIN = ".".join(HOSTNAME.split(".")[1:])
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ Don't use this in production!
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_HTTPONLY = False

# App-specific
PROSE_API_KEY = os.environ.get("PROSE_API_KEY", "sequoias")

# Swagger / drf_yasg
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Basic": {
            "type": "basic"
        }
    }
}
