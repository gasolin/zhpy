#!/usr/bin/python
# -*- coding: utf-8 -*-

"""zhpy is the full feature python with chinese keywords, variables, and 
parameters support, independent on python version.

zhpy is an convertor to translate chinese python code to nature python
code (english) and vice versa.

zhpy is motivated by HYRY's origin code.

gasolin+zhpy@gmail.com

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


from zhdc import worddict, twdict, cndict, replacedict

def merger(anno_dict, use_dict=worddict, verbose=True):
    """
    merge extra bindings into worddict
    
    merger could accept list input:
    
    >>> keys = [('遊戲', 'pygame'), ('系統', 'sys')]
    >>> merger(keys)
    add 遊戲=pygame
    add 系統=sys
    >>> '遊戲' in worddict
    True
    
    merger could accept dict input:
    
    >>> keydic = {'作業系統':'os', '路徑':'path'}
    >>> merger(keydic)
    add 路徑=path
    add 作業系統=os
    >>> '系統' in worddict
    True
    """
    if type(anno_dict) == type([]):
        for k,v in anno_dict:
            #worddict.update({k:v})
            if k not in use_dict:
                use_dict[k] = v
                if verbose:
                    print "add %s=%s"%(k, v)
            else:
                if verbose:
                    print "already has key: %s, %s" % (k, v)

    if type(anno_dict) == type({}):
        for tmp in anno_dict.keys():
            if tmp not in use_dict:
                use_dict[tmp] = anno_dict[tmp]
                if verbose:
                    print "add %s=%s"%(tmp, anno_dict[tmp])
            else:
                if verbose:
                    print "already has key: %s, %s" % (tmp, anno_dict[tmp])

import os
import ConfigParser
import pkg_resources

def ini_annotator(verbose=True):
    """
    find ini files and use keywords defined in ini during 
    convertion progress.
    """
    # ini
    #inifiles = [x for x in os.listdir(".") if x.endswith(".ini")]
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
            merger(conf.items(sect))    

def py_annotator(verbose=False):
    """
    find python keyword plugins and update to dicts
    
    'verbose' argument is only for debug(will generate too mush messages).
    """
    # tw plugin
    for entrypoints in pkg_resources.iter_entry_points("zhpy.twdict"):
        tool = entrypoints.load()
        if verbose:
            print tool.title
        merger(tool.keyword, use_dict=twdict, verbose=verbose)
    merger(twdict, verbose=verbose)
    
    # cn plugin
    for entrypoints in pkg_resources.iter_entry_points("zhpy.cndict"):
        tool = entrypoints.load()
        if verbose:
            print tool.title
        merger(tool.keyword, use_dict=cndict, verbose=verbose)
    merger(cndict, verbose=verbose)
    
def annotator(verbose=True):
    """
    provide two ways to expand the worddict:
    
    1. ini files
        
    2. python plugin system.
    
    """
    ini_annotator(verbose)
    py_annotator(verbose=False)

def variable_to_number(tmp):
    """
    convert variable to hex number
    
    >>> '範例'.decode("utf8")
    u'\u7bc4\u4f8b'
    >>> s = '範例'.decode("utf8")
    >>> variable_to_number(s)
    '7bc4_4f8b'
    """
    #return '_'.join(map(lambda i:str(ord(i)), t[0]))
    word_list=[]
    for i in tmp:
        ori = str(hex(ord(i)))[2:]
        word_list.append(ori)
    return "_".join(word_list)

from pyparsing import srange, Word, quotedString

def convertToEnglish(s,l,t):
    """search worddict to match keywords
    
    if not in keyword, replace the chinese variable/argument/
    function name/class name/method name to a variable with prefix 'p'
    """
    tmp = t[0].encode("utf8")
    if tmp in worddict:
        word = worddict[tmp].decode("utf8")
    else:
        word = 'p_' + variable_to_number(t[0]) + '_v'
    return word

chineseChars = srange(r"[\0x0080-\0xfe00]")
chineseWord = Word(chineseChars)
chineseWord.setParseAction(convertToEnglish)
pythonWord = quotedString | chineseWord

try:
    import chardet
except:
    pass

def convertor(test, encoding=""):
    """
    convert zhpy source (Chinese) to Python Source.
    
    always run annotator before access convertor
    
    >>> annotator()
    >>> convertor("印出 'hello'")
    "print 'hello'"
    
    >>> convertor("印出 'hello'", encoding="utf8")
    "print 'hello'"
    
    more keyword test cases are in /tests folder.
    """
    for k, v in replacedict.items():
        test = test.replace(k,v)
    
    if encoding:
        utest = test.decode(encoding)
    else:
        try:
            #detect encoding
            det = chardet.detect(test)
            if det['confidence'] >= 0.8:
                encoding = chardet.detect(test)['encoding']
            else :
                #print 'low confidence encoding detection, use utf8 encoding'
                encoding = 'utf8'
            utest = test.decode(encoding)
        except UnicodeDecodeError, e:
            print "can't recognize your language, set to utf-8"
            utest = test.decode('utf8')
        except ImportError, e:
            #no chardet mode
            utest = test.decode('utf8')
    
    result = pythonWord.transformString(utest)
    result = result.encode("utf8")
    return result

def try_run(result):
    """
    execute result and catch exceptions
    
    >>> try_run("print 'hello'")
    hello
    """
    try:
        locals = {"__name__": "__main__", "__doc__": None}
        exec result in locals
    except Exception, e:
        print result
        s = str(e)
        print s
        for k, v in worddict.items():
            if "'" + v + "'" in s:
                print unicode(k,"utf8"), v
            if '"' + v + '"' in s:
                print unicode(k,"utf8"), v

def zh_exec(content):
    """
    the zhpy exec
    
    >>> zh_exec("印出 'hello'")
    hello
    """
    annotator()
    result = convertor(content)
    try_run(result)

if __name__=="__main__":
    from zhpyc import commandtool
    commandtool
