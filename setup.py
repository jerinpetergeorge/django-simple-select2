#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('VERSION.txt', 'r') as v:
    version = v.read().strip()

with open('README.md', 'r') as r:
    readme = r.read()

download_url = (
    'https://github.com/jerinpetergeorge/django-simple-select2/tarball/%s'
)

setup(
    name='django-simple-select2',
    packages=['simple_select2'],
    version=version,
    description='Tweaks for existing built-in Django"s autocomplete feature',
    long_description=readme,
    author='Jerin Peter George',
    author_email='jerinpetergeorge@gmail.com',
    url='https://github.com/jerinpetergeorge/django-simple-select2',
    download_url=download_url % version,
    install_requires=[],
    long_description_content_type='text/markdown',
    license='MIT-Zero'
)
