#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Chinese keyword dictionaries

This is the MIT license:
http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2007 Fred Lin and contributors. zhpy is a trademark of Fred Lin.

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to 
deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
"""


# Universal keywords repository
# always run annotator before access worddict
worddict = {}
# Traditional Chinese keywords repository
twdict = {}
# Simplified Chinese keywords repository
cndict = {}

# punctuations
replacedict = {
    "（":"(",
    "）":")",
    "。":".",
    """:'"',
    """:'"',
    "'":"'",
    "'":"'",
    "，":",",
    "：":":",
    "！":"!",
    }


class ZhpyPlugin(object):
    """
    basic plugin class
    """
    pass


# Traditional chinese keywords
class tw_keyword(ZhpyPlugin):
    """
    python tw keyword
    """
    title = "內建關鍵詞"
    description = "Python 內建關鍵詞"
    keyword = {
          # logic
          "和":"and",
          "且":"and",
          "或":"or",
          "非":"not",
          "是":"is",
          "為":"is",
          "不是":"is not",
          "不為":"is not",
          "真":"True",
          "假":"False",
          "實":"True",
          "虛":"False",
          "空":"None",
          # def
          "定義":"def",
          "類別":"class",
          "共用":"global",
          # import
          "從":"from",
          "導入":"import",
          "作為":"as",
          # flow
          "返回":"return",
          "略過":"pass", 
          "示警":"raise",
          "繼續":"continue",
          # control
          "如果":"if",
          "假使":"elif",
          "否則如果":"elif",
          "否則":"else",
          # for loop
          "取":"for",
          "在":"in",
          "自":"in",
          "不在":"not in",
          # while loop
          "當":"while",
          "跳出":"break",
          "中斷":"break",
          # try
          "嘗試":"try",
          "異常":"except",
          "最後":"finally",
          "宣告":"assert",
          # build in methods
          "執行":"exec",
          "方程式":"lambda",
          "印出":"print",
          
          "伴隨":"with",
          "產生":"yield",
          "刪除":"del",
          }


class tw_buildin_method(ZhpyPlugin):
    """
    python tw methods
    """
    title = "內部函數"
    description = "Python 內部函數"
    keyword = {
          "輸入":"raw_input",
          # build-in types
          "字串":"str",
          "布林":"bool",
          "列表":"list",
          "字典":"dict",
          "數組":"tuple",
          "集合":"set",
          "符號":"chr",
          "符號轉整數":"ord",
          "文件":"file",
          # number methods
          "整數":"int",
          "浮點數":"float",
          "複數":"complex",
          "十六進位":"hex",
          "絕對值":"abs",
          "比較":"cmp",
          "最大":"max",
          "最小":"min",
          # string methods
          "開頭為":"startswith",
          "結尾為":"endswith",
          "連接":"join",
          "分離":"split",
          "編碼":"encoding",
          "解碼":"decoding",
          # list methods
          "加入":"append",
          "追加":"append",
          "擴展":"extend",
          "插入":"insert",
          "彈出":"pop",
          "下一筆":"next",
          "移除":"remove",
          "計數":"count",
          "索引":"index",
          "排序":"sort",
          # file methods
          "打開":"open",
          "讀取":"read",
          "寫入":"write",
          "讀一行":"readline",
          "讀多行":"readlines",
          "關閉":"close",
          # dict methods
          "關鍵字列表":"keys",
          "值列表":"values",
          "項目列表": "items",
          "更新":"update",
          # OO
          "可調用":"callable",
          "列出屬性":"dir",
          "取屬性":"getattr",
          "有屬性":"hasattr",
          "設定屬性":"setattr",
          # build in methods
          "列舉":"enumerate",
          "求值":"eval",
          "過濾":"filter",
          "長度":"len",
          "映射":"map",
          "範圍":"range",
          "快速範圍":"xrange",
          "總和":"sum",
          "型別":"type",
          "打包":"zip",
          "說明":"help",
          "幫助":"help",
          }


class tw_exception(ZhpyPlugin):
    """
    python tw exceptions
    """
    title = "例外"
    description = "Python 內建例外關鍵詞"
    keyword = {
          "例外":"Exception",
          # error
          "停止迭代":"StopIteration",
          "型別錯誤":"TypeError",
          "解碼錯誤":"UnicodeDecodeError",
          "導入錯誤":"ImportError",
          }


class tw_zhpy(ZhpyPlugin):
    """
    zhpy tw keyword plugin
    """
    title = "周蟒"
    description = "周蟒內建關鍵詞"
    keyword = {
          "周蟒":"zhpy",
          "主程式":'if __name__=="__main__"',
          # must do 'from zhpy import zh_exec'/'從 周蟒 導入 中文執行' first
          "中文執行":"zh_exec",
          # logic
          "等於":"==",
          "不等於":"!=",
          }


# Simplized chinese keywords
class cn_keyword(ZhpyPlugin):
    """
    python cn keyword
    """
    title = "内建关键词"
    description = "Python 内建关键词"
    keyword = {
          # logic
          "和":"and",
          "且":"and",
          "或":"or",
          "非": "not",
          "是":"is",
          "为":"is",
          "不是":"is not",
          "不为":"is not",
          "真": "True",
          "假":"False",
          "实":"True",
          "虛":"False",
          "空":"None",
          # def
          "定义":"def",
          "类":"class",
          "共用":"global",
          # import
          "从":"from",
          "导入":"import",
          "作为":"as",
          # flow
          "传回":"return",
          "略过":"pass",
          "示警":"raise",
          "继续":"continue",
          # control
          "如果":"if",
          "假使":"elif",
          "否则如果":"elif",
          "否则":"else",
          # for loop
          "取":"for",
          "在":"in",
          "自":"in",
          "不在":"not in",
          # while loop
          "当":"while",
          "跳出":"break",
          "中断":"break",
          # try
          "尝试":"try",
          "异常":"except",
          "最后":"finally",
          "宣告":"assert",
          # build in methods
          "执行":"exec",
          "函数":"lambda",
          "打印":"print",
          "伴隨":"with",
          "产生":"yield",
          "刪除":"del",
         }


class cn_buildin_method(ZhpyPlugin):
    """
    python cn methods
    """
    title = "内部函数"
    description = "Python 内部函数"
    keyword = {
          "输入":"raw_input",
          # build-in types
          "字符串":"str",
          "布尔":"bool",
          "列表": "list",
          "字典":"dict",
          "数组":"tuple",
          "集合":"set",
          "符号":"chr",
          "符号转整数":"ord",
          "文件":"file",
          # number methods
          "整数":"int",
          "浮点数":"float",
          "复数":"complex",
          "十六进制":"hex",
          "绝对值":"abs",
          "比较":"cmp",
          "最大":"max",
          "最小":"min",
          # string methods
          "开头为":"startswith",
          "结尾为":"endswith",
          "连接":"join",
          "分离":"split",
          "编码":"encoding",
          "解码":"decoding",
          # list methods
          "加入":"append",
          "追加":"append",
          "扩展":"extend",
          "插入":"insert",
          "弹出":"pop",
          "下一笔":"next",
          "移除":"remove",
          "逆转":"reverse",
          "计数":"count",
          "索引":"index",
          "排序":"sort",
          # file methods
          "打开":"open",
          "读取":"read",
          "写入":"write",
          "读一行":"readline",
          "读多行":"readlines",
          "关闭":"close",
          # dict methods
          "关键字列表":"keys",
          "值列表":"values",
          "项目列表":"items",
          "更新":"update",
          # OO
          "可调用":"callable",
          "列出属性":"dir",
          "取属性":"getattr",
          "有属性":"hasattr",
          "设定属性":"setattr",
          # build in methods
          "列举":"enumerate",
          "求值":"eval",
          "过滤":"filter",
          "长度":"len",
          "映射":"map",
          "范围":"range",
          "快速范围":"xrange",
          "总和":"sum",
          "类型":"type",
          "打包":"zip",
          "帮助":"help",
          "说明":"help",
         }


class cn_exception(ZhpyPlugin):
    """
    python cn exceptions
    """
    title = "例外"
    description = "Python 内建例外关键词"
    keyword = {
          "例外":"Exception",
          # error
          "停止迭代":"StopIteration",
          "类型错误":"TypeError",
          "解码错误":"UnicodeDecodeError",
          "导入错误":"ImportError",
         }


class cn_zhpy(ZhpyPlugin):
    """
    zhpy cn keyword plugin
    """
    title = "周蟒"
    description = "周蟒内建关键词"
    keyword = {
          "周蟒":"zhpy",
          "主程序":'if __name__=="__main__"',
          # must do 'from zhpy import zh_exec'/'从 周蟒 导入 中文执行' first
          "中文执行":"zh_exec",
          # logic
          "等于":"==",
          "不等于":"!=",
         }

def revert_dict(lang_dict):
    """make a reverse dictionary from the input dictionary
    
    >>> revert_dict({'a':'1', 'b':'2'})
    {'1': 'a', '2': 'b'}
    """
    rev_dict = {}
    dict_keys = lang_dict.keys()
    dict_keys.reverse()
    #map(rev_dict.update, map(lambda i: {lang_dict[i]:i}, dict_keys))
    for i in dict_keys:
        rev_dict.update({lang_dict[i]:i})
    return rev_dict
