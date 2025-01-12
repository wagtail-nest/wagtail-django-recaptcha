from __future__ import absolute_import, unicode_literals

import os

from setuptools import find_packages, setup

from wagtailcaptcha import __version__

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Testing dependencies
testing_extras = [
    # Required for running the tests
    "tox>=4.18.1,<4.19",
    # For coverage and PEP8 linting
    "coverage>=6.5.0,<6.6",
    "flake8>=7.0.0,<7.1",
    "isort>=5.10.1",
    # For test site
    "wagtail>=4.1",
]

# Documentation dependencies
documentation_extras = []

setup(
    name="wagtail-django-recaptcha",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="A simple recaptcha field for Wagtail Form Pages.",
    long_description=README,
    url="http://github.com/springload/wagtail-django-recaptcha",
    author="Wagtail Nest team",
    author_email="hello@wagtail.org",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 5",
        "Framework :: Wagtail :: 6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "wagtail>=5.0",
        "django-recaptcha>=4"
    ],
    extras_require={
        "testing": testing_extras,
        "docs": documentation_extras,
    },
    zip_safe=False,
)
