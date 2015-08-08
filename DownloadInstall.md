# 1. 安裝 Python 程式語言 #

首先您需安裝 Python 程式語言。

Python 程式語言屬於自由軟體，您不需為了使用 Python 程式語言，而付錢給某個公司以取得使用 python 程式語言的權利。

多數的作業系統都已經預先安裝好 Python 程式語言，除了 Windows 作業系統之外。
有時候作業系統上所提供的預設版本可能稍微舊了一些。這時，你也許會想自行下載較新版本的 Python 程式語言。

## 安裝在 Windows 作業系統上 ##

有兩種方式可以在 Windows 作業系統上安裝 Python 程式語言軟體。


> 方法一：前往 [python 程式語言官方網站](http://www.python.org/download/)下載最新的安裝檔案 (.exe)。
> > 下載好的安裝檔，其安裝方式就跟其他的 Windows 程式的安裝方式一樣。

  * 註釋: 在安裝時請不要取消預設的勾選項目，有些項目會在之後的書中用到，比如 "IDLE" 這個 Python 程式語言的編輯器。


> 方法二：下載並安裝 [ActivePython 安裝程式](http://www.activestate.com/Products/activepython/downloads/)。 ActiveState 公司提供了另一個預先包裝好許多 Windows 環境下專用工具 (如 PythonWin) 的安裝版本。對 Windows 作業系統的使用者來說相當有用。

註釋: [ShowMeDo.com 網站](http://showmedo.com/videos/series?name=PythonDownloadInstallTest)(英文)上有一些影片演示如何下載， 安裝，和執行 Python 環境。可供您參考。

目前實際業界在使用的版本是 2.x 版, 本書範例全以 2.x 版撰寫。
如果您要參考 3.x 版範例，請前往 http://www.swaroopch.com/notes/Python_en:Table_of_Contents 對照查看。

### 透過 Windows 作業系統命令列使用 Python 語言 ###

如果你想透過 Windows 命令列來使用 Python 語言，那麼你需要先設定好 Windows 環境變數。

在 Windows 2000， XP， 2003 這些作業系統裡，點選 "控制台" -> "系統" -> "進階" -> "環境變數"。

在"系統變數(S)"欄中，選取 'PATH' 變數名稱後，再點選 '編輯(I)' 按鈕。

請先確定你安裝 Python 語言程式的路徑是 'C:\Python25'，接著在彈出的視窗中將 ';C:\Python25' (注意要以分號隔開)這字串添在原本的字串之後。

在比較舊的 Windows 作業系統版本上，則是在 'C:\AUTOEXEC.BAT' 這個檔案中加入

```
 'PATH=%PATH%;c:\python25;c:\python25\Scripts;' 
```

一行訊息後重新啟動作業系統即可。在 Windows NT 作業系統上，則改成修改檔名為 'AUTOEXEC.NT' 的檔案。

## 安裝在 Linux/BSD 作業系統上 ##

如果你正使用某個 Linux 的發行版本如 Ubuntu， Fedora， Mandriva 等等，或者某個 BSD 系統如 FreeBSD，那麼你的系統裡應該早就預先安裝好 Python 程式語言軟體了。要測試 Python 程式語言軟體是否真的已經安裝好在你的作業系統上， 你可以開啟一個命令列 (Shell) 程式 (如 konsole 或 gnome-terminal)， 輸入命令 'python -V' ('V' 最好為大寫)。

```
$ python -V
Python 2.x.x
```

註釋: '$' 符號是命令列程式的提示符號。出現的符號與你的系統設定有關。本書中一律以 '$' 符號表示。

如果你看見了如上所示的一些版本訊息，那就表示系統已經預先安裝好 Python 程式語言軟體了。

然而， 如果你看到的是如下訊息:

```
$ python -V
bash: python: command not found
```

那就表示你的作業系統上還未安裝 Python。雖然這種情況不太可能發生。

當你遇到這種情況時，可以透過這兩種方式在你的作業系統上安裝 Python 程式語言軟體。

  * 透過作業系統提供的安裝管理員程式來安裝 (比如 Ubuntu/Debian Linux 作業系統上的 apt-get ， Fedora Linux 作業系統上的 yum， Mandriva Linux 作業系統上的 urpmi， FreeBSD 作業系統上的 pkg\_add...等等). 請注意你需要連在網路上才能使用上述方式安裝。
  * 或者你可以下載打包好的套件(如 .deb 或 .rpm 檔)後直接安裝。
  * 你也可以自行編譯 python 程式語言軟體的程式碼並安裝. 在 python 語言軟體的原始碼中有說明編譯的步驟. http://www.python.org/download/

在 Ubuntu 7.04 以上版本已經內建了 Python 2.x。

## 安裝在 Mac 作業系統上 ##

在 Mac OS X 10.3 以上的版本中已經預先安裝了 Python 程式語言軟體. 如果你想安裝較新的 Python 程式語言軟體版本， 可以使用 'DarwinPorts' 程式:

  * 安裝 DarwinPorts 程式 http://www.darwinports.org/getdp/
  * 執行 'sudo port search python' 命令以取得 python 軟體列表。
> > 目前 DarwinPorts 中 Python 2.5.1 版本的代號為 python25。
  * 執行 'sudo port install python25' 命令

在更舊版本的 Mac 作業系統上， 請造訪 MacPython 官方網站並下載適合你的作業系統版本的 .dmg 檔。 掛載(mount)起這個磁碟檔並執行安裝程式即可. http://homepages.cwi.nl/~jack/macpython/download.html

在 Mac OS X 上已經內建了 Python 與 easy\_install 等相關工具。

要在命令行中能使用自動完成功能，請安裝 readline 模組
```
$ sudo easy_install readline
```

# 2. 安裝周蟒模組 #

現在我們假設你已經在你的作業系統上準備好了 Python 語言軟體。

接著，請使用命令行(command line) 執行命令以安裝周蟒(zhpy):

## 線上安裝周蟒 ##

1. 如果已安裝過 easy\_install 命令模組的話， 請直接執行以下指令安裝 zhpy 模組：

```
$ easy_install zhpy
```

此指令會透過網路自動安裝 zhpy 模組。

如果是在 Ubuntu 或 Debian 作業系統上，可以使用
```
$ sudo apt-get install python-setuptools
```
命令來安裝 easy\_install 命令模組。


2. 如果想從頭全新安裝的話， 請下載 [ez\_setup.py](http://peak.telecommunity.com/dist/ez_setup.py) 檔案並執行以下指令來安裝 zhpy (周蟒)模組：

```
$ python ez_setup.py zhpy
```

zhpy 是周蟒的代號，此指令會透過網路自動安裝一個用來線上安裝 Python 模組的工具: "easy\_install" 命令，然後線上安裝 zhpy 模組。

## 透過原始碼安裝周蟒 ##

自 [pypi](http://pypi.python.org/pypi/zhpy/) 下載 zip 格式壓縮的原始碼，
使用 zip 解壓縮程式解開後， 使用命令列執行以下指令安裝 zhpy 模組：

```
$ python setup.py install
```

## Ubuntu 作業系統上安裝周蟒 ##

在 Debian 系列作業系統上安裝周蟒很容易，只需要輸入兩行命令：

```
$ sudo apt-get install python-setuptools
$ sudo easy_install zhpy
```

## 驗證 ##


你可以用以下方法來確認是否已安裝成功。
開啟一個命令列 (Shell) 程式 (如 konsole 或 gnome-terminal)， 輸入命令 'zhpy -V'。
```
$ zhpy -V
zhpy 1.x on python 2.x.x
```

現在我們假設你也已經在你的作業系統上準備好了 Python 與周蟒語言軟體。

接著我們就來寫我們的第一個 Python 程式吧。

[簡介](IntroZhpy.md) | [學習程式的第一個範例](ExampleHello.md)