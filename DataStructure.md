# 簡介 #

基本上資料結構只是些用來保存資料的架構。
換句話說， 資料結構被用來儲存一系列相關聯的資料.

在周蟒/Python 語言裡有三種內建的資料結構: 列表(list)， 元組(tuple)， 與字典(dictionary)。 我們將學習如何使用它們。

## 列表 (List) ##

列表是處理一組有序項目的資料結構，即你可以在一個列表中存儲一序列的項目。
列表很容易理解，例如你有一個上面記載著你所要買的東西的購物清單。
只不過在你的購物清單上，可能每樣東西都獨自佔有一行，而在周蟒語言中，你用逗號來分隔各個項目。

列表中的項目應該包括在中括弧(方括號)中，這樣周蟒語言直譯器就能理解你正指明了一個列表。
一旦你新建了一個列表，你就可以在列表中加入、刪除或是搜索其中的項目。
由於我們可以加入或刪除項目，所以我們說列表是一種"可變的"資料類型，即這種類型是可以被改變的。

## 物件與類別的快速入門 ##

雖然我一直盡量延後關於物件與類別的討論，但是現在先對物件與類別做一點解釋可以讓你更容易了解列表這個型態。
我們會在相應的章節詳細探索這個主題。

列表是使用物件與類別的一個例子。當你使用變量 i 並給它賦值的時候(比如賦整數5)，你可以將之視為你新建了一個類型為整數(int)的物件(實體)。
當然，你可以用 說明(整數) (help(int)) 查看一下以更好地理解這一點。

一個類別可以有需多方法，這些方法都是只能透過這個類別來使用的函數。只有當你有該類別的物件的時候，你才可以使用這些函數提供的功能。
例如，"列表"(list) 類別有一個 "加入"(append) 方法，這個方法讓你能在列表尾端加入一個新的項目。例如:

```
我的列表.加入('一個項目')
```

python 版:
```
mylist.append('an item')
```

這個語句將在 "我的列表"(mylist) 列表尾端加入 '一個項目'('an item') 這個字串。
注意運用點號標記法來調用物件方法的使用方式與處理模組屬性的方式完全相同 - 這種存取與標記方式的一致性使得周蟒語言超簡單。

一個類別也可以擁有只為類別定義的變量欄位。你只能在擁有一個該類別的物件的時候，才可以使用這些變量/名稱。
我們也是通過點號標記法來使用欄位，例如 "我的列表.欄位"(mylist.field):
```
#!/usr/bin/env zhpy
# 檔名: list1.py
# 這是我的購物清單
購物清單 = ['蘋果', '芒果', '胡蘿蔔', '香蕉']
印出 '我有', 長度(購物清單), '個項目待購買.'
印出 '要購買的項目有:', # 注意行尾的逗點符號
取 項目 自 購物清單:
    印出 項目,
印出 ' [結束]'
印出 '我也得買米.'
購物清單.加入('米')
印出 '我的購物清單現在有', 購物清單
印出 '來排序一下我的清單'
購物清單.排序()
印出 '排好的清單是', 購物清單
印出 '第一項要買的是', 購物清單[0]
舊項目 = 購物清單[0]
刪除 購物清單[0]
印出 '我買了', 舊項目
印出 '我的購物清單現在有', 購物清單
```

輸出結果:
```
$ zhpy list1.py
我有 4 個項目待購買.
要購買的項目有: 蘋果, 芒果, 胡蘿蔔, 香蕉  [結束]
我也得買米.
我的購物清單現在有 ['蘋果', '芒果', '胡蘿蔔', '香蕉', '米']
來排序一下我的清單
排好的清單是 ['蘋果', '香蕉', '胡蘿蔔', '芒果', '米']
第一項要買的是 蘋果
我買了 蘋果
我的購物清單現在有 ['香蕉', '胡蘿蔔', '芒果', '米']
```


---


python 版:
```
#!/usr/bin/env python
# File name: list1.py
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have'， len(shoplist), 'items to purchase.'
print 'These items are:', # Notice the comma at the end of the line
for item in shoplist:
    print item,
print ' [end]'
print 'I also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist
print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is', shoplist
print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist
```

python 版輸出結果:
```
$ python list1.py
I have 4 items to purchase.
These items are: apple mango carrot banana  [end]
I also have to buy rice.
My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
The first item I will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
```


---


### 程式如何運作 ###

變量 shoplist 是某個正要前去購物的人的購物清單。在 shoplist 變量中，我們只儲存將購買物品的名稱，即只儲存字串。
但是其實列表物件裡可以包含任何種類的對象， 包含數字， 甚至是其他的列表物件。

我們也使用了"取..自"(for..in) 迴圈在列表的各項目間遞迴。從現在開始，你一定已經意識到列表也是一個序列。
序列的特點會在後面的章節中討論。

注意，我們在"印出"(print) 語句的結尾使用了一個 逗號 來消除每個 "印出"(print) 語句自動印出的換行符號。
這樣做有點難看，但確實簡單而有效。

接著我們使用"加入"(append) 方法在列表中加入了一個項目，然後我們通過印出列表的內容來確認這個項目是不是真的已經加進列表中了。
只需簡單地把列表傳遞給"印出"(print) 語句，我們就可以得到一個乾淨的輸出。

接下來，我們使用列表的"排序"(sort) 方法來對列表排序。這個方法會修改到列表本身的內容，
而不是返回一個修改後的列表——這展現了列表是可變的， 與字串是不可變的特性相當地不同。

接著，當我們在市場裡買到第一樣東西的時候，我們想要將這樣東西從列表中刪除。我們可以使用"刪除"(del) 語句來完成這個工作。
我們指出哪個列表中的項目應該被刪除，然後"刪除"(del)語句就為我們從列表中刪除這個項目。
我們使用 "刪除 購物清單[0](0.md)"(del shoplist[0](0.md)) 語句指明我們想要刪除列表中的第一個元素，記住周蟒語言是從0而非從1開始計數。

如果你想要知道列表類別所定義的所有方法，你可以透過使用 "說明(列表)"(help(list)) 命令來取得相關的說明。

## 元組 (Tuple) ##

元組和列表十分相似，只不過元組和字串一樣是 不可變的，即你不能修改元組的內容。
元組的定義方式是在小括弧(圓括號)中使用逗號分隔各個項目。元組通常用在那些語句或函數使用的值不會改變的時候:
```
#!/usr/bin/env zhpy
# 檔名: tuple1.py
動物園 = ('狼', '大象', '企鵝')
印出 '動物園中的動物數目是', 長度(動物園)
新動物園 = ('猴子', '海豚', 動物園)
印出 '新動物園中的動物數目是', 長度(新動物園)
印出 '新動物園中的所有動物有', 新動物園
印出 '從舊動物園過來的動物有', 新動物園[2]
印出 '最後一隻從舊動物園過來的動物是', 新動物園[2][2]
```

輸出結果:
```
$ python tuple1.py
動物園中的動物數目是 3
新動物園中的動物數目是 3
新動物園中的所有動物有 ('猴子', '海豚', ('狼', '大象', '企鵝'))
從舊動物園過來的動物有 ('狼', '大象', '企鵝')
最後一隻從舊動物園過來的動物是 企鵝
```


---

python 版:
```
#!/usr/bin/env python
# File name: tuple1.py
zoo = ('wolf', 'elephant', 'penguin')
print 'Number of animals in the zoo is', len(zoo)
new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in new zoo are', new_zoo
print 'Animals brought from the old zoo are', new_zoo[2]
print 'Last animal brought over from the old zoo is', new_zoo[2][2]
```

python 版輸出結果:
```
$ python tuple1.py
Number of animals in the zoo is 3
Number of animals in the new zoo is 3
All animals in new zoo are ('monkey', 'dolphin', ('wolf', 'elephant', 'penguin'))
Animals brought from the old zoo are ('wolf', 'elephant', 'penguin')
Last animal brought over from the old zoo is penguin
```


---


### 程式如何運作 ###

變量'動物園'(zoo) 是一個包含許多項目的元組，我們看到"長度"(len) 函數可以用來取得元組的長度。這也表示元組同樣也是一個序列。

由於老動物園即將關閉，我們現在得把這些動物轉移到新的動物園裡。
因此，"新動物園"(new\_zoo) 元組中包含了一些已經在那裡的動物和從老動物園帶過來的動物。
回到話題，注意元組之內的組合不會失去它的身份。

如同列表的用法一樣， 我們同樣可以通過在一對中括弧(方括號)中指明某個項目的位置，來存取元組中的項目。
這個動作稱為署名(subscription)或索引(indexing)。
我們使用"新動物園[2](2.md)"(new\_zoo[2](2.md)) 來存取 "新動物園"(new\_zoo) 中的第三個項目。
我們使用"新動物園[2](2.md)[2](2.md)"(new\_zoo[2](2.md)[2](2.md)) 來存取"新動物園[2](2.md)"(new\_zoo[2](2.md)) 項目中的第三個項目。

當你瞭解這個語言特性後，你會發現這種存取項目的方式非常容易.

**給 Perl 使用者的話**

> 列表中的列表不會失去它的身份，即列表不會像 Perl 中那樣被打散。
> 同樣地，元組中的元組，或列表中的元組，或元組中的列表等等都是如此。 在 Python 語言裡，它們都只是另一個物件內所儲存的物件。

## 含有0個或1個項目的元組 ##

一個空的元組由一對空的小括弧(圓括號)組成，如 myempty = ()。

然而，含有單個元素的元組就不那麼簡單了。你必須在第一個（唯一一個）項目後加上一個逗號，
這樣 Python 直譯器才能區分出元組和表達式中一個帶圓括號的物件的不同。
例如， singleton = (2, ) 指明了一個元組， 而 number = (2) 只是一個儲存著數字的變量。

## 元組與 % 運算符 ##

元組最常與 % 運算符一起被使用， 常出現在印出語句中. 下面是一個例子:
```
#!/usr/bin/env zhpy
# File name: tuple2.py
年齡 = 23
名稱 = 'gasolin'
s = '%s 已經 %d 歲了.' % (名稱, 年齡)
印出 s
印出 '為什麼 %s 要玩周蟒哩?' % 名稱
```

輸出結果:
```
$ zhpy tuple2.py
gasolin 已經 26 歲了.
為什麼 %s 要玩周蟒哩?
```


---


python 版:
```
#!/usr/bin/env python
# File name: tuple2.py
age = 26
name = 'Swaroop'
s = '%s is %d years old' % (name, age)
print s
print 'Why is %s playing with that python?' % name
```

python 版輸出結果:
```
$ python tuple2.py
Swaroop is 26 years old
Why is Swaroop playing with that python?
```


---


### 程式如何運作 ###

% 運算符可以使用跟著 % 符號的項目元組的字串，這些字符串具備定制的功能，讓輸出滿足某種特定的格式。
定制的字串的格式可以為 %s， %d 等等. 's' 表示字串， 'd' 表示整數。元組必須按照相同的順序來對應這些定制。

觀察我們使用的第一個元組，首先我們使用字串 %s，來對應元組中的第一個項目變量"名稱"(name)。
而第二個定制是整數的 %d，它對應組合的第二個項目年齡 (age)。

Python 在這裡所做的是把元組中的每個項目轉換成字符串並且用字符串的值替換定制的位置。
因此 %s 被替換為變量 "名稱"(name) 的值，依此類推。

% 運算符使得編寫輸出變得極其簡單，也避免了許多字符串操作。同時它也避免了我們一直以來必須使用的諸多逗號。

在大多數時候，你可以只使用%s定制，而讓 Python 語言直譯器來替你自動將物件轉換成字串。
這種方法對數字同樣有效。然而，我們仍然建議您使用明確的 %d 定制以確保你的程式能正確運行。

在第二個印出語句中，我們使用了一個約定規則。後面跟著%符號後的單個項目——沒有元組。當字串中只有一個定制的時候這方式才有效。

## 字典 (Dictionary) ##

字典類似於聯絡簿， 你可以通過聯絡人名字查找地址和聯絡人詳細情況，即，我們把鍵（名字）和值（詳細情況）聯繫在一起。
注意鍵必須是唯一的，就像如果有兩個人恰巧同名的話，你無法找到正確的信息。

注意，你只能使用不可變的物件（比如字符串）來作為字典的鍵，但是你可以用任何型態的物件當作字典的值。
基本說來就是，你應該只使用簡單的對象作為鍵。

在字典中我們以這樣的方式來標記鍵與值的配對：d = {key1 : value1, key2 : value2 }。
所有字典中的配對都包括在大括弧中，注意鍵與值的配對是使用冒號來作分隔，而各配對則是使用逗號來分隔。

字典中鍵與值的配對是沒有順序的。如果你想要一個特定的順序，那麼你應該在使用前自己對它們排序。

字典是"字典"(dict) 類別的物件(實體):
```
#!/usr/bin/env zhpy
# 檔名: dict1.py
聯絡簿 = { 'Swaroop' : 'swaroop -at- swaroopch.info',
            'Larry' : 'larry -at- wall.org',
            'Matz' : 'matz -at- ruby-lang.org',
            'Spammer' : 'spammer -at- hotmail.com'
}
印出 "Swaroop 的郵件地址是 %s" % 聯絡簿['Swaroop']
# 加入一筆鍵-值對
聯絡簿['Guido'] = 'guido -at- python.org'
# 刪除一筆鍵-值對
刪除 聯絡簿['Spammer']
印出 '\n聯絡簿中有 %d 筆資料\n' % 長度(聯絡簿)
取 名稱, 郵件地址 自 聯絡簿.項目列表():
    印出 '聯絡 %s 透過 %s' % (名稱, 郵件地址)
if 'Guido' 在 聯絡簿:
    印出 "\nGuido 的郵件地址是 %s" % 聯絡簿['Guido']
```

輸出結果:
```
$ zhpy dict1.py
Swaroop 的郵件地址是 swaroop -at- swaroopch.info

聯絡簿中有 4 筆資料

聯絡 Swaroop 透過 swaroop -at- swaroopch.info
聯絡 Larry 透過 larry -at- wall.org
聯絡 Matz 透過 matz -at- ruby-lang.org
聯絡 Guido 透過 guido -at- python.org

Guido 的郵件地址是 guido -at- python.org
```


---


python 版:
```
#!/usr/bin/env python
# File name: dict1.py
# 'ab' is short for 'a'ddress'b'ook
ab = { 'Swaroop' : 'swaroop -at- swaroopch.info',
            'Larry' : 'larry -at- wall.org',
            'Matz' : 'matz -at- ruby-lang.org',
            'Spammer' : 'spammer -at- hotmail.com'
}
print "Swaroop's address is %s" % ab['Swaroop']
# Add a key-value pair
ab['Guido'] = 'guido -at- python.org'
# Deleting a key-value pair
del ab['Spammer']
print '\nThere are %d contacts in the address book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)
if 'Guido' in ab: # OR ab.has_key('Guido')
    print "\nGuido's address is %s" % ab['Guido']
```

python 版輸出結果:
```
$ python dict1.py
Swaroop's address is swaroop -at- swaroopch.info

There are 4 contacts in the address book

Contact Swaroop at swaroop -at- swaroopch.info
Contact Larry at larry -at- wall.org
Contact Matz at matz -at- ruby-lang.org
Contact Guido at guido -at- python.org

Guido's address is guido -at- python.org
```


---


### 程式如何運作 ###

我們使用已經介紹過的格式來建立字典"聯絡簿"(ab)。然後我們使用索引運算元來存取鍵與值的配對。可以看到字典的語法也相當地簡單。

## 關鍵字參數與字典 ##

如果你已經在函數中使用過關鍵字參數，那麼你已經使用過字典了！回想一下——你在函數定義的參數列表中已經使用過鍵與值的配對。
當你在函數中使用變量的時候，它就是使用一個字典的鍵。

無論它是一個函數，模組或類別，這個字典表示的是那個物件的名稱空間。
在編譯器設計的術語中，這個名稱空間字典也被稱為符號表(symbol table)。

## 序列 (Sequences) ##

現在終於可以談談什麼是序列了。列表、組合和字串都是序列的例子，但是序列是什麼?它們為什麼如此特別呢？
序列的兩個主要特點是\*索引運算\*和\*分割運算**。索引運算讓我們可以從序列中抓取一個特定項目。
分割運算讓我們能夠取得序列的一個分割，即序列的一部分:
```
#!/usr/bin/env zhpy
# 檔名: seq.py
購物清單 = ['蘋果', '芒果', '胡蘿蔔', '香蕉']
# 作索引運算
印出 '項目 0 是', 購物清單[0]
印出 '項目 1 是', 購物清單[1]
印出 '項目 2 是', 購物清單[2]
印出 '項目 3 是', 購物清單[3]
印出 '項目 -1 是', 購物清單[-1]
印出 '項目 -2 是', 購物清單[-2]
# 分割一個列表
印出 '項目 1 到 3 項是', 購物清單[1:3]
印出 '項目從第 2 項開始是', 購物清單[2:]
印出 '項目從 1 到 -1 項是', 購物清單[1:-1]
印出 '項目從開始項到結束項是', 購物清單[:]
# 分割一個字串
名稱 = 'swaroop'
印出 '從第 1 個到第 3 個字元是', 名稱[1:3]
印出 '從第 2 個到最後一個字元是', 名稱[2:]
印出 '從第 1 個到第 -1 個字元是', 名稱[1:-1]
印出 '從開始到結束字元是', 名稱[:]
```**

輸出結果:
```
$ zhpy seq.py
項目 0 是 蘋果
項目 1 是 芒果
項目 2 是 胡蘿蔔
項目 3 是 香蕉
項目 -1 是 香蕉
項目 -2 是 胡蘿蔔
項目 1 到 3 項是 ['芒果', '胡蘿蔔']
項目從第 2 項開始是 ['胡蘿蔔', '香蕉']
項目從 1 到 -1 項是 ['芒果', '胡蘿蔔']
項目從開始項到結束項是 ['蘋果', '芒果', '胡蘿蔔', '香蕉']
從第 1 個到第 3 個字元是 wa
從第 2 個到最後一個字元是 aroop
從第 1 個到第 -1 個字元是 waroo
從開始到結束字元是 swaroop
```


---

python 版:
```
#!/usr/bin/env python
# File name: seq.py
shoplist = ['apple', 'mango', 'carrot', 'banana']
# Indexing or 'subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]
# Slicing of a list
print 'Item from position 1 up to position 3 is', shoplist[1:3]
print 'Item from position 2 up to end is', shoplist[2:]
print 'Item from position 1 up to position -1 is', shoplist[1:-1]
print 'Item from start up to end is', shoplist[:]
# Slicing on a string
name = 'swaroop'
print 'Characters from position 1 up to position 3 is', name[1:3]
print 'Characters from position 2 up to end is', name[2:]
print 'Characters from position 1 up to position -1 is', name[1:-1]
print 'Characters from start up to end is', name[:]
```

python 版輸出結果:
```
$ python seq.py
Item 0 is apple
Item 1 is mango
Item 2 is carrot
Item 3 is banana
Item -1 is banana
Item -2 is carrot
Item from position 1 up to position 3 is ['mango', 'carrot']
Item from position 2 up to end is ['carrot', 'banana']
Item from position 1 up to position -1 is ['mango', 'carrot']
Item from start up to end is ['apple', 'mango', 'carrot', 'banana']
Characters from position 1 up to position 3 is wa
Characters from position 2 up to end is aroop
Characters from position 1 up to position -1 is waroo
Characters from start up to end is swaroop
```


---


### 程式如何運作 ###

首先，我們來看看如何使用索引來取得序列中的單個項目。這也被稱作是署名(subscription)運算。
每當你用中括弧(方括號)中的一個數字來指定一個序列的時候，程式會抓取序列中對應位置的項目。
記住 Python 程式語言是從 0 開始計數的。因此，"購物清單[0](0.md)"(shoplist[0](0.md)) 將抓取第一個項目，
而 "購物清單[3](3.md)"(shoplist[3](3.md)) 將抓取 "購物清單"(shoplist) 序列中的第四個項目。

索引同樣可以是負數，在那樣的情況下，位置是從序列的尾端開始計算的。
因此，-1 表示序列的最後一個元素， 而 -2 抓取序列的倒數第二個項目， 依此類推。

分割運算則是透過在序列的名稱後加上中括弧(方括號)， 裡面使用一對用冒號分割的可選數字，來指定序列的特定部份。
注意這與使用索引運算的方式十分相似。記住分割運算裡的數字是可選的，而'冒號'是必須的。

在分割運算中的第一個數字（冒號之前的數字）表示分割開始的位置，第二個數字（冒號之後的數字）表示分割到哪個位置結束。
如果不指定第一個數，Python 就會從序列開頭端開始。如果沒有指定第二個數，則 Python 會在原序列的尾端停止。
注意，返回的序列從開始位置開始 ，而剛好在結束位置之前結束。即開始位置是包含在序列切片中的，而結束位置則被排斥在切片外面。

這樣，"購物清單[1:3]"(shoplist[1:3]) 回傳一個從位置 1 開始，包括位置2，但是停止在位置3的一個新的序列分割。
因此回傳的是一個含有兩個項目的分割。同樣地，"購物清單[:]"(shoplist[:]) 回傳的是整個序列的一個複製品。

你可以用負數表示位置來做分割。負數會從序列尾端開始計算位置。
例如，"購物清單[:-1]"(shoplist[:-1]) 會回傳除了最後一個項目之外包含所有其他項目的序列分割。

例如， 如果你想要移除字串中的換行標示符號， 我們可以這麼做:
```
>>> 行 = '這是一行.\n'
>>> 行
'這是一行.\n'
>>> 如果 行.結尾為('\n'): # '結尾為' 是一個字串(str)類別的屬性
...  行 = 行[:-1]
...
>>> 行
'This is a line.'
```

python 版:
```
>>> s = 'This is a line.\n'
>>> s
'This is a line.\n'
>>> if s.endswith('\n'): # 'endswith' is a method of the str class
...  s = s[:-1]
...
>>> s
'This is a line.'
```

你可以透過周蟒/Python 互動式直譯器來試看看各種組合，並立即得到各種嘗試的結果。
序列最棒的特性是你可以使用一致的方式來存取元組、列表和字串!

## 引用 (References) ##

當你建立一個物件並將這個物件賦予一個變量的時候，變量只能引用這個物件，而不能代表這個物件本身!
換句話說， 變量名稱只是指出你的電腦中存放這個物件的記憶體位置，這被稱作物件名稱繫結.

一般來說， 你不需要擔心這個，只是在引用上， 有些細微的影響需要注意。這將通過下面這個例子來加以說明:
```
#!/usr/bin/env zhpy
# 檔名: ref.py
印出 '簡單項目分派'
購物清單 = ['蘋果', '芒果', '胡蘿蔔', '香蕉']
我的清單 = 購物清單 # "我的清單"只是另一個同樣指向相同物件的名稱
印出 '購物清單是', 購物清單
印出 '我的清單是', 我的清單
印出 '移除第一個項目'
刪除 購物清單[0] # 我買到了第一個項目，所以我把清單中的第一個項目移除了
印出 '購物清單是', 購物清單
印出 '我的清單是', 我的清單
# 注意到兩個清單印出了相同的列表
印出 '透過使用完整分割來複製列表'
我的清單 = 購物清單[:] # 使用完整分割來複製列表
刪除 我的清單[0] # 移除第一個項目
印出 '購物清單是', 購物清單
印出 '我的清單是', 我的清單
# 注意到現在兩個清單不同了
```

輸出結果:
```
$ zhpy ref.py
簡單項目分派
購物清單是 ['蘋果', '芒果', '胡蘿蔔', '香蕉']
我的清單是 ['蘋果', '芒果', '胡蘿蔔', '香蕉']
移除第一個項目
購物清單是 ['mango', 'carrot', 'banana']
我的清單是 ['mango', 'carrot', 'banana']
透過使用完整分割來複製列表
購物清單是 ['mango', 'carrot', 'banana']
我的清單是 ['carrot', 'banana']
```


---

python 版:
```
#!/usr/bin/env python
# File name: ref.py
print 'Simple assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object
print 'shoplist is', shoplist
print 'mylist is', mylist
print 'Removing first item'
del shoplist[0] # I purchased the first item, so I am removing it from the list
print 'shoplist is', shoplist
print 'mylist is', mylist
# Notice that both shoplist and mylist both print the same list
print 'Copy by making a full slice'
mylist = shoplist[:] # Make a copy by doing a full slicing
del mylist[0] # Remove first item
print 'shoplist is', shoplist
print 'mylist is', mylist
# Notice that now shoplist and mylist are different
```

python 版輸出結果:
```
$ python ref.py
Simple assignment
shoplist is ['apple', 'mango', 'carrot', 'banana']
mylist is ['apple', 'mango', 'carrot', 'banana']
Removing first item
shoplist is ['mango', 'carrot', 'banana']
mylist is ['mango', 'carrot', 'banana']
Copy by making a full slice
shoplist is ['mango', 'carrot', 'banana']
mylist is ['carrot', 'banana']
```


---


### 程式如何運作 ###

注意當 "我的清單 = 購物清單"(mylist = shoplist) 語句運行的時候，兩個名稱都指向同樣的物件。
因此當我們移除"購物清單"(shoplist) 中第一個項目的時候，"我的清單"(mylist) 也會顯示有個項目被移除了。

如果我們想要真的複製 "購物清單"(shoplist) 並儲存到"我的清單"(mylist)，那麼我們必須使用分割運算來複製。

只是將一個名稱賦給另一個名稱的情況下，兩個名稱都將引用同一個物件，而並不會複製一個新的物件。

**給 Perl 使用者的話**

> 記得列表的賦值語句並不建立一個新的拷貝。你得使用分割運算來複製一個序列。

# 結語 #

我們已經詳細探討了多種 Python 內建的資料結構。這些資料結構將是編寫程式時至關重要的部分。

我高度建議你在繼續閱讀本書前先瀏覽 說明(字串)(help(str))、說明(列表)(help(list))、
說明(元組)(help(tuple))、說明(字典)(help(dict)) 的內容。

接下來我們將學習如何設計和編寫一個實用的周蟒/Python程式。

[模組](ZhpyModules.md) | [解決問題](SolvingProblem.md)