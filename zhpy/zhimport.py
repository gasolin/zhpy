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
from pyzh import zh_chr
import imputil

#def handle_zhpy(fullpath, fileinfo, name):
#    """
#    zhpy import handler
#    
#    directly import zhpy module with cnpy, twpy subname.
#    """
#    data = convertor(open(fullpath).read())
#    return 0, compile(data,fullpath,'exec'),{}
#
#im = imputil.ImportManager()
#im.add_suffix('.cnpy',handle_zhpy)
#im.add_suffix('.twpy',handle_zhpy)
#im.install()

imported = 0
import __builtin__
trueimport = __builtin__.__import__

def chinese_import(*arg):
    """chinese import 
    
    convert uri file name back to chinese filename
    """
    arg = list(arg)
    modname = arg[0]
    arg[0] = zh_chr(modname)
    return apply(trueimport, arg)

if not imported:
    __builtin__.__import__  = chinese_import
imported = 1
