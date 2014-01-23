import os, sys
from django.conf import settings
import django

DIRNAME = os.path.dirname(__file__)

settings.configure(
    INSTALLED_APPS=('django.contrib.staticfiles',
                    'djfrontend',
    )
)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)