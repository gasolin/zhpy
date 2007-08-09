# -*- coding: utf-8 -*-
version = "0.2"
author = "Fred Lin"
email = "gasolin+zhpy@gmail.com"
copyright = "Copyright 2007 Fred Lin and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "http://hg.python.org.tw/zhpy"
description="write python code in chinese"
long_description = """zhpy is an toy convertor to translate chinese (Traditional and Simplified) python code 
to nature python code (english).

zhpy use pyparsing to detect chinese keywords, class name, methods, arguments, variables and 
translate them back to python.

zhpy refactored the origin code from HYRY.

Install mopowg
--------------

You could use easy_install command to install zhpy::


    $ easy_install zhpy

Usage
-----

::

    $ zhpy hello.py
    hello, world!

Export normal python code (english)

::

    $ zhpy hello.py nhello.py

::

    $ python nhello.py
    hello, world!
    
"""
