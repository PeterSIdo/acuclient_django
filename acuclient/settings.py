# acuclient_django/acuclient/settings.py |||
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


print(f"MONGO_DB_URI: {os.getenv('MONGO_DB_URI')}")
print(f"DB_NAME: {os.getenv('DB_NAME')}")


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djongo',
    'clients.apps.ClientsConfig',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'acuclient.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['clients.filters'],  # Add your filters module here
        },
    },
]

WSGI_APPLICATION = 'acuclient.wsgi.application'

# c:/Users/Peter/acuclient-django/clients/settings.py |||
# MongoDB database configuration
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('DB_NAME'),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': os.getenv('MONGO_DB_URI'),
            'username': os.getenv('MONGO_DB_USER'),
            'password': os.getenv('MONGO_DB_PASSWORD'),
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}


# Database router to handle MongoDB operations
DATABASE_ROUTERS = ['clients.routers.MongoRouter']
# Database router to handle MongoDB operations
DATABASE_ROUTERS = ['clients.routers.MongoRouter']

# MongoDB connection
MONGODB_URI = os.getenv('MONGO_URI')
# Authentication settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'