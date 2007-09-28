# -*- coding: utf-8 -*-

"""zhpy interactive interpretor

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


from code import InteractiveConsole
from zhpy import convertor, annotator

class ZhPyConsole(InteractiveConsole):
    """
    Wrapper around Python and filter input/output to the shell
    """
    def push(self, line):
        self.buffer.append(line)
        source = "\n".join(self.buffer)
        more = self.runsource(convertor(source), self.filename)
        if not more:
            self.resetbuffer()
        return more

import sys
from release import version

def interpreter(lang=None):
    """
    zhpy interpreter

Accept args:
    lang:
        interpreter language
    """
    try:
        import readline
        import rlcompleter
        readline.parse_and_bind("tab: complete")
    except ImportError:
        pass

    con = ZhPyConsole()
    if lang == 'tw':
        banner = '周蟒 %s 於 %s 基於 Python %s'%(version, sys.platform,
                                                  sys.version.split()[0])
    elif lang == 'cn':
        banner = '周蟒 %s 于 %s 基于 Python %s'%(version, sys.platform,
                                                  sys.version.split()[0])
    else:
        banner = 'zhpy %s in %s on top of Python %s'%(version, sys.platform,
                                                  sys.version.split()[0])
    annotator()
    con.interact(banner)
