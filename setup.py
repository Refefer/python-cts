# !/usr/bin/env python

from setuptools import setup

setup(name='python-cts',
      version="0.1.7.5",
      description='Command line ctag search',
      url="https://github.com/Refefer/python-cts",
      py_modules=['cts'],
      license="LICENSE",
      scripts=['bin/cts'],
      author='Andrew Stanton',
      author_email='Andrew Stanton',
      install_requires=['python-ctags'],
      classifiers=[
       "License :: OSI Approved :: Apache Software License",
       "Programming Language :: Python :: 2.6",
       "Operating System :: OS Independent"
      ])
