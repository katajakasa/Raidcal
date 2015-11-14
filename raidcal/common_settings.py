# -*- coding: utf-8 -*-

# Application definition
INSTALLED_APPS = (
    'raidcal.maincal',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'compressor',
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'raidcal.urls'

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
                'django.core.context_processors.request',
                'custom.context_processors.language_code',
            ],
        },
    },
]

LOGIN_URL = '/login'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

WSGI_APPLICATION = 'raidcal.wsgi.application'

# For event descriptions, frontpage decorations, forum messages.
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace",
    'theme': "advanced",
    'height': 400,
    'width': 600,
    'resize': 'both',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

# To sanitize tinymce stuff
SANITIZER_ALLOWED_TAGS = ['a', 'strong', 'img', 'li', 'ol', 'ul', 'em', 'span', 'p',
                          'address', 'sup', 'h1', 'h2', 'n3', 'h4', 'h5', 'h6', 'pre']
SANITIZER_ALLOWED_ATTRIBUTES = ['href']
SANITIZER_ALLOWED_STYLES = []

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'scss -m -C {infile} {outfile}'),
)

CSP_DEFAULT_SRC = ("'self'", )
CSP_SCRIPT_SRC = ("'self'", "'unsafe-eval'", )
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", )
CSP_IMG_SRC = ("'self'", "*")
CSP_MEDIA_SRC = ("'self'", "*")
CSP_REPORT_ONLY = False

USE_I18N = True
USE_L10N = True
USE_TZ = True
