try:
    from setuptools import setup, find_packages
except ImportError:
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
required_modules = ["chardet >=1.0.1"]
#if mac, install readline
#if(sys.platform=="darwin"):
#    required_modules.append("readline >= 2.6.4")

# pyparsing already included in release
# nose is used for test
extra_modules = {'pyparsing': ["pyparsing >=1.5.2"], 'nose':  ["nose>=0.9"]}

setup(
    name="zhpy",
    version=version,
    author=author,
    author_email=email,
    download_url=download_url,
    license=license,
    keywords = "traditional, simplified, chinese",
    description=description,
    long_description=long_description,
    url=url,
    zip_safe=False,
    install_requires = required_modules,
    extras_require = extra_modules,
    include_package_data = True,
    packages=find_packages(exclude=["ez_setup", 'examples', 'apidocs', "tests"]),
    entry_points = """
    [console_scripts]
    zhpy = zhpy.commandline:commandline
    [pygments.lexers]
    zhpy = zhpy.ext.pygmentplugin:ZhpyLexer
    """,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
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

