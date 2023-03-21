from django.conf import settings
import sys
import pytest


def pytest_addoption(parser):
    # https://docs.pytest.org/en/7.1.x/example/markers.html#custom-marker-and-command-line-option-to-control-test-runs
    parser.addoption("--test-spatial", action="store_true", default=False)


def should_run_spatial(config):
    return config.getoption("--test-spatial")


def pytest_runtest_setup(item):
    requires_spatial = any(mark.name == "spatial" for mark in item.iter_markers())
    if requires_spatial:
        if not should_run_spatial(item.config):
            pytest.skip("cannot run without the --test-spatial parameter")


def pytest_configure(config):
    COMMON_CONFIG = dict(
        STATIC_URL="",
        INSTALLED_APPS = [
            "location_field",
            "tests",
        ],
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
            },
        ],
    )

    if sys.platform == 'darwin':
        COMMON_CONFIG['SPATIALITE_LIBRARY_PATH'] = '/usr/local/lib/mod_spatialite.dylib'
    elif sys.version_info[0] == 2:
        COMMON_CONFIG['SPATIALITE_LIBRARY_PATH'] = 'mod_spatialite'

    if should_run_spatial(config):
        settings.configure(**dict(COMMON_CONFIG,
            DATABASES = {
                'default': {
                    'ENGINE': 'django.contrib.gis.db.backends.spatialite',
                    'NAME': 'db.sqlite3',
                }
            }
        ))
    else:
        settings.configure(**dict(COMMON_CONFIG,
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'db.sqlite3',
                }
            }
        ))
