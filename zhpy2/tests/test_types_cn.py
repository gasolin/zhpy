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
    assert convertor("整数(2.0)") == "int(2.0)"

def test_float():
    """
    test float type
    """
    assert convertor("浮点数(2)") == "float(2)"

def test_bool():
    """
    test boolean type
    """
    assert convertor("布尔(1)") == "bool(1)"
    assert convertor("n is 真") == "n is True"
    assert convertor("n 是 真") == "n is True"
    assert convertor("p 为 假") == "p is False"
    assert convertor("q 不是 实") == "q is not True"
    assert convertor("r 不为 虛") == "r is not False"

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
    assert convertor("s.开头为('he')") == "s.startswith('he')"
    assert convertor("s.结尾为('py')") == "s.endswith('py')"
    assert convertor("items = 'zero one two three'.分离()") == "items = 'zero one two three'.split()"
    assert convertor("''.连接(s)") == "''.join(s)"

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
    assert convertor('p.分离(",")') == 'p.split(",")'

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
    assert convertor("元组([1,2,3,4]) == (1,2,3,4)") == \
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
    assert convertor('fd = 打开("ReadMe_test.txt", "r")') == \
                    'fd = open("ReadMe_test.txt", "r")'
    assert convertor('temp = fd.读一行()') == 'temp = fd.readline()'
    assert convertor('temp = fd.读多行()') == 'temp = fd.readlines()'
    assert convertor('temp = fd.读取()') == 'temp = fd.read()'
    assert convertor('fd.写入(temp)') == 'fd.write(temp)'
    assert convertor('fd.关闭()') == 'fd.close()'

def test_docstring():
    """
    test docstring
    """
    assert convertor('印出 """哈啰, 世界"""') == 'print """哈啰, 世界"""'
    assert convertor("印出 '''哈啰, 世界'''") == "print '''哈啰, 世界'''"
