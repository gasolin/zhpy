#coding=utf-8
"""
test build-in types
"""
from zhpy import convertor

def test_int():
    """
    test int type 
    """
    assert convertor("整數(2.0)") == "int(2.0)"
    
def test_float():
    """
    test float type
    """
    assert convertor("浮點數(2)") == "float(2)"

def test_boolean():
    """
    test boolean type
    """
    assert convertor("n = 真") == "n = True"
    assert convertor("p = 假") == "p = False"
    assert convertor("q = 實") == "q = True"
    assert convertor("r = 虛") == "r = False"
        
def test_string():
    """
    same as print test
    """
    s = "hello.py"
    assert convertor("s.開始字串('he')") == "s.startswith('he')"
    assert convertor("s.結束字串('he')") == "s.endswith('he')"
    
def test_list():
    """
    test list type
    """
    assert convertor("列表((1,2,3,4)) == [1,2,3,4]") == \
                    "list((1,2,3,4)) == [1,2,3,4]"
    assert convertor("a = []; a.加入(2); 宣告 a == [2]") == \
                    "a = []; a.append(2); assert a == [2]"
    p = "h,e,l,l,o"
    assert convertor('p.分離(",")') == 'p.split(",")'
    
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
    assert convertor("數組([1,2,3,4]) == (1,2,3,4)") == \
                    "tuple([1,2,3,4]) == (1,2,3,4)"

def test_set():
    """
    test set type
    """
    assert convertor("類組([1,2,3,4]) = set([1, 2, 3, 4])") == \
                    "set([1,2,3,4]) = set([1, 2, 3, 4])"

def test_file():
    """
    test file type
    """
    assert convertor('fd = 開啟("ReadMe_test.txt", "r")') == \
                    'fd = open("ReadMe_test.txt", "r")'
    assert convertor('temp = fd.讀一行()') == 'temp = fd.readline()'
    assert convertor('temp = fd.讀多行()') == 'temp = fd.readlines()'
    assert convertor('temp = fd.讀取()') == 'temp = fd.read()'
    assert convertor('fd.寫入(temp)') == 'fd.write(temp)'
    assert convertor('fd.關閉()') == 'fd.close()'