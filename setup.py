from setuptools import setup, find_packages

version = '1.0.1'

setup(name='django-frontend-static',
      version=version,
      description="A basic Django application to install often used static files.",
      long_description=open("README.rst", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Framework :: Django",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='',
      author='Jon Faustman',
      author_email='jon@faustman.org',
      url='http://github.com/jonfaustman/django-frontend-static',
      license='MIT',
      packages=find_packages(),
      install_requires = [],
      include_package_data=True,
      zip_safe=False,
    )