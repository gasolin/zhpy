#coding=utf-8
"""
test keywords
"""
from zhpy import convertor

def test_print():
    """
    test output statement and string types
    
    >>> print "hello"
    hello
    """
    assert convertor("印出 'hello'") == "print 'hello'"
    assert convertor('印出 "hello"') == 'print "hello"'
    assert convertor("""印出 'hello'""") == "print 'hello'"

def test_input():
    """
    test input statement
    """
    assert convertor("name = 輸入('your name:')") == \
                    "name = raw_input('your name:')"

def test_variable():
    """
    test variable
    """
    assert convertor("代號 = 'zhpy'") == "p_4ee3_865f_v = 'zhpy'"

def test_operators():
    """
    test operators
    
    >>> 1 == 1
    True
    """
    assert convertor("a 等於 b") == "a == b"
    assert convertor("a 不等於 b") == "a != b"

def test_def():
    """
    test definition
    """
    assert convertor("定義 hello(): 印出 'hello'") == "def hello(): print 'hello'"

def test_class():
    """
    test class
    """
    assert convertor("類別 hello: 定義 hello(): 印出 'hello'") == \
                    "class hello: def hello(): print 'hello'"

def test_import():
    """
    test import statement with from/import/as
    """
    assert convertor("導入 sys") == "import sys"
    assert convertor("導入 sys 作為 unix") == "import sys as unix"
    assert convertor("從 os 導入 path 作為 url") == "from os import path as url"
