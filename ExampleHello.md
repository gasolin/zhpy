# 簡介 #

我們現在來看一下怎麼使用 Python 和周蟒程式語言來寫個常見的「Hello World」程式。透過這個程式，你將學會如何撰寫、儲存和執行 Python 與周蟒程式。

Python 和周蟒有兩種執行程式的方式 - 使用互動式的直譯器，或者直接執行原始檔。現在我們就分別來看看這兩種方式。

# 使用互動式的周蟒直譯器 #

開啟命令列，在命令列中輸入「python」來啟動 Python 互動式直譯器，或在命令列中輸入「zhpy」來啟動周蟒互動式直譯器。

Windows 使用者要先照著前一章的說明，設定好<tt>PATH</tt>變數後，才能在命令列中執行Python 或周蟒互動式直譯器。

當我們啟動了直譯器後，在系統提示符號 '>>>' 後方輸入 [印出 '哈囉, 世界']:
```
>>> 印出 '哈囉, 世界'
```
並按下輸入鍵 (Enter)。

你將看到螢幕上印出了你剛才輸入的文字:
```
$ zhpy
zhpy 1.0 in darwin on top of Python 2.5.1
>>> 印出 '哈囉, 世界'
哈囉, 世界
```

**註解
> ">>> " (三個箭頭加一個空白) 符號是周蟒/python直譯器的提示符號，用意是提醒你可以在提示符號後輸入要編寫的程式。**

你應該注意到了，當輸入任一行 Python或周蟒「語句」時，Python 或周蟒互動式直譯器就可以立即作出回應！

我們使用了 '印出' (print) 命令來印出任何我們所提供的內容到螢幕上。

範例中，我們提供了一串文字 '哈囉, 世界'，這段文字馬上被印到了螢幕上。

周蟒同時支援[繁(正)體中文，簡體中文，英文的關鍵字](ZhpyExample.md)，因此在周蟒中以下兩種語句也是合法的:

簡體中文:
```
$ zhpy
zhpy 1.0 in darwin on top of Python 2.5.1
>>> 印出 '哈啰, 世界'
哈啰, 世界
```

英文:
```
$ zhpy
zhpy 1.0 in darwin on top of Python 2.5.1
>>> print '哈囉, 世界'
哈囉, 世界
```

如果你僅使用英文關鍵字，你也可以使用互動式的 Python 直譯器執行上段程式。

啟動 Python 直譯器的方式跟啟動周蟒直譯器的方式完全相同，只是輸入命令得改成 'python':
```
$ python
Python 2.5.1 (r251:54869, Apr 18 2007, 22:08:04) 
[GCC 4.0.1 (Apple Computer, Inc. build 5367)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print '哈囉, 世界'
哈囉, 世界
```

之所以如此是因為周蟒是全功能的中文 Python 語言，周蟒仍然保留所有 Python 語言的功能。

**註解
> 你可以將周蟒直譯器 (zhpy) 當作 python 直譯器來執行 python 程式。大部份本書中的範例都可以只用周蟒直譯器來執行。
> 如果希望執行直譯器後看到的是中文提示的話, 可以在後面加上 "--tw" 或 "--cn" 參數來顯示中文提示。
```
  $ zhpy --tw
  周蟒 1.0 於 darwin 基於 Python 2.5.1
  >>>
```**

## 如何離開周蟒直譯器 ##

  * Windows 使用者 - 同時按下 Ctrl 與 Z 鍵 (Ctrl-Z)後, 再按下輸入鍵(Enter)
  * Linux/BSD/Mac OS X 使用者 - 同時按下 Ctrl 與 D 鍵 (Ctrl-D)

# 使用檔案執行周蟒 #

## 選擇一個 Python 語言編輯器 ##

在我們開始學習如何在原始檔中編寫周蟒語言時，我們需要一個好用的編輯器。

選擇編輯器的重要性就和選擇妳將要購買的轎車一樣地重要。

一個好的編輯器會幫助你更容易寫作周蟒程式，讓你的程式之旅更加舒適，並助你更加快捷安全地到達目的地（實現目標）。

一個好的編輯器的基本要求之一是語法高亮度功能，語法高亮度功能使你的 Python 程式碼能根據語法的不同而被標示以不同的顏色，這樣你就可以清楚地檢視你的程式，並視覺化地了解它的運行方式。

特別值得注意的是：請不要使用記事本 (Notepad) 程式來編寫 Python 程式 —— 記事本程式是一個糟糕的選擇，因為它沒有語法高亮度功能，而且更加重要的是，它不支援文字自動縮排，而且記事本程式中使用 utf-8 編碼很不方便。

### ulipad ###

中國人 limodou 寫的編輯器，對 utf-8 編碼支援佳。
Windows 環境下的 python 編輯器首選。

http://code.google.com/p/ulipad

### eclipse+pydev ###

eclipse 是個通用的編輯器平台，透過 pydev 提供相當完整的 python 語言支援，
只是對於初學者來說用不到 eclipse 的多數功能，且安裝稍嫌複雜。
作者即在 Mac 上使用 eclipse+pydev 來寫作。

http://pydev.sourceforge.net/

建議初學者使用預先包裝好的 easyeclipse python 版本
http://www.easyeclipse.org/site/distributions/python.html

### Vim 或 Emacs 編輯器 ###

Vim 和 Emacs 編輯器是兩個非常強悍的編輯器。兩者都支援多種平台- Windows，Mac OS X，Linux 和 BSD 等。

http://www.vim.org/

http://www.gnu.org/software/emacs/emacs.html

如果你是有經驗的程式設計者。你也可以使用習慣的 Vim 或 Emacs 來編輯 Python 程式語言。


如果你打算寫大量的周蟒/Python 程式碼，我建議你從中挑一個來學習。因為這些編輯器能幫助你更容易地寫作。

你可以在 Python 編輯器列表中找到其他的選擇。或是你也可以從 Python 支援的 IDE (整合開發環境) 列表中選擇使用。

http://www.python.org/cgi-bin/moinmoin/PythonEditors

http://www.python.org/cgi-bin/moinmoin/IntegratedDevelopmentEnvironments

再次提醒您請選擇一個合適的編輯器——一個好的編輯器可以讓你更容易地編寫 Python 程式。

## 使用原始檔 ##

資訊領域有一個傳統，當你學習一個新的程式語言時，第一個寫作與執行的程式大都是歡迎 (Hello World) 程式。這個程式的功能是讓你透過這門語言，在螢幕上印出 "Hello World" (哈囉, 世界) 字樣。

'Beginning Perl' 一書的作者西蒙.寇森斯 (Simon Cozens) 說: 歡迎 (Hello World) 程式是能幫助你更容易學好程式的程式之神的傳統魔法。

啟動你的編輯器，輸入下面這段程式並把它儲存到 'helloworld.twpy' 這個檔案中。

範例:
```
#coding=utf-8
印出 '哈囉, 世界'
```

請打開命令列程式，然後鍵入 "zhpy helloworld.twpy" 命令。如果你使用的是 IDLE 編輯器，請在選單中選擇 Run→ Run Module。

輸出結果如下:
```
$ zhpy helloworld.py
哈囉, 世界
```


python 版:
```
print 'Hello World'
```

輸出結果如下:
```
$ python helloworld.py
Hello World
```

如果你得到的輸出與上面所示的一樣，那麼恭喜你！——你已經成功地運行了你的第一個周蟒(Python)程式。

萬一你得到的是一個錯誤回報，那麼請確保你剛剛鍵入的程式與以上範例所示完全相同，然後再試著執行一下程式。

注意在周蟒語言中繁，簡中文，英文大小寫都是被區分開來的。

例如'定義'跟'定义'是不一樣的——繁簡中文不同， print 與 Print 也是不一樣的—— P 字元的大小寫不同
。此外，也請確保在每一行的開始符號前沒有任何空格或者 Tab 符號——我們將在後面討論為什麼確認空白和 Tab 符號，這點很重要。

## 程式如何運作 ##

'印出'(print)語句的作用是將我們提供的 "哈囉, 世界" 這串文字印出到螢幕上。

注意在 Python 語言裡，我們使用"引號"把文字的部份圍了起來。這種文字的型態被稱作'字串 (string)'，
因為這些文字正是一串字元所組合起來的。

'#coding=utf-8'語句的作用是指定程式中所使用的文字編碼。(請參考 註解)

**註解**

> 電腦原本是美國人發明的東西，因此只有內建支援英文文字，電腦中以一些代號來表示這些英文文字，這種表示方式稱作 ASCII 編碼。

> 程式語言是與電腦溝通的語言，要在程式語言中使用非英語字詞的話，通常得作額外的宣告，好通知程式接受其他支援非英語字詞的文字編碼格式。

> 在華文地區要在電腦中顯示中文的編碼格式，常見的有 Big5(繁體)、GB2312、GBK、GB18030(簡體)、UTF-8(繁，簡)等編碼格式。
> 其中 UTF-8 編碼格式是相容ASCII 編碼，而且是全球通用的標準格式。
> 因此雖然周蟒支援使用上述各種版本編碼的程式。但是在周蟒中強烈建議使用 UTF-8編 碼格式。


## 註解 ##

> 當我們正在寫程式的時候，我們可能會想在程式旁邊加上一些註解好幫助我們回答 "為什麼在那個時候我會這麼編寫程式?"的問題，
> 或是記下代辦事項列表好來提醒在這份程式碼中我們還需要加入什麼功能等等。我們可以透過'註解'語法來在我們的程式中加入註解。

在周蟒程式裡, 井字符號'#' 右邊的任何文字都會被當作是程式的註解。舉個例子如下:

```
# 開始寫程式
印出 '哈囉, 世界' # 傳統的第一個程式
```

Python 版:
```
# Start of the program
print 'Hello World' # The traditional first program
```

這個程式會產生跟前一個程式一樣的輸出結果。唯一的不同就是我們在程式碼中加入了一行註解。

註解相當的重要，它可以讓你在程式中寫下這份程式的註釋, 讓閱讀這份程式的人更容易瞭解。

它也可以幫助你在六個月後還能快速讀懂你自己編寫的程式。

所以呀，請儘量地在你的程式裡加入註解吧。

記得要寫下你的程式可以提供些什麼功能，而不只是程式怎麼運作 (因為去閱讀程式碼就能告訴你程式怎麼運作, 但是沒辦法馬上告訴你這個程式能提供些什麼功能)。

## 可執行的周蟒程式 ##

**註解:
> 本節主要針對 Linux/BSD/Mac 使用者而寫，Windows 使用者可以跳過這節。**

在周蟒程式中的第一列做註解可以達成一些特殊的功能。這行被稱為事務列(shebang line):
```
#!/usr/bin/env zhpy
印出 '哈囉, 世界'
```

Python 版:
```
#!/usr/bin/env python
print 'Hello World'
```

這個程式輸出的結果仍然跟 '哈囉, 世界' 程式的輸出結果相同。但是第一行的內容有相當特別的含意。

當直接執行這個原始檔時，只要原始檔第一列中的前兩個字元為 '#!' ，後方接著的是程式的路徑時，周蟒直譯器會通知你的 Linux/BSD/Mac OS X 系統: 這個程式應該使用放在原始檔第一列這個路徑的周蟒直譯器來執行。(因為你可以在系統上安裝多個不同版本的 Python，而周蟒是依賴於 python 語言的)

注意你可以在任何平台透過執行諸如 "zhpy helloworld.twpy" 這樣的命令來指定周蟒語言直譯器運行程式。

然而如果我們想像原生程式一樣地執行我們的周蟒程式，我們可以透過事務列(shebang line)這樣的方式來達成。

我們使用 /usr/bin/env zhpy 查找周蟒直譯器的路徑，而不是指定特定的 zhpy 命令路徑。

因為有的系統將 Python 裝在 /usr/local/bin/python 路徑裡，有的裝在 /usr/bin/python 路徑裡，這樣做可以保證程式執行在不同系統時的相容性，讓我們的程式可以直接運行在不同的 Unix-like 系統上。

來看看事務列(shebang line)是多麼有用吧。首先我們使用'chmod'命令來改變程式的執行權限。

這個命令告訴我們的系統這個程式並不是個普通檔案，而是可以執行的檔案。接著我們就開始運行程式:
```
$ chmod a+x helloworld.twpy
$ ./helloworld.twpy
哈囉, 世界
```

Python 版:
```
$ chmod a+x helloworld.py
$ ./helloworld.py
Hello World
```

'chmod' 命令在這被用來改變檔案的執行權限。

接著我們指定了檔案名稱後直接執行了程式。我們使用'./'路徑來表示這個檔案就在當前的資料夾下。

那麼系統怎麼知道該運行這個原始檔呢？ 事務列(shebang line)的作用就在這了.

系統做的只是找出在事務列中指出的 zhpy 直譯器路徑，接著將程式傳入直譯器後，我們的程式就能運行啦。

接著來看點更有趣的吧，你可以把原本的檔案名稱 helloworld.twpy 改了叫 helloworld，
然後執行 './helloworld' 命令，這樣程式仍然能運行。看來作業系統確實知道怎麼執行這樣的一個程式。

現在你只要知道程式的路徑就可以運行這個程式囉。但是，如果你想在任何地方都能運行這個程式呢?

你可以透過將程式儲存在一個紀錄在 PATH 環境變數中的資料夾目錄, 來在任何地方運行這個程式。

無論你在你的系統上運行了哪個程式，系統都會查詢 PATH 環境變數中的資料夾目錄列表並運行這個程式。

我們可以將讓我們的程式複製到其中一個列在 PATH 環境變數中的資料夾目錄中，從而達到可以在任何地方運行這個程式的目的:

# 將程式複製到一個已存在於 PATH 參數的資料夾下
```
$ echo $PATH
/bin:/sbin:/usr/bin:/usr/sbin:/Users/swaroop/Code
$ cp helloworld.py /Users/swaroop/Code/helloworld
$ helloworld
哈囉, 世界
```

或者:
```
# 將目錄加入 PATH 參數
$ pwd # 印出當前目錄
/Users/gasolin/Code
$ export PATH=$PATH:/Users/gasolin/Code # 將目錄加入 PATH 參數
$ echo $PATH
/bin:/sbin:/usr/bin:/usr/sbin:Users/gasolin/Code
$ helloworld
哈囉, 世界
```

我們可以透過在環境變數名稱前加上一個 '$'符號，並使用 'echo' 命令來顯示 PATH 環境變數。

'$'符號表示我們想取得變數的內容資料。我們可以看到 '/Users/gasolin/Code' 這個路徑存在於 PATH 變數中。

注意 'gasolin' 是作者 Mac OS X 系統的使用者名稱。你的系統上可能會有個類似的 HOME 資料夾目錄包含了你的使用者名稱。

我們可以把程式複製到這個資料夾裡，然後在任何目錄執行 "helloworld" 這個檔案。系統會透過 PATH 變數找到這個程式並運行它。

在第二個範例裡，我們要在 PATH 變數中加入一個資料夾路徑。我們使用 '$PATH' 敘述來取的環境變數的值，
並把添加好目錄的內容填回到 PATH 變數。

注意: 要重點注意的是當我們這麼做的時候，我們的檔案就像其他那些我們用過的命令一樣成了系統的一部分。

因此你可以寫一些程式來自動化一些日常工作，並讓這些程式成為系統的一部分。

## 取得說明檔 ##

如果你需要迅速的瞭解 Python 語法和函式的訊息，你可以使用 python 語言內建的"說明" (help) 功能。

當你使用互動式直譯器時，這個功能超有用的。

目前周蟒並不提供繁簡中文的說明檔，但是你仍然可以透過周蟒直譯器查詢 Python 語法和函式的訊息。

舉個例子，運行:
```
>>> 說明(字串)
```

python 版:
```
>>> help(str)
```

結果會顯示 str 這個 Pyhton '類別'怎麼儲存你在程式中用上的字串(文字)的說明檔。(我們會在其他章節詳細說明什麼是'類別')

按下 q 鍵來離開說明。

同樣地，你應該可以透過同樣的方式在周蟒中取得幾乎任何東西的說明。你可以運行 "說明()"(help) 來取得更多關於"說明"本身的說明。

假使你需要 "印出(print)" 敘述的說明，你需要先正確地設定 PYTHONDOCS 環境變數。
在 Linux/BSD/Mac OS X 作業系統上可以簡單地使用'env'命令來完成。當然，首先你需要從 python.org 網站下載 HTML 文件:

http://www.python.org/doc/current/download.html
```
$ export PYTHONDOCS=/Users/gasolin/Documents/Python/Docs/
$ zhpy
zhpy 1.0 in darwin on top of Python 2.5.1
>>> 說明('印出')
```

注意我們需要在"印出" (print) 敘述旁加上引號，好讓周蟒直譯器知道我們想要取得的是'印出'語句的說明，而不是想在螢幕上顯示什麼東西。

# 結語 #

你現在應該能輕鬆地寫作，儲存，並運行周蟒程式了。

現在你已經是個周蟒語言使用者囉，讓我們在下一章中學習更多周蟒語言的概念吧。

[下載與安裝](DownloadInstall.md) | [基礎觀念](BasicConcept.md)

[Source](http://zhpy.googlecode.com/svn/trunk/examples/hello/n_hello.py)


