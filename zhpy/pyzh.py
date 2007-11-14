#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Transform python source to zhpy source

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

 
from zhpy import annotator, tripleQuote
from zhdc import twdict, cndict, revert_dict

annotator()
# make reverse traditional chinese dicts
rev_twdict = revert_dict(twdict)
# make reverse simplified chinese dicts
rev_cndict = revert_dict(cndict)
    
def rev_merger(anno_dict, use_dict, verbose=False):
    """
    merge extra bindings into reverse dict

Accept args:
    anno_dict:
        source dict
    use_dict:
        target dict to be merged
    verbose:
        show detail message, default: True
    
    >>> keys = [('遊戲', 'pygame'), ('螢幕', 'screen')]
    >>> rev_merger(keys, rev_twdict, True)
    add pygame=遊戲
    add screen=螢幕
    >>> 'pygame' in rev_twdict
    True
    
    >>> keys = [('游戏', 'pygame'), ('螢幕', 'screen')]
    >>> rev_merger(keys, rev_cndict, True)
    add pygame=游戏
    add screen=螢幕
    >>> 'pygame' in rev_cndict
    True
    
    >>> keys = {"作業系統":"os", "選項解析":"optparse"}
    >>> rev_merger(keys, rev_twdict, True)
    add optparse=選項解析
    add os=作業系統
    >>> 'os' in rev_twdict
    True
    
    >>> keys = {"作业系统":"os", "选项解析":"optparse"}
    >>> rev_merger(keys, rev_cndict, True)
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
                    print "already has key: %s:%s" % (tmp, anno_dict.keys()[num]) 

def rev_ini_annotator(use_dict, verbose=True):
    """
    update revert dict by ini files
    
Accept args:
    use_dict:
        target dict to be merged
    verbose:
        show detail message, default: True

    """
    # ini
    inifiles = []
    import os
    import ConfigParser
    for x in os.listdir("."):
        if x.endswith(".ini"):
            inifiles.append(x)
    for f in inifiles:
        if verbose:
            print "file", f
        conf = ConfigParser.ConfigParser()
        try:
            conf.read(f)
            sects = conf.sections()
            for sect in sects:
                if verbose:
                    print "sect:", sect
                rev_merger(conf.items(sect), use_dict)
        except:
            print "!%s is not a valid keyword file"%f

def rev_py_annotator(use_dict, entry_point, verbose=False):
    """
    update revert dict by python plugins
    
    'verbose' argument is only for debug(will generate too mush messages).
    """
    for tool in entry_point:
        if verbose:
            print tool.title
        rev_merger(tool.keyword, use_dict)
               
def rev_annotator(lang='tw', verbose=True):
    """
    To expand the reverse dict

    ther are 2 ways to extend the reverse dict

      1. python keyword plugins

      2. ini file in local directory

Accept args:
    lang:
        'tw' or 'cn'

    """
    if lang == 'tw':
        use_dict = rev_twdict
        #entry_point = "zhpy.twdict"
        from plugtw import tools
        # tw plugin
        rev_py_annotator(use_dict, entry_point=tools, verbose=False)

    if lang == 'cn':
        use_dict = rev_cndict
        #entry_point = "zhpy.cndict"
        from plugcn import tools
        # cn plugin
        rev_py_annotator(use_dict, entry_point=tools, verbose=False)
    # ini
    rev_ini_annotator(use_dict, verbose)

import re

def val_matching(tmp):
    """
    match and convert the identifiers
    """
    tmp2 = ''
    for word in tmp.split('_')[1:]:
        if not ('v' in word and 'p' in word):
            tmp2 += unichr(int(word, 16)).encode('utf8')
    return tmp2

def zh_chr(tmp):
    """
    convert number back to chinese variable
    
    >>> print zh_chr('p_7bc4_4f8b_v')
    範例
    >>> print zh_chr('p_7bc4_4f8b_v_1')
    範例_1
    >>> print zh_chr('p_7bc4_4f8b_v1')
    範例1
    >>> print zh_chr("p_6e2c_8a66_v_p_7bc4_4f8b_v")
    測試_範例
    >>> print zh_chr("p_6e2c_8a66_v_p_7bc4_4f8b_v2")
    測試_範例2
    """ 
    if tmp.startswith("p_") and "_v" in tmp:
        tmp, profix = tmp.split('_v', 1)
        tmp2 = val_matching(tmp)
        if not ('v' in profix and 'p' in profix):
            return tmp2 + profix
        else: # allow 2 cascade identifiers
            sep = profix[0:profix.index('p_')]
            tmp = profix[profix.index('p_')::]
            tmp, profix = tmp.split('_v', 1)
            tmp2 += sep + val_matching(tmp)
            return tmp2 +profix
    else:
        return tmp

# backward compatibility
number_to_variable = zh_chr

from pyparsing import srange, Word, alphanums, \
                      quotedString, pythonStyleComment

def convertToTW(s,l,t):
    """
    search rev_twdict to match keywords
    """
    tmp = t[0]
    if tmp in rev_twdict:
        return rev_twdict[tmp]
    elif re.match(r'^p_[_a-f\d]*_v\w*$', tmp):
        return zh_chr(tmp)
    else:
        return tmp
    
def convertToCN(s,l,t):
    """
    search rev_cndict to match keywords
    """
    tmp = t[0]
    if tmp in rev_cndict:
        return rev_cndict[tmp]
    elif re.match(r'^p_[_a-f\d]*_v\w*$', tmp):
        return zh_chr(tmp)
    else:
        return tmp

twenWord = Word(alphanums+"_")
twenWord.setParseAction(convertToTW)
twpyWord = tripleQuote | quotedString | pythonStyleComment | twenWord

cnenWord = Word(alphanums+"_")
cnenWord.setParseAction(convertToCN)
cnpyWord = tripleQuote | quotedString | pythonStyleComment | cnenWord 

def python_convertor(test, lang='tw'):
    """
    convert python source to zhpy source

Accept args:
    lang:
        'tw' or 'cn'
    
    >>> print python_convertor("print 'hello'", 'tw')
    印出 'hello'
    >>> print python_convertor("print 'hello'", 'cn')
    打印 'hello'
    >>> print python_convertor("# print 'hello'", 'tw')
    # print 'hello'
    >>> print python_convertor("print '''哈囉, 世界'''", 'tw')
    印出 '''哈囉, 世界'''
    >>> print python_convertor("p_6e2c_8a66_v_p_7bc4_4f8b_v2")
    測試_範例2
    >>> print python_convertor("p_6e2c_8a66_v2p_7bc4_4f8b_v")
    測試2範例
    >>> print python_convertor("p_6e2c_8a66_v2p_7bc4_4f8b_v2")
    測試2範例2
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
