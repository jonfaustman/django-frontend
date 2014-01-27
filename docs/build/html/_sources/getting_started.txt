Getting Started
================

Install
--------
1. install `django-frontend` (pip install, add to your requirements files, etc.)
2. add `'djfrontend'` to your INSTALLED_APPS
3. make sure `'django.contrib.staticfiles'` is also in your INSTALLED_APPS

Extend
-------
Extend djfrontend's base template in your template(s)
::

    {% extends 'djfrontend/base.html' %}

Load
-----
Load all the djfrontend tags if you want to add or change the template's defaults.
::

    {% load djfrontend %}