#!/usr/bin/env python3
from setuptools import setup

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
    description='Tweaks for existing built-in Django\'s autocomplete feature',
    long_description=readme,
    author='Jerin Peter George',
    author_email='jerinpetergeorge@gmail.com',
    url='https://github.com/jerinpetergeorge/django-simple-select2',
    download_url=download_url % version,
    python_requires='>=3.6',
    setup_requires=[
        'setuptools>=38.6.0',  # for long_description_content_type
    ],
    install_requires=['Django>=2.2'],
    long_description_content_type='text/markdown',
    license='MIT-Zero'
)
