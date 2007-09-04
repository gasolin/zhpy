# -*- coding: utf-8 -*-
version = "0.9"
author = "Fred Lin"
email = "gasolin+zhpy@gmail.com"
copyright = "Copyright 2007 Fred Lin and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "http://code.google.com/p/zhpy/"
download_url="http://code.google.com/p/zhpy/"
description="Write python language in chinese"
long_description = """zhpy is the full feature python with chinese keywords, 
variables, and parameters support.

zhpy on python is good for Taiwan and China beginners to learn python in 
our native language.

zhpy is a lightweight python module and a chinese source convertor on python, 
which provides interpreter and command line tool to translate zhpy code to 
python. The python code written by traditional and simplified 
chinese could be translated and execute as nature python code.

zhpy support full python syntax. Code written in zhpy could be 
converted to natual python and be used in normal python programs.

zhpy provide interpreter, which allow execise zhpy and python interactivily.

zhpy provide a method 'zh_exec' that allow to embed 
chinese script in python, zhpy could be used as the chinese script in 
shell as well.

zhpy is fully tested, which use ~60 test cases to test the small(<10k) source.

zhpy use pyparsing module to detect chinese keywords, class name, methods, 
arguments, variables and translate them back to python.

It's possible for developers to port zhpy to python on korean or 
python on japenese.

Check examples_ here.

.. _examples: "http://code.google.com/p/zhpy/wiki/ZhpyExample"

Install zhpy
--------------

You could use easy_install command to install zhpy::

    $ easy_install zhpy

or check instructions_ for detail.

.. _instructions: "http://code.google.com/p/zhpy/wiki/DownloadInstall"

Usage
-----

You could use zhpy interpreter to test zhpy::

    $ zhpy
    >>> print 'hello in chinese'
    hello in chinese

Browse project_ homepage to get examples in chinese.

.. _project: http://code.google.com/p/zhpy/

check the BasicUsage_ for detail.

.. _BasicUsage: "http://code.google.com/p/zhpy/wiki/BasicUsage"

Programming
-----------

You could mix original english keywords and Chinese keywords in 
your zhpy source.

Reserved keywords are listed here_

.. _here: http://code.google.com/p/zhpy/wiki/KeyWords 

You could view the ChangeLog_ to see what's new in these version

.. _ChangeLog: http://zhpy.googlecode.com/svn/trunk/CHANGELOG.txt

"""
