from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
from pkg_resources import DistributionNotFound

import sys
import os
import glob

execfile(os.path.join('zhpy', 'release.py'))

# setup params
install_requires = ["pyparsing >=1.4.7"]


setup(
    name="zhpy",
    version=version,
    author=author,
    author_email=email,
    license=license,
    description=description,
    long_description=long_description,
    url=url,
    zip_safe=False,
    install_requires = install_requires,
    packages=find_packages(),
    entry_points = """
    [console_scripts]
    zhpy = zhpy.zhpy:commandtool
    """,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite = 'nose.collector',
    )

