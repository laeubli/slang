#!/usr/bin/env python3

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='slang',
      version='1.0',
      description='Converts a Swiss German sentences into slang.',
      url='http://github.com/laeubli/slang',
      author='Samuel Läubli',
      author_email='laeubli@cl.uzh.ch',
      license='LGPL',
      packages=['slang'],
      scripts=['bin/slang'])
