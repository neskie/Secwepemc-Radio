ADMINS = (
    ('Neskie Manuel', 'neskiem@gmail.com'),
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', 
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SECRET_KEY = 'thisisasecret'
