# !/usr/bin/env python

from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='python-cts',
      version="0.1.5.1",
      description='Command line ctag search',
      url="https://github.com/Refefer/python-cts",
      license="LICENSE",
      scripts=['bin/cts'],
      author='Andrew Stanton',
      author_email='Andrew Stanton',
      long_description = long_description,
      install_requires=['python-ctags'],
      categories=[
       "License :: OSI Approved :: Apache Software License",
       "Programming Language :: Python :: 2.6",
       "Operating System :: OS Independent"
      ])
