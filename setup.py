#!/usr/bin/env python
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='scraper',
    version='1.0.0',
    description='',
    author='Johannes Ahlmann',
    author_email='johannes@sensatus.io',
    license='BSD',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=required,
    python_requires='~=3.6',
)
