#coding=utf-8
"""
test signals
"""
from zhpy import convertor

def test_comment():
    """
    # comment should not be translated
    """
    assert convertor("# 测试") == "# 测试"
    assert convertor("""# ！（），。；：''""【】{}""") == """# ！（），。；：''""【】{}"""

def test_comma():
    """
    test signal used ！（），。；：''""【】
    """
    assert convertor("！") =="!"
    assert convertor("（") == "("
    assert convertor("）") == ")"
    assert convertor("，") == ","
    assert convertor("。") == "."
    assert convertor("；") == ";"
    assert convertor("：") == ":"
    assert convertor("'") == "'"
    assert convertor("'") == "'"
    assert convertor('"') == '"'
    assert convertor('"') == '"'
    assert convertor("【") == "["
    assert convertor("】") == "]"
