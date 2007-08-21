#coding=utf-8
"""
test build-in methods
"""
from zhpy import convertor

def test_len():
    """
    test len method
    """
    assert convertor("长度('hello')") == "len('hello')"

def test_range():
    """
    test preload moudle: range
    """
    assert convertor("取 i 在 范围(10): 打印 i") == "for i in range(10): print i"