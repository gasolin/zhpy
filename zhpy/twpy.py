#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import tokenize
import plugtw
import runpy

def translate_code(readline):
    for type, name, _,_,_ in tokenize.generate_tokens(readline):
        if type == tokenize.NAME and name in plugtw.trans:
            yield tokenize.NAME, plugtw.trans[name]
        else:
            yield type, name
            
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("usage: twpy file.py")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("twpy: file '%s' does not exists" % file_path)
        sys.exit(1)

    #sys.meta_path = [ImportHook()]

    sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))

    source = tokenize.untokenize(
            list(translate_code(open(file_path).readline)))

    #translate_module(__builtins__)

    code = compile(source, file_path, "exec")

    runpy._run_module_code(code, mod_name="__main__")