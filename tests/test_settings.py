import sys


SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "location_field.apps.DefaultConfig",
    "tests",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': 'db.sqlite3',
    }
}

STATIC_URL = '/static/'


if sys.platform == 'darwin':
    SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'
