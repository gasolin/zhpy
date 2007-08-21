#coding=utf-8
"""
test build-in methods
"""
from zhpy import convertor

def test_len():
    """
    test len method
    """
    assert convertor("長度('hello')") == "len('hello')"

def test_range():
    """
    test preload moudle: range
    """
    assert convertor("取 i 在 範圍(10): 印出 i") == "for i in range(10): print i"