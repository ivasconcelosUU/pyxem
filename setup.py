#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017-2020 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

exec(open('pyxem/release_info.py').read())  # grab version info


setup(
    name=name,
    version=version,
    description='Crystallographic Diffraction Microscopy in Python.',
    author=author,
    author_email=email,
    license=license,
    url="https://github.com/pyxem/pyxem",
    long_description=open('README.rst').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],

    packages=find_packages(),
    # adjust the tabbing
    install_requires=[
        'scikit-image >= 0.15.0',   # exclude_border argument in peak_finder laplacian (PR #436)
        'matplotlib >= 3.1.1',     # 3.1.0 failed
        'scikit-learn >= 0.19',     # reason unknown
        'hyperspy >= 1.5.2',        # earlier versions incompatible with numpy >= 1.17.0
        'diffsims > 0.2.1',        # Makes use of functionality introduced in this release
        'lmfit >= 0.9.12',
        'pyfai'
    ],
    package_data={
        "": ["LICENSE", "readme.rst"],
        "pyxem": ["*.py", "hyperspy_extension.yaml"],
    },
    entry_points={'hyperspy.extensions': ['pyxem = pyxem']},
)
