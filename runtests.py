import os
import sys


os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


import django
django.setup()


def runtests():
    from django.test.utils import get_runner
    from django.conf import settings

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)

    failures = test_runner.run_tests(['tests'])

    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
