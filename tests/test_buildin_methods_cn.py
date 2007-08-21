#coding=utf-8
"""
test build-in methods
"""
from zhpy import convertor

def test_type():
    """
    test type method
    """
    assert convertor('类型("sting") == 类型("abc")') == \
                    'type("sting") == type("abc")' 
    
def test_len():
    """
    test len method
    """
    assert convertor("长度('hello')") == "len('hello')"
