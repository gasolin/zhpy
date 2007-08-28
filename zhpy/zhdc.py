# -*- coding: utf-8 -*-
"""
Chinese keyword dictionaries
"""

# Traditional chinese keywords
twdict = {# io
          "印出":"print",
          "輸入":"raw_input",
          # def
          "定義":"def",
          "類別":"class",
          # global
          "共用":"global",
          # import
          "從":"from",
          "導入":"import",
          "作為":"as",
          # flow
          "返回":"return",
          "傳回":"return",
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
          "下一筆":"next",
          # while loop
          "當":"while",
          "跳出":"break",
          "中止":"break",
          "例外":"Exception",
          # try
          "嘗試":"try",
          "異常":"except",
          "最後":"finally",
          # else
          "宣告":"assert",
          "刪除":"del",
          "執行":"exec",
          "方程式":"lambda",
          "產生":"yield",
          "伴隨":"with",
          # logic
          "等於":"==",
          "不等於":"!=",
          "是":"is",
          "為":"is",
          "不是":"is not",
          "或":"or",
          "和":"and",
          "且":"and",
          "真":"True",
          "假":"False",
          "實":"True",
          "虛":"False",
          "空":"None",
          # build in methods
          "型別":"type",
          "長度":"len",
          "執行":"exec",
          # build-in types
          "字串":"str",
          "布林":"bool",
          "列表": "list",
          "字典":"dict",
          "數組":"tuple",
          "集合":"set",
          # number methods
          "整數":"int",
          "浮點數":"float",
          "絕對值":"abs",
          # file methods
          "打開":"open",
          "讀取":"read",
          "寫入":"write",
          "讀一行":"readline",
          "讀多行":"readlines",
          "關閉":"close",
          # list methods
          "加入":"append",
          "追加":"append",
          "擴展":"extend",
          "插入":"insert",
          "彈出":"pop",
          "移除":"remove",
          "排序":"sort",
          # string methods
          "開頭為":"startswith",
          "結尾為":"endswith",
          "連接":"join",
          "分離":"split",
          # dict methods
          "關鍵字列表":"keys",
          "值列表":"values",
          "項目列表": "items",
          "更新":"update",
          # encoding
          "編碼":"encoding",
          "解碼":"decoding",
          # preloaded modules
          "範圍":"range",
          "列舉":"enumerate",
          "過濾":"filter",
          "打包":"zip",
          # error
          "停止迭代":"StopIteration",
          "型別錯誤":"TypeError",
          }

# Simplized chinese keywords
cndict = {# io
          "打印":"print",
          "输入字符串":"raw_input",
          # def
          "定义":"def",
          "类":"class",
          # global
          "共用":"global",
          "全局":"global",
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
          "否则如果":"elif",
          "否则":"else",
          # for loop
          "取":"for",
          "在":"in",
          "自":"in",
          "不在":"not in",
          "下一笔":"next",
          # while loop
          "当":"while",
          "跳出":"break",
          "中断":"break",
          # try
          "尝试":"try",
          "异常":"except",
          "最后":"finally",
          "例外":"Exception",
          # else
          "宣告":"assert",
          "刪除":"del",
          "执行":"exec",
          "函数":"lambda",
          "产生":"yield",
          "伴隨":"with",
          # logic
          "等于":"==",
          "不等于":"!=",
          "是":"is",
          "不是":"is not",
          "或者":"or",
          "并且":"and",
          "真": "True",
          "假":"False",
          "实":"True",
          "虛":"False",
          "空":"None", 
          # build in methods
          "类型":"type",
          "长度":"len",
          "执行":"exec",
          # build-in types
          "字符串":"str",
          "布尔":"bool",
          "列表": "list",
          "字典":"dict",
          "数组":"tuple",
          "集合":"set",
          # number methods
          "整数":"int",
          "小数":"float",
          "绝对值":"abs",
          # file methods
          "打开":"open",
          "读取":"read",
          "写入":"write",
          "读一行":"readline",
          "读多行":"readlines",
          "关闭":"close",
          # list methods
          "加入":"append",
          "追加":"append",
          "扩展":"extend",
          "插入":"insert",
          "弹出":"pop",
          "移除":"remove",
          "逆转":"reverse",
          "排序":"sort",
          # string methods
          "开头为":"startswith",
          "结尾为":"endswith",
          "连接":"join",
          "分离":"split",
          # dict methods
          "关键字列表":"keys",
          "值列表":"values",
          "项目列表":"items",
          "更新":"update",
          # encoding
          "编码":"encoding",
          "解码":"decoding",
          # preloaded modules
          "范围":"range",
          "列举":"enumerate",
          "过滤":"filter",
          "打包":"zip",
          # error
          "停止迭代":"StopIteration",
          "类型错误":"TypeError",
          }

# Traditional chinese and simplized chinese keywords
worddict = twdict.copy()
for i in cndict:
    if i in twdict:
        continue
    else:
        worddict[i]= cndict[i]

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

def _indict(lang_dict):
    """make a reverse dictionary from the input dictionary
    
    >>> _indict({'a':'1', 'b':'2'})
    {'1': 'a', '2': 'b'}
    """
    rev_dict = {}
    dict_keys = lang_dict.keys()
    dict_keys.reverse()
    #map(rev_dict.update, map(lambda i: {lang_dict[i]:i}, dict_keys))
    for i in dict_keys:
        rev_dict.update({lang_dict[i]:i})
    return rev_dict

# make reverse traditional chinese dicts
rev_twdict = _indict(twdict)
# make reverse simplified chinese dicts
rev_cndict = _indict(cndict)