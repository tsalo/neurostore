#!/usr/bin/env python
import os
from setuptools import setup, find_packages


requirements = ['numpy', 'pandas', 'flask', 'flask_security',
                'email_validator', 'flask-dance', 'sqlalchemy-utils',
                'flask-cors', 'flask-sqlalchemy', 'flask-restful', 'pyld',
                'flask-graphql']

print("PACKAGES:", find_packages(exclude=['tests', 'test_*']))

setup(
    name="nsnew",
    version='0.0.0',
    description="NeuroStuff",
    install_requires=requirements,
    maintainer='Tal Yarkoni',
    maintainer_email='tyarkoni@gmail.com',
    packages=find_packages(exclude=['tests', 'test_*']),
    license='MIT'
)
