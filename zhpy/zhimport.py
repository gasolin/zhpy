#!/usr/bin/python
# -*- coding: utf-8 -*-

"""zhpy import handler

This is the MIT license:
http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2007 Fred Lin and contributors. zhpy is a trademark of Fred Lin.

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to 
deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
"""

from zhpy import convertor
import imputil

def handle_zhpy(fullpath, fileinfo, name):
    """
    zhpy handle
    """
    data = convertor(open(fullpath).read())
    return 0, compile(data,fullpath,'exec'),{}
im = imputil.ImportManager()
im.add_suffix('.zhpy',handle_zhpy)
im.add_suffix('.cnpy',handle_zhpy)
im.add_suffix('.twpy',handle_zhpy)
im.add_suffix('.cn',handle_zhpy)
im.add_suffix('.tw',handle_zhpy)
im.install()

imported = 0
import __builtin__
trueimport = __builtin__.__import__

def zhchr(tmp):
    """
    convert hex number back to chinese charactor

    >>> zhchr('p_7bc4_4f8b_v')
    "範例"
    """
    if tmp.startswith("p_") and tmp.endswith("_v"):
        tmp2 = ''
        for i in tmp.split('_')[1:-1]:
            if not ('v' in i and 'p' in i):
                tmp2 += unichr(int(i, 16)).encode('utf8')
        return tmp2
    else:
        return tmp

def myimport(*arg):
    """myimport
    """
    arg = list(arg)
    modname = arg[0]
    arg[0] = zhchr(modname)
    return apply(trueimport, arg)

if not imported:
    __builtin__.__import__  = myimport
imported = 1
