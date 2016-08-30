#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Resources
- [https://packaging.python.org/en/latest/distributing/#readme-rst](https://packaging.python.org/en/latest/distributing/#readme-rst
)

https://packaging.python.org/en/latest/distributing/#readme-rst

http://docs.python-guide.org/en/latest/writing/structure/
"""

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ands",  # name of this project to be listed on PyPI
    version="0.0.4a1",  # alpha release
    author="Nelson Brochado",
    author_email="nelson.brochado@outlook.com",
    packages=find_packages(exclude=["env"]),
    install_requires=["tabulate", "pdoc"],  # package's dependencies
    description="Algorithms and Data Structures",
    long_description=read("README.md"),
    license="MIT",
    keywords="algorithms data structures",
    url="https://github.com/dossan/ands",
    include_package_data=True,  # include everything in source control
    exclude_package_data={'': ['__pycache__']},  # but exclude __pycache__ from all packages
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Algorithms and Data Structures",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: Mac OS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Linux",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    # entry_points = {  # http://stackoverflow.com/questions/774824/explain-python-entry-points
    #        "console_scripts" : [
    #        "ands = ands.main:main"  # type `ands` on the command line to run the function main with main.py
    #    ]
    # }
)
