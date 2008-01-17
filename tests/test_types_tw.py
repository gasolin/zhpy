#coding=utf-8
"""
test build-in types
"""
from zhpy import convertor

def test_int():
    """
    test int type
    
    >>> int(2.0)
    2
    >>> int(3.1415926)
    3
    """
    assert convertor("整數(2.0)") == "int(2.0)"

def test_float():
    """
    test float type
    """
    assert convertor("浮點數(2)") == "float(2)"

def test_bool():
    """
    test boolean type
    
    """
    assert convertor("布林(1)") == "bool(1)"
    assert convertor("n is 真") == "n is True"
    assert convertor("n 是 真") == "n is True"
    assert convertor("p 為 假") == "p is False"
    assert convertor("q 不是 實") == "q is not True"
    assert convertor("r 不為 虛") == "r is not False"

def test_string():
    """
    same as print test
    
    >>> s = "hello.py"
    >>> s.startswith('he')
    True
    >>> s.endswith('py')
    True
    >>> s = ['one', 'two']
    >>> ''.join(s)
    'onetwo'
    """
    assert convertor("s.開頭為('he')") == "s.startswith('he')"
    assert convertor("s.結尾為('py')") == "s.endswith('py')"
    assert convertor("items = 'zero one two three'.分離()") == "items = 'zero one two three'.split()"
    s = ['one', 'two']
    assert convertor("''.連接(s)") == "''.join(s)"

def test_list():
    """
    test list type
    
    >>> list((1,2,3,4)) == [1,2,3,4]
    True
    """
    assert convertor("列表((1,2,3,4)) == [1,2,3,4]") == \
                    "list((1,2,3,4)) == [1,2,3,4]"
    assert convertor("a = []; a.加入(2); 申明 a == [2]") == \
                    "a = []; a.append(2); assert a == [2]"
    p = "h,e,l,l,o"
    assert convertor('p.分離(",")') == 'p.split(",")'

def test_dict():
    """
    test dict type
    
    >>> dict(a=1, b=2) == {'a':1, 'b':2}
    True
    """
    assert convertor("字典(a=1, b=2) == {'a':1, 'b':2}") == \
                    "dict(a=1, b=2) == {'a':1, 'b':2}"

def test_tuple():
    """
    test tuple type
    
    >>> tuple([1,2,3,4]) == (1,2,3,4)
    True
    """
    assert convertor("元組([1,2,3,4]) == (1,2,3,4)") == \
                    "tuple([1,2,3,4]) == (1,2,3,4)"

def test_set():
    """
    test set type
    
    >>> set([1,2,3,4]) == set([1, 2, 3, 4])
    True
    """
    assert convertor("集合([1,2,3,4]) == set([1, 2, 3, 4])") == \
                    "set([1,2,3,4]) == set([1, 2, 3, 4])"

def test_file():
    """
    test file type
    """
    assert convertor('fd = 打開("ReadMe_test.txt", "r")') == \
                    'fd = open("ReadMe_test.txt", "r")'
    assert convertor('temp = fd.讀一行()') == 'temp = fd.readline()'
    assert convertor('temp = fd.讀多行()') == 'temp = fd.readlines()'
    assert convertor('temp = fd.讀取()') == 'temp = fd.read()'
    assert convertor('fd.寫入(temp)') == 'fd.write(temp)'
    assert convertor('fd.關閉()') == 'fd.close()'

def test_docstring():
    """
    test docstring
    """
    assert convertor('印出 """哈囉, 世界"""') == 'print """哈囉, 世界"""'
    assert convertor("印出 '''哈囉, 世界'''") == "print '''哈囉, 世界'''"
