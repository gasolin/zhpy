# 簡介 #

Python 語言安裝時已一同安裝了 Python 語言的標準函式庫。 Python 語言的標準函式庫包含了為數眾多的有用模組。
熟悉標準函式庫相當重要， 使用這些標準函式庫就能簡單地解決我們大部分的程式問題。

在周蟒中也能直接使用這些 Python 模組。

我們將探索標準函式庫中的一些常用的模組。 你可以在 Python 語言的標準函式庫文件裡找到詳細資訊。

http://docs.python.org/lib/

## os 和 sys 模組 ##

os 模組包含與作業系統相關的功能，sys 模組包含與 Python 直譯器相關的系統與環境的功能。

```
#!/usr/bin/env zhpy
# 檔名: cat.py
導入 os, sys
定義 讀檔(檔名):
    '''將檔案從標準輸出中印出.'''
    如果 非 os.path.exists((檔名):
        印出 '檔名', (檔名, '不存在.'
        sys.exit(1)

    取 行 自 檔案(檔名):
        印出 行,
如果 長度(sys.argv) < 2:
    印出 '無指定動作.'
    sys.exit()
如果 sys.argv[1].開頭為('--'):
    選項 = sys.argv[1][2:]
    如果 選項 == 'version':
        印出 'Version 1.5'
    否則 選項 == 'help':
        印出 '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version : Prints the version number
    --help    : Display this help.
'''
    否則:
        印出 '未知的選項.'
    sys.exit()
否則:
    取 檔名 自 sys.argv[1:]:
        讀檔(filename)
```

輸出結果:
```
$ zhpy cat.py
無指定動作.

$ zhpy cat.py --version
Version 1.5

$ zhpy cat.py --help
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version : Prints the version number
    --help    : Display this help.

$ zhpy cat.py --nonsense
未知的選項.

$ zhpy cat.py poem.txt
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```


---



python 版:
```
#!/usr/bin/env python
# File name: cat.py
import os, sys
def readfile(filename):
    '''Print a file to the standard output.'''
    if not os.path.exists(filename):
        print 'The file', filename, 'does not exist.'
        sys.exit(1)

    for line in file(filename):
        print line,
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print 'Version 1.5'
    elif option == 'help':
        print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version : Prints the version number
    --help    : Display this help.
'''
    else:
        print 'Unknown option.'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
```

python 版輸出結果:
```
$ python cat.py
No action specified.

$ python cat.py --version
Version 1.5

$ python cat.py --help
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version : Prints the version number
    --help    : Display this help.

$ python cat.py --nonsense
Unknown option.

$ python cat.py poem.txt
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```


---


### 程式如何運作 ###

這個程式試著模仿 Linux/BSD/Mac OS X 系統使用者熟悉的 cat 命令。
你可以指定文字檔的名稱，然後 cat 命令就會將檔案內容印出到螢幕上(標準輸出)。

當 Python 程式運行時 (即不是運行在互動模式時)，sys.argv 變量中至少會有一個變量，儲存著目前運行程式的名稱。
其他的命令行參數則羅列於其後。
因為 Python 語言是從 0 開始記數，我們可以使用 sys.argv[0](0.md) 來取得這個正在運行程式的名稱。

為了讓程式更易於使用，我們提供使用者一些選項，好讓使用者可以透過指定一些選項來觀看程式的說明。

當使用者傳給程式檔名時若不指定任何選項，那麼程式就只是照著命令行中的順序將各個檔案讀出一遍。

cat 這個名稱是 concatenate (連接) 的縮寫，這個程式的作用就如它的名稱所示的 - cat 命令可以將檔案依照順序印出。
因此可以用來將多個檔案串連在一起輸出。

sys 模組中還有許多類別欄位和類別方法可供使用， 例如 sys.version 和 sys.version\_info 能提供你目前所使用的 Python 版本。

對於有經驗的程式設計者來說， sys 模組中還有諸如 sys.stdin、sys.stdout 與 sys.stderr 來對應標準輸入、
標準輸出、標準錯誤訊息字串可供應用。

os 模組可以幫助你讓編寫的程式可跨平台使用。即你只需要寫一次程式，不需做任何修改，程式即可在 Linux、BSD、Mac OS X、
或 Windows 等作業系統平台上運行。
例如 os 模組中的 os.path.join 函式，可以將檔案夾路徑與檔案名稱連結起來，好在任何作業系統上使用。
也可以使用 os.sep 函式來取得特定系統的路徑標示符號。

在此列出一些有用的 os 模組功能. 許多功能都可以直接望名生義:

  * os.name 字串能指出目前正在使用的作業系統平台， 如 nt 表示是 Windows 平台，posix 表示是 Linux/BSD/Mac OS X 平台。
  * os.getcwd() 函式能取得程式當前所在目錄。
  * os.getenv() 和 os.putenv() 函式分別可用來取得和設定環境變數。也可以使用 os.environ 字典來達到同樣的目的。
  * os.listdir() 函式返回指定目錄中的所有檔案和目錄名稱。
  * os.remove() 函式可以用來移除檔案。
  * os.system()函式可以用來執行 shell 命令。
  * os.path.split() 函式可以返回指定路徑的目錄和檔案的名稱。
  * os.path.isfile() 和 os.path.isdir() 函式可以用來確認指定的路徑是檔案還是目錄。
> 同樣地可以使用 os.path.exists() 來確認指定的路徑是否存在。

# 結語 #

我們已經學習了標準函式庫中 os 和 sys 模組的一部份功能。還有眾多的模組存在於 Python 標準函式庫中，分別提供適用於不同情境的各種功能。

接下來，我們將學習 Python 語言其它方面的內容，好讓整個 Python 語言學習過程更完整。

[例外處理](HandleExceptions.md) | [進一步瞭解](NextStep.md)