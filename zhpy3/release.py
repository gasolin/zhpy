# -*- coding: utf-8 -*-

"""Release information"""


version = "3.0.0a1"
author = "Fred Lin"
email = "gasolin+zhpy@gmail.com"
copyright = "Copyright 2007~ Fred Lin and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "http://zhpy.googlecode.com/"
download_url="http://code.google.com/p/zhpy/"
description="Write python(3) language in chinese"
long_description = """
.. contents::
  :depth: 2

Introduction
--------------

"If it walks like a duck and quacks like a duck, I would call it a duck."

Zhpy3 on python 3 is good for non-native-english beginners to learn python 3 in our native language (Currently support Traditional and Simplified chinese).

Zhpy3 acts like python 3 and play like python 3, user
could use it as python 3 to educate yourself the program skills
plus with your native language.

Check examples here.

  * http://code.google.com/p/zhpy/source/browse/#hg%2Fzhpy3%2Fexamples

Install
----------

If you'd like to play zhpy3 with full features, you should install zhpy3.

You could use easy_install command to install or upgrade zhpy3::

    $ easy_install -U zhpy3

to use easy_install command, you should install distribute module for python 3 first:

http://pypi.python.org/pypi/distribute/

And check your system path params if it contains python3.x/bin path.

ex: edit .bashrc to include "/Library/Frameworks/Python.framework/Versions/3.x/bin" in your PATH parameter. 

What is Zhpy3
---------------

Zhpy3 is the successor of zhpy, to provider the python 3 language translator with fully tested chinese keywords, variables, and parameters support. Zhpy is INDEPENDENT on python 3 version(3.x….).

The core of zhpy3 is a lightweight python module and a language
source convertor based on python3, which provides
command line tool to translate zhpy3 code to python 3.

See http://www.flickr.com/photos/gasolin/2064120327

You could invoke interpreter with 'twpy', 'cnpy' command instead of "python3" in command line to execute source code wrote in either Traditional/Simplified Chinese or English.

The framework is not hard to extend to another languages such as japenese or korean.


Change Log
-------------

You could view the ChangeLog to see what's new in these version.

  * http://code.google.com/p/zhpy/source/browse/CHANGELOG.txt

"""
