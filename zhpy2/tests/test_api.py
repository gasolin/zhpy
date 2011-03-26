#coding=utf-8
"""
test api
"""
from zhpy import zh_ord, convertor
from zhpy.pyzh import zh_chr
from zhpy.pyzh import rev_annotator, python_convertor

def test_convertor():
    """
    test convertor
    """
    rev_annotator()
    assert convertor("印出 'hello'") == "print 'hello'" 
    assert python_convertor("print 'hello'") == ("印出 'hello'")
    assert python_convertor(convertor("印出 'hello'")) == ("印出 'hello'")
    # check if variable convert correctly, not a python valid syntax
    assert python_convertor(convertor("打出 '''哈囉'''")) == ("打出 '''哈囉'''")
    assert python_convertor(convertor("打出 '''p_哈囉_v'''")) == ("打出 '''p_哈囉_v'''")
    assert python_convertor(convertor("打出 '''哈\
    囉'''")) == ("打出 '''哈\
    囉'''")
    assert python_convertor(convertor('打出 """哈\
    _囉"""')) == ('打出 """哈\
    _囉"""')
    

def test_uri():
    """
    test uri
    """
    assert zh_ord('範例'.decode("utf8")) == 'p_7bc4_4f8b_v'
    assert zh_ord('p_範例_v'.decode("utf8")) == 'p_70_5f_7bc4_4f8b_5f_76_v'
    assert zh_chr('p_7bc4_4f8b_v') == '範例'
    assert zh_chr(zh_ord('範例'.decode("utf8"))) == '範例'
