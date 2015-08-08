
```
與其將時間浪費在質疑中文編程可不可行上，不如自己動手試試看，做了總比不做好。
```

以下是周蟒作者們想到如何協助周蟒專案，讓周蟒更有用的一些方式，要記得，幫助周蟒的同時，你也幫助自己獲得了一個好用的工具。

參與開源開發不僅僅是擁有電腦/計算機技術的朋友的專利，普通使用者也可以以各種方式成為其中的一個分子：您可以幫助編寫文檔，提供用戶反饋，共享使用當中的技巧，或者在您的朋友當中推廣Python和周蟒。

# 關鍵字改善 #

想要簡單地參與繁簡中詞典的改進，只要將 "繁簡中關鍵字: 英文關鍵字" 的對應發到改進繁簡中支援的 issue 中即可

http://code.google.com/p/zhpy/issues/detail?id=4

要測試繁簡中文支援很容易:

只要幫忙補完這 test suite 對應的繁簡中文 test case 即可:

http://zhpy.googlecode.com/svn/trunk/tests/

# 程式改善 #

## 提供建議 ##

您可以在 [issues](http://code.google.com/p/zhpy/issues/list) 加入您對 zhpy 的建議。
或前往[台灣](http://groups.google.com/group/pythontw), [中國](http://groups.google.com/group/python-cn) python 群組討論。

## 提供修補檔 ##

1. 首先您要能透過 svn 取得[原始碼](http://code.google.com/p/zhpy/source)。
2. 修改程式, 提交 patch 到 [issues](http://code.google.com/p/zhpy/issues/list)。


## 測試 ##

發佈時需通過所有測試

通過單元測試 (unittest) 與文件測試 (doctest)

```
$ nosetests --with-doctest
```

通過命令行測試跟範例測試

```
$ cd example
$ ./test_example.sh
```