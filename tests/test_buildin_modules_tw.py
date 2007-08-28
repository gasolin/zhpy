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

def test_enumerate():
    """
    test enumerate
    
    >>> items = ['zero', 'one', 'two', 'three']
    >>> print list(enumerate(items))
    [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three')]
    """
    assert convertor("取 (index, item) 在 列舉(items): 印出 index, item") == \
                    "for (index, item) in enumerate(items): print index, item"
    
    
