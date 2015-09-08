# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ReturnStackLocal.db3'
    }
}

# Configuring Email

ADMINS = (('Tom', 'me@tombryant.co.uk'))

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'returnstack'
EMAIL_HOST_PASSWORD = 'yeUPP7nsZUj6gXLg'
SERVER_EMAIL = 'noreply@returnstack.xyz'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^d95+y^gy_p*4cw)!lp@i&_$jmt0(f74pa31lwabmll4)1td1k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api.returnstack.xyz']
