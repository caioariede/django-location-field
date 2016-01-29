import sys
import os


TEST_SPATIAL = 'TEST_SPATIAL' in os.environ


SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "location_field.apps.DefaultConfig",
    "tests",
]

STATIC_URL = '/static/'


if TEST_SPATIAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.spatialite',
            'NAME': 'db.sqlite3',
        }
    }

    if sys.platform == 'darwin':
        SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
