import os, sys
from django.conf import settings
import django

DIRNAME = os.path.dirname(__file__)

if django.VERSION[1] < 4:
    # If the version is NOT django 4 or greater
    # then remove the TZ setting.

    settings.configure(
                        DATABASES={
                           'default': {
                               'ENGINE': 'django.db.backends.sqlite3',
                               }
                       },
                       STATIC_URL = '/static/',
                       INSTALLED_APPS = ('djfrontend',)
                       )
else:
    settings.configure(DATABASES={
                           'default': {
                               'ENGINE': 'django.db.backends.sqlite3',
                               }
                       },
                       STATIC_URL = '/static/',
                       INSTALLED_APPS = ('djfrontend',)
                       USE_TZ=True)




from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['djfrontend', ])
if failures:
    sys.exit(failures)