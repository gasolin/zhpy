#coding=utf-8
"""
test build-in types
"""
from zhpy import convertor

def test_int():
    """
    test int type 
    """
    assert convertor("整数(2.0)") == "int(2.0)"
    
def test_float():
    """
    test float type
    """
    assert convertor("小数(2)") == "float(2)"

def test_boolean():
    """
    test boolean type
    """
    assert convertor("n = 真") == "n = True"
    assert convertor("p = 假") == "p = False"
    assert convertor("q = 实") == "q = True"
    assert convertor("r = 虛") == "r = False"
        
def test_string():
    """
    same as print test
    """
    pass

def test_list():
    """
    test list type
    """
    assert convertor("列表((1,2,3,4)) == [1,2,3,4]") == "list((1,2,3,4)) == [1,2,3,4]"
    assert convertor("a = []; a.加入(2); 宣告 a == [2]") == \
                    "a = []; a.append(2); assert a == [2]"
    
def test_dict():
    """
    test dict type
    """
    assert convertor("字典(a=1, b=2) == {'a':1, 'b':2}") == \
                    "dict(a=1, b=2) == {'a':1, 'b':2}"

def test_tuple():
    """
    test tuple type
    """
    assert convertor("数组([1,2,3,4]) == (1,2,3,4)") == \
                    "tuple([1,2,3,4]) == (1,2,3,4)"

def test_set():
    """
    test set type
    """
    assert convertor("类组([1,2,3,4]) = set([1, 2, 3, 4])") == \
                    "set([1,2,3,4]) = set([1, 2, 3, 4])"
