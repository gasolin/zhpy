#!/usr/bin/python
# -*- coding: utf-8 -*-
"""zhpy is an convertor to translate chinese python code to nature python 
code (english) and vice versa.

zhpy refactored the origin code from HYRY.

fredlin 2007, gasolin+mopowg@gmail.com

This is the MIT license:
http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2007 Fred Lin and contributors. zhpy is a trademark of Fred Lin.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from zhdc import worddict, replacedict

def merger(anno_dict):
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
            if k not in worddict:
                worddict[k] = v
                print "add %s=%s"%(k, v)
            else:
                print "already has key: %s, %s" % (k, v)
            
    if type(anno_dict) == type({}):
        for tmp in anno_dict.keys():
            if tmp not in worddict:
                worddict[tmp] = anno_dict[tmp]
                print "add %s=%s"%(tmp, anno_dict[tmp])
            else:
                print "already has key: %s, %s" % (tmp, anno_dict[tmp])

import os
import ConfigParser

def annotator():
    """
    provide two ways to expand the worddict:
    
    1. inifiles:
        find ini files and use keywords defined in ini during 
        convertion progress.
    
    2. head docsting annotator（TODO）
    """
    #inifiles = [x for x in os.listdir(".") if x.endswith(".ini")]
    inifiles = []
    for x in os.listdir("."):
        if x.endswith(".ini"):
            inifiles.append(x)
    for f in inifiles:
        print "file", f
        conf = ConfigParser.ConfigParser()
        conf.read(f)
        sects = conf.sections()
        for sect in sects:
            print "sect:", sect
            merger(conf.items(sect))

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
    
    #TODO: able to convert code by annotate dict
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

def convertor(test):
    """
    convert zhpy source (Chinese) to Python Source 
    
    >>> convertor("印出 'hello'")
    "print 'hello'"
    
    more keyword test cases are in /tests folder.
    """
    for k, v in replacedict.items():
        test = test.replace(k,v)
    
    utest = test.decode("utf8")
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

def commandtool():
    """command line tool method
    
    input:
        speficy the input source
    output:
        speficy the output source
    python:
        compile to python and run
    cmp:
        input raw zhpy source and run
    """
    import os
    import sys
    from optparse import OptionParser
    from release import version
    parser = OptionParser(
            usage="usage: %prog [-i|-p] input [-o output]",
            version="zhpy %s"%version)
    parser.add_option("-i", "--input",
            help="speficy the input source",
            dest="input", default = None)
    parser.add_option("-o", "--output",
            help="speficy the output source",
            dest="output", default = None)
    parser.add_option("-p", "--python",
            help="compile to python and run",
            dest="python", default = None)
    parser.add_option("-c", "--cmd",
            help="input zhpy program as string and run",
            dest="cmp", default = None)
    (options, args) = parser.parse_args()
    
    os.chdir(os.getcwd())
    #run as script
    if options.cmp:
        test = options.cmp
        annotator()
        result = convertor(test)
        try_run(result)
        return
    #run as command
    #TODO: accept args
    argv = sys.argv[1:]
    if len(argv) >= 1:
        if (options.input is None) and argv[0].endswith("py"):
            options.input = argv[0]
        if options.python:
            options.input = options.python
        #if options.input:
        test = file(options.input, "r").read()
        annotator()
        result = convertor(test)
        if len(argv) == 2:
            if argv[0].endswith("py") and argv[1].endswith("py"):
                options.output = argv[1]
            if options.python:
                filename = os.path.splitext(options.python)[0]
                file("n_"+filename+".py","w").write(result)
                print "compile to python and run: %s"%("n_"+filename+".py")
        if options.output:
            file(options.output,"w").write(result)
        else:
            try_run(result)
    else:
        #TODO: start interpreter here
        print """please type "zhpy --help" for help"""
  
if __name__=="__main__":
    commandtool()