from pathlib import Path
import dj_database_url
import os
from dotenv import load_dotenv


load_dotenv()
# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (keep it private in production)
SECRET_KEY = 'django-insecure-74%8m_jsp7u0ns$dl2)i4dg^78bf^eev!m#p!hv7$a$+2h_q7&'

# Debugging (Turn off in production)
DEBUG = True

# Allowed hosts (Define properly in production)
ALLOWED_HOSTS = ['test-web-4.onrender.com','localhost']

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG","False").lower() == "true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
# Installed applications
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Ensure this matches your app name
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'myproject.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Path to templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration (Using SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

database_url = os.environ.get("DATABASE_URL")
DATABASES["default"] = dj_database_url.parse(database_url)
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Development static files
STATIC_ROOT = BASE_DIR / 'staticfiles'   # Used for `collectstatic` in production

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin admin configuration
JAZZMIN_SETTINGS = {
    "site_title": "Library Admin",
    "site_header": "Library",
    "site_brand": "Library",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to the library",
    "copyright": "Acme Library Ltd",
    "search_model": "auth.User",
    "show_sidebar": True,
    "navigation_expanded": True,
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Users", "url": "admin:auth_user_changelist", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    ],
    "hide_models": ["auth.Group"],
    "custom_css": "admin/css/custom.css",
}
ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost', 
    '9b78-14-191-162-211.ngrok-free.app'  # Add your ngrok domain here
]