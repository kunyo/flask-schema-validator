#!/usr/bin/env python

import os, glob
from setuptools import setup, find_packages

setup(
    name='flask_schema_validator',
    version='1.0.0',
    url='https://github.com/kunyo/flask-schema-validator',
    license='UNLICENSED',
    author='kn',
    author_email='',
    description='',
    long_description='',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: UNLICENSED',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'Flask>=1.1.2',
        'jsonschema>=3.2.0'
    ]
)