# !/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='traffic_lights',
    version='1.0',
    description='Turns the traffic light on/off   using Raspberry pi',
    author='CODEBASE PK',
    packages=find_packages(),
    scripts=['main']
)
