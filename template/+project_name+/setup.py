#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python packaging."""
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    """Test command that runs tox."""
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox  # import here, cause outside the eggs aren't loaded.
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


#: Absolute path to directory containing setup.py file.
here = os.path.abspath(os.path.dirname(__file__))
#: Boolean, ``True`` if environment is running Python version 2.
IS_PYTHON2 = sys.version_info[0] == 2


NAME = '{{ project_name }}'
DESCRIPTION = '{{ description }}'
README = open(os.path.join(here, 'README.rst')).read()
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
AUTHOR = u'{{ author|default('') }}'
EMAIL = '{{ author_email|default('') }}'
LICENSE = ''
URL = '{{ url|default("") }}'
CLASSIFIERS = [
    {% for python_version in python_versions -%}
        'Programming Language :: Python :: {{ python_version }}',
    {% endfor -%}
    # Add your classifiers here from
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
]
KEYWORDS = [
    '{{ keywords|default('') }}',
]
PACKAGES = [NAME.replace('-', '_')]
REQUIREMENTS = [
    'setuptools',
]
ENTRY_POINTS = {}
TEST_REQUIREMENTS = ['tox']
CMDCLASS = {'test': Tox}
SETUP_REQUIREMENTS = [
    'setuptools'
]


if __name__ == '__main__':  # Do not run setup() when we import this module.
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=README,
        classifiers=CLASSIFIERS,
        keywords=' '.join(KEYWORDS),
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        install_requires=REQUIREMENTS,
        entry_points=ENTRY_POINTS,
        tests_require=TEST_REQUIREMENTS,
        cmdclass=CMDCLASS,
        setup_requires=SETUP_REQUIREMENTS,
    )
