# 簡介 #

例外處理發生在當你的程式出現某些例外狀況的時候. 例如當你想要讀取一個不存在的檔案， 或是在程式運行中不小心將檔案刪除了， 在這些情況下你可以使用例外處理來解決問題。

假如你的程式裡有一些無效的語句時會怎麼樣呢？ 周蟒或 Python 直譯器會引發(raises)例外情形， 並通知你那裡有一個錯誤。

## 錯誤 (Errors) ##

考量一個簡單的"印出"(print) 語句。假如我們把"印出"的英文關鍵詞 print 誤拼為 Print(P大寫)，這種情況 Python 直譯器會引發一個語法錯誤(syntax error):
```
$ zhpy
>>> Print 'hello world'
  File "<stdin>", line 1
    Print 'hello world'
                      ^
SyntaxError: invalid syntax
```

python 版:
```
$ python
>>> Print 'hello world'
  File "<stdin>", line 1
    Print 'hello world'
                      ^
SyntaxError: invalid syntax
```

我們可以觀察到程式引發了一個"語法錯誤"(SyntaxError)，並且發生錯誤的位置也被檢測到並印了出來。這是 Python 語言預設的錯誤處理方式。

讓我們拿一個接受使用者輸入的程式作例子。看看假如使用者並不乖乖輸入資料， 而是嘗試使用 Ctrl-D 跳出程式時會發生什麼事:
```
$ zhpy
>>> 輸入('Enter something : ')
Enter something : Traceback (most recent call last):
  File "<stdin>", line 1, in ?
EOFError
    >>>
```

python 版:
```
$ python
>>> raw_input('Enter something : ')
Enter something : Traceback (most recent call last):
  File "<stdin>", line 1, in ?
EOFError
    >>>
```

Python 直譯器引發一個"空值錯誤"(EOFError)， 表示當周蟒或 Python 直譯器期望收到一些文字的時候，
卻收到了一個檔尾符號(end-of-file)，即檔案是空的或不存在。

## 例外(Exceptions)處理 ##

我們可以使用"嘗試..異常"(try...except) 語句來作例外處理. 我們將正常的區塊放在"嘗試"(try) 語句區塊中， 並將我們的例外處理語句放在"異常"(except) 從句區塊中:
```
#!/usr/bin/env zhpy
# 檔名: try_except.py
導入 sys
嘗試:
    s = 輸入('輸入些東西 : ')
異常 空值錯誤:
    印出 '\n為什麼你要給我空值哩?'
    sys.exit()
異常:
    印出 '\n不正確的輸入.'
    # 這裡，我們並不結束程式
印出 '完成'
```

輸出結果:
```
$ zhpy try_except.py
輸入些東西 : ^D
為什麼你要給我空值哩?

$ zhpy try_except.py
輸入些東西 : abc
完成
```


---


python 版:
```
#!/usr/bin/env python
# File name: try_except.py
import sys
try:
    s = raw_input('Enter something : ')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()
except:
    print '\nInvalid input.'
    # Here， we are not exiting the program
print 'Done'
```

python 版輸出結果:
```
$ python try_except.py
Enter something : ^D
Why did you do an EOF on me?

$ python try_except.py
Enter something : abc
Done
```


---


### 程式如何運作 ###

我們把所有可能引發錯誤的語句放在"嘗試"(try) 語句區塊中，然後在"異常"(except) 從句區塊中處理所有的錯誤和例外情況。
"異常"(except)從句可以用來處理單一的錯誤或例外情況，或者一整個組合(tuple)的錯誤和例外。
如果沒有明確提出錯誤或例外的名稱， 這個 "異常"(except) 從句會處理所有錯誤和例外情況。
對於每個 "嘗試"(try)  語句，至少都有一個相關聯的 "異常"(except) 從句。

如果我們並未處理某個錯誤或例外，Python 直譯器就會搜尋是否區塊外有定義任何例外處理方式。
假使程式裡並沒有定義任何例外處理方式。Python 直譯器就會呼叫預設的錯誤處理機制來印出一個錯誤訊息，並且終止程式的運行。

你還可以在"嘗試..異常"(try...except) 語句中關聯一個"否則"(else) 從句。當沒有例外情況發生的時候，就執行"否則"(else)從句的內容。

我們還可以在"異常"(except) 語句中取得例外處理物件以獲取更多這個例外情況的信息。這會在下一個例子中說明。

## 引發例外(Raising Exceptions)處理 ##

你可以使用"引發"(raise) 語句來引發例外處理。你也可以指明錯誤/例外的名稱與隨著例外處理所引發的例外物件。
你可以引發的錯誤或例外應該是一個直接或間接繼承自"錯誤"(Error) 或"例外"(Exception) 類別的類別:
```
#!/usr/bin/env zhpy
# 檔名: raising.py
類別 輸入太短例外(例外):
    '''自己定義的例外類別.'''
    定義 __初始化__(我, 長, 最短長度):
        例外.__初始化__(self)
        我.長 = 長
        我.最短長度 = 最短長度
嘗試 s = 輸入('輸入些東西 : ')
    如果 長度(s) < 3:
        引發 輸入太短例外(長度(s), 3)
    # 繼續其他動作
異常 空值錯誤:
    印出 '\n為什麼你要給我空值哩?'
異常 輸入太短例外, x:
    印出 '輸入長度 %d. 至少輸入長度 %d' % (x.長, x.最短長度)
否則:
    印出 '未引發任何例外.'
```

輸出結果:
```
$ zhpy raising.py
輸入些東西 : abcd
未引發任何例外.

$ zhpy raising.py
輸入些東西 : ab
輸入長度 2. 至少輸入長度 3
```


---


python 版:
```
#!/usr/bin/env python
# File name: raising.py
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = raw_input('Enter something : ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
    # Continue other work as usual here
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
    print 'Input was of length %d. I was expecting at least length of %d' % (x.length, x.atleast)
else:
    print 'No exception was raised.'
```

python 版輸出結果:
```
$ python raising.py
Enter something : abcd
No exception was raised.

$ python raising.py
Enter something : ab
Input was of length 2. I was expecting at least length of 3
```


---


### 程式如何運作 ###

例子中我們建立了我們自己的例外型別， 但其實我們可以使用任何內建的例外/錯誤型別來引發錯誤處理。
例如使用"值錯誤"(ValueError) 等. 你可以運行
```
導入 例外
說明(例外)
```

python 版
```
import exceptions
help(exceptions) 
```

來取得參考資料.

我們新建立的例外類別稱作"輸入太短例外"(ShortInputException) 類別。
它有兩個欄位——"長"(length)，欄位是輸入資料的長度，"最短長度"(atleast) 則是程式期望的最短長度。

在"異常"(except) 從句中， 我們也提到了錯誤類別和用來表示錯誤/例外物件的變量。這與函式呼叫中的形式參數和實際參數概念類似。
在這個特別的"異常"(except) 從句中，我們使用例外物件的"長"(length)和"最短長度"(atleast)欄位來為使用者印出一個適當的訊息。

## 使用"嘗試..最後"(try..finally) 語句 ##

當你打開一個檔案並讀取內容的時候， 你希望在將檔案關閉時無論是否引發例外處理，都一律呼叫"關閉"(close) 類別方法來關閉檔案。
這可以使用"嘗試..最後"(try..finally)語句區塊來做到。
注意你並不能同時使用"異常"(except)從句和"最後"(finally)從句。如果你要同時使用它們的話，需要使用兩個"嘗試"(try) 區塊，
並把其中一個嵌入另外一個。

**註解:
> Python > 2.5 版允許在同一個"嘗試"(try) 區塊中同時使用"異常"(except) 和 "最後"(finally) 從句:**

```
#!/usr/bin/env zhpy
# 檔名: finally.py
導入 time
f = 檔案('poem.txt')
嘗試:
    當 真:
        行 = f.讀一行()
        如果 長度(行) == 0:
            中斷
        time.sleep(2)
        印出 行,
最後:
    f.關閉()
    印出 '關閉檔案.'
```

輸出結果:
```
$ zhpy finally.py
Programming is fun
^C
關閉檔案.
Traceback (most recent call last):
  File "programs/finally.py"， line 13， in ?
    time.sleep(2)
KeyboardInterrupt
```


---


python 版:
```
#!/usr/bin/env python
# File name: finally.py
import time
f = file('poem.txt')
try:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Closed the file.'
```

python 版輸出結果:
```
$ python finally.py
Programming is fun
^C
Closed the file.
Traceback (most recent call last):
  File "programs/finally.py"， line 13， in ?
    time.sleep(2)
KeyboardInterrupt
```


---


### 程式如何運作 ###

我們在程式中進行一般的檔案讀取工作，但是我有意在每讀出一行用 time.sleep 類別方法來取得2秒鐘的間隔。
這樣故意延遲的作法是希望讓程式運行得慢一些， 好讓我們可以在程式運行中取消運行。
當我們在程式運行中輸入 Ctrl-c 命令， 會引發一個鍵盤中斷例外處理，但是在程式退出之前，會先運行"最後"(finally) 區塊中的語句。

# 結語 #

我們已經討論了"嘗試..異常"(try...except) 和"嘗試..最後"(try..finally) 語句的用法。
我們還學習了如何建立我們自己的例外型別和如何引發例外處理。

接下來，我們將探索 Python 標準函式庫。

[輸入, 輸出](InputOutput.md) | [標準函式庫](StandardModules.md)