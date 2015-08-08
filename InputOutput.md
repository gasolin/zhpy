# 簡介 #

當你想使你的程式可以與使用者(也可以是你自己)互動時， 往往會碰上許多問題。
例如， 你可能會想要從使用者那邊取得一些輸入資料， 對這些資料做一些處理， 然後印出一些結果。
我們已經學過使用 "輸入"(raw\_input) 和 "印出"(print) 語句來分別處理輸入與輸出。
我們也可以使用 "字串"(str) 類別提供的諸多類別方法來處理輸入與輸出，例如使用 rjust 類別方法來取得一個指定寬度並向右對齊的字串。
詳情可以參考"說明(字串)"(help(str))。

另一個常用的輸入/輸出類型是處理檔案。建立、讀取和寫入檔案是許多程式必備的功能，我們將會在這章探索如何實現這些功能。

## 檔案 (Files) ##

你可以透過建立一個"檔案"(file) 類別的實體來開啟一個檔案，
並分別使用"檔案"(file) 類別中的"讀取"(read)、"寫入"(write) 類別方法來讀寫檔案。
當你完成檔案的處理之後，你必須"關閉"(close)這個檔案物件好讓周蟒與 Python 直譯器能清空暫存器並確保所有的資料都已寫入了磁碟:
```
#!/usr/bin/env zhpy
# 檔名: using_file.py
詩句 = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
檔 = 檔案('poem.txt', 'w') # 開啟檔案以寫入('w')
檔.寫入(詩句) # 將文字寫入檔案
檔.關閉() # 關閉檔案
檔 = 檔案('poem.txt') # if no mode is specified, 'r'ead mode is assumed by default
當 真:
    行 = 檔.讀一行()
    如果 長度(行) == 0: # zero length indicates end-of-file
        中斷
    印出 行, # 加上逗點符號以取消自動換行
f.關閉() # 關閉檔案
```

輸出結果:
```
$ zhpy using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!

$ cat poem.txt     # 'cat' 命令能將檔案內容印出到螢幕上
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```


---


python 版:
```
#!/usr/bin/env python
# File name: using_file.py
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
f = file('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file
f = file('poem.txt') # if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # zero length indicates end-of-file
        break
    print line, # notice comma to avoid automatic line breaks
f.close() # close the file
```

python 版輸出結果:
```
$ python using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!

$ cat poem.txt     # 'cat' prints the file to the screen
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```


---


### 程式如何運作 ###

我們使用檔案的方法是透過指定想打開的檔案的檔名和檔案模式， 建立檔案類別的實體來使用檔案。
檔案模式可以是讀取模式（'r'）、寫入模式（'w'）或追加模式（'a'）。
這三個是最基本的模式。還有許多其他模式，可以參考 help(file)。

首先我們用寫入模式打開檔案，然後使用"檔案"(file) 類別的"寫入"(write) 類別方法來寫入檔案，
最後我們用"關閉"(close) 類別方法來關閉這個檔案。
你可以透過開啟 poem.txt 檔案來確認檔案裡確實寫入了內容。
例子裡我使用了 Unix 系統中的 cat 命令來印出檔案裡的內容。你也可以在你的作業系統上使用類似的命令。

接著我們再一次開啟同一個檔案來讀取文件。我們並沒有指定檔案模式，因為預設模式即是使用讀取模式。

在"當"(while) 回圈裡我們使用"讀一行"(readline) 類別方法來讀取檔案的每一行。
"讀一行"(readline) 類別方法會返回包括行末換行符號的一個完整行字串。

直到"讀一行"(readline) 類別方法返回的字串是空的時候，即表示已經到達文件尾端了，於是我們停止迴圈。
我們將每一行印出到螢幕上，但是我們在"印出"(print) 語句後都加上一個逗號以取消"印出"(print) 語句自動換行的功能。
因為每個字串裡已經包含了換行符號作結尾.最後我們再用"關閉"(close) 類別方法來關閉這個檔案。

我們也可以將讀取檔案部份的程式簡寫如下:
```
$ zhpy
>>> 取 行 自 檔案('poem.txt'):
... 印出 行,
...
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
>>>
```

python 版:
```
$ python
>>> for line in file('poem.txt'):
... print line,
...
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
>>>
```

## Pickle 模組 ##

Pyhton 語言提供一個內建的 pickle 模組來幫助你將任何類型的周蟒和 Python 物件儲存到檔案裡，或將它完整無缺地取出來。
這稱為'持久地'(persistently)儲存物件。

Python 內建模組庫裡另外還有一個名為 cPickle 的模組功能和 pickle 模組完全相同。
只是 cPickle 模組是以 C 語言寫成， 因此運行速度更快。
你可以從中擇一使用。我們將兩個模組都稱作 pickle 模組:
```
#!/usr/bin/env zhpy
# 檔名: pickling.py
導入 cPickle 作為 pickle
# 或 導入 pickle
購物清單檔案 = 'shoplist.data' # 用來持久地儲存物件的檔案
購物清單 = ['蘋果', '芒果', '胡蘿蔔']
# 寫入檔案
f = 檔案(購物清單檔案, 'w')
pickle.dump(購物清單, f) # 將物件保存成檔案
f.關閉()
刪除 購物清單 # 從記憶體中移除購物清單物件
f = 檔案(購物清單檔案)
儲存清單 = pickle.load(f) # 轉換回 Python 物件
印出 儲存清單
```

輸出結果:
```
$ zhpy pickling.py
['蘋果', '芒果', '胡蘿蔔']
$ cat shoplist.data
(lp1
S'蘋果'
p2
aS'芒果'
p3
aS'胡蘿蔔'
p4
a.
```


---


python 版:
```
#!/usr/bin/env python
# File name: pickling.py
import cPickle as pickle
# OR import pickle
shoplist_file = 'shoplist.data' # the file where we will persistently store the object
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = file(shoplist_file, 'w')
pickle.dump(shoplist, f) # dump the object to a file
f.close()
del shoplist # remove the shoplist from memory
f = file(shoplist_file)
storedlist = pickle.load(f) # convert back to a Python object
print storedlist
```

python 版輸出結果:
```
$ python pickling.py
['apple', 'mango', 'carrot']
$ cat shoplist.data
(lp1
S'apple'
p2
aS'mango'
p3
aS'carrot'
p4
a.
```


---


### 程式如何運作 ###

我們使用"導入..作為"(import...as) 語法來為導入的模組提供一個別名。
這麼做讓我們能透過修改一行語句就簡單地使用具有相同類別方法和欄位的模組。
在這個例子中就是 cPickle 和 pickle 這兩個具有相同介面但具有不同背後運作機制的模組。

要在檔案中儲存物件，我們首先需要建立一個使用寫入模式的檔案物件，然後透過呼叫 pickle 模組的 dump 函式來將物件儲存到檔案裡。
這個過程在 Python 語言中稱為 pickling。 一般則稱作'序列化(serializing)'。

我們使用 pickle 模組的 load 函式來取回對象。這個函式能將以字串表示的物件轉換成 Python 物件。
這個過程稱為 'unpickling'。 一般也稱作 'unserializing'。

# 關於字串 #

## 使用三個雙引號 ##

你可以透過使用三個單引號或雙引號(‘’’ or """)來指定多行字串，如此一來你就可以使用在這個多行字串中自由使用單一的單引號或雙引號。

舉個例子:
```
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
```

## 跳出符號 (Escape Sequences) ##

你該怎麼指定一個含有單引號(')的字串呢? 例如 "What's your name?" 這個字串。你不能用 'What's your name?' 這樣的形式，
因為 Python 直譯器會無法辨識字串正確的開始和結束所以你需要特別指示那一個單引號不代表字串的結尾. 這可以透過跳出符號來達成。
你可以在單引號前加入一個反斜線來跳出原本單引號在 Python 語言中代表的意義。所以前面的例子可以寫成 'What's your name'。

另一個指定這個特定字串的方法是 "What's your name?"， 即使用雙引號。
類似的情況下，你也可以在雙引號內的字串中使用跳出符號來達到相同的目的。
所以，你可以使用 \ 以在字串中表示反斜線。

那麼當我想要指定長度為兩行的字串時該怎麼辦呢？一個方法是使用前面提到的使用三個雙引號。
或者你可以使用 n 跳出符號來表示要換新的一行。
`'This is the first line.nThis is the second line.'`
就是一個簡單的例子。還有很多有用的跳出符號，在此我們只講述了最常應用的。

在字串中，在行末的一個單一反斜線表示著這個字串將接續到下一行。其中不自動加入換行符號。

舉例來說:
```
"這是第一行.\
這是第二行."
```

與下面的例子相當:
```
"這是第一行. 這是第二行."
```


---


python 版:
```
"This is the first sentence.\
This is the second sentence."
```

python 版:
```
"This is the first sentence.This is the second sentence."
```


---


## 原始字串 (Raw Strings) ##

如果你需要指定一些不需要特別處理的字串，你可以透過在字串括號前加入 r 或 R 來表示這是一個原始字串。例如
`r"Newlines are indicated by n"`

**給正則表達式 (Regular Expression) 使用者的話**

> 處理正則表達式時請用原始字串， 否則可能會用上很多反斜線符號. 舉例來說， 自我參照可以寫成 '\1' 或 r'1'。

## Unicode 字串 ##

Unicode 是編寫多國語言檔案的標準. 如果你的檔案裡出現如中文或日文等當地語言的時候，你需要一個能處理 Unicode 的文字編輯器。
同樣地， Python 語言允許你處理 Unicode 文件。你只要在字串括號前加入 u 或 U 即可指定為 Unicode 字串。
例如 u"This is a Unicode string." 就是一個 Unicode 字串。

當你知道檔案裡可能有非英文的文字出現時，請使用 Unicode 字串來處理文字檔案。

## 字串是不可變的 ##

'字串是不可變的'的意思是當你一旦建立了一個字串，你就無法修改它。雖然這看起來不是件好事情，但它事實上非常有益。
我們將在稍後學到的程式中瞭解到為什麼'字串是不可變的'並不是個限制。

## 字串接續 ##

當你把兩個字串擺在一起時，Python 直譯器會自動將兩個字串接續成一個。
例如 'What's' 'your name?' 會自動被轉換成 "What's your name?"。

# 結語 #

我們已經討論了多種類型的輸入/輸出，檔案處理和 pickle 模組的使用。

接下來，我們將探索'例外處理'的概念。

[物件導向程式設計](ObjectOrient.md) | [例外處理](HandleExceptions.md)