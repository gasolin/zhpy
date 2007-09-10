#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Convert python source to zhpy source

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

 
from zhpy import annotator
from zhdc import twdict, cndict, revert_dict

hexval = '0123456789abcdef'

annotator()
# make reverse traditional chinese dicts
rev_twdict = revert_dict(twdict)
# make reverse simplified chinese dicts
rev_cndict = revert_dict(cndict)
    
def rev_merger(anno_dict, use_dict, verbose=True):
    """
    merge extra bindings into reverse dict
    
    >>> keys = [('遊戲', 'pygame'), ('系統', 'sys')]
    >>> rev_merger(keys, rev_twdict)
    add pygame=遊戲
    add sys=系統
    >>> 'pygame' in rev_twdict
    True
    
    >>> keys = [('游戏', 'pygame'), ('系统', 'sys')]
    >>> rev_merger(keys, rev_cndict)
    add pygame=游戏
    add sys=系统
    >>> 'pygame' in rev_cndict
    True
    
    >>> keys = {"作業系統":"os", "選項解析":"optparse"}
    >>> rev_merger(keys, rev_twdict)
    add optparse=選項解析
    add os=作業系統
    >>> 'os' in rev_twdict
    True
    
    >>> keys = {"作业系统":"os", "选项解析":"optparse"}
    >>> rev_merger(keys, rev_cndict)
    add os=作业系统
    add optparse=选项解析
    >>> 'os' in rev_cndict
    True
    """
    if type(anno_dict) == type([]):
        for k,v in anno_dict:
            if v not in use_dict:
                use_dict[v] = k
                if verbose:
                    print "add %s=%s"%(v, k)
            else:
                if verbose:
                    print "already has key: %s, %s" % (v, k)
    if type(anno_dict) == type({}):
        for num, tmp in enumerate(anno_dict.values()):
            if tmp not in use_dict:
                use_dict[tmp] = anno_dict.keys()[num]
                if verbose:
                    print "add %s=%s"%(tmp, anno_dict.keys()[num])
            else:
                if verbose:
                    print "already has key: %s, %s" % (tmp, anno_dict.keys()[num]) 
                
def rev_ini_annotator(use_dict, verbose=True):
    """
    update revert dict by ini files
    """
    # ini
    inifiles = []
    for x in os.listdir("."):
        if x.endswith(".ini"):
            inifiles.append(x)
    for f in inifiles:
        if verbose:
            print "file", f
        conf = ConfigParser.ConfigParser()
        conf.read(f)
        sects = conf.sections()
        for sect in sects:
            if verbose:
                print "sect:", sect
            rev_merger(conf.items(sect), use_dict)

def rev_py_annotator(use_dict, entry_point, verbose=False):
    """
    update revert dict by python plugins
    
    'verbose' argument is only for debug(will generate too mush messages).
    """
    for entrypoints in pkg_resources.iter_entry_points():
        tool = entrypoints.load()
        if verbose:
            print tool.title
        rev_merger(tool.keyword, use_dict)
               
def rev_annotator(lang='tw', verbose=True):
    """
    To expand the reverse dict
    
    lang: tw or cn
    
    2 ways to extend the reverse dict
    
      1. python keyword plugins
    
      2. ini file in local directory
    """
    if lang == 'tw':
        use_dict = rev_twdict
        entry_point = "zhpy.twdict"
        # tw plugin
        rev_py_annotator(use_dict, entry_point, verbose=False)

    if lang == 'cn':
        use_dict = rev_cndict
        entry_point = "zhpy.cndict"
        # cn plugin
        rev_py_annotator(use_dict, entry_point, verbose=False)
    # ini
    rev_ini_annotator(use_dict, verbose)
    
def number_to_variable(tmp):
    """
    convert number back to variable
    
    >>> number_to_variable('7bc4_4f8b')
    u'\u7bc4\u4f8b'
    
    #'範例'
    """
    word_list = tmp.split('_')
    term = ''
    for i in word_list:
        ori = 0
        for a, b in enumerate(i[::-1]):
            for i, s in enumerate(hexval):
                if b == s:
                    ori += i*16**a
        term +=  unichr(ori)
    return term

from pyparsing import srange, Word, quotedString

import re
def convertToTW(s,l,t):
    """
    search rev_twdict to match keywords
    """
    tmp = t[0]
    if tmp in rev_twdict:
        return rev_twdict[tmp]
    elif re.match(r'^p_[_\d]*_v\d?$', tmp):
        return number_to_variable(tmp)
    else:
        return tmp

def convertToCN(s,l,t):
    """
    search rev_cndict to match keywords
    """
    tmp = t[0]
    if tmp in rev_cndict:
        return rev_cndict[tmp]
    elif re.match(r'^p_[_\d]*_v\d?$', tmp):
        return number_to_variable(tmp)
    else:
        return tmp

#esworddict = _indict(seworddict)
englishChars = srange('[0-z]')

twenWord = Word(englishChars)
twenWord.setParseAction(convertToTW)
twpyWord = quotedString | twenWord

cnenWord = Word(englishChars)
cnenWord.setParseAction(convertToCN)
cnpyWord = quotedString | cnenWord 

def python_convertor(test, lang='tw'):
    """
    convert python source to zhpy source
    'print': '\xe6\x89\x93\xe5\x8d\xb0'
    
    lang: tw or cn
    
    >>> print python_convertor("print 'hello'", 'tw')
    印出 'hello'
    >>> print python_convertor("print 'hello'", 'cn')
    打印 'hello'
    """
    if lang == 'tw':
        result = twpyWord.transformString(test)
    elif lang == 'cn':
        result = cnpyWord.transformString(test)
    else:
        #TODO: auto detect coding
        print "not valid lang option in python_convertor"
        return
    return result
