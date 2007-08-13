# -*- coding: utf-8 -*-
version = "0.3"
author = "Fred Lin"
email = "gasolin+zhpy@gmail.com"
copyright = "Copyright 2007 Fred Lin and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "http://code.google.com/p/zhpy/"
download_url="http://code.google.com/p/zhpy/"
description="Write python language in chinese"
long_description = """zhpy is python on Chinese, which good for Taiwan and China beginners to 
learn python in their native language.

zhpy is a lightweight python module and a source convertor, which provides a command line 
tool to translate python code. The python code written by traditional and simplified 
chinese would be translated to nature python code (english).

zhpy use pyparsing module to detect chinese keywords, class name, methods, arguments, v
ariables and translate them back to python.

It's possible for developers to port zhpy to python on korean or python on japenese.

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

You could use 'zhpy' command instead of "python" in command line to 
execute source code mixed in Chinese and English.::

    $ zhpy hello.py
    hello, world!

You could assign a file name to export the zhpy source to the normal python source (english)::

    $ zhpy hello.py nhello.py

Then run the exported file as normal python source::

    $ python nhello.py
    hello, world!

Programming
-----------

You could mix original english keywords and Chinese keywords in your zhpy source.

Reserved keywords are listed here_

.. _here: http://code.google.com/p/zhpy/wiki/KeyWords

"""