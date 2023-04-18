#!/usr/bin/env python
from os import path
from setuptools import (  # Always prefer setuptools over distutils
    find_packages,
    setup,
)
from {{cookiecutter.package_name}} import __version__

here = path.abspath(path.dirname(__file__))

setup(
    name="{{cookiecutter.project_name}}",
    version=__version__,
    description="{{cookiecutter.short_description}}",
    long_description="",
    url="{{cookiecutter.url}}",
    # Author details
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    package_data = {
        "{{cookiecutter.package_name}}": ["schemas/*.json"]
    },
    test_suite="tests",
    py_modules=["{{cookiecutter.package_name}}"],
    install_requires=[],
    entry_points="""
        [console_scripts]
        {{cookiecutter.project_name}}={{cookiecutter.package_name}}:main
        """,
)
