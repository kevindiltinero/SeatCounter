# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='seatcounter',
    version='0.0.1',
    description='Simple program to track empty seats in a seating arrangement based on input from a file',
    long_description=readme,
    author='Kevin Fitzpatrick',
    author_email='mastery414@gmail.com,
    url='https://github.com/kevindiltinero/seass3.git',
    license=license,
    packages = find_packages(exclude=('tests', 'docs'))
)

