#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Traditional Chinese keyword dictionaries

This is the MIT license:
http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2007~ Fred Lin and contributors. zhpy is a trademark of Fred Lin.

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


from zhdc import ZhpyPlugin

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
          "真":"True",
          "假":"False",
          "實":"True",
          "虛":"False",
          "空":"None",
          # def
          "定義":"def",
          "類別":"class",
          "我":"self",
          "共用":"global",
          "全域":"global",
          # import
          "從":"from",
          "導入":"import",
          "作為":"as",
          # flow
          "返回":"return",
          "略過":"pass",
          "引發":"raise",
          "繼續":"continue",
          # control
          "如果":"if",
          "假使":"elif",
          "否則如果":"elif",
          "否則":"else",
          # for loop
          "取":"for",
          "自":"in",
          "在":"in",
          "不在":"not in",
          # while loop
          "當":"while",
          "跳出":"break",
          "中斷":"break",
          # try
          "嘗試":"try",
          "異常":"except",
          "最後":"finally",
          "申明":"assert",
          # build in methods
          "執行":"exec",
          "方程式":"lambda",
          "印出":"print",
          "伴隨":"with",
          "產生":"yield",
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
          "元組":"tuple",
          "集合":"set",
          "定集合":"frozenset",
          "符號":"chr",
          "符號轉整數":"ord",
          "檔案":"file",
          # number methods
          "整數":"int",
          "浮點數":"float",
          "複數":"complex",
          "十六進位":"hex",
          "絕對值":"abs",
          "比較":"cmp",
          # string methods
          "開頭為":"startswith",
          "結尾為":"endswith",
          "連接":"join",
          "分離":"split",
          "代換":"replace",
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
          "反轉":"reverse",
          "計數":"count",
          "索引":"index",
          "排序":"sort",
          # dict methods
          "鍵列表":"keys",
          "值列表":"values",
          "項目列表": "items",
          "更新":"update",
          "複製":"copy",
          # set methods
          "清除":"clear",
          "加":"add",
          "丟棄":"discard",
          "聯集":"union",
          "交集":"intersection",
          "差集":"difference",
          "對稱差集":"symmetric_difference",
          # file methods
          "打開":"open",
          "讀取":"read",
          "寫入":"write",
          "讀一行":"readline",
          "讀多行":"readlines",
          "關閉":"close",
          # OO
          "可調用":"callable",
          "列出屬性":"dir",
          "取屬性":"getattr",
          "有屬性":"hasattr",
          "設定屬性":"setattr",
          "屬性":"property",
          # build in functions
          "長度":"len",
          "最大值":"max",
          "最小值":"min",
          # build in methods
          "列舉":"enumerate",
          "評估":"eval",
          "過濾":"filter",
          "映射":"map",
          "範圍":"range",
          "快速範圍":"xrange",
          "總和":"sum",
          "型別":"type",
          "物件":"object",
          "打包":"zip",
          "說明":"help",
          "幫助":"help",
          "區域變量":"locals",
          "全域變量":"globals",
          "類別方法":"classmethod",
          }


class tw_exception(ZhpyPlugin):
    """
    python tw exceptions
    """
    title = "例外"
    description = "Python 內建例外關鍵詞"
    keyword = {
          "例外":"Exception",
          "錯誤":"Error",
          # error
          "運算錯誤":"ArithmeticError",
          "申明錯誤":"AssertionError",
          "屬性錯誤":"AttributeError",
          "相容性警示":"DeprecationWarning",
          "空值錯誤":"EOFError",
          "環境錯誤":"EnvironmentError",
          "浮點數錯誤":"FloatingPointError",
          "輸出入錯誤":"IOError",
          "導入錯誤":"ImportError",
          "縮排錯誤":"IndentationError",
          "索引錯誤":"IndexError",
          "鍵錯誤":"KeyError",
          "鍵盤中斷":"KeyboardInterrupt",
          "查找錯誤":"LookupError",
          "記憶體錯誤":"MemoryError",
          "名稱錯誤":"NameError",
          "尚未實作":"NotImplemented",
          "尚未實作錯誤":"NotImplementedError",
          "作業系統錯誤":"OSError",
          "溢值錯誤":"OverflowError",
          "溢值警告":"OverflowWarning",
          "引用錯誤":"ReferenceError",
          "運行期錯誤":"RuntimeError",
          "運行期警告":"RuntimeWarning",
          "標準錯誤":"StandardError",
          "停止迭代":"StopIteration",
          "語法錯誤":"SyntaxError",
          "語法警告":"SyntaxWarning",
          "系統錯誤":"SystemError",
          "系統結束":"SystemExit",
          "型別錯誤":"TypeError",
          "跳格錯誤":"TabError",
          "未綁定區域變量錯誤":"UnboundLocalError",
          "萬國碼解碼錯誤":"UnicodeError",
          "自訂警告":"UserWarning",
          "值錯誤":"ValueError",
          "警告":"Warning",
          "Windows錯誤":"WindowsError",
          "除零錯誤":"ZeroDivisionError",
          "解碼錯誤":"UnicodeDecodeError",
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
          "非":"not",
          "是":"is",
          "為":"is",
          "不是":"is not",
          "不為":"is not",
          # private
          "文件":"doc",
          "初始化":"init",
          "刪除":"del",
          "描述":"repr",
          "測試":"test",
          }

#enter traditional chinese dict here
class tw_sys(ZhpyPlugin):
    """
    zhpy sys module traditional chinese plugin
    """
    title = "系統"
    description = "系統模組"
    keyword = {"系統":"sys",
               "版本":"version",
               "參數":"argv",
               "結束":"exit",
               "取得檔案系統編碼":"getfilesystemencoding",
               "模組列表":"modules",
               "平台":"platform",
               "標準錯誤":"stderr",
               "標準輸入":"stdin",
               "標準輸出":"stdout",
               # sys path with list methods
               "路徑":"path",
               }

class tw_traceback(ZhpyPlugin):
    """
    zhpy traceback traditional chinese plugin
    """
    title = "系統"
    description = "系統模組"
    keyword = {"未定義":"is not defined",
               "名稱":"name",
               "行":"line",
               "檔案":"File",
               "不合法的":"invalid",
               "語法":"syntax",
               }

#    [zhpy.twdict]
twkeyword = tw_keyword()
twmethod = tw_buildin_method()
twexception = tw_exception()
twzhpy= tw_zhpy()
twsys = tw_sys()
twtrace = tw_traceback()

tools = [twkeyword, twmethod, twexception, twzhpy, twsys]
trace = [twkeyword, twmethod, twexception, twtrace, twsys]
