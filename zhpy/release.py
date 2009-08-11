# -*- coding: utf-8 -*-

"""Release information"""


version = "1.7.3"
author = "Fred Lin"
email = "gasolin+zhpy@gmail.com"
copyright = "Copyright 2007~ Fred Lin and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "http://zhpy.googlecode.com/"
download_url="http://code.google.com/p/zhpy/"
description="Write python language in chinese"
long_description = """
.. contents::
  :depth: 2

Introduction
--------------

"If it walks like a duck and quacks like a duck, I would call it a duck."

Zhpy on python is good for Taiwan and China beginners to learn python in
our native language (Currently support Traditional and Simplified chinese).

Zhpy acts like python and play like python, you (chinese users)
could use it as python to educate yourself the program skills
plus with your native language.

Check examples here.

  * http://zhpy.googlecode.com/svn/trunk/examples

Play Zhpy Online
--------------------

Zhpy has online version (with limited feature) running
with google app engine!

 * http://zhpy.appspot.com


Play locally
--------------

To play zhpy locally, you even don't need to install it.

All you need to do is follow the 3 steps guide:

  1. Download the source pack (the zip file)
  2. Extract the pack with zip tool. Enter the folder
  3. Run::

      $ python interpreter.py

Then you got the usable zhpy interpreter!


Install
----------

If you'd like to play zhpy with full features, you should install zhpy.

You could use easy_install command to install or upgrade zhpy::

    $ easy_install -U zhpy

or check instructions for detail.

  * http://code.google.com/p/zhpy/wiki/DownloadInstall


Usage
-------

You could use zhpy interpreter to test zhpy::

    $ zhpy
    zhpy [version] in [platform] on top of Python [py_version]
    >>> print 'hello in chinese'
    hello in chinese

Browse project homepage to get examples in chinese.

  * http://code.google.com/p/zhpy/

check the BasicUsage for detail.

  * http://code.google.com/p/zhpy/wiki/BasicUsage


Programming Guide
-------------------

You could freely view the C.C. licensed book "A Byte of python (Zhpy)"
on zhpy website, which contained zhpy example codes as well.

  * http://code.google.com/p/zhpy/wiki/ByteOfZhpy

There's the API document available in zhpy download list, too.

  * http://code.google.com/p/zhpy/downloads/list

PS: The book is based on "A Byte of Python".

  * http://swaroopch.info/text/Byte_of_Python:Main_Page


What is Zhpy
--------------

Zhpy is the full feature python language with fully tested chinese
keywords, variables, and parameters support. Zhpy is INDEPENDENT on python
version(2.4, 2.5....), bundle with command line tool, interpreter,
bi-directional zhpy <-> python code translation,
chinese shell script capability, in-place ini reference feature
for keyword reuse, and great document (the book Byte of Python with chinese examples).

The core of zhpy is a lightweight python module and a chinese
source convertor based on python, which provides interpreter and
command line tool to translate zhpy code to python.

See http://www.flickr.com/photos/gasolin/2064120327

You could invoke interpreter with 'zhpy' command instead of "python" in command line to execute source code wrote in either Chinese or English.
The zhpy interpreter also support autocomplete function to save your typing.

Zhpy provide a method 'zh_exec' that allow you to embed
chinese script in python; Zhpy could be used as the chinese
shell script as well.

The zhpy code written in traditional and simplified chinese could be
translated and converted to natual python code.
Thus it could be execute as nature python code and be used in
normal python programs.

Bidirectional python-zhpy translation is possible.
Normal python programs could be translated to traditional(.twpy) or
simplified(.cnpy) chinese zhpy source via 'zhpy' command line tool.

The framework is not hard to extend to another languages such as japenese or korean.


Change Log
-------------

You could view the ChangeLog to see what's new in these version.

  * http://zhpy.googlecode.com/svn/trunk/CHANGELOG.txt

"""
