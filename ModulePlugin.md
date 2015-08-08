# 簡介 #

周蟒(>0.9)中實現了插件擴展功能, 可以透過定義進入點 (entrypoint) 來擴展周蟒的內建字典.
實現了容易安裝, 擴充, 使用的中文編程系統.

文中分兩部份講述如何使用擴充插件即如何製作新的擴充插件

# 為什麼要用中文擴充插件 #

周蟒要取用非內建關鍵詞的功能時, 其中一個方法是使用[外掛的 ini 字典檔](PlugKeywords.md).
沒有製作字典檔時, 就只能使用

```
$zhpy
>>> 導入 sys
```

這樣的語句。因為 sys 不是內建的關鍵詞。

我們希望隨時可以使用

```
$ zhpy
>>> 導入 系統
```

這樣的語句。 而不需要每次透過自訂 ini 字典檔來達成。

中文擴充插件就是為了解決這問題而產生。

# 怎麼使用擴充插件 #

## 1. 安裝擴充插件 ##

前往 [pypi](http://www.python.org/pypi) 找尋適當的周蟒的擴充插件,
使用 easy\_install 命令來安裝自己需求的擴充插件

```
 $ easy_install zh_模組名
```

例如 sys 模組:

```
$ easy_install zh_sys
```

## 2. 使用擴充插件 ##

周蟒會自動找到所有模組然後將字典嵌入 worddict 中,
使用者不用為此操心.

安裝好 zh\_sys 後就可以在 zhpy 中使用

```
$ zhpy
>>> 導入 系統
```

這樣的語句。

## 3. 取消擴充插件 ##

要取消解析一個庫, 只要使用同樣的 easy\_install 命令來反安裝擴充插件

```
 $ easy_install -m zh_pygame
```

setuptools 就會將模組從進入點 (entrypoint) 中移除.
要再取用時再運行 easy\_install 命令即可。

## 4. 查看擴充插件 ##

周蟒提供 -V/--info 命令選項來查看插件

```
$ zhpy --info
Complete zhpy Version Information

zhpy requires:

  * python 2.5.1
  * zhpy 0.9.2
  * chardet 1.0
  * pyparsing 1.4.7

zhpy extends:

Traditional Chinese Keywords 

  * twkeyword (zhpy 0.9.2)
  * twmethod (zhpy 0.9.2)
  * twexception (zhpy 0.9.2)
  * twzhpy (zhpy 0.9.2)

Simplified Chinese Keywords 

  * cnmethod (zhpy 0.9.2)
  * cnexception (zhpy 0.9.2)
  * cnzhpy (zhpy 0.9.2)
  * cnkeyword (zhpy 0.9.2)
```

命令會列出周蟒關聯的模組.
已安裝的插件會列在 Traditional Chinese Keywords(繁體中文關鍵詞)  和 Simplified Chinese Keywords(簡體中文關鍵詞) 下方。

# 怎麼製作中文擴充插件 #

周蟒還是個相當新的語言, 奇缺各 python 模組的中文擴充插件.
所幸周蟒的中文模組擴充插件相當容易製作.
只要掌握 python 字典型別與簡單的命令行用法, 不難做出屬於自己的插件.

在周蟒網站上可以下載[中文擴充插件範本](http://code.google.com/p/zhpy/downloads/list)(zhpy plugin sample template)，周蟒的原始壓縮檔中也提供了一個相同的 [zhpy\_ext 目錄](http://zhpy.googlecode.com/svn/trunk/zhpy_ext/)。
你可以透過範本來製作自己的插件。

以下製作中文擴充插件的步驟。

## 0. 下載範例 ##

我們以製作 sys 模組的中文插件為例。

首先到 zhpy 下載列表下載	zhpy plugin sample template

http://code.google.com/p/zhpy/downloads/list

下載完後將它解壓縮, 並將資料夾改名為 zh\_sys。

接著就可以進入資料夾繼續下面的步驟。

## 1. 創建一個字典 ##

首先建立一個空目錄, 在目錄中建立一個任意 .py 檔案. 範例中已經預先建立好一個名為 word.py 的檔案,
你可以在檔案中建立對應繁, 簡中文關鍵詞的關鍵詞字典.

```
#coding=utf-8

tw_keyword = {"系統":"sys", "版本":"version"}

cn_keyword = {"系統":"sys", "版本":"version"}

```

## 2 建立插件物件(對象) ##

在檔案中建立對應繁, 簡中文關鍵詞的關鍵詞字典物件.

```
from zhpy.zhdc import ZhpyPlugin

class tw_sys(ZhpyPlugin):
    """
    sys tw module
    """
    title = "模組"
    description = "敘述" 
    keyword = tw_keyword # 裝入上面定義的字典

class cn_sys(ZhpyPlugin):
    ....
```

## 3. 設定插件訊息 ##

3. 準備一個 setup.py 文件, 加入 [zhpy.twdict] 或 [zhpy.cndict] 字典的進入點
(entrypoint).

setup.py
```

entry_points = """
[zhpy.twdict]
twsys = zh_sys.word:tw_sys
[zhpy.cndict]
cnsys = zh_sys.word:cn_sys
"""

```

## 4. 開發使用 ##

至此你已經得到一個可用的插件. 你可以在目錄中運行
```
$ python setup.py install
```

來安裝它。 setuptools 會將你的插件目錄拷貝一份到 python 目錄下。

而一般在開發中則偏好使用
```
$ python setup.py develop
```

命令，這樣 setuptools 會在python 目錄中加入一條捷徑指到你的開發目錄下，
如此一來所有的改動就會即時反應到結果上。

## 5. 將擴充插件上傳到 pypi ##

開發到一階段了，
你可以使用 python setuptools 內建的功能將檔案封裝成 zip 檔，
上傳到 pypi 上讓大家能共享你製作的插件。

```
$ python setup.py register sdist --format=zip upload
```

**註釋:**

> 有釋出以周蟒撰寫的程式的需求時, 可以在 setup.py 中指定關聯模組

```
  install_requires = ["zh_sys >=1.0"]
```

> 這樣使用 easy\_install 命令安裝時就能一並安裝.