from .base import *

ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

