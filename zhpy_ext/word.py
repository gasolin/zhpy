#coding=utf-8

"""
zh_module plugin
"""
from zhpy.zhdc import ZhpyPlugin

#enter traditional chinese dict here
class tw_module(ZhpyPlugin):
    """
    繁體中文 關鍵詞插件
    """
    title = "中文名稱"
    description = "中文敘述"
    keyword = {"系統":"sys", "版本":"version"}


#enter simplified chinese dict here
class cn_module(ZhpyPlugin):
    """
    简体中文 关键词插件
    """
    title = "中文名称"
    description = "中文叙述"
    keyword = {"系统":"sys", "版本":"version"}
