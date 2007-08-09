# -*- coding: utf-8 -*-
version = "0.2"
author = "Fred Lin"
email = "gasolin+zhpy@gmail.com"
copyright = "Copyright 2007 Fred Lin and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "http://code.google.com/p/zhpy/"
download_url="http://code.google.com/p/zhpy/"
description="Write python language in chinese"
long_description = """zhpy is an toy convertor to translate chinese (Traditional and Simplified) python code 
to nature python code (english).

zhpy use pyparsing to detect chinese keywords, class name, methods, arguments, variables and 
translate them back to python.

zhpy refactored the origin code from HYRY.

Check examples_ here.
 
.. _examples: "http://code.google.com/p/zhpy/wiki/ExampleHello"

Install zhpy
--------------

You could use easy_install command to install zhpy::

    $ easy_install zhpy

Usage
-----

::

    $ zhpy hello.py
    hello, world!

You could assign a file name to export the zhpy source to the normal python source (english)

::

    $ zhpy hello.py nhello.py

::

    $ python nhello.py
    hello, world!

Programming
-----------

You could mix original english keywords and Chinese keywords in your zhpy source.

Reserved keywords are listed here_

.. _here: http://code.google.com/p/zhpy/wiki/KeyWords
"""