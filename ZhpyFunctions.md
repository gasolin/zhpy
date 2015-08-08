# 簡介 #

函式是可以重複使用(重用)的程式區段。函式讓你能賦予一區塊語句一個名稱，然後你可以在程式中的任何地方多次地使用這個名稱代表的語句區塊。
這被稱為 "調用" 函式。我們已經使用了許多內建的函式，比如"長度"(len) 和 "範圍"(range) 函式。

周蟒語言中使用"定義"(def)關鍵字來定義函式。"定義"(def)關鍵字後跟一個函式的標識符名稱，然後再跟一對小括弧。
小括弧裡可以包含一些變量名稱。括弧後再放上一個冒號做結尾。接下來則是接著一塊語句，這塊語句形成了函式的主體:

```
#!/usr/bin/env zhpy
# 檔名: function1.py
定義 說哈囉():
    印出 '哈囉, 世界!' # 函式主體
說哈囉() # 呼叫函式
```

輸出結果:
```
$ zhpy function1.py
哈囉, 世界!
```


---


python 版:
```
#!/usr/bin/env python
# File name: function1.py
def say_hello():
    print 'Hello World!' # body of the function
say_hello() # calling the function
```

python 版輸出結果:
```
$ python function1.py
Hello World!
```


---


### 程式如何運作 ###

我們使用上面解釋的語法定義了一個名稱為"說哈囉"(sayHello) 的函式。
這個函式並未使用任何參數，因此在小括弧中並沒有聲明任何變量。
參數對於函數而言只是一些給函數的輸入值，以便於我們可以在呼叫函式時傳遞不同的值給函式，然後得到相應的結果。

我們呼叫這個函式時不必加上括弧就能運作。在函式完成運行後，程式會自動移至呼叫這個函式的區塊中的下一個語句執行。

## 函式參數 ##

函式可以接受你提供的參數，利用這些參數值來做一些處理並返回適當的結果。
這些參數就像變量一樣，只不過這些變量的值是在我們調用函式的時候定義的，而不是在函式中賦值的。

參數是在函式的小括弧中定義，我們可以使用逗號分割多個參數定義。當我們調用函式的時候，我們就以相同的順序提供這些參數。

注意我們使用的術語——函式中的參數名稱為函式參數。
而你提供給函數調用的值稱為實際參數:
```
#!/usr/bin/env zhpy
# 檔名: param.py
定義 印出最大值(甲, 乙):
    如果 甲 > 乙:
        印出 甲, '最大'
    否則:
        印出 乙, '最大'
印出最大值(3， 4) # 直接提供字面常量作為參數
子 = 5
丑 = 7
印出最大值(子, 丑) # 傳入變量當作參數
```

輸出結果:
```
$ zhpy param.py
4 最大
7 最大
```


---


python 版輸出結果:
```
#!/usr/bin/env python
# File name: param.py
def print_max(x, y):
    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'
print_max(3, 4) # directly give literal constants as arguments
a = 5
b = 7
print_max(a, b) # pass in variables as arguments
```

python 版:
```
$ python param.py
4 is maximum
7 is maximum
```


---


### 程式如何運作 ###

我們定義了一個名稱為"印出最大值"(print\_max) 的函式，我們提供了兩個函式參數甲(x) 和乙(y)。
我們使用 "如果..否則"(if..else) 語句來找出兩者之中較大的一個數字，並且輸出較大的那個數字。

在範例中第一次使用"印出最大值" (print\_max) 函式時，我們直接提供實際參數(這裡提供的是字面常量)給函式。
在第二次使用"印出最大值"函式時，我們調用函數時只提供了變量名稱。
注意到在周蟒/Python 語言中，兩種情況的處理方式完全相同。

呼叫 印出最大值(子,丑) 將實際參數"子"(a) 的值賦給函式參數"甲"(x)，將實際參數"丑"(b) 的值賦給函式參數"乙"(y)。

## 局部變量 ##

當你在函式定義內聲明變量的時候，它們與函數外同名的其他變量沒有任何關係，即變量名稱對於函式來說是局部的。
這稱為變量的作用區域 。從變量的名稱被定義的地方開始，變量被定義的區塊就是它們的作用區域:

```
#!/usr/bin/env zhpy
# 檔名: local.py
定義 函式(x):
    印出 'x 是', x
    x = 2
    印出 '區域變數x改變成', x
x = 50
函式(x)
印出 'x 仍然是', x
```

輸出結果:
```
$ zhpy local.py
x 是 50
區域變數x改變成 2
x 仍然是 50
```


---


python 版:
```
#!/usr/bin/env python
# File name: local.py
def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x
x = 50
func(x)
print 'x is still', x
```

python 版輸出結果:
```
$ python local.py
x is 50
Changed local x to 2
x is still 50
```


---


### 程式如何運作 ###

在函式中，在我們第一次使用變量 x 值的語句中，周蟒使用函式聲明的函式參數的值。
接下來，我們把數值 2 賦給 x。 x 是函式的局部變量。
所以，當我們在函數內改變 x 的值的時候，在主要區塊中定義的 x 變量並不受影響。
在最後一個"印出"(print) 語句中，我們證明了主要區塊中的 x 的值確實並沒有受到影響。

## 名稱空間 (Namespace) ##

對於函式你可以這麼理解: 函式就像是一個可以裝進你所定義的變量的袋子。變量僅存在於袋子中 -
換句話說，變量名稱僅存在在於袋子的空間中，因此這些函式也是名稱空間。

### 使用"共用"(global) 語句 ###

如果你想要為一個定義在函數外的變量賦值，那麼你就得告訴周蟒這個變量名不是局部的，而是全局的。
我們使用"共用"(global) 語句來達成這個功能。沒有"共用"(global)語句的話，就不可能為定義在函數外的變量賦值。

雖然假設在函數內沒有同名的變量的時候，你可以使用在函式外定義的變量的值。
但是我並不鼓勵你這麼做，因為這使得讀者不容易搞清楚這個變量是在哪裡被定義的。
使用"共用"(global) 語句可以清楚地表明變量是在區塊外面被定義的:

```
#!/usr/bin/env zhpy
# 檔名: global.py
def 函式():
    共用 x

    印出 'x 是', x
    x = 2
    印出 '共用變量x改變成', x
x = 50
函式()
印出 'x 的值是', x
```

輸出結果:
```
$ zhpy global.py
x 是 50
共用變量x改變成 2
x 的值是 2
```


---


python 版:
```
#!/usr/bin/env python
# File name: global.py
def func():
    global x

    print 'x is', x
    x = 2
    print 'Changed global x to', x
x = 50
func()
print 'Value of x is', x
```

python 版輸出結果:
```
$ python global.py
x is 50
Changed global x to 2
Value of x is 2
```


---


### 程式如何運作 ###

"共用"(global) 語句被用來聲明 x 是共用的變量 —— 因此，當我們在函式內把值賦給 x 的時候，
這個變化也反映在我們在主要區塊中使用 x 的值的時候。

你可以在一個"共用"語句中指定多個共用變量. 例如:
```
共用 x, y
```

python 版:
```
global x, y
```

宣告了 x， y 兩個變量都是全局變量。

## 參數預設值 (Default argument values) ##

你可能會希望在函式中有些參數是可選的，如果使用者不特別指定的話，就讓這些參數使用預設的值。
這個功能可以透過使用預設參數值來達成。你可以在定義函數時在函式參數名稱後加上賦值運算符（=）與默認值。

注意，默認的參數值應該是一個常量。更準確的說，預設參數值應該是不可變的——這會在後面的章節中做詳細解釋:
```
#!/usr/bin/env zhpy
# 檔名: default.py
定義 說(訊息, 次數 = 1):
    印出 訊息 * 次數
說('Hello')
說('World'， 5)
```

輸出結果:
```
$ zhpy default.py
Hello
WorldWorldWorldWorldWorld
```


---


python 版:
```
#!/usr/bin/env python
# File name: default.py
def say(message, times = 1):
    print message * times
say('Hello')
say('World', 5)
```

python 版輸出結果:
```
$ python default.py
Hello
WorldWorldWorldWorldWorld
```


---


### 程式如何運作 ###

函式"說"(say) 的作用是輸出指定次數的字串。而當我們不提供指定次數的時候，函式僅輸出一次。
我們可以透過提供預設值 1 當作指定次數的參數來達成這個目的。

在第一次呼叫函式"說"(say) 的時候， 我們只提供一個字串，因此函式只輸出字串一次。
在第二次呼叫"說"(say) 函式的時候，我們提供了字符串和參數值 5，結果是同一字串輸出了 5 遍。

值得一提的是你只能提供預設值給在參數列表後端的參數。而不能在沒有提供預設值的參數前提供預設參數值。
這是因為值是根據值所在的位置提供給參數的。例如：
```
定義 函式(a, b=5) 
```

是有效的， 但
```
定義 函式(a=5, b)
```

是無效的。


---


Python 版:
```
def function(a, b=5)
```

Python 版:
```
def function(a=5, b)
```

---


## 關鍵字參數 ##

如果你的一些函數中有許多參數，而你只想指定其中的一部分，那麼你可以通過命名這些參數來為這些參數賦值——
這被稱作關鍵字參數。我們使用名稱（關鍵字）來取代位置（我們前面所一直使用的方法）來為函式指定實際參數。

這麼做有兩個優點 —— 一第一， 由於我們不必擔心參數的順序，使用函式變得更加簡單了。
第二、在定義函式時就先給其他參數默認值，使用時我們就可以只對我們想要的那些參數賦值:

```
#!/usr/bin/env zhpy
# 檔名: keyword.py
定義 函式(a, b=5, c=10):
    印出 'a 是', a, '且 b 是', b, '而 c 是', c
函式(3, 7)
函式(25, c=24)
函式(c=50, a=100)
```

輸出結果:
```
$ zhpy keyword.py
a 是 3 且 b 是 7 而 c 是 10
a 是 25 且 b 是 5 而 c 是 24
a 是 100 且 b 是 5 而 c 是 50
```


---


python 版:
```
#!/usr/bin/env python
# File name: keyword.py
def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c
func(3, 7)
func(25, c=24)
func(c=50, a=100)
```

python 版輸出結果:
```
$ python keyword.py
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50
```


---


### 程式如何運作 ###

名稱為"函式"(func) 的函式有一個沒有默認值的參數，和兩個有默認值的參數。

在第一次使用函式
```
函式(3， 7) 
```

的時候，參數 a 得到數值 3，參數 b 得到數值 7，而參數 c 則得到它的默認值 10。
```
#!/usr/bin/env zhpy
# 檔名: return.py
定義 最大數值(x, y):
    如果 x > y:
        返回 x
    否則:
        返回 y
印出 最大數值(2, 3)
```

輸出結果:
```
$ zhpy return.py
3
```


---


python 版:
```
#!/usr/bin/env python
# File name: return.py
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
print maximum(2, 3)
```

python 版輸出結果:
```
$ python return.py
3
```


---


### 程式如何運作 ###

最大數值(maximum) 這個函式傳回兩個參數中較大的值。

在例子中，在呼叫函式時我們提供兩個數字。函式使用一個簡單的"如果..否則"(if..else) 語句來找出較大的數字，然後傳回那個數字。

注意 沒有返回值的"返回"(return) 語句等於 "返回 空"(return None) 語句，
當每個周蟒函式運行結束時，如果我們沒有提供"返回"(return) 語句，則函式就會傳回 None (空)這個值。
None (空)是周蟒中表示沒有任何東西的特殊類型。例如，如果一個變量的值為 None(空)，則表示這個變量中沒有值。

例如， 如果我們運行
```
印出 某個函式() 
```

這個語句， 而"某個函式"這個函式並未使用"返回"語句，我們可以看到輸出的結果為 None(空):
```
>>> 定義 某個函式():
...    略過
...
>>> 印出 某個函式()
None
>>>
```


---


python 版:
```
>>> def some_function():
...  pass
...
>>> print some_function()
None
>>>
```


---


"略過"(pass) 語句表示一個空的語句塊。

## 文件字串 (DocStrings) ##

周蟒有一個很奇妙的特性，稱為文件字串(Document Strings)，在 Python 中文件字串通常被簡稱為 docstrings。
文件字串是一個重要的工具，我們在程式運行中甚至可以取得文件字串。它能幫助你的程式更加簡單易懂，你應該盡量使用它:

```
#!/usr/bin/env zhpy
# 檔名: docstrings.py
定義 印出較大值(x， y):
    '''印出兩個數之中較大的數。

    這兩個數必須是整數或是包含整數的字串。'''

    x = 整數(x) # 將x轉換成整數
    y = 整數(y)

    如果 x > y:
        印出 x, '較大'
    否則:
        印出 y, '較大'
印出較大值(3， 5)
印出 印出較大值.__文件__
```


輸出結果:
```
$ zhpy docstrings.py
5 較大
印出兩個數之中較大的數。

這兩個數必須是整數或是包含整數的字串。
```


---


python 版:
```
#!/usr/bin/env python
# File name: docstrings.py
def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers or strings containing integers.'''

    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'
print_max(3, 5)
print print_max.__doc__
```

python 版輸出結果:
```
$ python docstrings.py
5 is maximum
Prints the maximum of two numbers.

The two values must be integers or strings containing integers.
```


---


### 程式如何運作 ###

函式中第一個邏輯行的字串就是這個函式的文件字串。注意，文件字串也適用於模組和類型，我們會在後面相應的章節中學習它們。

文件字串慣例是一個多行的字串，它的首行以大寫字母開始，以句號結尾。第一行通常是這個函式的簡介。
如果要包含更長的解釋，那麼就空一行後從第三行再開始是詳細的描述。強烈建議你在使用文件字串時遵循這個慣例。

我們可以透過使用 "印出較大值"(print\_max) 函式的 "文件"(doc)（注意雙下劃線）屬性來取得文件字串。
我們會在後面講解物件導向編程的章節中學習更多關於物件的知識。
請記住 Python 和周蟒把每一樣東西都視為物件。
當函式中包含文件字串時，文件字串就是函式的一部分，可以使用"文件"(doc) 屬性來存取文件字串。

我們已經在周蟒中使用過 "說明"(help) 函式了，所以你也已經看到過文件字串的使用。
"說明"(help) 函式所做的只是抓取函數的文件字串，即那個函式的"文件"(doc) 屬性，然後漂亮地展示給你。
你可以對上面這個函數嘗試一下， 只要在你的程式裡包括 "說明(印出較大值) 語句即可。記得按 q 鍵就可以退出 help 的顯示。

自動化工具也可以以同樣的方式從你的程式中取得文件。因此，你應該為你所寫的正式函式編寫文件字串。

Python 發行版附帶的 pydoc 命令使用文件字串的方式與 "說明"(help) 函式相似。

# 結語 #

我們已經學習了很多函數方面的知識，不過其實我們還沒有涉及所有方面。然而，我們已經瞭解了在日常使用中，你可能用到的大多數函數知識。

接下來，我們將學習如何創建和使用周蟒/Python 模組。

[控制流程](ControlFlow.md) | [模組](ZhpyModules.md)



