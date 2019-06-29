#!/usr/bin/env python

from __future__ import print_function

import os
import subprocess
import sys

from setuptools import setup, find_packages
from codecs import open

from alttext import __version__

# Get the long description from the README file
with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

# Bump version and generate CHANGELOG
# npm install -g conventional-changelog-cli
if sys.argv[:2] == ["setup.py", "bump"]:
    try:
        version = sys.argv[2]
    except IndexError:
        print("Please provide a version number in the format X.X.X")
        sys.exit(1)
    with open("alttext/__init__.py", "w") as f:
        f.write('__version__ = "%s"\n' % version)
    with open("package.json", "w") as f:
        f.write('{ "version": "%s" }' % version)
    subprocess.call("conventional-changelog -p angular -i CHANGELOG.md -s", shell=True)
    os.remove("package.json")
    subprocess.call("git commit -am \"chore: bump version to %s\"" % version)
    sys.exit()

# Tag and release the package to PyPI
if sys.argv[:2] == ["setup.py", "release"]:
    subprocess.call("git tag v%s" % __version__)
    subprocess.call("git push")
    subprocess.call("git push --tags")
    subprocess.call("rm -rf dist/")
    subprocess.call("python setup.py sdist")
    subprocess.call("python setup.py bdist_wheel")
    subprocess.call("twine upload dist/*")
    sys.exit()

setup(
    name="django-alttext",
    version=__version__,
    description="Add alt text to images",
    long_description=long_description,
    url="https://github.com/unplugstudio/django-alttext",
    author="Unplug Studio",
    author_email="hello@unplug.studio",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="django mezzanine",
    packages=find_packages(),
    install_requires=[
        "django>=1.8",
    ],
    include_package_data=True
)
