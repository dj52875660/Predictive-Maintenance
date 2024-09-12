#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

setup(
    name='as_pm',
    packages=find_packages(
        include=['as_pm', 'as_pm.*']
    ),
    test_suite='tests',
    version="0.1.0",
)
