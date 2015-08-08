周蟒是針對華文地區，以簡化程式教學為主要目的的 Python 程式語言方言。周蟒中文程式語言是目前唯一有多位開發者、持續更新版本、並提供電子書、API、完整測試用例的開放原始碼中文程式語言。

Update: zhpy is not maintained, please try blockly https://blockly-demo.appspot.com/static/apps/code/index.html?lang=zh-hans

ZHPY 已不再維護，對周蟒概念感興趣的使用者請參考 Blockly https://blockly-demo.appspot.com/static/apps/code/index.html?lang=zh-hant

```
新手在程式莊園外徘徊。

門房跟新手說：
「你要先買一本導覽手冊，我才準許你進來」。

新手遞出了金幣，門房交給新手一本程式語言導覽手冊。


新手在程式殿堂外徘徊。

門口的警衛跟新手說：
「你要能使用英語溝通，我才准許你進來」。

新手學懂了英語回來，門口的警衛終於打開了門。

程式的殿堂裡面，不出所料，

果然已擠滿了外國人。
```
如何了解周蟒程式語言?

**如果想從頭學起，你可以
# 閱讀 [咬一口 Python (周蟒) 程式語言電子書](ByteOfZhpy.md) #**

**如果要快速上手，你可以照著做 [安裝使用周蟒](DownloadInstall.md)。**

**如果你已經學過 Python 程式語言，你可以對照 Python 語法，
# 查看 [快速語法參考手冊](QuickRef.md) #**

## 關於 ##
  * [關於周蟒](AboutZhpy.md)
  * [編程風格](CodingStyle.md)

&lt;wiki:gadget url="http://www.ohloh.net/p/zhpy/widgets/project\_languages.xml" width="340" height="200" border="1" /&gt;

---


## About ZHPY ##

zhpy (pronounce as 'zippy' or 'Z-H-pi') is the full feature python language with
fully tested chinese keywords, variables, and parameters support,
independent on python version,
bundle with command line tool, interpreter, pluggable keyword system and
great document.

zhpy on python is good for Taiwan and China beginners to
learn python in their native language.

The core of zhpy is a lightweight python module and a chinese source convertor
based on python,
which provides interpreter and command line tool to translate zhpy code to
python. zhpy integrated a setuptools-based plugin system for keyword reuse.
The zhpy code written in traditional and simplified
chinese could be translated and converted to natual python code.
Thus it could be execute as nature python code and be used in normal
python programs.

Use 'zhpy' command instead of "python" in command line to execute source code wrote in Chinese and English.

zhpy provide a method 'zh\_exec' that allow to embed
chinese script in python, zhpy could be used as the chinese script in
shell as well.

zhpy use **pyparsing** module to detect chinese **keywords, class name, methods, arguments, variables** and translate them back to python.
I'd recommand developers to reuse zhpy architecture for python on korean or
python on japenese.

Check the BasicUsageEn to glance zhpy examples.