#!/usr/bin/python
# -*- coding: utf-8 -*-

"""zhpy command line tool

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

import os
import sys
from optparse import OptionParser
from release import version
from zhpy import annotator, convertor, try_run

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
    encoding:
        specify the encoding
    """
    parser = OptionParser(
            usage="usage: %prog [-i|-p] input [-o] [output] [--e] [encoding]",
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
            help="input raw zhpy source and run",
            dest="cmp", default = None)
    parser.add_option("-e", "--encoding",
            help="specify the encoding",
            dest="encoding", default = "")
    (options, args) = parser.parse_args()
    
    os.chdir(os.getcwd())
    #run as script
    if options.cmp:
        test = options.cmp
        annotator()
        if options.encoding:
            result = convertor(test, options.encoding)
        else:
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
        if options.encoding:
            result = convertor(test, options.encoding)
        else:
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
        from zhpy_interpreter import interpreter
        interpreter()
  
if __name__=="__main__":
    commandtool()
