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
    'django_summernote',
    'eadred',
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

SUMMERNOTE_CONFIG = {
    'iframe': False,
    'airMode': False,
    'styleWithTags': False,
    'height': '400',
    'width': '100%',
    'toolbar': [
        ["style", ["style"]],
        ["font", ["bold", "italic", "underline", "superscript", "subscript", "strikethrough", "clear"]],
        ["color", ["color"]],
        ["para", ["ul", "ol", "paragraph"]],
        ["insert", ["link", "picture"]],
        ["view", ["fullscreen", "codeview"]]
    ],
}

# To sanitize tinymce stuff
SANITIZER_ALLOWED_TAGS = ['a', 'strong', 'img', 'li', 'ol', 'ul', 'em', 'u', 'span', 'p', 'strike',
                          'address', 'sup', 'h1', 'h2', 'n3', 'h4', 'h5', 'h6', 'pre', 'blockquote', 'br']
SANITIZER_ALLOWED_ATTRIBUTES = ['href', 'target', 'style', 'class', 'title', 'width', 'height', 'src', 'alt']
SANITIZER_ALLOWED_STYLES = ['color', 'background-color', 'text-align', 'margin-left']

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'scss -m -C {infile} {outfile}'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True
