# !/usr/bin/env python

from setuptools import setup

setup(name='python-cts',
      version="0.1.2",
      description='Command line ctag search',
      license="LICENSE",
      scripts=['bin/cts'],
      author='Andrew Stanton',
      author_email='Andrew Stanton',
      install_requires=['python-ctags'])
