#!/usr/bin/python
# -*- coding: utf-8 -*-

# © Copyright 2018 CERN
#
# This software is distributed under the terms of the GNU Lesser General Public
# Licence version 3 (LGPL Version 3), copied verbatim in the file “LICENSE”
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
    name="runregcrawlr",
    version="0.5.1",
    desription="CERN CMS Run Registry crawler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ptrstn/runregcrawlr",
    author="Peter Stein",
    author_email="peter.stein@cern.ch",
    packages=["runregcrawlr"],
    install_requires=["requests", "simplejson", "future"],
    classifiers=["License :: OSI Approved :: GNU General Public License v3 (GPLv3)"],
    entry_points={"console_scripts": ["runregcrawl=runregcrawlr.main:main"]},
)
