#coding=utf-8
"""
test build-in modules
"""
from zhpy import convertor

def test_range():
    """
    test preload moudle: range
    """
    assert convertor("取 i 在 範圍(10): 印出 i") == "for i in range(10): print i"