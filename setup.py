#! /usr/bin/env python

from setuptools import setup

setup(
    name="warc3",
    version="0.2.1",
    description="Python 3 library to work with ARC and WARC files",
    long_description=open('Readme.rst').read(),
    license='GPLv2',
    author="Internet Archive and others",
    author_email="info@archive.org",
    url="https://github.com/erroneousboat/warc3",
    packages=["warc"],
    platforms=["any"],
    package_data={'': ["LICENSE", "Readme.rst"]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
