# 預備 #

  * 安裝好 python
  * 從[下載區](http://code.google.com/p/zhpy/downloads/list)取得周蟒(zhpy)源碼包解壓縮

# 試玩 #

  * 打開命令行執行

```
$ python interpreter.py
zhpy X.X in darwin on top of Python 2.X.X
>>>
```

> 你可以立即試用周蟒中文 Python 直譯器. 試著在直譯器上輸入
```
印出 '哈囉, 世界'
```

```
$ python interpreter.py
zhpy X.X in darwin on top of Python 2.X.X
>>> 印出 '哈囉, 世界'
哈囉
```

這樣你就完成了你的第一個中文程式囉!

# 基本安裝 #

你可以直接使用
```
$ easy_install -U zhpy
```
命令來自動安裝周蟒(不需先抓源碼包)

或是解壓縮下載的源碼包, 輸入
```
$ python setup.py install
```
以安裝周蟒.


# 基本操作 #

建立一個名為 hello.py 的檔案, 使用支援 utf-8 編碼的編輯器開啟, 填入:

```
印出 "哈囉, 世界"
```

儲存檔案內容.

## 運行 ##

打開命令行, 進入檔案所在的目錄, 輸入 zhpy 指令, 你會看到一行提示:

```
$zhpy
please type "zhpy --help" for help
```

表示周蟒(zhpy)已正常安裝在你的系統中了.

接著執行 "zhpy hello.py" 指令, 你可以看到如下結果:

```
$ zhpy hello.py
哈囉, 世界
```

或者也可以使用指定命令行參數(-i 或 --input)的方式來指定要執行的檔案:

```
$ zhpy -i hello.py
哈囉, 世界
```

## 輸出 ##

你也可以將你所編寫的中文程式透過 zhpy 指令直接轉換為自然 Python 程式，
我們使用指定命令行參數(-o 或 --output)的方式來指定要轉換的檔案:

```
$ zhpy -i hello.py -o nhello.py
$ ls
hello.py nhello.py
```

產生出來的 nhello.py 程式是標準的 python 程式，你可以在一般的 Python 程式中直接導入或呼叫它。


你也可以使用指定命令行參數(-p)來要求 zhpy 自動轉換檔案後並執行程式:

```
$ zhpy -p hello.py
compile to python and run: n_hello.py
哈囉, 世界
$ ls
hello.py n_hello.py nhello.py
```

使用 -p 參數產生的檔案以 "n_" 為開頭。
產生出來的 n\_hello.py 程式與前一方法產生出來的程式一樣是標準的 python 程式，_

你可以在一般的 Python 程式中直接導入或呼叫它。

## 與 Python 程式的雙向轉換 ##

你也能將這個產生出來的 python 程式再轉回周蟒程式.

```
$ zhpy --tw n_hello.py
$ ls
hello.twpy, n_hello.py, v_n_hello.twpy
```

使用"--tw"或"--cn"參數產生出來的檔案是以 "v