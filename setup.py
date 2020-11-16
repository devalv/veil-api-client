# -*- coding: utf-8 -*-
"""Python package config."""
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='veil-api-client',
    version='2.0.3',
    author='Aleksey Devyatkin',
    author_email='a.devyatkin@mashtab.org',
    description='VeiL ECP Api client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://gitlab.bazalt.team/vdi/veil-api-client',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    install_requires=['aiohttp==3.6.*', 'ujson==3.0.*']
)
