#coding=utf-8
"""
test keywords
"""
from zhpy import convertor

def test_print():
    assert convertor("印出 'hello'") == "print 'hello'"
    assert convertor('印出 "hello"') == 'print "hello"'
    assert convertor("""印出 'hello'""") == "print 'hello'"

def test_input():
    assert convertor("name = 輸入('your name:')") == "name = raw_input('your name:')"

def test_variable():
    assert convertor("代號 = 'gasolin'") == "p0 = 'gasolin'"

def test_operators():
    assert convertor("a 等於 b") == "a == b"
    assert convertor("a 不等於 b") == "a != b"

def test_def():
    assert convertor("定義 hello(): 印出 'hello'") == "def hello(): print 'hello'"

def test_class():
    assert convertor("類別 hello: 定義 hello(): 印出 'hello'") == \
                    "class hello: def hello(): print 'hello'"

def test_import():
    assert convertor("導入 sys") == "import sys"
    assert convertor("導入 sys 取名 unix") == "import sys as unix"
    assert convertor("從 os 導入 path 取名 url") == "from os import path as url"
