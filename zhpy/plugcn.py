#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Simplified Chinese keyword dictionaries

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
          "真": "True",
          "假":"False",
          "实":"True",
          "虛":"False",
          "空":"None",
          # def
          "定义":"def",
          "类":"class",
          "我":"self",
          "自个儿":"self",
          "共用":"global",
          "全域":"global",
          # import
          "从":"from",
          "导入":"import",
          "作为":"as",
          # flow
          "返回":"return",
          "略过":"pass",
          "引发":"raise",
          "继续":"continue",
          # control
          "如果":"if",
          "假使":"elif",
          "否则如果":"elif",
          "否则":"else",
          # for loop
          "取":"for",
          "自":"in",
          "在":"in",
          "不在":"not in",
          # while loop
          "当":"while",
          "跳出":"break",
          "中断":"break",
          # try
          "尝试":"try",
          "异常":"except",
          "最后":"finally",
          "申明":"assert",
          # build in methods
          "执行":"exec",
          "函数":"lambda",
          "打印":"print",
          "伴隨":"with",
          "产生":"yield",
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
          "元组":"tuple",
          "集合":"set",
          "定集合":"frozenset",
          "符号":"chr",
          "符号转整数":"ord",
          "档案":"file",
          # number methods
          "整数":"int",
          "浮点数":"float",
          "复数":"complex",
          "十六进制":"hex",
          "绝对值":"abs",
          "比较":"cmp",
          # string methods
          "开头为":"startswith",
          "结尾为":"endswith",
          "连接":"join",
          "分离":"split",
          "代换":"replace",
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
          "反转":"reverse",
          "计数":"count",
          "索引":"index",
          "排序":"sort",
          # dict methods
          "键列表":"keys",
          "值列表":"values",
          "项目列表":"items",
          "更新":"update",
          "拷贝":"copy",
          # set methods
          "清除":"clear",
          "加":"add",
          "丢弃":"discard",
          "联集":"union",
          "交集":"intersection",
          "差集":"difference",
          "对称差集":"symmetric_difference",
          # file methods
          "打开":"open",
          "读取":"read",
          "写入":"write",
          "读一行":"readline",
          "读多行":"readlines",
          "关闭":"close",
          # OO
          "可调用":"callable",
          "列出属性":"dir",
          "取属性":"getattr",
          "有属性":"hasattr",
          "设定属性":"setattr",
          "属性":"property",
          # build in functions
          "长度":"len",
          "最大值":"max",
          "最小值":"min",
          # build in methods
          "列举":"enumerate",
          "评估":"eval",
          "过滤":"filter",
          "映射":"map",
          "范围":"range",
          "快速范围":"xrange",
          "总和":"sum",
          "类型":"type",
          "对象":"object",
          "打包":"zip",
          "帮助":"help",
          "说明":"help",
          "区域变量":"locals",
          "全域变量":"globals",
          "类方法":"classmethod",
          }


class cn_exception(ZhpyPlugin):
    """
    python cn exceptions
    """
    title = "例外"
    description = "Python 内建例外关键词"
    keyword = {
          "例外":"Exception",
          "错误":"Error",
          # error
          "运算错误":"ArithmeticError",
          "申明错误":"AssertionError",
          "属性错误":"AttributeError",
          "相容性警示":"DeprecationWarning",
          "空值错误":"EOFError",
          "环境错误":"EnvironmentError",
          "浮点数错误":"FloatingPointError",
          "输出入错误":"IOError",
          "导入错误":"ImportError",
          "缩排错误":"IndentationError",
          "索引错误":"IndexError",
          "键错误":"KeyError",
          "键盘中断":"KeyboardInterrupt",
          "查找错误":"LookupError",
          "内存错误":"MemoryError",
          "名称错误":"NameError",
          "尚未实作":"NotImplemented",
          "尚未实作错误":"NotImplementedError",
          "操作系统错误":"OSError",
          "溢值错误":"OverflowError",
          "溢值警告":"OverflowWarning",
          "引用错误":"ReferenceError",
          "运行期错误":"RuntimeError",
          "运行期警告":"RuntimeWarning",
          "标准错误":"StandardError",
          "停止迭代":"StopIteration",
          "语法错误":"SyntaxError",
          "语法警告":"SyntaxWarning",
          "系统错误":"SystemError",
          "系统结束":"SystemExit",
          "型别错误":"TypeError",
          "跳格错误":"TabError",
          "未绑定区域参数错误":"UnboundLocalError",
          "万国码解码错误":"UnicodeError",
          "自订警告":"UserWarning",
          "值错误":"ValueError",
          "警告":"Warning",
          "Windows错误":"WindowsError",
          "除零错误":"ZeroDivisionError",
          "解码错误":"UnicodeDecodeError",
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
          "非": "not",
          "是":"is",
          "为":"is",
          "不是":"is not",
          "不为":"is not",
          # private
          "文件":"doc",
          "初始化":"init",
          "刪除":"del",
          "描述":"repr",
          "测试":"test",
          }

#enter simplified chinese dict here
class cn_sys(ZhpyPlugin):
    """
    zhpy sys module simplified chinese plugin
    """
    title = "系统"
    description = "系统模块"
    keyword = {"系统":"sys",
               "版本":"version",
               "参数":"argv",
               "结束":"exit",
               "取得档案系统编码":"getfilesystemencoding",
               "模块列表":"modules",
               "平台":"platform",
               "标准错误":"stderr",
               "标准输入":"stdin",
               "标准输出":"stdout",
               # sys path with list methods
               "路径":"path",
               }

class cn_traceback(ZhpyPlugin):
    """
    zhpy traceback simplified chinese plugin
    """
    title = "系统"
    description = "系统模组"
    keyword = {"未定义":"is not defined",
               "名称":"name",
               "行":"line",
               "档案":"File",
               "不合法的":"invalid",
               "语法":"syntax",
               }

#    [zhpy.cndict]
cnkeyword = cn_keyword()
cnmethod = cn_buildin_method()
cnexception = cn_exception()
cnzhpy= cn_zhpy()
cnsys = cn_sys()
cntrace = cn_traceback()

tools = [cnkeyword, cnmethod, cnexception, cnzhpy, cnsys]
trace = [cnkeyword, cnmethod, cnexception, cntrace, cnsys]