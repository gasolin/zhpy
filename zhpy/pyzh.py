#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Convert python source to zhpy source

"""

from zhpy import *

def _indict(dic):
    '''indict({'a':'1'})  -> {'1':'a'}
    '''
    d = {}
    dick = dic.keys()
    dick.reverse()
    map(d.update, map(lambda i: {dic[i]:i}, dick))
    return d

rev_twdict = _indict(twdict)
rev_cndict = _indict(cndict)

hexval = '0123456789abcdef'

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
