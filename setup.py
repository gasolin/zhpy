from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
from pkg_resources import DistributionNotFound

import sys
import os
import glob

execfile(os.path.join('zhpy', 'release.py'))

# setup params
# it's possible to remove chardet dependency while porting
install_requires = ["pyparsing >=1.4.7",
                    "chardet >=1.0"]

setup(
    name="zhpy",
    version=version,
    author=author,
    author_email=email,
    download_url="http://code.google.com/p/zhpy/downloads/list",
    license=license,
    keywords = "traditional, simplified, chinese",
    description=description,
    long_description=long_description,
    url=url,
    zip_safe=False,
    install_requires = install_requires,
    include_package_data = True,
    packages=find_packages(exclude=["ez_setup"]),
    entry_points = """
    [console_scripts]
    zhpy = zhpy.zhpy_cmd:commandtool
    [zhpy.twdict]
    twkeyword = zhpy.zhdc:tw_keyword
    twmethod = zhpy.zhdc:tw_buildin_method
    twexception = zhpy.zhdc:tw_exception
    twzhpy= zhpy.zhdc:tw_zhpy
    twreplacedict= zhpy.zhdc:replacedict
    [zhpy.cndict]
    cnkeyword = zhpy.zhdc:cn_keyword
    cnmethod = zhpy.zhdc:cn_buildin_method
    cnexception = zhpy.zhdc:cn_exception
    cnzhpy = zhpy.zhdc:cn_zhpy
    cnreplacedict= zhpy.zhdc:replacedict
    """,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Code Generators'],
    test_suite = 'nose.collector',
    )

