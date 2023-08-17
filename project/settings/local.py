from .base import *

ALLOWED_HOSTS = ['127.0.0.1:8000','127.0.0.1']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}