#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

from setuptools import setup, find_packages


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="ands",
    version="0.0.1",
    author="Nelson Brochado",
    author_email="nelson.brochado@outlook.com",
    packages=find_packages(exclude=["venv"]),
    install_requires=["numpy", "tabulate", "scipy"],
    description="Algorithms and Data Structures",
    long_description=read("README.md"),
    license="MIT",
    keywords="algorithms data structures python testing",
    url="https://github.com/nbro/ands",
    include_package_data=True,
    exclude_package_data={'': ['__pycache__']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers, Students, Scientists",
        "Topic :: Software Development :: Algorithms and Data Structures",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: Mac OS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)
