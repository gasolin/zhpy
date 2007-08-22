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
