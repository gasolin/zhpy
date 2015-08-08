# 嵌入 Python 程式中執行 : zh\_exec #

zhpy (>0.5 版) 提供一個在 Python 程式中嵌入中文程式執行的函式 "zh\_exec", 可以用如同 python exec 函式的用法使用:

```
$ python
>>> import zhpy
>>> zhpy.zh_exec("print 'hello'")
hello
>>> zhpy.zh_exec("印出 '哈囉'")
哈囉
>>> 
```