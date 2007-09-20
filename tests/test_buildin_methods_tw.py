#coding=utf-8
"""
test build-in methods
"""
from zhpy import convertor

def test_type():
    """
    test type method
    """
    assert convertor('型別("sting") == 型別("abc")') == \
                    'type("sting") == type("abc")'

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

def test_enumerate():
    """
    test enumerate
    
    >>> items = ['zero', 'one', 'two', 'three']
    >>> print list(enumerate(items))
    [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three')]
    """
    assert convertor("取 (index, item) 在 列舉(items): 印出 index, item") == \
                    "for (index, item) in enumerate(items): print index, item"