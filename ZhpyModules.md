# 簡介 #

你已經瞭解如何在程式中定義函式來重用程式碼。那麼如果你想要在其他程式中重用許多函式時該如何編寫呢？
是的，解答就是使用模組。模組基本上是一個包含了所有你定義的函式和變量的檔案。
為了在其他程式/模組中重用模組，我們可以"導入" (import) 整個模組或一部分的模組，並重用模組中提供的函式。

模組也是名稱空間之一 -- 在模組中定義的函式和變量只存在於該模組中 (即在名稱空間中)。

模組必須以 .py 為副檔名， 才能導入其他 Python 模組。

首先，我們將學習如何使用標準庫中的模組:
```
#!/usr/bin/env zhpy
# 檔名: using_sys.py
導入 系統
印出 '命令行參數有:'
取 i 自 系統.參數:
    印出 i
印出 '\nPYTHON 路徑有', 系統.路徑
```

輸出結果:
```
$ zhpy using_sys.py we are arguments
命令行參數有:
using_sys.py
we
are
arguments
PYTHON 路徑有 ['/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4'，
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/plat-darwin'，
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/plat-mac'，
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/plat-mac/lib-scriptpackages'，
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/lib-tk'，
'/opt/local/lib/python2.4/lib-dynload'，
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/site-packages'，
'/opt/local/lib/python2.4/site-packages'，
'/Users/swaroopch/Library/Python/2.4/site-packages']
```


---


python 版:
```
#!/usr/bin/env python
# File name: using_sys.py
import sys
print 'The command line arguments are:'
for i in sys.argv:
    print i
print '\nThe PYTHONPATH is', sys.path
```

python 版輸出結果:
```
$ python using_sys.py we are arguments
The command line arguments are:
using_sys.py
we
are
arguments
The PYTHONPATH is ['/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4',
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/plat-darwin',
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/plat-mac',
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/plat-mac/lib-scriptpackages',
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/lib-tk',
'/opt/local/lib/python2.4/lib-dynload',
'/opt/local/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/site-packages',
'/opt/local/lib/python2.4/site-packages',
'/Users/swaroopch/Library/Python/2.4/site-packages']
```


---


### 程式如何運作 ###

首先，我們利用"導入"(import) 語句導入"系統"(sys) 模組。基本上，這語句通知了周蟒直譯器我們想要使用這個模組。
我們透過"導入"(import) 語句將這個名稱帶入了我們的程式中，故此我們可以在程式裡使用這個模組。
sys 模組包含了與周蟒直譯器和它的環境有關的函數。 "sys" 是 "system (系統)" 的簡稱。

當周蟒執行
`導入 系統`
語句的時候，周蟒直譯器會在"系統.路徑"(sys.path) 變量列出的目錄中尋找對應的模組。
如果找到了這個模組或資料夾，這個"系統" (sys) 模組主要區塊中的語句將被運行，而後我們就可以在程式中使用這個模組。
注意，初始化過程僅在我們第一次輸入模組時進行。連續導入同樣的模組並不會發生任何事情。

"系統"(sys) 模組中的"參數"(argv) 變量通過使用點號標示 —
"系統.參數"(sys.argv) 通知周蟒直譯器我們想使用定義在"系統"(sys) 模組中的"參數"(argv)  變量。
這種方法的優勢是這個名稱不會與任何你的程式中已經定義的 "參數"(argv)  變量衝突。
而且，它也清晰地表明了這個名稱是 "系統"(sys) 模組名稱空間的一部分。

"系統.參數"(sys.argv) 變量是一個字串列表（列表會在後面的章節詳細解釋）。
準確地說，"系統.參數"(sys.argv)是命令行參數(即使用命令行傳遞到程式中的參數)的列表。

如果你使用 IDE 編寫運行這些程序，請在選單裡尋找一個指定程序的命令行參數的方法。
例如在 PythonWin IDE 中， 當你在選單上點擊 File → Run 後， 可以在參數 (Arguments) 對話框中加入文字。

這裡，當我們執行 `zhpy using_sys.py we are arguments` 的時候，
"系統.參數"(sys.argv) 列表裡就包含了程式本身名稱和我們提供的參數。
正運行程式的名稱總是 "系統.參數"(sys.argv) 列表中的第一個參數。
所以，在這個例子中，'using\_sys.py' 就是 "系統.參數[0](0.md)"(sys.argv)[0](0.md)) 的參數值、
而 'we'是 "系統.參數[1](1.md)"(sys.argv)[1](1.md)) 的參數值、'are' 是 "系統.參數[2](2.md)"(sys.argv)[2](2.md)) 的參數值，
以及 'arguments' 是 "系統.參數[3](3.md)"(sys.argv[3](3.md)) 的參數值。
注意，Python 和周蟒等大多數的程式語言相同，都是從 0 開始計數，而不是從 1 開始計數。

## 預編譯 .pyc 檔案 ##

導入模組是件相對比較費時的事情. 因此 python 直譯器用了一些技巧使得這個過程加快。
還記得我們曾討論過 python 直譯器將原始碼轉換成稱為位元碼的中介型式，再轉換成電腦的原生語言執行。
當你第一次導入這模組時，python 直譯器會將這些位元碼儲存成一個 .pyc 檔。
例如， 當你執行 `導入 mymodule` 的時候， 你會發現有個 mymodule.pyc 檔案出現在你編寫的 mymodule.py 模組旁。
下一次當你從任何程式導入這個模組的時候，python 直譯器會先取用編譯過的 .pyc 檔而不是原始的 .py 檔，因此導入的過程就加快了。
在 .py 模組被更新過後， python 直譯器也能夠聰明地自動重新建立 .pyc 檔。

這些位元編譯好的檔案是與平台無關的。而且假使 python 直譯器並沒有建立 .pyc 檔案的權限，
那麼python 直譯器就不會新建檔案，每次導入時都像模組第一次被導入時一樣地處理。

## 使用"從...導入"(from...import) 語句 ##

在前一個例子中， 如果你想要直接輸入"變數"(argv) 變量到你的模組/程式中，
好在每次使用"系統.參數"(sys.argv)時不需要打上這樣的全名。
那麼你該使用 "從 系統 導入 參數"(from sys import argv) 這語句。

如果你想要輸入所有"系統"(sys) 模塊使用的名稱，那麼你可以使用 "從 系統 導入 **"(from sys import**) 語句。
這語句對於所有模組都適用。

一般來說，應該避免使用"從...導入"(from...import) 語句，因為這樣使閱讀程式的讀者不容易察知這名稱來自何模組，
也容易與當前模組中定義的名稱衝突。

## 模組的 name 屬性 ##

每個模組都有一個名稱，和一個能在模組中找出它的模組名稱的功能。

這個功能在一個特殊的情形下極為有用. 還記得當我們導入一個模組的時候，
這個模組主要區塊中的語句都將被運行，而這個名稱就已導入到我們的模組(名稱空間)中。
那麼如果我們只想在程式本身被使用的時候運行主要區塊，而在它被別的模塊輸入的時候就不運行主要區塊的話，我們該怎麼做呢？
這樣的情況就可以通過模組的 name 屬性來達成:
```
#!/usr/bin/env zhpy
# 檔名: name.py
如果 __name__ == '__main__':
    印出 '程式正自行運行.'
    印出 '我可以在此加入其他動作.'
否則:
    印出 '我正被導入其他模組.'
```

也能寫成:

```
#!/usr/bin/env zhpy
# 檔名: name.py
主程式:
    印出 '程式正自行運行.'
    印出 '我可以在此加入其他動作.'
否則:
    印出 '我正被導入其他模組.'
```

輸出結果:
```
$ zhpy name.py
程式正自行運行.
我可以在此加入其他動作.

$ zhpy
>>> 導入 name
我正被導入其他模組.
```


---


python 版:
```
#!/usr/bin/env python
# File name: name.py
if __name__ == '__main__':
    print 'This program is being run by itself.'
    print 'I can do other stuff here.'
else:
    print 'I am being imported from another module.'
```

python 版輸出結果:
```
$ python name.py
This program is being run by itself.
I can do other stuff here.

$ python
>>> import name
I am being imported from another module.
```


---


### 程式如何運作 ###

每個 Python 模組都有它的 name 屬性，如果這個屬性是設定為 'main' 這個值的時候，表示使用者是單獨運行這個模組。
對此我們可以進行相應的動作。屬性不為 'main' 的情況則表示這個模組是被其他模組導入的狀況。

為了方便使用，周蟒提供"主程式"(if name == 'main')這個關鍵詞，以增進中文程式的可讀性。

## 編寫自己的模組 ##

建立自己的模組是件相當容易的事，其實你也一直在這麼做！怎麼說呢? 其實每個 Python 和周蟒程式都可視作一個個模組。
你只需確保這個程式使用了 .py 作為副檔名:
```
#!/usr/bin/env zhpy
# 檔名: mymodule.twpy
定義 說嗨():
    印出 '嗨，我是', __name__
版本 = '0.1'
# mymodule.py 的結尾
```

python 版:
```
#!/usr/bin/env python
# File name: mymodule.py
def sayhi():
    print 'Hi, this is', __name__, 'speaking'
version = '0.1'
# End of mymodule.py
```

上面是一個模組的簡單例子。如你所見，這例子與我們一般編寫的周蟒程式相比並沒有什麼特別之處。
我們接下來將看看如何在其他的周蟒程式中使用這個模組。

請記得模組必須被放置在"系統.路徑"(sys.path) 列表中的目錄之一，如此一來周蟒直譯器才能知道從何取得這個模組。
因為當前的目錄也會存在於"系統.路徑"(sys.path) 列表中，
所以最簡單使用模組的方法是將 mymodule.py 和使用到這個模組的程式放在同一個目錄中。
如此周蟒直譯器也能得知從何取得這個模組:
```
#!/usr/bin/env zhpy
# 檔名: mymodule_demo.twpy
導入 mymodule
mymodule.說嗨()
印出 '版本', mymodule.版本
# mymodule_demo.py 的結尾
```

也可以寫成
```
#!/usr/bin/env zhpy
# 檔名: mymodule_demo.twpy
導入 mymodule 作為 我的模組
我的模組.說嗨()
印出 '版本', 我的模組.版本
# mymodule_demo.py 的結尾
```

輸出結果:
```
$ zhpy mymodule_demo.py
嗨，我是 mymodule
版本 0.1
```


---


python 版:
```
#!/usr/bin/env python
# File name: mymodule_demo.py
import mymodule
mymodule.sayhi()
print 'Version', mymodule.version
# End of mymodule_demo.py
```

python 版輸出結果:
```
$ python mymodule_demo.py
Hi, this is mymodule speaking
Version 0.1
```


---


### 程式如何運作 ###

當我們導入 mymodule 模組時， 周蟒直譯器從相同的目錄中找到對應的模組，
運行模組主要區塊並將 mymodule 這個名稱帶入我們程式的名稱空間中。

接著， 我們使用點號標示法來使用模組的成員。我們稱這種方法作 "屬性存取"。

你也可以透過 "導入 .. 作為"(import..as) 這種語法將導入的模組重新命名，
以我們命名的名稱將這個模組帶入我們程式的名稱空間中。

你也該注意到特殊變量 name 的使用方法。

這裡舉出一個運用"從..導入"(from..import) 語法的版本:
```
#!/usr/bin/env zhpy
# 檔名: mymodule_demo2.py
從 mymodule 導入 說嗨, 版本
# 可用以下語法替代: 從 mymodule 導入 *
說嗨()
印出 '版本', 版本
# mymodule_demo2.py 的結尾
```

python 版:
```
#!/usr/bin/env python
# File name: mymodule_demo2.py
from mymodule import sayhi, version
# Alternative: from mymodule import *
sayhi()
print 'Version', version
# End of mymodule_demo2.py
```

上面這個程式的輸出與前一個範例的輸出完全相同。

## 列出屬性(dir) 函式 ##

內建的"列出屬性"(dir) 函式可以用來列出模組中定義過的識別符號。這邊所指的識別符號指的是定義在模組中的函式、類型和變量。

當你為"列出屬性"(dir) 提供一個模組名稱的時候，它會返回模組中定義過名稱的列表。
如果不額外提供參數的話，它會返回當前模組中所定義過名稱的列表。

實際上不僅在模組中， 我們可以在任何周蟒物件上使用"列出屬性"(dir) 函式:
```
$ zhpy
>>> 導入 mymodule
>>> 列出屬性(mymodule)
['__builtins__'， '__doc__'， '__file__'， '__name__'， 'sayhi'， 'version']
>>>
>>> 列出屬性()
['__builtins__'， '__doc__'， '__name__'， 'mymodule']
>>> a = 5
>>> 列出屬性()
['__builtins__'， '__doc__'， '__name__'， 'a'， 'mymodule']
>>> 刪除 a
>>> 列出屬性()
['__builtins__'， '__doc__'， '__name__'， 'mymodule']
```

python 版:
```
$ python
>>> import mymodule
>>> dir(mymodule)
['__builtins__', '__doc__', '__file__', '__name__', 'sayhi', 'version']
>>>
>>> dir()
['__builtins__', '__doc__', '__name__', 'mymodule']
>>> a = 5
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'mymodule']
>>> del a
>>> dir()
['__builtins__', '__doc__', '__name__', 'mymodule']
```

### 程式如何運作 ###

首先，我們來看一下在導入的模組上使用 "列出屬性"(dir) 函式的情況。我們可以看到一個包含所有 mymodule 模組的屬性列表。

接下來，我們不傳任何參數到 "列出屬性"(dir) 函式中， 這種預設情況下，它返回了當前模組屬性的列表。
注意，輸入的模組同樣屬於列表的一部分。

為了觀察 "列出屬性"(dir) 函式的功用，我們定義一個新的變量 a 並且賦一個值給它，
並檢驗 "列出屬性"(dir) 命令的輸出，結果我們觀察到在列表中也加入了 a 的值。
接著我們使用 "刪除"(del) 語句來取消定義當前模塊中的這名稱，我們觀察到 "列出屬性"(dir) 的列表中不再包含 a 的值。

"刪除"(del) 語句是用來從當前模組的名稱空間中刪除一個變量/名稱。在"刪除"(del)  語句運行過後，
你將無法再使用變量/名稱 a——如同這個變量從未存在過一樣。

# 結語 #

模組相當有用， 它們可以幫助我們將服務與功能集中在一個可以重用的程式裡。

Python 附帶的標準函式庫就是這樣的模組集合的例子。

我們已經學習了如何使用這些模組以及如何建立我們自己的模組。

接下來，我們將學習一些關於資料結構的概念。

[函式](ZhpyFunctions.md) | [資料結構](DataStructure.md)


