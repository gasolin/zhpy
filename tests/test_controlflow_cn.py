#coding=utf-8
"""
test control flow
"""
from zhpy import convertor

def test_if():
    """
    test if, elif, else
    """
    assert convertor("如果 a: 略过") == "if a: pass"
    assert convertor("如果 a: 略过; 否则: 略过") == "if a: pass; else: pass"
    assert convertor("如果 a: 略过; 否则如果 b: 略过; 否则: 略过") == \
                    "if a: pass; elif b: pass; else: pass"

def test_for_loop():
    """
    test for loop
    """
    assert convertor("取 i 在 [1,2,3,4]: 打印 i") == "for i in [1,2,3,4]: print i"

def test_while_loop():
    """
    test while loop
    """
    assert convertor("当 1: 打印 'hello'; 中断") == "while 1: print 'hello'; break"

def test_try():
    """
    test try except
    """
    assert convertor("尝试: 导入 a; 异常 ImportError, e: 打印 e") == \
                "try: import a; except ImportError, e: print e"
    assert convertor("引发 例外") == "raise Exception"

def test_is():
    """
    test is, is not statement
    """
    assert convertor("4 為 4") == ("4 is 4")
    assert convertor("4 是 4") == ("4 is 4")
    assert convertor("4 不是 2") == ("4 is not 2")