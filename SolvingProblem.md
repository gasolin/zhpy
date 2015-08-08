# 簡介 #

我們已經探索了周蟒語言與 Python 語言的眾多內容，現在我們將來學習一下怎麼把這些內容結合起來。
我們將設計編寫一個能夠做一些確實有用的事情的程式。
我們仍然還有許多語言的特性尚未探索，但是在繼續探索之前，先讓我們用已知的知識來解決一些問題吧。

## 問題 ##

我想解決的問題是： 我想要一個可以為我的所有重要文件建立備份的程式。

雖然這是一個簡單的問題， 但是問題本身並沒有給我們足夠的信息來解決它。我們需要做一點進一步的分析。
例如，我們該如何確定哪些文件應該備份？我們該在哪裡保存備份？備份該以什麼形式來保存？

在適當地分析這個問題後， 我們開始設計我們的程式。
我們列了一張表，關於我們的程序應該如何工作在這個例子裡我已經建立了下面這個列表以說明我想如何讓它工作。
如果是你設計的話，你可能不會這樣來解決問題——每個人都有自己的做事方法，這很正常。

1. 用一個列表來指定所有需要備份的檔案和目錄。

2. 備份檔必需保存在主要的備份目錄中。

3. 所有檔案將備份成一個壓縮的 zip 檔案。

4. zip檔案的名稱以當前的日期和時間來命名。

5. 我們使用 Linux//BSD/Mac OS X 系統預設提供的標準 zip 命令來實現這個功能。
Windows 使用者可以安裝 Info-Zip 程式來達到相同目的。

注意你可以使用任何壓縮檔案的命令，只要這個壓縮檔案的命令具有有命令行界面即可。
如此我們就可以從我們的腳本中傳遞參數給這個壓縮檔案的命令。

## 解決方案 ##

當我們程式的基本設計方案已經差不多確定了，我們就可以開始編寫程式碼了，程式碼中將實現我們的解決方案。

## 第一個版本 ##
```
#!/usr/bin/env zhpy
# 檔名: backup1.py
導入 os, time
# 1. 用一個列表來指定所有需要備份的檔案和目錄。
來源目錄 = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# 如果你使用 Windows 作業系統, 請用 "來源目錄 = [r'C:\Documents', r'D:\Work']" 或其他類似語句
# 2. 備份檔必需保存在主要的備份目錄中。
目的目錄 = '/Users/swaroopch/Backup/'
# 3. 所有檔案將備份成一個壓縮的 zip 檔案。
# 4. zip檔案的名稱以當前的日期和時間來命名。
目的 = 目的目錄 + time.strftime('%Y%m%d_%H%M%S') + '.zip'
5. 我們使用標準 zip 命令來實現這個功能。
zip命令= "zip -qr '%s' %s" % (目的, ' '.連接(來源目錄))
印出 zip命令
# 運行備份
如果 os.system(zip命令) == 0:
    印出 '成功備份到', 目的
否則:
    印出 '備份失敗'
```

輸出結果:
```
$ zhpy backup1.py
zip -qr '/Users/swaroopch/Backup/20051113_234436.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
成功備份到 /Users/swaroopch/Backup/20051113_234436.zip
```


---


python 版:
```
#!/usr/bin/env python
# File name: backup1.py
import os, time
# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory.
target_directory = '/Users/swaroopch/Backup/'
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_directory + time.strftime('%Y%m%d_%H%M%S') + '.zip'
# 5. We use the standard ``zip`` command to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target， ' '.join(source))
print zip_command
# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
```

python 版輸出結果:
```
$ python backup1.py
zip -qr '/Users/swaroopch/Backup/20051113_234436.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
Successful backup to /Users/swaroopch/Backup/20051113_234436.zip
```


---


現在，我們已經處於測試階段了，在這個階段，我們測試我們的程式是否能正常地運作。
如果它的運作與我們所期望的不一樣，我們就得"除錯"我們的程式，即消除程式中的"臭蟲"（錯誤）。

### 程式如何運作 ###

接下來你會看到我們如何一步步地將我們的設計轉換成程式碼.

我們會使用到 os 和 time 模組，所以我們先導入它們到我們的名稱空間(程式)中。
然後我們在"來源目錄"(source) 列表中指定需要備份的文件和目錄。
目標目錄是我們想要存儲備份文件的地方，由 "目的目錄"(target\_dir) 變量來指定。
我們將建立的 zip 壓縮檔使用的名稱是從 time.strftime 函式獲得的當前的日期和時間。
這個壓縮檔會使用 .zip 作為副檔名， 並被保存在 target\_directory 目錄中。

time.strftime 函式需要我們指定在之前的程式中使用過的時間格式設定。%Y 格式設定會被兩位數的西元年份所替代。
%m 格式設定會被 01~12 之間的一個十進位月份所替代，其他依此類推。這些格式設定的詳細資訊可以在《Python參考手冊》中獲得。
《Python參考手冊》(Python Reference Guide) 包含在你的Python發行版中。注意這些格式設定與使用 %運算元 的格式設定相當類似。

我們使用加法運算元來串連目標壓縮檔名，並建立它。串連的意義即把兩個字串連接在一起返回一個新的字串。
接著，我們建立一個包含我們將執行的命令的"zip命令"(zip\_command) 字串你可以在 shell 提示符中運行它，以檢驗我們的程式是否工作。

我們所使用的 zip 命令帶有一些選項和參數。-q (quiet)選項用來指示 zip 命令運作時將不另外顯示額外訊息(安靜地工作)。
-r(recursively) 選項表示遞迴地對指定的目錄執行 zip 命令，即執行的範圍包含子目錄以及子目錄中的檔案。
這兩個選項可以組合成"-qr"這樣的縮寫形式。選項後面是將建立的 zip 壓縮檔的名稱，然後跟著的是待備份檔案和目錄的列表。
我們使用已經學習過的(字串的) join 方法來將 source 列表中的各個項目串連起來轉換為單一的字串。
在這個例子中是形成一個以空白符號分隔的檔案名稱與目錄列表。

最後，我們使用 os.system 函式來運行命令，這函式的作用是能讓我們如同在系統中運行命令地使用系統功能，
如同在 shell 中運行命令一樣——如果命令成功運行，程式會返回0，否則它返回錯誤號碼(error number)。

我們根據命令的輸出來印出相應的訊息，顯示備份是否成功或失敗。

就這樣， 我們已經建立了一個腳本來備份我們的重要文件！

**給 Windows 使用者的話**

> 你可以把"來源目錄"(source) 列表和"目的"(target) 目錄設置成任何檔案和目錄名稱，但是在 Windows 中你得小心一些。
> Windows 會使用反斜線符號（\）來作為目錄分隔符號，而周蟒與 Python 語言中，反斜線符號表示的是轉義符號(escape sequences)。
> 所以，你得使用兩個反斜線符號（\\）來代表反斜線符號（\）本身，或者你也可以使用自然字符串。
> 例如，使用 'C:\\Documents' 或 r'C:\Documents'， 而千萬不要使用 'C:\Documents' ——
> 周蟒或 Python 會認為你在使用一個不知名的轉義符號 "\D"。

現在我們已經有了一個可以工作的備份腳本，我們可以在任何我們想要建立檔案備份的時候用上它。
Linux/BSD/Mac OS X 使用者建議使用前面介紹的可執行的方法，這樣就可以在任何地方任何時候運行備份腳本了。
這被稱為操作階段或開發階段。

上面的程式可以正常地運作，但是通常第一個程式與你所期望的並不完全一樣。
例如，如果你沒有恰當地設計你的程式，或者你在輸入程式碼的時候拼錯了字等等，你的程式可能會出現些問題。
適當情況下，你需要回到設計階段重新檢視或者你需要除錯你的程式。

## 第二個版本 ##

我們腳本的第一個版本可以正常運作，然而，我們可以再對這個腳本做些優化，好讓這個腳本能更好地運作。
通常這個階段稱作"軟體的維護階段"。

我認為優化的手段之一是採用更好的檔案命名機制——使用當前的時間作為檔案名，而當前的日期則作為目錄名，存放在主備份目錄中。
這樣做的一個優點是你的備份會以階層的方式儲存，使得這些備份檔更加容易管理。另一個優點則是檔名的長度也可以縮短許多。
還有一個優點是採用分開的檔案夾可以協助你更方便地檢驗是否你每天都建立了備份，
因為只有當你在那天裡建立了備份，主備份目錄中才會出現當天的目錄:
```
#!/usr/bin/env zhpy
# 檔名: backup2.py
導入 os, time
# 1. 用一個列表來指定所有需要備份的檔案和目錄。
來源目錄 = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# 如果你使用 Windows 作業系統, 請用 "來源目錄 = [r'C:\Documents', r'D:\Work']" 或其他類似語句
# 2. 備份檔必需保存在主要的備份目錄中。
目的目錄 = '/Users/swaroopch/Backup/'
# 3. 所有檔案將備份成一個壓縮的 zip 檔案。
# 4. zip檔案的名稱以當前的日期和時間來命名。
今天 = 目的目錄 + time.strftime('%Y%m%d')
# 使用當前時間作為 zip 壓縮檔名稱
現在 = time.strftime('%H%M%S')
# 如果目錄不存在, 就建立子目錄
如果 非 os.path.exists(今天):
    os.mkdir(今天)
    印出 '成功建立目錄'， 今天
# zip 檔名
目的 = os.path.join(今天, 現在 + '.zip')
# 5. We use the standard ``zip`` command to put the files in a zip archive
zip命令 = "zip -qr '%s' %s" % (目的, ' '.連接(來源目錄))
印出 zip命令
# 運行備份
如果 os.system(zip命令) == 0:
    印出 '成功備份到', 目的
否則:
    印出 '備份失敗'
```

輸出結果:
```
$ zhpy backup2.py
成功建立目錄 /Users/swaroopch/Backup/20051114
zip -qr '/Users/swaroopch/Backup/20051114/001955.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
成功備份到 /Users/swaroopch/Backup/20051114/001955.zip
```


---


python 版:
```
#!/usr/bin/env python
# File name: backup2.py
import os, time
# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# If you are using Windows, use source = [r'C:\Documents'， r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory.
target_directory = '/Users/swaroopch/Backup/'
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
today = target_directory + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
# Create the subdirectory if it does not exist already
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory'， today
# The name of the zip file
target = os.path.join(today, now + '.zip')
# 5. We use the standard ``zip`` command to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target， ' '.join(source))
print zip_command
# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
```

python 版輸出結果:
```
$ python backup2.py
Successfully created directory /Users/swaroopch/Backup/20051114
zip -qr '/Users/swaroopch/Backup/20051114/001955.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
Successful backup to /Users/swaroopch/Backup/20051114/001955.zip
```


---


### 程式如何運作 ###

程式的大部分內容仍然是相同的。改變的部分是我們使用 os.exists 函式來檢驗在主備份目錄中是否有以當前日期作為名稱的目錄。
如果該目錄不存在，我們就使用 os.mkdir 函式來建立目錄。

注意 os.path.join 函式的使用方法，這個函式轉換檔案名稱列表(目錄後接著目錄，最後則是接著檔案(可選擇))成完整的檔案存取路徑。
使用 os.path.join 函式使得我們的程式具有可移植性，能在不同的系統上運作。

## 第三個版本 ##

第二個版本在我製作多個備份檔的時候運作的相當不錯，但是如果有非常多的備份檔的時候，我發現要區分哪個備份是幹什麼的則會變得十分困難！
舉個例子，我可能對一個程式或者一份演講稿做出了一些重要的改變，於是我想要把這些改變與 zip 備份檔的名稱聯繫起來。
這功能很容易地可以透過在 zip 備份檔名上附帶一個使用者提供的補註來地實現:
```
#!/usr/bin/env zhpy
# 檔名: backup3.py
導入 os, time
# 1. 用一個列表來指定所有需要備份的檔案和目錄。
來源目錄 = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# 如果你使用 Windows 作業系統, 請用 "來源目錄 = [r'C:\Documents', r'D:\Work']" 或其他類似語句
# 2. 備份檔必需保存在主要的備份目錄中。
目的目錄 = '/Users/swaroopch/Backup/'
# 3. 所有檔案將備份成一個壓縮的 zip 檔案。
# 4. zip檔案的名稱以當前的日期和時間來命名。
今天 = 目的目錄 + time.strftime('%Y%m%d')
# 使用當前時間作為 zip 壓縮檔名稱
現在 = time.strftime('%H%M%S')
# 接受使用者輸入訊息作為壓縮檔名
訊息 = 輸入('輸入訊息 --> ')
如果 長度(訊息) == 0: # 確認有輸入訊息
    目的 = os.path.join(今天, 現在 + '.zip')
否則:
    目的 = os.path.join(今天, 現在 + '_' * 訊息.代換(' '， '_') + '.zip')
# 如果目錄不存在, 就建立子目錄
如果 非 os.path.exists(今天):
    os.mkdir(今天)
    印出 '成功建立目錄'， 今天
# 5. We use the standard ``zip`` command to put the files in a zip archive
zip命令 = "zip -qr '%s' %s" % (目的, ' '.連接(來源目錄))
印出 zip命令
# 運行備份
如果 os.system(zip命令) == 0:
    印出 '成功備份到', 目的
否則:
    印出 '備份失敗'
```

輸出結果:
```
$ zhpy backup3.py
輸入訊息 --> Added new chapter
Traceback (most recent call last):
  File "programs/backup3.py", line 25， in ?
    target = os.path.join(today， now + '_' * comment.replace(' '， '_') + '.zip')
TypeError: can't multiply sequence by non-int
```


---

python 版:
```
#!/usr/bin/env python
# File name: backup3.py
import os, time
# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# If you are using Windows， use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory.
target_directory = '/Users/swaroopch/Backup/'
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
today = target_directory + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
# Take a comment from the user to create the name of the zip archive
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = os.path.join(today， now + '.zip')
else:
    target = os.path.join(today， now + '_' * comment.replace(' '， '_') + '.zip')
# Create the subdirectory if it does not exist already
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today
# 5. We use the standard ``zip`` command to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
print zip_command
# Run the backup
if os.system(zip_command) == 0:
   print 'Successful backup to', target
else:
   print 'Backup FAILED'
```

python 版輸出結果:
```
$ python backup3.py
Enter a comment --> Added new chapter
Traceback (most recent call last):
  File "programs/backup3.py", line 25， in ?
    target = os.path.join(today， now + '_' * comment.replace(' '， '_') + '.zip')
TypeError: can't multiply sequence by non-int
```


---


### 程式如何運作 ###

这个程式竟然不能運作！

我們觀察周蟒和 Python 直譯器裡的錯誤訊息並試著找出為什麼程式中會出現乘法(multiplication)運算。
看起來我們犯了一個錯誤， 在第25行(line 25)我們誤把+號寫成\*號。所以我們修正了程式的錯誤並嘗試再次運行程式。
這種行為稱作"錯誤修正(bug fixing)"。

## 第四個版本 ##
```
#!/usr/bin/env zhpy
# 檔名: backup3.py
導入 os, time
# 1. 用一個列表來指定所有需要備份的檔案和目錄。
來源目錄 = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# 如果你使用 Windows 作業系統, 請用 "來源目錄 = [r'C:\Documents', r'D:\Work']" 或其他類似語句
# 2. 備份檔必需保存在主要的備份目錄中。
目的目錄 = '/Users/swaroopch/Backup/'
# 3. 所有檔案將備份成一個壓縮的 zip 檔案。
# 4. zip檔案的名稱以當前的日期和時間來命名。
今天 = 目的目錄 + time.strftime('%Y%m%d')
# 使用當前時間作為 zip 壓縮檔名稱
現在 = time.strftime('%H%M%S')
# 接受使用者輸入訊息作為壓縮檔名
訊息 = 輸入('輸入訊息 --> ')
如果 長度(訊息) == 0: # 確認有輸入訊息
    目的 = os.path.join(今天, 現在 + '.zip')
否則:
    目的 = os.path.join(今天, 現在 + '_' + 訊息.代換(' '， '_') + '.zip')
# 如果目錄不存在, 就建立子目錄
如果 非 os.path.exists(今天):
    os.mkdir(今天)
    印出 '成功建立目錄'， 今天
# 5. We use the standard ``zip`` command to put the files in a zip archive
zip命令 = "zip -qr '%s' %s" % (目的, ' '.連接(來源目錄))
印出 zip命令
# 運行備份
如果 os.system(zip命令) == 0:
    印出 '成功備份到', 目的
否則:
    印出 '備份失敗'
```

輸出結果:
```
$ zhpy backup4.py
輸入訊息 --> added new chapter
zip -qr '/Users/swaroopch/Backup/20051114/004004_added_new_chapter.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
成功備份到 /Users/swaroopch/Backup/20051114/004004_added_new_chapter.zip

$ zhpy backup4.py
輸入訊息 -->
zip -qr '/Users/swaroopch/Backup/20051114/004235.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
成功備份到 /Users/swaroopch/Backup/20051114/004235.zip
```


---


python 版:
```
#!/usr/bin/env python
# File name: backup4.py
import os， time
# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/swaroopch/Documents', '/Users/swaroopch/Code']
# If you are using Windows， use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory.
target_directory = '/Users/swaroopch/Backup/'
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
today = target_directory + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
# Take a comment from the user to create the name of the zip archive
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = os.path.join(today， now + '.zip')
else:
    target = os.path.join(today， now + '_' + comment.replace(' '， '_') + '.zip') # Bug fixed!
# Create the subdirectory if it does not exist already
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today
# 5. We use the standard ``zip`` command to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target， ' '.join(source))
print zip_command
# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
```

python 版輸出結果:
```
$ python backup4.py
Enter a comment --> added new chapter
zip -qr '/Users/swaroopch/Backup/20051114/004004_added_new_chapter.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
Successful backup to /Users/swaroopch/Backup/20051114/004004_added_new_chapter.zip

$ python backup4.py
Enter a comment -->
zip -qr '/Users/swaroopch/Backup/20051114/004235.zip' /Users/swaroopch/Documents/ /Users/swaroopch/Code/
Successful backup to /Users/swaroopch/Backup/20051114/004235.zip
```


---


### 程式如何運作 ###

這個程式現在可以運作了！我們用正確的+號改正了不小心輸入錯的\*號.

現在讓我們看一下版本三裡所作出的實質性改進。我們使用"輸入"(raw\_input) 函式來取得使用者的補註，
然後通過"長度"(len) 函式找出輸入的長度，以檢驗使用者是否確實輸入了些內容。
如果使用者只是按了輸入鍵而未輸入任何訊息（也許這只是一個例行備份，沒做什麼值得一提的修改），那麼我們就繼續如同之前版本那樣地運作。

然而，如果使用者提供了補註，那麼這個補註會被附加到 zip 備份檔名上，位於 .zip 副檔名之前。
注意我們把補註中的空格替換成底線——這是因為處理帶底線的檔案名要比處理帶空白的檔案名容易得多。

## 進一步的優化 ##

對於大多數使用者來說，第四個版本是一個令人相當滿意的工作腳本了，但是它仍然有進一步改進的空間。
比如，你可以在程式裡指定一個命令訊息的詳細程度——你可以用-v選項來使你的程式提供更多的訊息。

另一個可能的改進是使檔案和目錄能夠通過命令行直接傳遞給腳本。
我們可以通過 sys.argv 列表來取得額外的檔案和目錄，然後使用"列表.擴展"(list.extend) 方法把它們加到"來源目錄"(source) 列表中。

另一個優化則是使用 tar 命令來替代 zip 命令。這種做法的一個優點是當你結合使用 tar 和 gzip 命令的時候，備份檔案會更快，
檔案大小也會更小。如果你想要在 Windows 作業系統中使用這些備份檔案，WinZip 也能方便地處理這些.tar.gz文件。
在其他系統則都內建處理 .tar.gz 檔案的命令。 Windows 使用者也可以下載並安裝它。

改用 tar 命令後， 命令字串現在將是:
```
tar = 'tar -cvzf %s %s -X /Users/swaroopch/Documents/excludes.txt'
    % (target， ' '.join(srcdir))
```

tar 命令中用到的選項解釋如下

  * -c 表示建立一個備份檔。
  * -v 表示詳細訊息，即命令執行時顯示更詳盡的運行訊息。
  * -z 表示將使用 gzip 過濾器。
  * -f表示強迫建立備份檔，即如果已經存在一個同名的檔案，則這個檔案將被新建立的檔案所替換。
  * -X表示含在指定檔案名稱列表中的檔案會被排除在備份之外。例如，你可以在檔案中指定**.pyc不包含在檔名中，
> 從而不讓備份檔中包括所有以 .pyc 結尾的檔案。**

## 重要提示 ##

最理想建立這些備份檔的方法是分別使用 zipfile 和 tarfile 模組。它們都是 Python 標準函式庫的一部分。
使用這些函式庫就能避免使用 os.system 這個通常不推薦使用的函數，因為隨意使用它非常容易造成嚴重的錯誤(因為使用了系統權限)。
然而，我在本節中使用 os.system 的方法來建立備份，這純粹是為了教學的需要。
這樣的話，例子就可以簡單到讓每個人都能夠理解，同時也已經足夠用了。

# 軟體開發階段 #

現在我們已經走過了編寫一個軟體的各個階段。這些階段可以總結如下：

  1. 什麼（分析）
> 2. 如何（設計）
> 3. 編寫（實現）
> 4. 測試（測試與除錯）
> 5. 維護（優化）

我們建立這個備份腳本的過程是編寫程序的推薦方法——進行分析與設計。
開始時先實現一個簡單的版本。對它進行完整的測試與除錯。使用它以確認它如同預期那樣地工作。
然後再增加任何你所想要的特性，然後立刻繼續盡量多次地重複這個編寫－測試－使用的循環。
記住「軟體是漸漸成長起來的，而不是一夕建造好的」。

# 結語 #

我們已經學習如何建立我們自己的 Python 程式，以及在編寫這個程式時所牽涉到的多種不同的階段。
你可以發現當你在創建你自己的程式的時候這些知識會十分有用，讓你不管是對於使用 Python 程式或是解決問題方面都變得更加得心應手。

接下來，我們將討論物件導向的程式設計。

[資料結構](DataStructure.md) | [物件導向程式設計](ObjectOrient.md)