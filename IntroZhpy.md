Python 語言是少數能理直氣壯地宣稱自己是「既簡單又強大」的程式語言。

使用 Python 語言時，你會發現很容易就能將精力專注在解決問題上，而不是把時間花在搞清楚程式本身的語法和結構上。

周蟒是一個輕量的，與 Python 語言互相兼容的中文 Python 語言。使用周蟒讓你能透過中文學習，使用所有 Python 語言的特性，降低了學習程式語言必先熟悉英文後才能學習的門檻。

理解周蟒程式語言，即理解 Python 程式語言。

Python 語言的官方介紹如下：

```
Python 語言是一種簡單易學、功能強大的程式語言。它具有高效率的高階資料結構、簡單而有效的物件導向程式設計方式。
Python 語言具有簡潔的語法、動態的型別、和直譯式語言的本質。由於擁有這些特質，使得 Python 語言成為多數作業系統平台上，與眾多的應用領域裡，用作處理程式腳本、快速開發應用程式的理想程式語言。
```

我們會在下一節裡進一步討論周蟒與 Python 語言所共同擁有的特點。在後文中可能長常見到穿插使用周蟒與 Python 語言兩個詞彙的情形，因為兩者在大部份的使用情況下並無不同。

# Python 語言的特色 #

## 簡單 (Simple) ##

Python 語言是個奉行極簡主義的語言，閱讀一篇良好的 Python 程式就好像是在讀文章一樣，只是這種文章對格式的要求更為嚴格。

這種以接近自然語言的方式來描述程式邏輯(或稱為虛擬碼)的本質，是 Python 語言最大的優點之一。

## 易學 (Easy to Learn) ##

如同你即將見到的，Python 語言有極其簡單的語法，也極其容易上手。

## 自由、開放(Free and Open Source) ##

Python 語言是自由/開放原始碼軟體 (FOSS) 的範例之一。自由/開放原始碼軟體 (FOSS) 是基於社群應該分享彼此知識的概念。簡單地說來，你可以自由地散佈 Python 語言，允許複製、閱讀、修改它的原始碼、或是使用一部分程式於其他的自由軟體中。

Python 誕生之後就持續地被一個希望看到它更加優秀的社群改進著，這就是 Python 程式語言為何如此優秀的原因之一。

## 高階語言(High-level Language) ##

當你使用 Python 語言編寫程式的時候，你無需考慮諸如該怎麼管理程式使用的記憶體等底層細節。

## 可移植性 (Portable) ##

由於 Python 語言開放原始碼的本質，Python 語言已經被移植到（經過修改而使得 Python 能夠工作在）許多平台上。

這些平台包括 Linux、Windows、FreeBSD、Mac OS、Solaris、OS/2、Amiga、AROS、AS/400、 BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE、PocketPC， 甚至你還可以在 Nokia 60 系列手機上執行 Python 語言。

如果你能避免使用系統專屬的特性，那麼所有的 Python 程式應該無需修改就能在大多數的平台上執行。

## 直譯式 (Interpreted) ##

'直譯式'這個特性需要進一步多作一些解釋。

使用比如 C 或 C++ 這樣的編譯式語言寫程式時，會透過編譯器，在設定許多旗標和選項之後，將程式從原始碼編譯(轉換)成電腦能直接讀懂的語言（二進制碼，即 0 和 1）。

當你執行程式的時候，連結器(linker)/載入器(loader)會將編譯好的程式從硬碟複製到記憶體內，並開始執行。

Python 語言寫的程式則不需要預先編譯成二進位碼。 將寫好的 Python 程式，直接拿來執行就是了。

Python 語言則依循著另一種方式。寫好的程式不需要預先編譯成二進位碼。 你只要將寫好的 Python 程式，直接拿來執行就是了。Python 直譯器會自行將程式碼轉換成一種稱為位元碼 (bytecodes) 的中間形式，Python 直譯器內部會自行將原始檔轉成一種稱為「位元碼」(bytecodes)的中介格式，再轉換成你的電腦能讀懂的原生語言形式，再開始執行。
由於編寫程式時，我們不需要擔心怎麼編譯程式，或考慮函式庫如何設定才能正確連結並載入等等繁瑣的事，使得 Python 更加易於移植。因為只要將寫好的 Python 程式到另外一台電腦上，這個 Python 程式就可以執行。

## 物件導向 (Object-oriented) ##

Python 語言既支持流程導向程式設計，也支持物件導向程式設計。在''流程導向''的程式語言中，程式是藉由描述軟體的執行過程(流程)，與可以重複使用的函式所組織起來的。而在''物件導向''的程式語言中，程式是由一個個包含資料與運作方法的'物件'所組織起來的。Python 語言使用了一種非常強大，卻又簡明的方式，來實現物件導向程式設計 (OOP)，特別是當對比於那些像 C++ 或 Java 這樣龐大的程式語言。

## 擴充性 (Extensible) ##

如果你的某部份程式必需要運作得特別快速，或是某些關鍵演算法不希望公開，你可以使用 c 或 c++ 語言來設計這段程式碼，並在 Python 程式中呼叫使用。

## 可嵌入性 (Embeddable) ##

你可以把 Python 語言嵌入你的 C/C++ 程式中，好在程式中提供讓使用者可以自由運用的'腳本 (script)'功能。

## 豐富的函式庫 (Extensive Libraries) ##

Python 語言的標準函式庫相當龐大，這些函式庫能幫助你處理各種工作，比如處理正則表達式、產生文件、單元測試、線程、資料庫、網頁瀏覽器、CGI、 FTP、電子郵件、XML、XML-RPC、HTML、聲音資料、加密、圖形化介面(GUI)、與各種與系統相關的功能。
別忘了，當你安裝好了 Python 語言的時候，這些標準函式庫就已經能隨意供你使用。這被稱作 Python 語言的 "開箱即用"(Batteries Included) 哲學。

除了這些標準函式庫之外，Python 語言還有大量的高質量函式庫與眾多現成工具可供使用。例如 [wxPython](http://www.wxpython.org)、[Twisted](http://www.twistedmatrix.com/products/twisted)、[http://www.pythonware.com/products/pil/index.htm Python

你可以造訪 Python 程式庫網站 (Python Cheeseshop) 來查看 Python 函式庫的列表。

http://cheeseshop.python.org/pypi

# 結語 (Summary) #

Python 語言實在是一門既精彩又強大的程式語言。它合理地結合了高性能，與那些讓編寫程式這件事變得既簡單又有趣的特色。使用 Python 語言寫程式既有趣，又容易。透過周蟒，我們還可以透過中文語句，更直覺地來學習這門精彩的程式語言。

**為什麼不用 Perl 語言？**

> 也許你還不知道，Perl 語言是另外一種非常流行的開放原始碼直譯式程式語言。

> 如果你曾嘗試使用過 Perl 語言編寫一個大程式，你大概也能自己回答「為什麼不用 Perl 語言」這問題！換句話說，Perl 語言很適合寫作小型的應用程式和腳本，它能簡單的讓你「完成工作」。然而，一旦你使用 Perl 語言開始編寫一些大一點的程式的時候，Perl 語言就顯得不夠靈便了。這麼說是基於我在 Yahoo! 寫作大型 Perl 語言程式的經驗！

> 與 Perl 程式相比，Python 程式更簡單清晰、易於編寫，也更加容易理解與維護。

> 我個人也喜歡 Perl 語言，並使用它來處理日常碰到的問題。但是當我開始寫一個程式的時候，我總是用 Python 語言的方式來思考問題。因為使用 Python 語言的方式來思考，對我而言是那麼地自然。 Perl 語言經過那麼久的修改和演變，讓它變成一個渾身是補釘的產物。即使是在即將提出的 Perl 6 版本，這種情況也不會改善。

> 我覺得 Perl 語言唯一所剩的一個重要優勢，就是它擁有一個巨大的 Perl 程式函式資料庫: CPAN (Perl 語言資料大全網 Comprehensive Perl Archive Network)。就如同 CPAN 這個名字所指的意思，CPAN 蒐集了龐大的各種 Perl 模組資料，它的深度廣度都讓人難以置信——你幾乎可以使用這些模組讓電腦做任何事情。Perl 語言的模組比 Python 語言的模組多，原因之一是 Perl 語言擁有比 Python 語言更加悠久的歷史。 隨著Python 套件索引(Python Package Index, pypi) 的成長，這個優勢正在改變。

## 為什麼不用 Ruby 語言？ ##

也許你還不知道，Ruby 語言是另外一種非常流行的開放原始碼直譯式程式語言。

如果你已經很開心地在使用 Ruby 語言了，我會建議你繼續地使用下去。

對於那些尚未使用過 Ruby 語言，而試著在決定要學 Python 語言或學 Ruby 語言的人，純以簡單易學的角度來看，我會建議你來學習 Python 語言。

個人覺得我讀不太懂 Ruby 語言。但是那些學懂了 Ruby 語言的人，卻都讚嘆著 Ruby 語言的美麗。可能是我不夠聰明吧。

## 聽聽其他程式設計者怎麼說 ##

你可能會對像 ESR 這樣偉大的黑客們怎麼談論 Python 語言感興趣：

**艾力克 S 雷蒙 (Eric S Raymond)**

> 艾力克 S 雷蒙是 <教堂與市集> 一文的作者，享譽於開放原始碼與 Linux 社群。

> 他說道：「Python 已經成為我最愛的程式語言。」他的 'Why Python?' 這篇文章這篇文章也是促使我第一次接觸 Python 語言的原因。

> http://www.linuxjournal.com/article/3882

**布魯斯.艾可 (Bruce Eckel)**

> 布魯斯.艾可是著名的《Thinking in Java》和《Thinking in C++》書籍的作者。

> 他說: 沒有其他語言能讓他的工作效率像使用 Python 語言時這麼高。

> 同時他也說: Python 語言可能是唯一的一種專注於讓程式設計者做起事來更為容易的語言。

> 可在此查看更詳細的完整訪問內容。

> http://www.artima.com/intv/aboutme.html

**彼得.諾維格 (Peter Norvig)**

> 彼得.諾維格是著名的 Lisp 語言作者，同時也是現任 Google 公司的搜尋品質主任。

> 他說: Python 始終是 Google 公司不可或缺部分。

> 事實上你查證一下 Google 的招聘網頁就可以驗證這一點。在這個網頁上，「瞭解 Python 語言」是對應徵軟體工程師職位者的一個要求。

> http://www.google.com/jobs/

**吉多.范.羅森 (Python 語言創造者)**

> 同時， 吉多.范.羅森已經加入了 Google 公司，在 Google 他可以花一半的上班時間在開放原始碼的 Python 語言改進上。

> http://www.artima.com/weblogs/viewpost.jsp?thread=143947


延伸閱讀：

[[Marr 的 python 簡介](http://marrtw.blogspot.com/2007/07/python-handbook.html)]

[前言](Foreword.md) | [下載與安裝](DownloadInstall.md)