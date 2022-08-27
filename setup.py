# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='HW1',
    version='0.1.0',
    description='Program for addition of two numbers',
    long_description=readme,
    author='Group 5',
    url='https://github.com/alunavat/CSC510-22-group-5',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['numpy', ],
)