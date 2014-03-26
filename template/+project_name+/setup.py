#!/usr/bin/env python
import os
from setuptools import find_packages
from setuptools import setup


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read().strip()


README = read_relative_file('README.rst')
VERSION = read_relative_file('VERSION')


setup(
    name='{{ project_name }}',
    version=VERSION,
    description="{{ description }}",
    long_description=README,
    classifiers=[
        # Add your classifiers here from
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='{{ keywords|default('') }}',
    author='{{ author|default('') }}',
    author_email='{{ author_email|default('') }}',
    url='{{ url|default("http://www.github.com/organisation/project_name") }}',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
    ],
    entry_points={
        # 'console_scripts': [
        #     '{{ project_name }} = {{ project_name }}:main'
        # ],
    }
)
