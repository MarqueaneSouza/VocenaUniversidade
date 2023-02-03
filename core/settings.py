import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mcgir+r3lx4=p7c%2$7mo8vk8*2egew@don@c3j8q7i&3azz5_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagina.apps.PaginaConfig',
    'como_funciona.apps.ComoFuncionaConfig',
    'duvidas.apps.DuvidasConfig',
    'inscricoes.apps.InscricoesConfig',
    'normas.apps.NormasConfig',
    'ckeditor',
    'ckeditor_uploader',
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

ROOT_URLCONF = 'core.urls'

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
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pagina_vcnauniversidade', #nome do banco de dados criado - Aula 26.
        'USER': 'postgres',
        'PASSWORD': '201012',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {
                    'options': '-c search_path=pagina_bd'  # pagina_bd: nome do schema que eu quero acessa.
                 },
        }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#CONFIGURAÇÃO DO AMBIENTE DE DESENVOLVIMENTO
STATIC_URL = 'static/' #define caminho relativo para o diretório de arquivos estáticos da aplicação ou projeto.
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL) #define o caminho absoluto (URL) para o local em que os arquivos estáticos serão armazenados.


MEDIA_URL = 'images/' #pode ser qualquer nome no,lugar de 'images'
MEDIA_ROOT = os.path.join(BASE_DIR, '../pagina/static/images')

CKEDITOR_UPLOAD_PATH = 'uploads/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
