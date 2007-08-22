# -*- coding: utf-8 -*-
version = "0.6"
author = "Fred Lin"
email = "gasolin+zhpy@gmail.com"
copyright = "Copyright 2007 Fred Lin and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "http://code.google.com/p/zhpy/"
download_url="http://code.google.com/p/zhpy/"
description="Write python language in chinese"
long_description = """zhpy is the *python on Chinese*, 
which is good for Taiwan and China beginners to learn python in our native language.

zhpy is a lightweight python module and a source convertor, which provides a command line 
tool to translate python code. The python code written by traditional and simplified 
chinese could be translated to nature python code (english).

zhpy support full python syntax. Code written in zhpy could be converted to natual python and 
be used in normal python programs.

After v0.5, zhpy provide a method 'zh_exec' that allow to embed chinese script in python

After v0.6, zhpy could be used as the chinese script in shell as well.

zhpy is fully tested, which use ~50 test cases to test the small(<10k) source.

zhpy use pyparsing module to detect chinese keywords, class name, methods, arguments, 
variables and translate them back to python.

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

You could use interpretor to test zhpy with zh_exec_ method::

    $ python
    >>> from zhpy import zh_exec
    >>> zh_exec("print hello") # execute zhpy here, pypi not allow non ascii code.
    hello

.. _zh_exec: http://code.google.com/p/zhpy/wiki/EmbededInPython

You could use 'zhpy' command instead of "python" in command line to 
execute source code mixed in Chinese and English.::

    $ zhpy hello.py
    hello, world!

You could assign a file name to export the zhpy source to the normal python source (english)::

    $ zhpy hello.py n_hello.py

Then run the exported file as normal python source::

    $ python n_hello.py
    hello, world!

Or you could combine these two steps in one command (with '-p' option)::

    $ python -p hello.py
    hello, world!
    $ ls
    hello.py n_hello.py

check the BasicUsage_ for detail.

.. _BasicUsage: "http://code.google.com/p/zhpy/wiki/BasicUsage"

Programming
-----------

You could mix original english keywords and Chinese keywords in your zhpy source.

Reserved keywords are listed here_

.. _here: http://code.google.com/p/zhpy/wiki/KeyWords 

You could view the ChangeLog_ to see what's new in these version

.. _ChangeLog: http://zhpy.googlecode.com/svn/trunk/CHANGELOG.txt

"""