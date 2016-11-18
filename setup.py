#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
## Resources
- [https://packaging.python.org/en/latest/distributing/#readme-rst](https://packaging.python.org/en/latest/distributing/#readme-rst)
- [https://packaging.python.org/en/latest/distributing/#readme-rst](https://packaging.python.org/en/latest/distributing/#readme-rst)
- [http://docs.python-guide.org/en/latest/writing/structure/](http://docs.python-guide.org/en/latest/writing/structure/)
"""

import os
from setuptools import setup, find_packages


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="ands",
    version="0.0.1",
    author="Nelson Brochado",
    author_email="nelson.brochado@outlook.com",
    packages=find_packages(exclude=["env"]),
    install_requires=["numpy", "tabulate", "pdoc"],
    description="Algorithms and Data Structures",
    long_description=read("README.md"),
    license="MIT",
    keywords="algorithms data structures",
    url="https://github.com/nbro/ands",
    include_package_data=True,
    exclude_package_data={'': ['__pycache__']},
    classifiers=[
        # How mature is this project?
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Algorithms and Data Structures",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: Mac OS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Linux",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ]
)
