# !/usr/bin/env python

from setuptools import setup

setup(name='python-cts',
      version="0.1.5",
      description='Command line ctag search',
      url="https://github.com/Refefer/python-cts",
      license="LICENSE",
      scripts=['bin/cts'],
      author='Andrew Stanton',
      author_email='Andrew Stanton',
      install_requires=['python-ctags'])
