import os, sys
from django.conf import settings
import django

DIRNAME = os.path.dirname(__file__)

if django.VERSION[1] < 4:
    # If the version is NOT django 4 or greater
    # then remove the TZ setting.

    settings.configure(DEBUG=True,
                       ROOT_URLCONF = 'urls',
                       STATIC_URL = '/static/',
                       DATABASES={
                           'default': {
                               'ENGINE': 'django.db.backends.sqlite3',
                               }
                       },
                       INSTALLED_APPS=('django.contrib.auth',
                                       'django.contrib.contenttypes',
                                       'django.contrib.sessions',
                                       'django.contrib.admin',
                                       'djfrontend',))
else:
    settings.configure(DEBUG=True,
                       ROOT_URLCONF = 'urls',
                       STATIC_URL = '/static/',
                       DATABASES={
                           'default': {
                               'ENGINE': 'django.db.backends.sqlite3',
                               }
                       },
                       INSTALLED_APPS=('django.contrib.auth',
                                       'django.contrib.contenttypes',
                                       'django.contrib.sessions',
                                       'django.contrib.admin',
                                       'djfrontend',),
                       USE_TZ=True)




from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['djfrontend', ])
if failures:
    sys.exit(failures)