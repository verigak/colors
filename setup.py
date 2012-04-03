#!/usr/bin/env python

from setuptools import setup

import colors


setup(
    name='ansicolors',
    version=colors.__version__,
    description='ANSI colors for Python',
    long_description=open('README.rst').read(),
    author='Giorgos Verigakis',
    author_email='verigak@gmail.com',
    url='http://github.com/verigak/colors/',
    license='ISC',
    py_modules=['colors'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
