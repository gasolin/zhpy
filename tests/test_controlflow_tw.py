#coding=utf-8
"""
test control flow
"""
from zhpy import convertor

def test_if():
    """
    test if, elif, else
    """
    assert convertor("如果 a: 略過") == "if a: pass"
    assert convertor("如果 a: 略過; 否則: 略過") == "if a: pass; else: pass"
    assert convertor("如果 a: 略過; 假使 b: 略過; 否則: 略過") == \
                    "if a: pass; elif b: pass; else: pass"

def test_for_loop():
    """
    test for loop
    """
    assert convertor("取 i 在 [1,2,3,4]: 印出 i") == "for i in [1,2,3,4]: print i"

def test_while_loop():
    """
    test while loop
    """
    assert convertor("當 1: 印出 'hello'; 跳出") == "while 1: print 'hello'; break"

def test_try():
    """
    test try except
    """
    assert convertor("嘗試: 導入 a; 異常 ImportError, e: 印出 e") == \
                "try: import a; except ImportError, e: print e"
    assert convertor("引發 例外") == "raise Exception"
    
def test_is():
    """
    test is, is not statement
    """
    assert convertor("4 為 4") == ("4 is 4")
    assert convertor("4 是 4") == ("4 is 4")
    assert convertor("4 不是 2") == ("4 is not 2")