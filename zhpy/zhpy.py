#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Transform zhpy source to python source

zhpy is the python language with chinese native keywords, variables, and 
parameters support, independent on python's version.

zhpy's core function is a convertor to translate chinese python code to nature python
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


from zhdc import worddict, twdict, cndict

def merger(anno_dict, use_dict=worddict, verbose=True):
    """
    merge extra bindings into worddict

Accept args:
    anno_dict:
        source dict
    use_dict:
        target dict to be merged, default: 'worddict'
    verbose:
        show detail message, default: True

    merger could accept list input:
    
    >>> keys = [('遊戲', 'pygame'), ('螢幕', 'screen')]
    >>> merger(keys)
    add 遊戲=pygame
    add 螢幕=screen
    >>> '遊戲' in worddict
    True
    
    merger could accept dict input:
    
    >>> keydic = {'作業系統':'os', '分支':'fork'}
    >>> merger(keydic)
    add 分支=fork
    add 作業系統=os
    >>> '作業系統' in worddict
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

def ini_annotator(verbose=True):
    """
    find ini files and use keywords defined in ini during 
    convertion progress.
    
Accept args:
    verbose:
        show detail message, default: True
    
    """
    inifiles = []
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
                merger(conf.items(sect))
        except:
            print "!%s is not a valid keyword file"%f

def py_annotator(verbose=False):
    """
    find python keyword plugins and update to dicts
    
Accept args:
    verbose:
        show detail message, default: False

    'verbose' argument is only for debug(will generate too mush messages).
    """
    # parameter to check if there's any plugin available
    has_annotator = False
    # tw plugin
    try:
        from plugtw import tools as twtools
        for tool in twtools:
            if verbose:
                print tool.title
            merger(tool.keyword, use_dict=twdict, verbose=verbose)
        merger(twdict, verbose=verbose)
        has_annotator = True
    except ImportError, e:
        if verbose:
            print "import plugtw error", e
    # cn plugin
    try:
        from plugcn import tools as cntools
        for tool in cntools:
            if verbose:
                print tool.title
            merger(tool.keyword, use_dict=cndict, verbose=verbose)
        merger(cndict, verbose=verbose)
        has_annotator = True
    except ImportError, e:
        if verbose:
            print "import plugcn error", e
    
    if not has_annotator:
        raise ReferenceError("no plugin was referenced in annotator")

def annotator(verbose=True):
    """
    provide two ways to expand the worddict:
    
      1. ini files
        
      2. python plugin system.

Accept args:
    verbose:
        show detail message, default: True

    """
    ini_annotator(verbose)
    py_annotator(verbose=False)

def zh_ord(tmp):
    """
    convert chinese variable to hex number
    
    >>> '範例'.decode("utf8")
    u'\u7bc4\u4f8b'
    >>> s = '範例'.decode("utf8")
    >>> zh_ord(s)
    'p_7bc4_4f8b_v'
    """
    word_list=[]
    for i in tmp:
        ori = str(hex(ord(i)))[2:]
        word_list.append(ori)
    return 'p_' + "_".join(word_list) + '_v'

# backward compatibility
variable_to_number = zh_ord

from pyparsing import srange, Word, quotedString, pythonStyleComment, \
     QuotedString

def convertToEnglish(s,l,t):
    """search worddict to match keywords
    
    if not in keyword, replace the chinese variable/argument/
    function name/class name/method name to a variable with prefix 'p'
    """
    tmp = t[0].encode("utf8")
    if tmp in worddict:
        word = worddict[tmp].decode("utf8")
    else:
        word = zh_ord(t[0])
    return word

chineseChars = srange(r"[\0x0080-\0xfe00]")
chineseWord = Word(chineseChars)
chineseWord.setParseAction(convertToEnglish)
tripleQuote = QuotedString('"""', multiline=True, unquoteResults=False)+ \
            QuotedString("'''", multiline=True, unquoteResults=False)

pythonWord = tripleQuote | quotedString | pythonStyleComment | chineseWord

try:
    import chardet
except:
    pass

def convertor(test, verbose=False, encoding=""):
    """
    convert zhpy source (Chinese) to Python Source.
    
    always run annotator before access convertor
    
Accept args:
    test:
        source to be converted
    verbose:
        show detail message, default: False
    encoding:
        codec for encoding

    >>> annotator()
    >>> convertor("印出 'hello'")
    "print 'hello'"
    
    >>> convertor("印出 'hello'", encoding="utf8")
    "print 'hello'"
    
    more keyword test cases are in /tests folder.
    """
    if encoding:
        utest = test.decode(encoding)
    else:
        try:
            #detect encoding
            det = chardet.detect(test)
            if verbose:
                print "chardet", det
            if det['confidence'] >= 0.8:
                encoding = chardet.detect(test)['encoding']
            else :
                if verbose:
                    print 'low confidence encoding detection, use utf8 encoding'
                encoding = 'utf8'
            utest = test.decode(encoding)
        except UnicodeDecodeError, e:
            print "can't recognize your language, set to utf-8"
            utest = test.decode('utf8')
        except ImportError, e:
            if verbose:
                print "proceed no chardet mode"
            utest = test.decode('utf8')
    
    result = pythonWord.transformString(utest)
    #TODO: allow different output encoding?
    result = result.encode("utf8")
    return result

import sys

def try_run(result, global_ns={}, local_ns={}):
    """
    execute result and catch exceptions in specified namespace
    
Accept args:
    result:
        the converted source to be executed
    global_ns:
        Global namespace, deafult is {}
    local_ns:
        Local namespace, default is: {}

    >>> global_ns = {'x':'g'}
    >>> local_ns = {'x':'l'}
    >>> global_ns.update( {"__name__": "__main__", "__doc__": None})
    >>> try_run("print 'hello'", {}, {})
    hello
    >>> try_run("print x", global_ns, local_ns)
    l
    >>> try_run("print x", global_ns)
    g
    """
    try:
        # able to import modules in current directory
        sys.path.insert(0, '')
        exec result in global_ns, local_ns
    except Exception, e:
        print result
        s = str(e)
        print s
        for k, v in worddict.items():
            if "'" + v + "'" in s:
                print unicode(k,"utf8"), v
            if '"' + v + '"' in s:
                print unicode(k,"utf8"), v

def zh_exec(content, global_ns={"__name__": "__main__", "__doc__": None}, local_ns={}):
    """
    the zhpy exec
    
Accept args:
    content:
        the source to be converted and executed with zhpy in specified namespace
    global_ns:
        Global namespace, deafult is {"__name__": "__main__", "__doc__": None}
    local_ns:
        Local namespace, default is: {}
    
    >>> zh_exec("印出 'hello'")
    hello
    """
    annotator()
    result = convertor(content)
    if local_ns == {}:
        local_ns = global_ns
    try_run(result, global_ns, local_ns)
