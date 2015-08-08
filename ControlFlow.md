# 簡介 #

目前我們所寫的程式裡，都是按照著一系列語句的流程順序來執行它們。

那麼如果現在希望根據現在時間來輸出"早上好"或者"晚上好"，
我們該怎麼樣才能改變控制語句的執行順序呢？
該怎麼樣才能讓程式根據不同的情況，自行判斷做不同的事情?

可能你已經想到了，我們可以通過控制流語句，來實現程式判斷與改變執行順序。
在周蟒中有三種控制流語句—— "如果" (if)語句、"取"(for)語句、和"當"(while)語句。
這三種語句分別表示"判斷處理，迴圈處理，依情況處理"這三種控制流程。

## 使用"如果"語句 ##

"如果"(if)語句是一種用來檢驗條件的語句。
"如果"(if)檢驗的條件為"真"(True)，我們運行緊接著的程式區塊的語句（稱為 "如果"區塊 ），
"否則"(else)我們就改去處理另外一塊語句（稱為 "否則"區塊 ）。

"否則"(else)從句並不是必須的。

我們可以把相關連的"如果"語句使用簡化的"假使"(elif)語句串連起來, 以取代"否則 如果"語句:

```
#!/usr/bin/env zhpy
# 檔名: if.py
數字 = 23
猜測 = 整數(輸入('輸入一個數字: '))
如果 猜測 == 數字:
    印出 '恭喜, 你猜對了.' # 一個新區塊的開始
    印出 '(但沒有獎品喔!)' # 新區塊的結束
假使 猜測 < 數字:
    印出 '錯了, 數字再大一點.' # 另一個區塊
    # 你可以在區塊中做任何想做的事 ...
否則:
    印出 '錯了, 數字再小一點.'
    # 只有在猜測 > 數字 的情況下才會跑到這個區塊來
印出 '結束'
# 最後一行語句和"如果..假使..否則"語句是無關的，
# 因為最後的'印出'這行在主區塊中出現，所以這行永遠會被執行.
```

輸出結果:
```
$ zhpy if.py
輸入一個數字: 50
錯了, 數字再小一點.
結束

$ zhpy if.py
輸入一個數字: 22
錯了, 數字再大一點.
結束

$ zhpy if.py
輸入一個數字: 23
恭喜, 你猜對了.
(但沒有獎品喔!)
結束
```


---


pyhton 版:
```
#!/usr/bin/env python
# File name: if.py
number = 23
guess = int(raw_input('Enter an integer : '))
if guess == number:
    print 'Congratulations, you guessed it.' # New block starts here
    print '(but you do not win any prizes!)' # New block ends here
elif guess < number:
    print 'No, it is higher than that.' # Another block
    # You can do whatever you want in a block ...
else:
    print 'No, it is lower than that.'
    # you must have guess > number to reach this block
print 'Done'
# This last statement is separate from the if statement,
# and since it is present in the main block, it is always executed.
```

pyhton 版輸出結果:
```
$ python if.py
Enter an integer : 50
No, it is lower than that.
Done

$ python if.py
Enter an integer : 22
No, it is higher than that.
Done

$ python if.py
Enter an integer : 23
Congratulations, you guessed it.
(but you do not win any prizes!)
Done
```


---


### 程式如何運作 ###

在這個程式裡，我們從取得使用者猜測的數字，並檢查這個數字是否是我們手中的那個。

我們將變量"數字"設置成我們想要的任何整數，在這個例子中是 23。
接著，我們使用"輸入"(raw\_input)函數取得使用者猜測的數字。

別聽到函數這個名稱就覺得很可怕，事實上函數只是一段可以重用的程式。
我們將在下一章學習更多關於函數的知識。

"輸入"函數是周蟒語言的一部分，因此我們隨時都可以取用這個函數。

在我們提供"輸入"函數一個字串後，這個函數會將我們提供的字串輸出到螢幕上，然後等待使用者輸入。

一旦我們輸入了一些東西並按下確定鍵(enter /return)之後，這個函數會回傳使用者輸入的字串給我們。

我們通過"整數"(int) 函數把這個字串轉換為整數，並把它存儲在變量: "猜測"(guess) 中。

"整數"(int)型別事實上是一個類別，但是現在你所需要知道的是你可以使用"整數"型別來將一個字串轉換成
一個整數（假設這個字串的內容是一個有效的整數）。

接著，我們比較我們選擇的數字與使用者猜測的數字，如果相等的話就印出(print)一個執行成功的訊息。

注意我們使用了縮排的層次來讓周蟒語言解譯器能分辨哪行語句屬於哪個程式區塊。這就是為什麼縮排在 Python 與周蟒語言中這麼重要的原因。

作者希望你還記得遵守"每個縮排都以四個空白符號來表示"的規則，你應該可以做得到吧?

**注意：**

> "如果"(if)語句的結尾處都包含一個冒號(:)——這符號讓周蟒語言解譯器知道這個語句下面將緊跟著一個程式語句區塊。

我們接著檢驗是否使用者猜測的數字小於我們選擇的數字。

如果情況確實如此，我們就通知使用者再猜一個更大一點的數字。

我們在此使用的是"假使"(elif)從句來將兩個相關聯的"如果 否則/如果 否則"(if else-if else) 語句合併為一個
> "如果 假使 否則"(if-elif-else)語句。這使得程式更加易於閱讀，也減少了所需的縮排數量。

"假使"(elif)和"否則"(else)從句都必須在語句結尾處有一個冒號，下面並跟著一個相應正確縮排的程式語句區塊。

你也可以在一個"如果"區塊中使用另外一個"如果"語句，"否則"語句，或"假使"語句——這種形式被稱為"巢狀的'如果'語句"。
周蟒語言解譯器也將它視為一個"如果"區塊中的語句。

請記得在控制流程中，"假使"和"否則"語句並不是必要的。一個最簡單的有效"如果"語句如下:

```
如果 真:
     印出 '是的, 這是真的'
```

Python 版:
```
if True:
    print 'Yes, it is true'
```

在周蟒語言解譯器執行完一個完整的"如果"語句以及與它相關聯的"假使"和"否則"從句之後，它移向"如果"語句塊後的下一個語句。

在這個例子中，這個程式語句區塊是主要的語句區塊。
程式從這裡開始執行，而"如果"語句接著的語句是 "印出 '結束'" 語句。

在這個語句之之後，周蟒語言解譯器看到程式已經執行到結尾處了，於是結束運行這個程式。

儘管這是一個非常簡單的程式，但是我已經在這個簡單的程式中指出了許多你應該注意的地方。
多數的細微差別都相當直觀，它們在開始時會引起你的注意，但是當你熟悉後，會感到這麼些規則其實相當自然。

**給 C/C++ 使用者的話**

> 在 Python 或周蟒中沒有 switch 語句。你可以使用"如果 假使 否則" (if..elif..else) 語句來完成同樣的工作。

## 使用"當"(while) 語句 ##

"當"(while)語句允許你在一個條件為真的情況下，重複執行一塊語句。

"當"(while)語句是所謂循環語句(迴圈)的一個例子，循環語句(迴圈)就是會重複執行一塊語句直到要求的條件符合了才終止的語句。

"當"(語句可以附上一個可選的"否則"(else)從句:

```
#!/usr/bin/env zhpy
# 檔名: while.py
數字 = 23
運行 = 真
當 運行:
    猜測 = 整數(輸入('輸入一個數字: '))

    如果 猜測 == 數字:
        印出 '恭喜, 你猜對了.'
        運行 = 假 # 這會讓循環語句結束
    假使 猜測 < 數字:
        印出 '錯了, 數字再大一點.'
    否則:
        印出 '錯了, 數字再小一點.'
否則:
    印出 '循環語句結束'
印出 '結束'
```

輸出結果:
```
$ zhpy while.py
輸入一個數字: 50
錯了, 數字再小一點.
輸入一個數字: 22
錯了, 數字再大一點.
輸入一個數字: 23
恭喜, 你猜對了.
循環語句結束
結束
```


---


Python 版:
```
#!/usr/bin/env python
# File name: while.py
number = 23
running = True
while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.'
        running = False # this causes the while loop to stop
    elif guess < number:
        print 'No, it is higher than that.'
    else:
        print 'No, it is lower than that.'
else:
    print 'The while loop is over'
print 'Done'
```


Python 版輸出結果:
```
$ python while.py
Enter an integer : 50
No, it is lower than that.
Enter an integer : 22
No, it is higher than that.
Enter an integer : 23
Congratulations, you guessed it.
The while loop is over
Done
```


---


### 程式如何運作 ###

在這個程式裡，我們仍然使用了猜數字遊戲作為例子，但是現在這個程式的優勢在於使用者可以不斷的猜，
直到他猜到對的數字為止——不需要像前面例子那樣為每次猜測都得重複執行一遍程式。
這個例子適當地說明了"當"(while) 語句的使用。

我們把"輸入"和"如果"語句移到了循環語句裡。

首先我們將變量"運行"的值設置為"真"(True)。接著我們執行這個"當"(while)迴圈。
這個"當"(while)迴圈首先檢驗變量"運行"的值是否為"真"(第一次執行當然是用我們剛設置的值: "真")，然後執行緊接著的"當"區塊。

在這區塊的程式執行了之後，程式將回到迴圈開頭並再次檢驗條件符不符合。

在這個例子中，程式中的"條件"是"運行"變量。如果"運行"變量為真，"當"區塊的程式就會再次被執行。
否則，程式將繼續執行可選的"否則"區塊，並執行接著"當"語句之後的下一個語句。

當循環語句條件變為"假"的時候，"否則"區塊才會被執行——這情形也可能發生在第一次檢驗條件的時候。

只有一種情形下"否則"區塊不會被執行，那就是我們使用"中斷"(break) 語句來停止迴圈的時候。我們將在本章稍後的地方介紹"中斷"(break)語句。

註釋: 周蟒的關鍵字並非全為直接翻譯為中文，而是考慮了中文的思考習慣做出翻譯。一個英文關鍵字可以對應到多個中文關鍵字。
對中文關鍵字有任何建議都歡迎提出。

**給 C/C++ 使用者的話**

> 請記得你可以在"當"(while)迴圈後加入"否則"從句。如果用了"跳出"語句來停止迴圈的話，"否則"從句將不會被執行。

## 使用"取" (for) 語句 ##

"取..自" (for..in) 語句是另外一種循環語句(迴圈)，它依序地使用一序列的物件。意即"逐一使用序列中的每個項目"。
我們會在後面的章節中更加詳細地學習序列。

你現在只需要知道，序列就是一串有次序的項目的集合:
```
#!/usr/bin/env zhpy
# 檔名: for.py
取 i 自 範圍(1, 5):
    印出 i
```

輸出結果:
```
$ zhpy for.py
1
2
3
4
```


---


Python 版:
```
#!/usr/bin/env python
# File name: for.py
for i in range(1, 5):
    print i
```

Python 版輸出結果:
```
$ python for.py
1
2
3
4
```


---


### 程式如何運作 ###

在這個程式裡，我們輸出了一系列的數字。我們使用內建的"範圍"(range)函數生成了這個數字序列。

當我們提供兩個數字給"範圍"(range)函式, 它會返回從第一個數開始到第二個數前為止一序列的數字。
例如，`範圍(1,5)` 給出序列 [1, 2, 3, 4]。"範圍"函式回傳的序列只延展到第二個數前一個數為止，它不包含第二個數。

"取"(for)迴圈在這個範圍內遞迴(反覆地執行)——所以"`取 i 自 範圍(1, 5):`" 等同於"取 i 自 [1, 2, 3, 4]"。
序列中的所有項目，依序被賦值給了 i，並且對每個 i 分別執行了"取"(for)區塊中的語句。
在這個例子中，區塊中的語句只做了輸出 i 的值到螢幕上。

"取..自"(for..in) 迴圈對於任何物件序列都適用。在我們的例子中使用的是一個全為數字的列表。

"取"(for)迴圈中"否則"(else)從句是可選的，但如果用了"中斷"(break)語句來停止迴圈的話，"否則"(else)從句將不會被執行。

**給 C/C++ 使用者的話**

> Python 與周蟒程式語言的"取"(for)迴圈和傳統程式語言的 for 迴圈不盡相同。
> c 語言裡的 for 迴圈明確地使用了計數器(counter)。而 Python 與周蟒語言的 for 迴圈則只需直接對物件的序列做遞迴。

> c# 程式員會注意到 Python 與周蟒的 for 迴圈與 C# 中的 foreach 迴圈十分類似。
> Java 程式員會注意到 Python 與周蟒的 for 迴圈與 Java 1.5 中的 for (int i : IntArray) 句型相似。
> 重要的是 Python 與周蟒沒有對序列的物件型態加以限制 -- 序列中甚至也可以包含多種不同型態的物件。

## 使用中斷 (break) 語句 ##

"中斷"(break)語句是用來終止循環語句的，例如在當迴圈停止的條件還沒有符合或整個序列還沒有執行完時用來停止循環語句(迴圈)的執行。

當"中斷"(break)語句被使用時，任何對應的"否則"(else)迴圈將不會被執行:
```
#!/usr/bin/env zhpy
# 檔名: break.py
當 True:
    s = 輸入('輸入點東西: ')
    如果 s == 'quit':
        中斷
    印出 '字串長度為', 長度(s)
印出 '結束'
```

輸出結果:
```
$ zhpy break.py
輸入點東西: Programming is fun
字串長度為 18
輸入點東西: When the work is done
字串長度為 21
輸入點東西: if you wanna make your work also fun:
字串長度為 37
輸入點東西:       use Python!
字串長度為 12
輸入點東西: quit
結束
```


---


Python 版:
```
#!/usr/bin/env python
# File name: break.py
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print 'length of the string is', len(s)
print 'Done'
```

Python 版輸出結果:
```
$ python break.py
Enter something : Programming is fun
length of the string is 18
Enter something : When the work is done
length of the string is 21
Enter something : if you wanna make your work also fun:
length of the string is 37
Enter something :       use Python!
length of the string is 12
Enter something : quit
Done
```


---


### 程式如何運作 ###

在這個程式裡，我們重複地取得使用者的輸入值並輸出這個值的長度。
我們提供了一個特別的條件來停止程式，即檢驗使用者輸入的值為'quit'時。我們就透過"中斷"(break)語句來終止迴圈。

輸入字串的長度可以透過內建的"長度"(len)函數來取得。 請使用 說明(長度) 來觀看參考文件。
有趣的是 "長度"(len)函數可以用在任何物件序列上。在這個例子中是用一序列的字元(即字串)上。

請記得"中斷"語句也可以在"取"(for) 迴圈中使用。

## 使用繼續 (continue) 語句 ##

繼續 (continue)語句是用來告訴周蟒語言解釋器跳過目前迴圈區塊中剩下來的其他語句，繼續進行下一輪循環:
```
#!/usr/bin/env zhpy
# 檔名: continue.py
while True:
    s = 輸入('輸入點東西: ')
    if s == 'quit':
        中斷
    if len(s) < 3:
        繼續
    印出 '達到足夠輸入長度'
    # 繼續任何處理 ...
```

輸出結果:
```
$ zhpy continue.py
輸入點東西: a
輸入點東西: 12
輸入點東西: abc
達到足夠輸入長度
輸入點東西: quit
```


---


Python 版:
```
#!/usr/bin/env python
# File name: continue.py
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print 'Input is of sufficient length'
    # Do other kinds of processing here ...
```

Python 版輸出結果:
```
$ python continue.py
Enter something : a
Enter something : 12
Enter something : abc
Input is of sufficient length
Enter something : quit
```


---


### 程式如何運作 ###

在這個程式裡，我們接受使用者的輸入，但我們只處理那些大於三個字元的輸入值。因此我們使用內建的 len 函數來找出輸入值的長度。
當長度小於 3 時，我們就使用"繼續"(continue) 語句來跳過剩下的程式區塊；
否則，就繼續執行這個循環中的剩餘語句。

請注意，"繼續"(continue)語句也適用於"取"(for)迴圈。

## 結語 ##

我們已經學習了如何使用三種控制流程語句——"如果"(if)語句、"當"(while) 語句和 "取"(for) 語句，
以及與之相關的"中斷"(break) 和"繼續"(continue) 語句。
我們將頻繁地使用這些語句。因此，熟悉這些控制流程語句是你應當掌握的基本技能。

接下來，我們將學習如何建立並使用函式。

[運算符號和表達式](OperatorExpressions.md) | [函式](ZhpyFunctions.md)





