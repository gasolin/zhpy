#coding=utf-8
"""
test build-in modules
"""
from zhpy import convertor

def test_range():
    """
    test preload moudle: range
    """
    assert convertor("取 i 在 范围(10): 打印 i") == "for i in range(10): print i"

def test_enumerate():
    """
    test enumerate
    
    """
    assert convertor("取 (index, item) 在 列举(items): 打印 index, item") == \
                    "for (index, item) in enumerate(items): print index, item"