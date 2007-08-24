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
from pyparsing import *

# Traditional chinese keywords
twdict = {# io
          "印出":"print",
          "輸入":"raw_input",
          # def
          "定義":"def",
          "類別":"class",
          # global
          "共用":"global",
          # import
          "從":"from",
          "導入":"import",
          "作為":"as",
          # flow
          "返回":"return",
          "傳回":"return",
          "略過":"pass", 
          "示警":"raise",
          "繼續":"continue",
          # control
          "如果":"if",
          "假使":"elif",
          "否則如果":"elif",
          "否則":"else",
          # for loop
          "取":"for",
          "在":"in",
          "自":"in",
          "不在":"not in",
          # while loop
          "當":"while",
          "跳出":"break",
          "中止":"break",
          # try
          "嘗試":"try",
          "異常":"except",
          "最後":"finally",
          # else
          "宣告":"assert",
          "刪除":"del",
          "執行":"exec",
          "方程式":"lambda",
          "產生":"yield",
          "伴隨":"with",
          # logic
          "等於":"==",
          "不等於":"!=",
          "是":"is",
          "為":"is",
          "不是":"is not",
          "或":"or",
          "和":"and",
          "且":"and",
          "真":"True",
          "假":"False",
          "實":"True",
          "虛":"False",
          "空":"None",
          # build in methods
          "型別":"type",
          "長度":"len",
          # build-in types
          "字串":"str",
          "列表": "list",
          "字典":"dict",
          "數組":"tuple",
          "集合":"set",
          "整數":"int",
          "浮點數":"float",
          # file methods
          "打開":"open",
          "讀取":"read",
          "寫入":"write",
          "讀一行":"readline",
          "讀多行":"readlines",
          "關閉":"close",
          # list methods
          "加入":"append",
          "追加":"append",
          # string methods
          "開始字串":"startswith",
          "結束字串":"endswith",
          "連接":"join",
          "分離":"split",
          # dict methods
          "關鍵字列表":"keys",
          "值列表":"values",
          "項目列表": "items",
          # encoding
          "編碼":"encoding",
          "解碼":"decoding",
          # preloaded modules
          "範圍":"range",
          }

# Simplized chinese keywords
cndict = {# io
          "打印":"print",
          "输入字符串":"raw_input",
          # def
          "定义":"def",
          "类":"class",
          # global
          "共用":"global",
          "全局":"global",
          # import
          "从":"from",
          "导入":"import",
          "作为":"as",
          # flow
          "传回":"return",
          "略过":"pass",
          "示警":"raise",
          "继续":"continue",
          # control
          "如果":"if",
          "否则如果":"elif",
          "否则":"else",
          # for loop
          "取":"for",
          "在":"in",
          "自":"in",
          "不在":"not in",
          # while loop
          "当":"while",
          "跳出":"break",
          "中断":"break",
          # try
          "尝试":"try",
          "异常":"except",
          "最后":"finally",
          # else
          "宣告":"assert",
          "刪除":"del",
          "执行":"exec",
          "函数":"lambda",
          "产生":"yield",
          "伴隨":"with",
          # logic
          "等于":"==",
          "不等于":"!=",
          "是":"is",
          "不是":"is not",
          "或者":"or",
          "并且":"and",
          "真": "True",
          "假":"False",
          "实":"True",
          "虛":"False",
          "空":"None",          
          # build in methods
          "类型":"type",
          "长度":"len",
          # build-in types
          "字符串":"str",
          "列表": "list",
          "字典":"dict",
          "数组":"tuple",
          "集合":"set",
          "整数":"int",
          "小数":"float",
          # file methods
          "打开":"open",
          "读取":"read",
          "写入":"write",
          "读一行":"readline",
          "读多行":"readlines",
          "关闭":"close",
          # list methods
          "加入":"append",
          "追加":"append",
          # string methods
          "开始为":"startswith",
          "结束为":"endswith",
          "连接":"join",
          "分离":"split",
          # dict methods
          "关键字列表":"keys",
          "值列表":"values",
          "项目列表":"items",
          # encoding
          "编码":"encoding",
          "解码":"decoding",
          # preloaded modules
          "范围":"range",
          }

# Traditional chinese and simplized chinese keywords
worddict = twdict
for i in cndict:
    if i in twdict:
        continue
    else:
        worddict[i]= cndict[i]

replacedict = {
    "（":"(",
    "）":")",
    "。":".",
    """:'"',
    """:'"',
    "'":"'",
    "'":"'",
    "，":",",
    "：":":",
    "！":"!",
    }

def merger(anno_dict):
    """
    merge extra bindings into worddict
    
    merge could accept list input:
    
    >>> keys = [('遊戲', 'pygame'), ('系統', 'sys')]
    >>> merger(keys)
    add 遊戲=pygame
    add 系統=sys
    >>> '遊戲' in worddict
    True
    
    merge could accept dict input:
    
    >>> keydic = {'作業系統':'os', '路徑':'path'}
    >>> merger(keydic)
    add 路徑=path
    add 作業系統=os
    >>> '系統' in worddict
    True
    """
    if type(anno_dict) == type([]):
        for k,v in anno_dict:
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
    
    1. inifiles
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
    #return 'p_' + '_'.join(map(lambda i:str(ord(i)), t[0])) + '_v'
    word_list=[]
    for i in tmp:
        ori = str(hex(ord(i)))[2:]
        word_list.append(ori)
    return "_".join(word_list)

#vnum = 0

def convertToEnglish(s,l,t):
    """search worddict to match keywords
    
    if not in keyword, replace the chinese variable/argument/
    function name/class name/method name to a variable with prefix 'p'
    
    TODO: able to convert code by annotate dict
    """
    #global vnum
    tmp = t[0].encode("utf8")
#    if tmp not in worddict:
#        worddict[tmp] = "p_" + str(vnum)
#        vnum += 1
#    english = worddict[tmp]
#    return english.decode("utf8")
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
    convert Chinese source to Python Source 
    
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
    raw:
        input raw zhpy source and run
    """
    import os
    import sys
    from optparse import OptionParser
    parser = OptionParser(
            usage="zhpy source [output]")
    parser.add_option("-i", "--input",
            help="speficy the input source",
            dest="input", default = None)
    parser.add_option("-o", "--output",
            help="speficy the output source",
            dest="output", default = None)
    parser.add_option("-p", "--python",
            help="compile to python and run",
            dest="compile", default = None)
    #prepare to deprecated
    parser.add_option("-r", "--raw",
            help="input raw zhpy source and run (plz use -c instead)",
            dest="raw", default = None)
    #
    parser.add_option("-c", "--cmd",
            help="input zhpy program as string and run",
            dest="raw", default = None)
    (options, args) = parser.parse_args()
    
    os.chdir(os.getcwd())
    #run as script
    if options.raw:
        test = options.raw
        annotator()
        result = convertor(test)
        try_run(result)
        return
    #run as command
    if len(sys.argv) >= 2:
        if (options.input is None) and sys.argv[1].endswith("py"):
            options.input = sys.argv[1]
        if options.compile:
            options.input = options.compile
        #if options.input:
        test = file(options.input, "r").read()
        annotator()
        result = convertor(test)
        if len(sys.argv) == 3:
            if sys.argv[1].endswith("py") and sys.argv[2].endswith("py"):
                options.output = sys.argv[2]
            if options.compile:
                filename = os.path.splitext(options.compile)[0]
                file("n_"+filename+".py","w").write(result)
                print "compile to python and run: %s"%("n_"+filename+".py")
        if options.output:
            file(options.output,"w").write(result)
        else:
            try_run(result)
    else:
        print """please type "zhpy --help" for help"""
  
if __name__=="__main__":
    commandtool()