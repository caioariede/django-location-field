import os
import sys

import django

from django.test.utils import get_runner
from django.conf import settings


test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

django.setup()


def runtests():
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
