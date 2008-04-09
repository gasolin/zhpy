# -*- coding: utf-8 -*-

"""zhpy interactive interpretor

This is the MIT license:
http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2007~ Fred Lin and contributors. zhpy is a trademark of Fred Lin.

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
from zhpy import convertor
import sys

class ZhPyConsole(InteractiveConsole):
    """
    Wrapper around Python and filter input/output to the shell
    """

    def push(self, line):
        self.buffer.append(line)
        source = "\n".join(self.buffer)
        more = self.runsource(convertor(source, encoding=sys.stdout.encoding),
                            self.filename)
        if not more:
            self.resetbuffer()
        return more

try:
    from release import version
except:
    version = 'core'


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
        banner = '周蟒 %s 在 %s 基於 Python %s'%(version, sys.platform,
                                                  sys.version.split()[0])
        if sys.platform == 'win32':
            banner = unicode(banner, 'utf-8').encode(sys.stdout.encoding)
    elif lang == 'cn':
        banner = '周蟒 %s 在 %s 基于 Python %s'%(version, sys.platform,
                                                  sys.version.split()[0])
        if sys.platform == 'win32':
            banner = unicode(banner, 'utf-8').encode(sys.stdout.encoding)
    else:
        banner = 'zhpy %s in %s on top of Python %s'%(version, sys.platform,
                                                  sys.version.split()[0])
    #annotator()
    # able to import modules in current directory
    sys.path.insert(0, '')
    con.interact(banner)


if __name__=="__main__":
    try:
        import import_hook
    except:
        print "There's no zhimport support"

    import sys
    argv = sys.argv[1:]

    #profiling
    if len(argv)!=0 and argv[0] =="--profile":
        import profile
        profile.run("interpreter()", "prof.txt")
        import pstats
        p = pstats.Stats("prof.txt")
        p.sort_stats("time").print_stats()
    else:
        interpreter()