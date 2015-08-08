# 簡介 #

到目前為止，在我們討論過的程式中，我們都是透過使用函式和存取資料的語句區塊來設計我們的程式。這被稱為「流程導向的程式設計」。
還有另一種設計和組織程式的方法，那就是將「資料」和「功能」結合起來，封裝在一個稱為「物件」的東西中。這種方法稱為「物件導向的程式設計」。

在大多數時候，你可以使用流程式的方法來設計程式。但是有些時候當你想要編寫大型程式，或是尋求一個更加合適的解決方案的時候，你也可以使用物件導向的程式設計這個設計方式。

「類別」和「物件」是物件導向的程式設計的兩個主要方面。我們可以透過宣告「類別」(class) 的語句區塊來建立一個新的型別(type)；「物件」(objects)就是依賴這個「類別」所產生的實體(instance)。

比如你有一個整數(int)型別的變量，這個存儲整數「型別」(type) 的變量，即是整數(int)「類別」(class) 的物件實體（Object）。

**給 C++/Java/C# 使用者的話**

> C# 和 Java (>1.5) 程式設計者會覺得這個概念相當熟悉，因為它與封裝與解封裝的概念相似。
> 注意，在周蟒與 Python 語言中，即使整數也被視為是物件（請參考 "說明(整數)"(help(int))）。
> 這與 C++ 或 Java（< 1.5）將整數視為內建型別是不同的。

**(譯註)給初次接觸「物件導向程式設計」者的話**

> 本書並沒有特別解釋物件導向程式設計的概念，另提供 [wikipedia](http://zh.wikipedia.org/w/index.php?title=%E7%89%A9%E4%BB%B6%E5%B0%8E%E5%90%91&variant=zh-tw)  說明可以自行參考。

物件可以使用普通屬於物件的變量來儲存資料。屬於一個物件或類別的變量被稱為「欄位」(fields)。

物件也可以透過使用「屬於類別的函式」來使物件自身擁有函式的功能。這樣的函式被稱為類別的"方法"(method)。

這些術語相當重要，因為這些術語能幫助我們將"類別方法與欄位"和"函式與變量"區分開來。

"函式與變量"可以獨立使用，而"類別方法與欄位"必須和類別或物件一同使用。"欄位"和"類別方法"可以合稱為類別的「屬性」(property)。

欄位有兩種類型——欄位可以屬於個別實體/類別的物件，或者屬於類別本身。它們分別被稱為實體變量和類別變量。

我們可以使用"類別"(class) 關鍵字建立一個新的類別。屬於類別的欄位和類別方法則列在這個類別的縮排區塊中。

## "我"(self) 屬性 ##

類別方法與普通函式之間只有一個明顯地區別—— 在參數列表的開頭，類別方法必須有一個額外的參數，
但是在呼叫這個方法的時候你並不需要為這個參數賦值，因為周蟒和 Python 會自行提供這個參數的值。
這個特別的變量會指向呼叫這個類別方法的物件本身，因此按照慣例，這個變量的名稱是"我"(self)。

雖然你可以給這個參數任何名稱，但是我強烈建議你使用"我"(self)這個名稱——不要使用其他名稱。
使用一個標準的名稱有很多優點——你的編輯器可以高亮度顯示"我"(self)變量，而且閱讀你的程式的讀者也可以迅速地識別它。

**給 C++/Java/C# 使用者的話**

> 周蟒與 Python 語言中的"我"(self)等同於 C++ 中的 self 指針和 Java、C# 中的 this 參考。

你一定很想知道周蟒與 Python 語言如何對"我"(self)這個變量賦值以及為何你不需要直接對這個變量賦值。
雖然你必須明確地指定這個變數給類別方法的變量列表。舉一個例子來試著解釋這個情形。
假如你有一個叫"我的類別"(MyClass) 的類別，和這個類別的一個實體"我的物件"(MyObject)。
當你呼叫這個物件的方法

```
我的物件.方法(參數1, 參數2)
```

的時候，這個方法會由周蟒或 Python 直譯器自動轉換成
```
我的類別.方法(我的物件, 參數1, 參數2)
```


---


python 版:
```
MyObject.method(arg1, arg2)
```

python 版:
```
MyClass.method(MyObject, arg1, arg2)
```


---


——這就是"我"(self)這個參數的特別之處了。

這也意味著如果你有一個不需要參數的方法，你還是需要為這個方法定義一個"我"(self)參數。

## 類別 (Classes) ##

下面這個例子是一個盡可能簡單的類別例子:
```
#!/usr/bin/env zhpy
# 檔名: class1.py
類別 人:
    略過
哈利 = 人()
印出 哈利
```

輸出結果:
```
$ zhpy class1.py
<__main__.Person instance at 0x6c2b0>
```


---


python 版:
```
#!/usr/bin/env python
# File name: class1.py
class Person:
    pass
p = Person()
print p
```

python 版輸出結果:
```
$ python class1.py
<__main__.Person instance at 0x6c2b0>
```


---


### 程式如何運作 ###

我們使用"類別"(class) 語句後接著一個類別名稱來建立了一個新的類別。這個語句後面接著一個可選的括弧對，裡面可以包含類別的列表。
在這個例子中我們並不指定額外的類別列表-這會在稍後的章節中解釋。
接著，這行語句以冒號結束。其下則包含一個縮排的包含了類別欄位跟方法語句的程式區塊。
在這個例子中，我們並未宣告任何類別欄位或類別方法，我們使用 pass 語句來表示一個空白區塊。

接下來，我們建立了這個類別的一個物件/實體， 類別的物件/實體可以透過使用類別名稱後加上一對括弧對來建立。
我們將在下面的章節中學習更多的如何創建實體的方法。我們簡單地透過印出命令來確認這個變量的型別。
印出結果告訴我們在 main 模組中我們有了一個 Person 類別的實體。

注意到如何實體化類別的實體的方式跟呼叫函式的方式極為相似. 這是周蟒與 Python 語言提倡"簡單化"的又一個例子。
這個特點為什麼很重要? 因為你可以在不知道它內部如何運作的情況下一致地使用類別或函式，
回想一個例子，你還記得我們之前使用"整數"(int) 函式來將一個字串轉換成整數嗎? 我們可以使用"整數(5)"(int('5')) 函式來取得整數 5 !
事實上，恩，我們講的"整數"(int) 函式其實是個類別，而不是函式。詳情可參照"說明(整數)" (help(int))。

可以注意到儲存該物件的記憶體的位址也被印了出來。這個位址在你的電腦上會是另外一個值，
因為周蟒與 Python 直譯器可以在任何空的記憶體空間中保存物件。

## 物件方法 (Object Methods) ##

我們已經討論了類別和物件可以擁有類別方法，這些類別方法與函式相似，兩者的區別只是類別方法需要一個額外的"我"(self) 變量。
現在我們來看一個例子:
```
#!/usr/bin/env zhpy
# 檔名: method.py
類別 人:
    定義 說嗨(我):
        印出 '哈囉, 你好嗎?'
哈利 = 人()
哈利.說嗨()
# 這個簡短的例子也能寫成 人().說嗨()
```

輸出結果:
```
$ zhpy method.py
哈囉, 你好嗎?
```


---

python 版:
```
#!/usr/bin/env python
# File name: method.py
class Person:
    def say_hi(self):
        print 'Hello, how are you?'
p = Person()
p.say_hi()
# This short example can also be written as Person().say_hi()
```

python 版輸出結果:
```
$ python method.py
Hello, how are you?
```


---


### 程式如何運作 ###

這裡我們看到了"我"(self)參數的用法。你應該注意到"說嗨"(say\_hi) 這個類別方法並未取用任何參數，
但仍然在定義函式時將"我"(self)參數列入參數列表中。

## 初始化(init) 類別方法 ##

在周蟒與 Python 語言的類別中有很多類別方法的名字有特殊的重要意義。在這節中我們將學習初始化(init)類別方法的重要意義。

初始化(init)類別方法是當從類別初始化一個物件時，立即會運行的類別方法。
這個類別方法相當有用，可以依你希望的方式來初始化你的物件。注意，初始化(init)這個類別方法是以兩個底線作為名稱的開始與結尾:
```
#!/usr/bin/env zhpy
# 檔名: class_init.py
類別 人:

    定義 __初始化__(我, 名稱):
        我.名稱 = 名稱

    定義 說嗨(我):
        印出 '哈囉, 我的名字是', 我.名稱
哈利 = 人('Swaroop')
哈利.說嗨()
```

輸出結果:
```
$ zhpy class_init.py
哈囉, 我的名字是 Swaroop
```


---


python 版:
```
#!/usr/bin/env python
# File name: class_init.py
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, my name is', self.name
p = Person('Swaroop')
p.say_hi()
```

python 版輸出結果:
```
$ python class_init.py
Hello, my name is Swaroop
```


---


### 程式如何運作 ###

我們定義"初始化"(init) 類別方法時取用了一個"名稱"(name) 參數（加在普通的參數"我"(self) 之後），
賦給"名稱"(name) 參數一個值然後將它儲存到一個叫做"我.名稱"(self.name) 的欄位中。
注意它們是兩個不同的變量，雖然它們擁有相同的名字。這是因為他們擁有不同得名稱空間的原故。
在"初始化"(init) 類別方法中的名稱和 self.name 變量存在於特定的實體中。點號表示法能幫助我們來區分它們。

現在，我們能夠在我們的 say\_hi 類別方法中使用"我.名稱"(self.name)這個欄位。並且使用"我.名稱"(self.name)欄位來印出更多特定的訊息。

**給 C++/Java/C# 使用者的話**

> "初始化"(init) 類別方法可以類比於 C++，C#， Java 中的 _constructor_

## 類別與物件變量 (Object Variables) ##

我們已經討論過一部分類別與物件的功能， 現在我們將學習類別與物件的資料部份。
資料欄位並沒有什麼特別之處， 除了資料欄位的名稱必須與類別或物件的名稱空間繫結在一起。
即欄位的名稱只存在於類別或物件之中. 類別變量是類別所擁有的變量。物件變量則是物件所擁有的變量。

類別變量是分享的。 類別變量可以讓屬於該類別的所有物件/實體存取。
類別變量只有一份副本，當任何物件修改了類別變量，這個改變會影響到所有其他的實體。

物件變量是由該類別的物件/實體所各自擁有的。在這個例子裡，各個物件都有他自己的一份物件變量欄位的副本。
即這些物件變量欄位並不與其他物件分享，其中所存的資料與其他物件中同名的物件變量所存的資料無關:
```
#!/usr/bin/env zhpy
# 檔名: objvar.py
類別 人:
    '''表示一個人.'''
    人數 = 0 # 類別變量

    定義 __初始化__(我, 名稱):
        '''初始化這個人的資料.'''
        我.名稱 = 名稱 # 物件變量
        印出 '(初始化 %s)' % 我.名稱

        # 當建立這個人的物件時候, 將他/她加入人口數中
        人.人數 += 1

    定義 __刪除__(我):
        '''這個人要死了.'''
        印出 '%s 離開了.' % self.name

        人.人數 -= 1

        如果 人.人數 == 0:
            印出 '我是最後一個人.'
        否則:
            印出 '還剩 %d 個人.' % 人.人數

    定義 說嗨(我):
        '''這個人講的歡迎語.

        恩，就是這樣啦.'''
        印出 '哈囉, 我的名字是', 我.名稱

    定義 有多少(cls):
        '''印出當前人數.'''
        如果 人.人數 == 0:
            印出 '這裡沒有人.'
        不然 人.人數 == 1:
            印出 '只有一個人在這.'
        否則:
            印出 '這裡有 %d 個人.' % 人.人數
    有多少 = 類別方法(有多少)
swaroop = 人('Swaroop')
swaroop.說嗨()
人.有多少()
kalam = 人('Abdul Kalam')
kalam.說嗨()
人.有多少()
swaroop.說嗨()
人.有多少()
```

輸出結果:
```
$ zhpy objvar.py
(初始化 Swaroop)
哈囉, 我的名字是 Swaroop.
只有一個人在這.
(初始化 Abdul Kalam)
哈囉, 我的名字是 Abdul Kalam.
這裡有 2 個人.
哈囉, 我的名字是 Swaroop.
這裡有 2 個人.
Abdul Kalam 離開了.
還剩 1 個人.
Swaroop 離開了.
我是最後一個人.
```


---


python 版:
```
#!/usr/bin/env python
# File name: objvar.py
class Person:
    '''Represents a person.'''
    population = 0 # class variable

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name # object variable
        print '(Initializing %s)' % self.name

        # When this person is created， he/she adds to the population
        Person.population += 1

    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name

        Person.population -= 1

        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def say_hi(self):
        '''Greeting by the person.

        Really， that's all it does.'''
        print 'Hi， my name is %s.' % self.name

    def how_many(cls):
        '''Prints the current population.'''
        if Person.population == 0:
            print 'Nobody is alive as of now.'
        elif Person.population == 1:
            print 'There is just one person here.'
        else:
            print 'We have %d persons here.' % Person.population
    how_many = classmethod(how_many)
swaroop = Person('Swaroop')
swaroop.say_hi()
Person.how_many()
kalam = Person('Abdul Kalam')
kalam.say_hi()
Person.how_many()
swaroop.say_hi()
Person.how_many()
```

python 版輸出結果:
```
$ python objvar.py
(Initializing Swaroop)
Hi， my name is Swaroop.
There is just one person here.
(Initializing Abdul Kalam)
Hi， my name is Abdul Kalam.
We have 2 persons here.
Hi， my name is Swaroop.
We have 2 persons here.
Abdul Kalam says bye.
There are still 1 people left.
Swaroop says bye.
I am the last one.
```


---


### 程式如何運作 ###

這個例子有點長，但是它有助於我們瞭解類別與物件的本質。

"人數"(population)變量屬於"人"(Person) 類別，因此它是一個類別變量。
"名稱"(name) 變量屬於物件，因為它使用"我"(self) 參數來賦值，所以它是一個物件變量。
注意我們使用"人.人數"(Person.population) 來參考"人數"(population) 類別變量而不是使用"我.人數"(self.population) 來參考。
類別變量屬於類別，所以它應該使用類別名稱點號表示法存取。物件變量屬於物件，所以它應該使用物件名稱(self)點號表示法存取。

"初始化"(init) 類別方法被用來初始化"人"(Person) 實體。在此我們藉由提供一個"名稱"(name) 參數來初始化"人"(Person) 類別.
這樣一來各個實體都各有一個名字. 我們用相同於"名稱"(name)參數的值來初始化一個物件變量"我.名稱"(self.name) 時，我們也將"人.人數"(Person.population) 參數的值累增1。
因為我們加入了一個新"人"(person)， 應該要算進"人數"(population) 中.

在類別方法中 (包含 "初始化"(init) 和其他特別的類別方法)，
你可以使用 "我.類別方法名稱" 或 "我.欄位名稱" 這樣的點號表示法來參考屬於該物件的類別方法和欄位。
這特性稱作屬性參照。

我們也學習到類別和類別方法中的文件字串的使用方法。
我們可以在運行中使用欄位"人.文件"(Person.doc) 和類別方法的文件字串
"人.說嗨.文件"(Person.say\_hi.doc) 來存取類別的文件字串。

類同於"初始化"(init)類別方法， "刪除"(del) 類別方法是另一個特殊的類別方法，
在物件將消亡的時候會呼叫到"刪除"(del) 這個類別方法。
即當物件不再被使用而且將被系統消滅以釋放記憶體空間時會呼叫到這個類別方法。
在這例子中用到"刪除"(del) 類別方法的目的是在減少一個"人"(Person)物件的時候將人數減1。
"刪除"(del) 類別方法具有特殊的語意，因為當物件將消亡的時候，Python 直譯器會自動調用它。這個名字本身倒是沒有什麼特別的意義。

要注意的是所有資料欄位預設都是"公開"(Public) 的。可以在任何其他的物件中存取這些資料欄位。
你可以使用以兩個底線為開頭的"屬性"(attributes)來讓其他的物件不能存取這些資料欄位。
舉個例子，如果你有一個"我.私有 "(self.private) 資料欄位，則其他的物件無法存取這個欄位。

**給 C++/Java/C# 使用者的話**

> 所有類別方法在周蟒與 Python 語言中都是虛擬(virtual)的.

> 幾乎所有的周蟒與 Python 專案都遵循的約定是任何屬於類別/物件"內部"的變量都以一個底線為開頭 (例如"我.私有 "(self.private) )，
> 而所有其他的名稱都是公開(Public)並且可以讓其他類別/物件使用的。記得這只是個約定，周蟒與 Python 語言並不強制你非得這麼做。

> "刪除"(del) 類別方法可以類比於解構子 (destructor) 的概念

## 繼承 (Inheritance) ##

物件導向程式設計得一個主要優點是"程式碼重用"(code reuse) 而達到程式碼重用其中的一個途徑就是透過類別的繼承機制。
類別的繼承機制可以想成兩個類別是主要類型跟子類型的關係。

假設你想要寫一個程式來追蹤校園裡師生的情況。老師與學生有許多共同的特徵(屬性)，例如都有姓名(name)、年齡(age)、和住址(address)。
他們也都有各自的一些特殊屬性，例如老師的薪水(salary)、課程(courses)、和假期(leaves)，學生的成績(Marks)和學費(fees)。

你可以為師生這兩個類型建立兩個各自獨立的類別，
但是加入一個新的共同的特徵則表示你需要在這兩個各自獨立的類別裡分別加入新的共同的特徵。這麼做很快就會開始出問題.

比較好得替代方式則是建立一個共同的稱為"學校成員"(SchoolMember) 類別，
並且讓"老師"(teacher)，"學生"(student)類別各自繼承自"學校成員"(SchoolMember)類別。
即師生類別變成學校成員類別的副型態。我們可以將特自特殊的欄位加入這些副型態類別。

這種方式有許多優點。如果我們加入/修改任何"學校成員"(SchoolMember)類別，這修改會自動影響到副型態的類別。
舉個例子， 你可以透過在"學校成員"(SchoolMember)類別加入一個新的"識別卡"(ID-card) 欄位來簡單地替老師，學生類別加入這個欄位。

另一個優點則是你可以透過"學校成員"(SchoolMember)類別來蒐集師，生類別的動態。在一些諸如計算學校成員總數的情況下相當有用。
這個特性稱為"多態 (polymorphism)"，子型態可以在任何情形下取代任何需要父型態的情形。

我們觀察到程式碼重用的主要方式是因為我們將一些共同的特徵放在父類別中，因此子類別就可以透過繼承父類別來重用這些共同的特徵。

"學校成員"(SchoolMember)類別可以被稱作一個基本類別或超級類別，"老師"、"學生"類別則可以被稱作衍生類別或子類別。

我們這就編寫個例子試試看吧:
```
#!/usr/bin/env zhpy
# 檔名: inherit.py
類別 學校成員:
    '''表示任何學校成員.'''
    定義 __初始化__(我, 名稱, 年齡):
        我.名稱 = 名稱
        我.年齡 = 年齡
        印出 '(初始化 學校成員 %s)' % 我.名稱

    定義 __字串__(我):
        '''學校成員以字串表示.'''
        return '名稱:"%s" 年齡:"%s"' % (我.名稱, 我.年齡)
class 老師(學校成員):
    '''表示一名老師.'''

    定義 __初始化__(我, 名稱, 年齡, 月薪):
        學校成員.__初始化__(我, 名稱, 年齡)
        我.月薪 =月薪
        印出 '(初始化 老師 %s)' % 我.名稱

    定義 __字串__(我):
        返回 '%s 月薪:"%d"' % (學校成員.__字串__(我), 我.月薪)
class 學生(學校成員):
    '''表示一名學生.'''

    定義 __初始化__(我, 名稱, 年齡, 成績):
        學校成員.__初始化__(我, 名稱, 年齡)
        我.成績 = 成績
        印出 '(初始化 學生 %s)' % 我.名稱

    定義 __字串__(我):
        返回 '%s 成績:"%d"' % (學校成員.__字串__(我), 我.成績)
t = 老師('Mrs. Shrividya', 40, 30000)
s = 學生('Swaroop', 23, 75)
印出 # 印出一行空行
成員們 = [t, s]
取 成員 自 成員們:
    印出 成員 # 同樣適用於老師與學生
```

輸出結果:
```
$ zhpy inherit.py
(初始化 學校成員 Mrs. Shrividya)
(初始化 老師 Mrs. Shrividya)
(初始化 學校成員 Swaroop)
(初始化 學生 Swaroop)

名稱:"Mrs. Shrividya" 年齡:"40" 月薪:"30000"
名稱:"Swaroop" 年齡:"23" 成績:"75"
```


---


python 版:
```
#!/usr/bin/env python
# File name: inherit.py
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember %s)' % self.name

    def __str__(self):
        '''Represent the school member as a string.'''
        return 'Name:"%s" Age:"%s"' % (self.name, self.age)
class Teacher(SchoolMember):
    '''Represents a teacher.'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher %s)' % self.name

    def __str__(self):
        return '%s Salary:"%d"' % (SchoolMember.__str__(self), self.salary)
class Student(SchoolMember):
    '''Represents a student.'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student %s)' % self.name

    def __str__(self):
        return '%s Marks:"%d"' % (SchoolMember.__str__(self), self.marks)
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 23, 75)
print # prints a blank line
members = [t, s]
for member in members:
    print member # works for both Teachers and Students
```


python 版輸出結果:
```
$ python inherit.py
(Initialized SchoolMember Mrs. Shrividya)
(Initialized Teacher Mrs. Shrividya)
(Initialized SchoolMember Swaroop)
(Initialized Student Swaroop)

Name:"Mrs. Shrividya" Age:"40" Salary:"30000"
Name:"Swaroop" Age:"23" Marks:"75"
```


---


### 程式如何運作 ###

為了讓類別能繼承，我們定義類別時在類別名稱後的括號中指定基底類別名稱。

注意在衍生類別裡，我們明確地呼叫基底類別的"初始化"(init) 類別方法，因此基底類別中的物件可以被初始化到。
這點相當值得注意 - 周蟒與Python 語言並不自動呼叫基底類別的建構子，你必須自行明確地呼叫基底類別的建構子。

同樣我們也觀察到，我們可以使用點號表示法來呼叫基底類別的類別方法，並明確地傳遞"我"(self) 參數到那些類別方法中。

"字串"(str) 類別方法是另一個具有特殊語意的類別方法 - 當周蟒與 Python 直譯器需要字串化顯示這個物件時就會呼叫這個類別方法。
例如在我們的程式裡我們寫 "印出 成員"(print member)，我們需要一個印出物件的方法。
因此周蟒或 Python 呼叫這個物件的"字串"(str) 類別方法並印出這個類別方法得輸出結果到螢幕上。

注意當我們使用"取..自"(for..in) 迴圈時，可以將師、生的實體都視作學校成員的實體。
並取得學校成員的"名稱"(name)，年齡(age) 參數。這就是能用上多形之處。

如果師， 生類別並不包含各自的"字串"(str) 類別方法，
則周蟒與 Python 直譯器將到基底類別中找尋是否有有定義有"字串"(str) 這個同名的類別方法的類別，
在這個例子裡就是"學校成員"(SchoolMember) 類別定義有"字串"(str) 這個同名的類別方法。
周蟒與 Python 直譯器將會呼叫這個同名的類別方法。你可以試著將任何衍生類別的"字串"(str) 定義拿掉來試試是否如此。


# 結語 #

我們已經探討類別和物件的許多方方面面，並介紹了許多相關詞彙。我們也已經看到了物件導向程式設計的一些優缺點。

Python 語言是一種高度物件導向程式設計的語言，因此瞭解物件和類別的名詞有助於編寫和瞭解周蟒與 Python 程式如何運作。

接下來， 我們將學習如何用周蟒語言處理輸入/輸出和處理檔案。

[解決問題](SolvingProblem.md) | [輸入, 輸出](InputOutput.md)