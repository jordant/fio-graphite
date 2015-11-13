#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='fio-graphite',
    version='0.0.1',
    description='FIO graphite shipper',
    author='Jordan Tardif',
    author_email='jordan.tardif@gmail.com',
    url='https://github.com/jordant/fio-graphite',
    scripts=[
        'fio-graphite'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    license='GPLv2'
)
