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
    pass

def test_operators():
    pass

def test_def():
    assert convertor("定義 hello(): 印出 'hello'") == "def hello(): print 'hello'"

def test_class():
    pass

def test_import():
    pass
